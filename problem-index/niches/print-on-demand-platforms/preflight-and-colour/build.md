# Checking Resolution, Not What Goes Wrong

**Niche:** [[niches/print-on-demand-platforms/preflight-and-colour/profile|Preflight & Colour]]
**Industry:** [[industries/print-on-demand-platforms|Print on Demand Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Preflight tooling is a mature discipline in commercial printing and the version shipped here checks resolution and dimensions, which are not what causes customers to complain.
**Tags:** #numerical-methods #evaluation-metrics #object-detection #automation #confidence-intervals #descriptive-statistics #cnns #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to make the file check catch the things customers actually complain about — and whoever does that stops the reprints, because the current check passes almost everything that later fails.

## The Problem
A file passes preflight: three hundred dots per inch, correct dimensions, supported format. It contains a drop shadow with transparency that the raster processor will flatten against white, producing a grey box on a black shirt; a hairline border below the minimum reproducible stroke width; a brand red outside the achievable gamut; and a composition that will straddle a seam on the larger sizes. Four defects, all mechanically detectable, all missed, all producing a complaint. The check that ran verified two properties that have almost no relationship to whether the print will be acceptable.

## Why Nobody Has Built This
The preflight was written as file validation by engineers rather than as process verification by printers, and resolution is the check everybody knows. The remaining checks require a process profile and a product geometry model, neither of which the platform maintained. Adding checks increases the rejection rate at upload, which is friction in the growth funnel. And the defects it misses appear as production problems rather than as preflight failures.

## What to Build
Check against the process and the product, not against the file. Verify the artwork against the achievable gamut for its intended process and substrate, reporting the specific colours that will shift and what they will become, which is the largest single miss and requires the profiles the colour work builds. Check minimum feature size against the process — stroke width, text size, gap width — which is a simple geometric analysis against a documented process limit and catches the fill-in and drop-out failures. Validate placement against the product's geometry for every size, since a design that fits the medium fails on the extra-large and nobody checks the size range. Resolve transparency, blending and colour space explicitly and report what will happen rather than letting the raster processor decide silently, which the fix note develops. Check light artwork against dark substrates and the underbase behaviour, since that interaction is a recurring complaint and is deterministic. Report every finding to the merchant in plain language with the consequence, rather than as a technical pass or fail. Rank by severity so the merchant fixes what matters. Offer automatic correction where it is safe. And measure the preflight's own effectiveness by the share of complaints it would have caught, which is computable from history and is the number that should govern which checks exist.

## Target Customer
Platform prepress and engineering, merchants uploading artwork, and the production facilities absorbing what preflight lets through.

## Impact If Built
The check verifies two properties with almost no relationship to acceptability while four detectable defects pass. Measuring preflight against the share of actual complaints it would have caught is computable from history and is the number that should decide which checks exist.
