# The AI Summary Every Competitor Also Has

**Niche:** [[niches/asset-managers/fundamental-equity-research/profile|Fundamental Equity Research]]
**Industry:** [[industries/asset-managers|Asset Managers]]
**Type:** Fix (Pain Point)
**One-liner:** Managers are paying for generative summaries of public transcripts that every other subscriber receives within the same minute, which by construction confers no edge.
**Tags:** #large-language-models #transformers #word-embeddings #evaluation-metrics #quick-win #data-integration
**Contested on:** Every serious competitor in this niche is fighting to capture and grade the analyst's read of management before the numbers confirm it — and whoever does that turns the most expensive judgment on the research floor into something the firm keeps when the analyst leaves.

## The Problem
The first wave of generative AI on the research floor summarises earnings calls, filings and broker notes. It saves time, and the time saved is real. But the output is identical across every manager using the same vendor, so it accelerates consensus rather than differentiating from it.

## Why It's Still Broken
Vendors can only build on data shared across all clients. The firm's own notes, models and recommendation history — the only inputs that would make a summary specific to this firm's view — sit in separate systems the vendor cannot reach and the firm has not connected.

## What a Fix Looks Like
Point the same models at the firm's own record. Summaries that open with "relative to our thesis" rather than "management said", built by joining vendor transcripts to the firm's notes and model assumptions inside the firm's perimeter. This needs a research store with an API, permissioning by information barrier, and a small integration team — not a new vendor.

## Who Feels the Pain
Analysts reading the same summary as their competitors; CIOs paying for productivity that does not show up as differentiated decisions.

## Impact If Fixed
AI spend on the research floor starts compounding the firm's own knowledge instead of commoditising it.
