# Twenty Years of Forecasts Are Archived as Pages, Not Claims

**Niche:** [[niches/alterations-tailoring/apparel-trend-forecasting/profile|Apparel Trend Forecasting Services]]
**Industry:** [[industries/alterations-tailoring|Alterations & Tailoring]]
**Type:** Fix (Pain Point)
**One-liner:** The firm's entire intellectual history is stored as published layouts, searchable by keyword and season, so an analyst cannot ask what the house has previously said about a silhouette without reading twenty years of pages.
**Tags:** #bert #transformers #large-language-models #word-embeddings #graph-neural-networks #dimensionality-reduction #evaluation-metrics #tacit-knowledge-ml #data-integration #workflow-orchestration

## The Problem
Two decades of forecasts, trend reports, colour cards, and market analyses exist as published artifacts — beautifully produced, keyword-searchable, and analytically inert. The information an analyst actually needs from them is not in a form that can be retrieved: which claims the house made about a given attribute over time, how its position shifted, which arguments it used, what evidence it cited. Answering "have we called this before, and what did we say" means someone remembering roughly when, then reading. In practice nobody does it, so the house re-argues positions it has already taken, contradicts itself across categories without noticing, and cannot show a subscriber the through-line of its own thinking. The archive is simultaneously the firm's deepest asset and functionally unreadable at analytical resolution.

## Why It's Still Broken
The publishing system was built to produce and deliver pages, and the archive is a by-product of publishing rather than a designed asset. Content was authored as layout, so the semantic structure — which paragraph is a claim, which is supporting evidence, which subject a colour story refers to — was never captured and cannot be recovered from formatting. The vocabulary also moved: terms the house used in 2008 have been superseded, so even keyword search fails on the older half. And because no one is accountable for the archive as a product, the cost of restructuring it has never had an owner willing to carry it.

## What a Fix Looks Like
Retrospective structuring of the archive into a claim graph: each historical forecast decomposed into its subjects, positions, and supporting arguments, with subjects resolved against a controlled attribute vocabulary that carries its own synonym history so 2008 terminology and 2026 terminology reach the same node. Claims link to the claims they revise, extend, or contradict, which is what makes the house's evolving position on any attribute traversable in a single view. Going forward, structure is captured at authoring time as a by-product of the writing rather than as a retrofit — the analyst names the subject and the direction of the call as part of composing it. With that in place, an analyst opening a new season sees the house's prior positions on the attribute, when they shifted, and on what basis; an editor can find contradictions between categories before publication rather than after a subscriber notices; and the archive becomes queryable in the way that supports scoring, which is the precondition for the firm ever measuring its own accuracy.

## Who Feels the Pain
Analysts re-deriving positions the house already holds; editors responsible for coherence across a publication volume no individual can read; senior staff who function as the archive's index and are the bottleneck on every question about precedent; and subscribers who buy a long-view service from a firm that cannot itself retrieve its long view.

## Impact If Fixed
Converts published output into a compounding asset instead of a stack of finished work. Consistency becomes checkable, which is a direct quality gain in a product whose credibility rests on the appearance of a coherent point of view. And the structured claim history is the substrate everything else needs — accuracy scoring, trained attribute extraction, and any retrieval-based assistance to analysts all require the archive to be claims rather than pages, so this is the fix that unblocks the others.
