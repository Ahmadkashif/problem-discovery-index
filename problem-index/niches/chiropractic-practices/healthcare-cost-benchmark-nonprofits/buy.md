# Coding Normalization Adapted to Procedure Code Churn

**Niche:** [[niches/chiropractic-practices/healthcare-cost-benchmark-nonprofits/profile|Healthcare Cost Benchmark Data Organizations]]
**Industry:** [[industries/chiropractic-practices|Chiropractic Practices]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Healthcare data platforms map code sets between versions; benchmark continuity needs something harder — knowing whether a service is economically the same thing after a code was split into three, and whether the trend line across that boundary means anything.
**Tags:** #bert #transformers #word-embeddings #contrastive-learning #change-point-detection #time-series-forecasting #evaluation-metrics #hypothesis-testing #data-integration #compliance

## The Problem
Benchmarks are longitudinal and the coding system underneath them is not stable. Procedure codes are added, retired, split, merged, and redefined annually; modifier conventions shift; a service billed under one code in one year is billed under two in the next. A trend line computed naively across those boundaries shows movement that is entirely artifact. Analysts handle it with crosswalks and judgment about which historical series remain comparable, maintained document by document, and the judgment is neither recorded with the published series nor consistently applied across the product line. Users receive a continuous-looking series with no indication of where the ground shifted under it.

## What Already Exists
Healthcare data tooling covers the mechanical half well. Code set crosswalk products, terminology servers, and the major healthcare data platforms all handle version mapping, hierarchy navigation, and standard groupers competently. The annual code updates are distributed in machine-readable form and ingesting them is routine.

## The Customization Gap
Crosswalks answer which code replaced which code. Benchmark continuity requires answering whether the underlying service population is economically comparable across the change — and that is an empirical question, not a lookup. When a code splits, the resulting codes may cover different service intensities at different price points, so the pre-split series is comparable to a weighted blend of the post-split ones only if the mix is stable, which is exactly what needs testing. The adaptation is empirical continuity assessment: for every code set change affecting a published series, compare the observed distribution before and after, test whether the change is consistent with a pure relabelling or with a genuine shift in what is being billed, and classify the boundary as continuous, adjustable with a stated method, or genuinely broken. That classification then attaches to the published series, so a user sees where the series is comparable and where it is not. The same machinery detects unannounced changes — shifts in coding behaviour with no corresponding code set update, which are common and currently invisible.

## Target Customer
Heads of data science and methodology at benchmark organizations, and the analysts who maintain crosswalk judgments as documents rather than as tested assertions.

## Impact If Solved
Makes longitudinal claims defensible where they are defensible and honest where they are not, which matters because trend citations are among the most consequential uses of these benchmarks. Detecting unannounced coding behaviour shifts is also a genuine new capability — those shifts currently enter published series as apparent cost trends and nobody catches them.
