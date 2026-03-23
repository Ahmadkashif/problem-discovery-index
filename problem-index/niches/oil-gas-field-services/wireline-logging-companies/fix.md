# Petrophysical Interpretation Consistency Across Analysts

**Niche:** [[niches/oil-gas-field-services/wireline-logging-companies/profile|Wireline Logging Companies]]
**Industry:** [[industries/oil-gas-field-services|Oil & Gas Field Services]]
**Type:** Fix (Pain Point)
**One-liner:** Two petrophysicists interpreting the same well log produce different net pay estimates 40-60% of the time because parameter selection, cutoff criteria, and interpretation models are personal choices, not standardized.
**Tags:** #gradient-boosting #anomaly-detection #tabular-ml #compliance #worker-facing

## The Problem
A wireline logging company delivers a well log to an operator. Petrophysicist A interprets 45 feet of net pay with average porosity of 8.5% and average water saturation of 42%. Petrophysicist B, given the same log, interprets 62 feet of net pay with average porosity of 9.8% and average water saturation of 38%. The difference: A used a higher porosity cutoff (7% vs. 5%), a different shale volume model, and applied a more conservative saturation calculation. Both interpretations are technically defensible. But the 17-foot difference in net pay changes the well's economic forecast by $2-5M and directly affects completion design decisions. The operator has no way to evaluate which interpretation is "better" without running both through production data and waiting months for results.

## Why It's Still Broken
Petrophysical interpretation is part science, part art. Multiple valid interpretation methodologies exist for every step (porosity calculation, saturation model, cutoff selection), and industry standards (SPWLA, API) provide guidelines but not prescriptive requirements. Each petrophysicist develops preferences based on their training, the basins they have worked in, and their personal experience with which methods produce interpretations that best match production data. There is no standardized "right answer" for interpretation, making quality assurance difficult — a QA reviewer can check for errors but cannot objectively determine which of two valid interpretations is superior without production validation.

## What a Fix Looks Like
An interpretation consistency framework that: establishes company-wide or basin-wide standard parameter sets and interpretation workflows (the "baseline" interpretation), automatically flags interpretations that deviate significantly from the baseline (e.g., "your net pay is 30% higher than the baseline — your porosity cutoff is 2% lower than the company standard, is this intentional?"), requires documentation of deviations with justification, and tracks which interpretation approaches best predict actual production outcomes over time. The system does not enforce a single interpretation but creates transparency around differences and learns which approaches are most accurate.

## Who Feels the Pain
Operators who receive inconsistent interpretations from different logging companies or different analysts within the same company, petrophysics managers who cannot quality-control interpretation consistency across their team, and completion engineers who make $1-10M investment decisions based on interpretations with undisclosed uncertainty ranges.

## Impact If Fixed
Reduces interpretation variability by 40-60% through baseline standardization, identifies the highest-accuracy interpretation approaches through production validation tracking, and provides operators with uncertainty quantification on net pay estimates — enabling risk-informed completion investment decisions.
