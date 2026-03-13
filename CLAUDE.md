# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This project generates a structured Obsidian knowledge graph of industry problems worth solving. There are two complementary specs:

1. **CLAUDE_CODE_SPEC.md** — A simpler approach: Claude reasons from its own knowledge to generate a static problem index across ~120 industries. Uses `generate.ts` with the Anthropic SDK, processing industries in batches with bookmark-based crash recovery.

2. **industry-problem-miner.md** — A more advanced pipeline approach with 5 stages: industry seeding → signal collection (Reddit, G2, job posts via web scraping) → LLM pain extraction → engineering filter scoring → two-agent debate engine. Full TypeScript codebase with `src/stages/`, `src/types/`, `src/utils/`.

**No source code has been written yet.** Both files are specs/blueprints.

## Architecture (When Implemented)

### Simple Generator (CLAUDE_CODE_SPEC.md)
- Single entry point: `generate.ts`
- Depends on `industries.ts` for the ordered industry list
- Output: `problem-index/` directory with `_bookmark.md` (state), `_index.md` (master index), `industries/*.md`, `problems/{industry-id}/*.md`
- Each industry produces 6 API calls (1 profile + 5 problem cards)
- `_bookmark.md` tracks completed/in-progress/queued industries for crash recovery

### Pipeline (industry-problem-miner.md)
- 5-stage pipeline orchestrated by `src/orchestrator.ts`
- Stages: `stage1-industries.ts` → `stage2-signals.ts` → `stage3-extraction.ts` → `stage4-scoring.ts` → `stage5-debate.ts`
- Uses `src/utils/llm.ts` (Anthropic wrapper), `src/utils/scraper.ts` (HTTP + rate limiting), `src/utils/storage.ts` (JSON persistence)
- Output: `output/` directory with per-industry JSON results and final `problem-index.json`

## Commands (When Implemented)

```bash
# Simple generator
npm install @anthropic-ai/sdk tsx typescript
npx tsx generate.ts

# Pipeline (uses pnpm)
pnpm install
pnpm run pipeline           # full pipeline
pnpm run pipeline:stage2    # individual stages
pnpm run pipeline:resume    # resume from checkpoint

# Check progress
cat problem-index/_bookmark.md
```

## Key Concepts

- **Problem types:** high-impact (industry-transforming), low-impact (customization of generic solutions), worker-life (individual worker quality-of-life)
- **155 industries** listed in CLAUDE_CODE_SPEC.md (120 unique after deduplication), grouped into 22 categories
- All output files use Obsidian `[[wiki-link]]` syntax for graph navigation
- Rate limit strategy: 1.5s between API calls, configurable BATCH_SIZE (3-10 industries per run)

## Environment

- Requires `ANTHROPIC_API_KEY` environment variable
- Pipeline spec also requires `REDDIT_CLIENT_ID`, `REDDIT_CLIENT_SECRET` for signal collection
