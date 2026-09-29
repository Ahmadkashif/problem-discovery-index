# Effort Reported in Person-Weeks

**Niche:** [[niches/ai-red-teaming-firms/coverage-measurement/profile|Coverage Measurement]]
**Industry:** [[industries/ai-red-teaming-firms|AI Red Teaming Firms]]
**Type:** Fix (Pain Point)
**One-liner:** The only quantity in an assessment report is how long the engagement lasted, which is a measure of what the client paid rather than of what was examined.
**Tags:** #evaluation-metrics #descriptive-statistics #confidence-intervals #compliance #hypothesis-testing #quick-win #worker-facing #monte-carlo-methods
**Contested on:** Every serious competitor in this niche is fighting to say what fraction of a system's risk surface an assessment examined — and whoever does that takes the market, because without it a clean report is an assertion and with it it is evidence.

## The Problem
Two firms assess the same system for four weeks each. One spends most of that time on a systematic sweep across a broad harm taxonomy and finds three medium findings. The other spends it on deep exploration of one promising area and finds one critical. Both reports say four weeks. A client comparing them, or comparing this year's assessment to last year's, has one number that means nothing about what was done. Procurement selects on price per week, which rewards breadth-free cheapness, and the firms doing systematic work cannot demonstrate it.

## Why It's Still Broken
Person-weeks is what gets billed, so it is what gets recorded. Recording effort by harm category and technique requires researchers to track their time against a taxonomy, which is administrative overhead nobody wants during an engagement. There is no shared taxonomy to track against. And clients have not asked, because they do not know a better report is possible.

## What a Fix Looks Like
Report what the time was spent on. Track effort against harm category and technique class during the engagement, at a coarse granularity that costs a researcher a minute a day, and report the grid — which converts an opaque duration into a picture of the assessment and is the fix. Report findings alongside effort per cell, so a reader can see which areas were examined hard and yielded nothing, which is the informative combination. Report the queries or probes attempted per category as a second effort dimension, since machine-assisted exploration and human hours are different currencies. Publish the taxonomy used, so a reader knows the shape of the grid. Report what was deliberately excluded and on whose instruction, since scope exclusions requested by a client are common and invisible in the current format. Make the effort record a standard report section, which any firm can adopt unilaterally and which immediately differentiates thorough work from cursory work. Compare against the firm's own historical assessments of similar systems, giving a reader a reference. And resist reporting a single coverage percentage, since a fabricated denominator is worse than an honest grid.

## Who Feels the Pain
Clients comparing incomparable reports; firms whose systematic work is indistinguishable from a cheaper competitor's; and regulators receiving documents whose only quantity is a billing figure.

## Impact If Fixed
A coarse effort grid across harm categories and techniques costs a researcher a minute a day and converts an opaque duration into a picture of the assessment. Reporting effort and findings together is what lets a reader see where the system was examined hard and held.
