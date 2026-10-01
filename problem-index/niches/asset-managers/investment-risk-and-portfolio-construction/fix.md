# The Risk Report Nobody Reads

**Niche:** [[niches/asset-managers/investment-risk-and-portfolio-construction/profile|Investment Risk & Portfolio Construction]]
**Industry:** [[industries/asset-managers|Asset Managers]]
**Type:** Fix (Pain Point)
**One-liner:** Risk analysts produce thirty-page monthly packs of exposures that PMs skim, because nothing in them says what changed and why it matters.
**Tags:** #large-language-models #descriptive-statistics #change-point-detection #worker-facing #quick-win #automation
**Contested on:** Every serious competitor in this niche is fighting to make the ex-ante risk forecast something a portfolio manager believes — explaining why realised tracking error and drawdowns differed from the model — and whoever does that becomes the risk system PMs actually consult before trading.

## The Problem
The monthly risk pack lists active factor exposures, top contributors to risk, sector and country bets, liquidity buckets and stress results, for every portfolio. Most of it is unchanged from last month. The analyst's real insight — this portfolio's momentum exposure has doubled because three names rallied, not because the PM chose it — is buried or absent.

## Why It's Still Broken
Report templates are built for completeness, because compliance and boards want coverage. Writing the narrative takes the analyst's time, which is consumed by producing the pack.

## What a Fix Looks Like
Generate the pack automatically and lead with a short, ranked list of material changes, each explained by decomposition into PM trades versus market drift, drafted by a language model from the numbers and checked by the analyst. Track which items PMs click into, and use that to tune materiality.

## Who Feels the Pain
Risk analysts producing reports nobody reads; PMs missing unintended bets.

## Impact If Fixed
Risk communication shifts from coverage to signal, and the analyst's time moves from production to judgment.
