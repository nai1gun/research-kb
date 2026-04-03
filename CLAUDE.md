# Research Knowledge Base - Claude Instructions

This is a personal research knowledge base for tracking papers and articles on autonomous driving and HMI topics.

## Interaction Model

The primary way to interact with this KB is through Claude Code conversation, not CLI scripts. When the user asks to review papers or work with the KB:

### Paper Review Format

Present papers in a **scannable table** with ratings:

```
| # | Title | Relevance | Complexity | TLDR |
|---|-------|-----------|------------|------|
| 1 | **ShortName** | ⭐⭐⭐ High | 🔶 Intermediate | 1-2 sentence summary |
```

**Relevance** (to user's topic):
- ⭐⭐⭐ High - Directly addresses the topic
- ⭐⭐ Medium - Related concepts, transferable ideas  
- ⭐ Low - Tangential or false positive

**Complexity**:
- 🟢 Entry - Survey, tutorial, accessible explanations
- 🔶 Intermediate - Standard research paper, some background needed
- 🔴 Advanced - Heavy math, assumes deep domain knowledge

**User preference:** Entry/intermediate papers are interesting even if topic match is partial. Advanced papers only worth it if topic is a perfect match.

### After Presenting Papers

1. List recommended actions (approve/consider/reject with brief reasoning)
2. Offer options: approve batch, show more, or deep-dive on specific paper

### Deep Dive Format

When user requests deep dive on a paper:

1. **Header:** Full title, authors, links (arXiv, PDF, code)
2. **Problem Statement:** What gap does it address?
3. **Key Contribution:** 2-3 bullets
4. **Technical Approach:** Table format
5. **Results:** Benchmarks and metrics
6. **Why It Matters:** Connect to user's context (Alpamayo, VLAs, their hardware)
7. **Comparison:** To related work the user knows

### File Operations

When user says "approve" or "reject":
- Approved papers: Move from `inbox/` to `papers/<topic>/`
- Rejected papers: Move from `inbox/` to `rejected/`

## Discovery

Run `uv run python scripts/discover.py` to fetch new papers. Use `--backfill` for initial seeding.

## Topics

Current topics of interest (defined in `config/topics.yaml`):
- **autonomous-driving**: E2E systems, VLAs, perception, planning, world models
- **hmi**: Human-machine interaction in autonomous vehicles, trust, takeover

## User Context

Interests: End-to-end autonomous driving, VLA models, practical deployment on consumer hardware
