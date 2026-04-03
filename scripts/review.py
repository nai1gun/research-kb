#!/usr/bin/env python3
"""
Interactive review CLI for research knowledge base.
Review inbox items, generate TLDRs, approve/reject.
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import urllib.request
from datetime import datetime
from pathlib import Path

def safe_str(text: str) -> str:
    """Make string safe for Windows console output."""
    return text.encode('ascii', 'replace').decode('ascii')


# Paths
SCRIPT_DIR = Path(__file__).parent
ROOT_DIR = SCRIPT_DIR.parent
INBOX_DIR = ROOT_DIR / "inbox"
PAPERS_DIR = ROOT_DIR / "papers"
ARTICLES_DIR = ROOT_DIR / "articles"
REJECTED_DIR = ROOT_DIR / "rejected"


def parse_frontmatter(content: str) -> tuple[dict, str]:
    """Parse YAML frontmatter from markdown."""
    if not content.startswith("---"):
        return {}, content

    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}, content

    frontmatter = {}
    for line in parts[1].strip().split("\n"):
        if ":" in line:
            key, _, value = line.partition(":")
            value = value.strip().strip('"\'')
            frontmatter[key.strip()] = value

    return frontmatter, "---".join(["", parts[1], parts[2]])


def extract_abstract(content: str) -> str:
    """Extract abstract section from markdown."""
    match = re.search(r'## Abstract\s*\n(.*?)(?=\n##|\Z)', content, re.DOTALL)
    if match:
        return match.group(1).strip()
    return ""


def generate_tldr_prompt(title: str, abstract: str) -> str:
    """Generate prompt for TLDR generation."""
    return f"""Generate a 2-3 sentence TLDR for this research paper. Focus on:
- What problem does it solve?
- What is the key approach/contribution?
- What are the main results?

Title: {title}

Abstract: {abstract}

Respond with ONLY the TLDR, no preamble or labels."""


def call_claude_for_tldr(title: str, abstract: str) -> str:
    """Try to generate TLDR using Claude CLI if available."""
    try:
        prompt = generate_tldr_prompt(title, abstract)
        # Try claude CLI
        result = subprocess.run(
            ["claude", "-p", prompt],
            capture_output=True,
            text=True,
            timeout=60
        )
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass
    return ""


def display_item(filepath: Path, idx: int, total: int):
    """Display an inbox item for review."""
    content = filepath.read_text(encoding="utf-8")
    frontmatter, body = parse_frontmatter(content)

    title = frontmatter.get("title", "Unknown")
    source = frontmatter.get("source", "unknown")
    topic = frontmatter.get("topic", "general")
    date = frontmatter.get("date", "")

    abstract = extract_abstract(content)

    # Check for existing TLDR
    tldr_match = re.search(r'## TLDR\s*\n(.*?)(?=\n##|\Z)', content, re.DOTALL)
    tldr = tldr_match.group(1).strip() if tldr_match else ""
    if tldr.startswith("<!--"):
        tldr = ""

    print("\n" + "=" * 70)
    print(f"[{idx}/{total}] {source.upper()} | {topic}")
    print("=" * 70)
    print(f"\n{safe_str(title)}\n")
    print(f"Date: {date}")
    print("-" * 70)

    if tldr:
        print(f"\nTLDR: {safe_str(tldr)}\n")
    else:
        print(f"\nAbstract: {safe_str(abstract[:400])}{'...' if len(abstract) > 400 else ''}\n")

    return frontmatter, content, abstract, tldr


def update_tldr_in_content(content: str, tldr: str) -> str:
    """Update TLDR section in content."""
    pattern = r'(## TLDR\s*\n).*?((?=\n##|\Z))'
    replacement = f'\\1{tldr}\n\n'
    return re.sub(pattern, replacement, content, flags=re.DOTALL)


def approve_item(filepath: Path, content: str, frontmatter: dict):
    """Move item from inbox to appropriate folder."""
    topic = frontmatter.get("topic", "general")
    source = frontmatter.get("source", "unknown")

    # Determine destination
    if source in ["arxiv", "semantic_scholar", "s2"]:
        dest_dir = PAPERS_DIR / topic
    else:
        dest_dir = ARTICLES_DIR / topic

    dest_dir.mkdir(parents=True, exist_ok=True)

    # Update status in frontmatter
    content = content.replace("status: pending", "status: approved")
    content = content.replace(
        f"discovered: {frontmatter.get('discovered', '')}",
        f"discovered: {frontmatter.get('discovered', '')}\napproved: {datetime.now().strftime('%Y-%m-%d')}"
    )

    # Save to destination
    dest_path = dest_dir / filepath.name
    dest_path.write_text(content, encoding="utf-8")

    # Remove from inbox
    filepath.unlink()

    print(f"  -> Approved: {dest_path.relative_to(ROOT_DIR)}")
    return dest_path


def reject_item(filepath: Path, content: str, frontmatter: dict):
    """Move item to rejected folder."""
    REJECTED_DIR.mkdir(parents=True, exist_ok=True)

    # Update status
    content = content.replace("status: pending", "status: rejected")

    # Save minimal version to rejected (just frontmatter + title for dedup)
    dest_path = REJECTED_DIR / filepath.name
    dest_path.write_text(content, encoding="utf-8")

    # Remove from inbox
    filepath.unlink()

    print(f"  -> Rejected")


def download_pdf(url: str, dest_dir: Path, filename: str) -> Path | None:
    """Download PDF file."""
    if not url:
        return None

    try:
        dest_path = dest_dir / f"{filename}.pdf"
        print(f"  Downloading PDF...")

        req = urllib.request.Request(url)
        req.add_header("User-Agent", "ResearchKB/1.0")

        with urllib.request.urlopen(req, timeout=60) as response:
            # Check size
            size = response.headers.get("Content-Length")
            if size and int(size) > 25 * 1024 * 1024:  # 25MB limit
                print(f"  PDF too large ({int(size) / 1024 / 1024:.1f}MB), skipping download")
                return None

            data = response.read()
            dest_path.write_bytes(data)
            print(f"  -> Downloaded: {dest_path.name} ({len(data) / 1024 / 1024:.1f}MB)")
            return dest_path

    except Exception as e:
        print(f"  PDF download failed: {e}")
        return None


def main():
    parser = argparse.ArgumentParser(description="Review inbox items")
    parser.add_argument("--auto-tldr", action="store_true", help="Auto-generate TLDRs using Claude")
    parser.add_argument("--download-pdf", action="store_true", help="Download PDFs for approved papers")
    parser.add_argument("--topic", type=str, help="Only review specific topic")
    args = parser.parse_args()

    # Get inbox items
    if not INBOX_DIR.exists():
        print("Inbox is empty. Run 'python scripts/discover.py' first.")
        return

    items = sorted(INBOX_DIR.glob("*.md"), key=lambda x: x.stat().st_mtime, reverse=True)

    if args.topic:
        filtered = []
        for item in items:
            content = item.read_text(encoding="utf-8")
            if f"topic: {args.topic}" in content:
                filtered.append(item)
        items = filtered

    if not items:
        print("No items to review in inbox.")
        return

    print(f"\nFound {len(items)} items to review")
    print("\nCommands:")
    print("  y/yes    - Approve and add to KB")
    print("  n/no     - Reject (won't be suggested again)")
    print("  s/skip   - Skip for now (stays in inbox)")
    print("  t/tldr   - Generate TLDR using Claude")
    print("  o/open   - Open URL in browser")
    print("  q/quit   - Exit review")
    print()

    approved = 0
    rejected = 0
    skipped = 0

    for idx, filepath in enumerate(items, 1):
        frontmatter, content, abstract, tldr = display_item(filepath, idx, len(items))

        while True:
            try:
                action = input("\n[y/n/s/t/o/q] > ").strip().lower()
            except (EOFError, KeyboardInterrupt):
                print("\n\nExiting...")
                break

            if action in ["y", "yes"]:
                # Generate TLDR if missing and auto-tldr enabled
                if args.auto_tldr and not tldr:
                    print("  Generating TLDR...")
                    tldr = call_claude_for_tldr(frontmatter.get("title", ""), abstract)
                    if tldr:
                        content = update_tldr_in_content(content, tldr)
                        print(f"  TLDR: {safe_str(tldr[:100])}...")

                dest_path = approve_item(filepath, content, frontmatter)
                approved += 1

                # Download PDF if requested
                if args.download_pdf:
                    pdf_match = re.search(r'\[PDF\]\((.*?)\)', content)
                    if pdf_match:
                        download_pdf(pdf_match.group(1), dest_path.parent, filepath.stem)

                break

            elif action in ["n", "no"]:
                reject_item(filepath, content, frontmatter)
                rejected += 1
                break

            elif action in ["s", "skip"]:
                print("  -> Skipped")
                skipped += 1
                break

            elif action in ["t", "tldr"]:
                print("  Generating TLDR...")
                new_tldr = call_claude_for_tldr(frontmatter.get("title", ""), abstract)
                if new_tldr:
                    tldr = new_tldr
                    content = update_tldr_in_content(content, tldr)
                    filepath.write_text(content, encoding="utf-8")
                    print(f"\n  TLDR: {safe_str(tldr)}\n")
                else:
                    print("  Could not generate TLDR (Claude CLI not available?)")

            elif action in ["o", "open"]:
                url_match = re.search(r'\[Original\]\((.*?)\)', content)
                if url_match:
                    url = url_match.group(1)
                    print(f"  Opening: {url}")
                    if sys.platform == "win32":
                        os.startfile(url)
                    elif sys.platform == "darwin":
                        subprocess.run(["open", url])
                    else:
                        subprocess.run(["xdg-open", url])
                else:
                    print("  No URL found")

            elif action in ["q", "quit"]:
                print("\n\nExiting...")
                break

            else:
                print("  Unknown command. Use y/n/s/t/o/q")

        else:
            continue
        break

    print(f"\n{'=' * 50}")
    print(f"Review complete:")
    print(f"  Approved: {approved}")
    print(f"  Rejected: {rejected}")
    print(f"  Skipped:  {skipped}")
    print(f"  Remaining in inbox: {len(list(INBOX_DIR.glob('*.md')))}")


if __name__ == "__main__":
    main()
