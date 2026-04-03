# Research Knowledge Base

A personal knowledge base for tracking research papers and articles, inspired by [Andrej Karpathy's approach](https://x.com/karpathy/status/2039805659525644595).

## Features

- **Auto-discovery**: Fetches papers from arXiv, Semantic Scholar, and RSS feeds
- **Topic tracking**: Configure keywords and categories for your research interests
- **Review workflow**: Interactive CLI or conversational review through Claude Code
- **Simple storage**: Markdown files, viewable in Obsidian or any editor

## Structure

```
research-kb/
├── config/
│   ├── topics.yaml      # Research topics and keywords
│   └── feeds.yaml       # RSS feeds to follow
├── inbox/               # New discoveries awaiting review
├── papers/              # Approved research papers
├── articles/            # Approved blog posts/articles
├── rejected/            # Rejected (for deduplication)
├── scripts/
│   ├── discover.py      # Fetch new papers
│   ├── review.py        # Interactive review CLI
│   └── search.py        # Search your KB
└── CLAUDE.md            # Instructions for Claude Code
```

## Setup

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/research-kb.git
cd research-kb

# Edit topics and feeds for your interests
# config/topics.yaml - keywords, arXiv categories
# config/feeds.yaml - RSS feeds to follow

# Run initial discovery (backfill mode fetches 90 days)
uv run python scripts/discover.py --backfill

# Review inbox
uv run python scripts/review.py
```

## Usage

### Discovery

```bash
# Weekly discovery (default: 7 days)
uv run python scripts/discover.py

# Backfill mode (90 days, more results)
uv run python scripts/discover.py --backfill

# Single topic only
uv run python scripts/discover.py --topic autonomous-driving
```

### Review

**Option 1: Claude Code (recommended)**

Open the project in Claude Code and ask:
- "Show me new papers in my inbox"
- "Review autonomous-driving papers"

Claude will present papers with relevance/complexity ratings and handle approvals.

**Option 2: CLI**

```bash
uv run python scripts/review.py
uv run python scripts/review.py --topic autonomous-driving
```

### Search

```bash
uv run python scripts/search.py "VLA driving"
uv run python scripts/search.py "end-to-end" --topic autonomous-driving
```

## Customization

### Adding Topics

Edit `config/topics.yaml`:

```yaml
topics:
  - name: your-topic
    description: "What this topic covers"
    keywords:
      - "keyword one"
      - "keyword two"
    arxiv_categories:
      - cs.AI
      - cs.LG
```

### Adding RSS Feeds

Edit `config/feeds.yaml`:

```yaml
feeds:
  - name: "Blog Name"
    url: "https://example.com/feed.xml"
    topic: your-topic
```

## Requirements

- Python 3.11+
- [uv](https://github.com/astral-sh/uv) package manager
- (Optional) [Claude Code](https://claude.ai/code) for conversational review

## License

MIT
