#!/usr/bin/env python3
"""
Discovery script for research knowledge base.
Fetches new papers from arXiv, Semantic Scholar, and RSS feeds.
"""

import argparse
import hashlib
import json
import re
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional

# Paths
SCRIPT_DIR = Path(__file__).parent
ROOT_DIR = SCRIPT_DIR.parent
CONFIG_DIR = ROOT_DIR / "config"
INBOX_DIR = ROOT_DIR / "inbox"
PAPERS_DIR = ROOT_DIR / "papers"
ARTICLES_DIR = ROOT_DIR / "articles"
REJECTED_DIR = ROOT_DIR / "rejected"


def load_yaml_simple(path: Path) -> dict:
    """Simple YAML parser for our config format (no external deps)."""
    content = path.read_text(encoding="utf-8")

    # Remove comments
    lines = []
    for line in content.split("\n"):
        if "#" in line:
            # Keep content before #, but be careful with URLs
            if "://" in line and "#" in line:
                # URL with fragment or comment after - keep the URL part
                parts = line.split("#")
                if "://" in parts[0]:
                    lines.append(parts[0].rstrip())
                else:
                    lines.append(line.split("#")[0].rstrip())
            else:
                lines.append(line.split("#")[0].rstrip())
        else:
            lines.append(line)
    content = "\n".join(lines)

    # Parse into structure
    result = {}
    current_list = None
    current_list_key = None
    current_topic = None
    topics = []
    feeds = []
    settings = {}

    for line in content.split("\n"):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue

        # Check indentation level
        indent = len(line) - len(line.lstrip())

        if stripped.startswith("- name:") and indent <= 2:
            # New topic or feed
            name = stripped.replace("- name:", "").strip().strip('"\'')
            if current_list_key == "topics":
                current_topic = {"name": name}
                topics.append(current_topic)
            elif current_list_key == "feeds":
                current_topic = {"name": name}
                feeds.append(current_topic)
        elif stripped.startswith("- ") and current_list is not None:
            # List item
            value = stripped[2:].strip().strip('"\'')
            current_list.append(value)
        elif ":" in stripped:
            key, _, value = stripped.partition(":")
            key = key.strip().strip("-").strip()
            value = value.strip().strip('"\'')

            if key == "topics":
                current_list_key = "topics"
                current_list = None
            elif key == "feeds":
                current_list_key = "feeds"
                current_list = None
            elif key == "settings":
                current_list_key = "settings"
                current_list = None
            elif key in ["keywords", "arxiv_categories", "semantic_scholar_fields"]:
                current_list = []
                if current_topic:
                    current_topic[key] = current_list
            elif current_topic and value:
                if value.isdigit():
                    current_topic[key] = int(value)
                else:
                    current_topic[key] = value
            elif current_list_key == "settings" and value:
                if value.isdigit():
                    settings[key] = int(value)
                else:
                    settings[key] = value

    return {"topics": topics, "feeds": feeds, "settings": settings}


def get_existing_ids() -> set:
    """Get IDs of papers/articles already in KB or rejected."""
    ids = set()

    for folder in [INBOX_DIR, PAPERS_DIR, ARTICLES_DIR, REJECTED_DIR]:
        if folder.exists():
            for f in folder.rglob("*.md"):
                # Extract ID from filename or content
                ids.add(f.stem)
                # Also check for arxiv/doi in content
                try:
                    content = f.read_text(encoding="utf-8")
                    for match in re.findall(r'arxiv[:/](\d+\.\d+)', content, re.I):
                        ids.add(f"arxiv_{match}")
                    for match in re.findall(r'doi[:/](10\.\d+/[^\s]+)', content, re.I):
                        ids.add(f"doi_{match}")
                except:
                    pass

    return ids


def fetch_arxiv(topic: dict, days_back: int = 7, max_results: int = 20) -> list:
    """Fetch papers from arXiv API."""
    papers = []

    # Build query
    keywords = topic.get("keywords", [])
    categories = topic.get("arxiv_categories", [])

    # Create search query
    keyword_query = " OR ".join(f'all:"{kw}"' for kw in keywords[:5])  # Limit keywords
    cat_query = " OR ".join(f"cat:{cat}" for cat in categories)

    query = f"({keyword_query})"
    if cat_query:
        query = f"({query}) AND ({cat_query})"

    # URL encode and build request
    params = {
        "search_query": query,
        "start": 0,
        "max_results": max_results,
        "sortBy": "submittedDate",
        "sortOrder": "descending"
    }

    url = f"http://export.arxiv.org/api/query?{urllib.parse.urlencode(params)}"

    try:
        with urllib.request.urlopen(url, timeout=30) as response:
            xml_data = response.read().decode("utf-8")

        # Parse XML
        root = ET.fromstring(xml_data)
        ns = {"atom": "http://www.w3.org/2005/Atom"}

        cutoff_date = datetime.now() - timedelta(days=days_back)

        for entry in root.findall("atom:entry", ns):
            try:
                # Extract fields
                title = entry.find("atom:title", ns).text.strip().replace("\n", " ")
                abstract = entry.find("atom:summary", ns).text.strip().replace("\n", " ")

                # Get arxiv ID
                id_url = entry.find("atom:id", ns).text
                arxiv_id = id_url.split("/abs/")[-1]

                # Get published date
                published = entry.find("atom:published", ns).text
                pub_date = datetime.fromisoformat(published.replace("Z", "+00:00"))

                # Skip if too old
                if pub_date.replace(tzinfo=None) < cutoff_date:
                    continue

                # Get authors
                authors = []
                for author in entry.findall("atom:author", ns):
                    name = author.find("atom:name", ns).text
                    authors.append(name)

                # Get PDF link
                pdf_url = None
                for link in entry.findall("atom:link", ns):
                    if link.get("title") == "pdf":
                        pdf_url = link.get("href")
                        break

                papers.append({
                    "id": f"arxiv_{arxiv_id.replace('/', '_')}",
                    "source": "arxiv",
                    "title": title,
                    "abstract": abstract,
                    "authors": authors,
                    "date": pub_date.strftime("%Y-%m-%d"),
                    "url": f"https://arxiv.org/abs/{arxiv_id}",
                    "pdf_url": pdf_url,
                    "topic": topic["name"]
                })
            except Exception as e:
                print(f"  Error parsing arXiv entry: {e}")
                continue

    except Exception as e:
        print(f"  Error fetching arXiv: {e}")

    return papers


def fetch_semantic_scholar(topic: dict, days_back: int = 7, max_results: int = 20) -> list:
    """Fetch papers from Semantic Scholar API."""
    papers = []

    keywords = topic.get("keywords", [])
    fields = topic.get("semantic_scholar_fields", ["Computer Science"])

    # Use first few keywords for query
    query = " ".join(keywords[:3])

    params = {
        "query": query,
        "limit": max_results,
        "fields": "paperId,title,abstract,authors,year,publicationDate,url,openAccessPdf",
        "year": f"{datetime.now().year - 1}-"
    }

    url = f"https://api.semanticscholar.org/graph/v1/paper/search?{urllib.parse.urlencode(params)}"

    try:
        req = urllib.request.Request(url)
        req.add_header("User-Agent", "ResearchKB/1.0")

        with urllib.request.urlopen(req, timeout=30) as response:
            data = json.loads(response.read().decode("utf-8"))

        cutoff_date = datetime.now() - timedelta(days=days_back)

        for paper in data.get("data", []):
            try:
                pub_date_str = paper.get("publicationDate")
                if pub_date_str:
                    pub_date = datetime.fromisoformat(pub_date_str)
                    if pub_date < cutoff_date:
                        continue
                else:
                    pub_date = datetime.now()

                paper_id = paper.get("paperId", "")
                title = paper.get("title", "")
                abstract = paper.get("abstract", "") or ""

                if not title or not paper_id:
                    continue

                authors = [a.get("name", "") for a in paper.get("authors", [])[:5]]

                pdf_info = paper.get("openAccessPdf") or {}
                pdf_url = pdf_info.get("url")

                papers.append({
                    "id": f"s2_{paper_id}",
                    "source": "semantic_scholar",
                    "title": title,
                    "abstract": abstract,
                    "authors": authors,
                    "date": pub_date.strftime("%Y-%m-%d"),
                    "url": paper.get("url", f"https://www.semanticscholar.org/paper/{paper_id}"),
                    "pdf_url": pdf_url,
                    "topic": topic["name"]
                })
            except Exception as e:
                print(f"  Error parsing S2 paper: {e}")
                continue

    except Exception as e:
        print(f"  Error fetching Semantic Scholar: {e}")

    return papers


def fetch_rss_feed(feed: dict) -> list:
    """Fetch articles from RSS feed."""
    articles = []

    url = feed.get("url", "")
    if not url:
        return articles

    try:
        req = urllib.request.Request(url)
        req.add_header("User-Agent", "ResearchKB/1.0")

        with urllib.request.urlopen(req, timeout=30) as response:
            xml_data = response.read().decode("utf-8")

        root = ET.fromstring(xml_data)

        # Handle both RSS and Atom feeds
        items = root.findall(".//item") or root.findall(".//{http://www.w3.org/2005/Atom}entry")

        for item in items[:10]:  # Limit to 10 per feed
            try:
                # RSS format
                title = item.findtext("title") or item.findtext("{http://www.w3.org/2005/Atom}title") or ""
                link = item.findtext("link") or ""
                if not link:
                    link_elem = item.find("{http://www.w3.org/2005/Atom}link")
                    if link_elem is not None:
                        link = link_elem.get("href", "")

                description = item.findtext("description") or item.findtext("{http://www.w3.org/2005/Atom}summary") or ""
                pub_date = item.findtext("pubDate") or item.findtext("{http://www.w3.org/2005/Atom}published") or ""

                if not title or not link:
                    continue

                # Generate ID from URL
                article_id = f"rss_{hashlib.md5(link.encode()).hexdigest()[:12]}"

                # Clean up HTML in description
                description = re.sub(r'<[^>]+>', '', description)[:500]

                articles.append({
                    "id": article_id,
                    "source": "rss",
                    "feed_name": feed.get("name", "Unknown"),
                    "title": title.strip(),
                    "abstract": description.strip(),
                    "authors": [],
                    "date": pub_date[:10] if pub_date else datetime.now().strftime("%Y-%m-%d"),
                    "url": link,
                    "pdf_url": None,
                    "topic": feed.get("topic", "general")
                })
            except Exception as e:
                print(f"  Error parsing RSS item: {e}")
                continue

    except Exception as e:
        print(f"  Error fetching RSS {feed.get('name', url)}: {e}")

    return articles


def save_to_inbox(item: dict):
    """Save a discovered item to inbox as markdown."""
    INBOX_DIR.mkdir(parents=True, exist_ok=True)

    filename = f"{item['id']}.md"
    filepath = INBOX_DIR / filename

    authors_str = ", ".join(item.get("authors", [])[:5])
    if len(item.get("authors", [])) > 5:
        authors_str += " et al."

    content = f"""---
id: {item['id']}
source: {item['source']}
topic: {item['topic']}
title: "{item['title'].replace('"', "'")}"
date: {item['date']}
discovered: {datetime.now().strftime("%Y-%m-%d")}
status: pending
---

# {item['title']}

**Source:** {item['source']}
**Date:** {item['date']}
**Authors:** {authors_str or "N/A"}
**Topic:** {item['topic']}

## Links

- [Original]({item['url']})
{f"- [PDF]({item['pdf_url']})" if item.get('pdf_url') else ""}

## Abstract

{item.get('abstract', 'No abstract available.')}

## TLDR

<!-- To be generated during review -->

## Notes

<!-- Add notes after review -->
"""

    filepath.write_text(content, encoding="utf-8")
    return filepath


def main():
    parser = argparse.ArgumentParser(description="Discover new research papers and articles")
    parser.add_argument("--days", type=int, default=7, help="Days to look back (default: 7)")
    parser.add_argument("--topic", type=str, help="Only fetch for specific topic")
    parser.add_argument("--backfill", action="store_true", help="Backfill mode: 90 days, more results")
    args = parser.parse_args()

    # Load config
    topics_config = load_yaml_simple(CONFIG_DIR / "topics.yaml")
    feeds_config = load_yaml_simple(CONFIG_DIR / "feeds.yaml")

    topics = topics_config.get("topics", [])
    feeds = feeds_config.get("feeds", [])
    settings = topics_config.get("settings", {})

    days_back = args.days
    max_results = settings.get("max_results_per_source", 20)

    if args.backfill:
        days_back = 90
        max_results = 50
        print("Backfill mode: 90 days, 50 results per source")

    # Get existing IDs to avoid duplicates
    existing_ids = get_existing_ids()
    print(f"Found {len(existing_ids)} existing items in KB")

    all_items = []

    # Fetch from each source
    for topic in topics:
        if args.topic and topic["name"] != args.topic:
            continue

        print(f"\nDiscovering for topic: {topic['name']}")

        # arXiv
        print("  Fetching arXiv...")
        papers = fetch_arxiv(topic, days_back, max_results)
        print(f"    Found {len(papers)} papers")
        all_items.extend(papers)

        # Semantic Scholar
        print("  Fetching Semantic Scholar...")
        papers = fetch_semantic_scholar(topic, days_back, max_results)
        print(f"    Found {len(papers)} papers")
        all_items.extend(papers)

    # RSS feeds
    print("\nFetching RSS feeds...")
    for feed in feeds:
        if args.topic and feed.get("topic") != args.topic:
            continue
        print(f"  {feed.get('name', 'Unknown')}...")
        articles = fetch_rss_feed(feed)
        print(f"    Found {len(articles)} articles")
        all_items.extend(articles)

    # Filter duplicates and save new items
    new_count = 0
    for item in all_items:
        if item["id"] in existing_ids:
            continue
        existing_ids.add(item["id"])

        filepath = save_to_inbox(item)
        # Handle Unicode safely on Windows
        title_safe = item['title'][:60].encode('ascii', 'replace').decode('ascii')
        print(f"  + {title_safe}...")
        new_count += 1

    print(f"\n{'='*50}")
    print(f"Discovery complete: {new_count} new items added to inbox")
    print(f"Run 'python scripts/review.py' to review them")


if __name__ == "__main__":
    main()
