#!/usr/bin/env python3
"""
Simple search CLI for research knowledge base.
Searches across papers and articles using keyword matching.
"""

import argparse
import re
from pathlib import Path

# Paths
SCRIPT_DIR = Path(__file__).parent
ROOT_DIR = SCRIPT_DIR.parent
PAPERS_DIR = ROOT_DIR / "papers"
ARTICLES_DIR = ROOT_DIR / "articles"


def parse_frontmatter(content: str) -> dict:
    """Parse YAML frontmatter from markdown."""
    if not content.startswith("---"):
        return {}

    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}

    frontmatter = {}
    for line in parts[1].strip().split("\n"):
        if ":" in line:
            key, _, value = line.partition(":")
            value = value.strip().strip('"\'')
            frontmatter[key.strip()] = value

    return frontmatter


def search_file(filepath: Path, query_terms: list[str], case_sensitive: bool = False) -> dict | None:
    """Search a file for query terms."""
    try:
        content = filepath.read_text(encoding="utf-8")

        if not case_sensitive:
            search_content = content.lower()
            search_terms = [t.lower() for t in query_terms]
        else:
            search_content = content
            search_terms = query_terms

        # Check if all terms are present
        matches = sum(1 for term in search_terms if term in search_content)
        if matches == 0:
            return None

        # Calculate relevance score
        score = matches / len(search_terms)

        # Bonus for matches in title
        frontmatter = parse_frontmatter(content)
        title = frontmatter.get("title", "").lower() if not case_sensitive else frontmatter.get("title", "")
        title_matches = sum(1 for term in search_terms if term in title)
        score += title_matches * 0.5

        # Extract snippet around first match
        snippet = ""
        for term in search_terms:
            idx = search_content.find(term)
            if idx != -1:
                start = max(0, idx - 50)
                end = min(len(content), idx + len(term) + 100)
                snippet = "..." + content[start:end].replace("\n", " ") + "..."
                break

        return {
            "path": filepath,
            "title": frontmatter.get("title", filepath.stem),
            "topic": frontmatter.get("topic", "unknown"),
            "date": frontmatter.get("date", ""),
            "score": score,
            "snippet": snippet
        }

    except Exception as e:
        return None


def main():
    parser = argparse.ArgumentParser(description="Search the knowledge base")
    parser.add_argument("query", nargs="+", help="Search terms")
    parser.add_argument("--topic", type=str, help="Filter by topic")
    parser.add_argument("--limit", type=int, default=10, help="Max results (default: 10)")
    parser.add_argument("--case-sensitive", action="store_true", help="Case sensitive search")
    parser.add_argument("--paths-only", action="store_true", help="Output only file paths (for piping)")
    args = parser.parse_args()

    query_terms = args.query
    results = []

    # Search papers and articles
    for search_dir in [PAPERS_DIR, ARTICLES_DIR]:
        if not search_dir.exists():
            continue

        for filepath in search_dir.rglob("*.md"):
            # Topic filter
            if args.topic and args.topic not in str(filepath):
                continue

            result = search_file(filepath, query_terms, args.case_sensitive)
            if result:
                results.append(result)

    # Sort by score
    results.sort(key=lambda x: x["score"], reverse=True)
    results = results[:args.limit]

    if args.paths_only:
        for r in results:
            print(r["path"])
        return

    if not results:
        print(f"No results found for: {' '.join(query_terms)}")
        return

    print(f"\nFound {len(results)} results for: {' '.join(query_terms)}\n")
    print("=" * 70)

    for i, r in enumerate(results, 1):
        rel_path = r["path"].relative_to(ROOT_DIR)
        print(f"\n[{i}] {r['title']}")
        print(f"    Topic: {r['topic']} | Date: {r['date']}")
        print(f"    Path: {rel_path}")
        if r["snippet"]:
            print(f"    {r['snippet'][:150]}")


if __name__ == "__main__":
    main()
