# Variance Analysis From Management Accounting

**Niche:** [[niches/cloud-cost-management/finance-facing-chargeback/profile|Finance-Facing Allocation & Chargeback]]
**Industry:** [[industries/cloud-cost-management|Cloud Cost Management]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Management accounting decomposes a variance into price, volume and mix and has done for a century, and cloud cost tools report the largest movers.
**Tags:** #descriptive-statistics #linear-regression #hypothesis-testing #confidence-intervals #evaluation-metrics #time-series-forecasting #revenue-impact #automation
**Contested on:** Every serious competitor here is fighting to produce a cloud allocation that reconciles to the invoice, survives audit and forecasts accurately enough to plan against — and whoever does that takes the finance account, because a number that does not add up is worse than no number.

## The Problem
A cost line is up by a substantial amount. Management accounting has a standard answer to why: separate the effect of price, of volume and of mix, and report each, so the reader knows whether more was consumed, it cost more per unit, or the composition shifted. Cloud cost tools report the resources whose cost increased most, which conflates all three and leaves the finance business partner to reconstruct the explanation by hand every month.

## What Already Exists
Variance decomposition methodology from management accounting, taught universally and implemented in every enterprise planning system; contribution and mix analysis; seasonal adjustment; and attribution methods that assign a total change to contributing factors. All standard and none of it novel.

## The Customization Gap
The adaptation is to cloud consumption with a complicated rate structure. It requires: (1) a genuine price-versus-volume split, which is harder than it looks because the effective rate changes with commitment coverage, negotiated discounts and tier thresholds — so a bill that rose because coverage lapsed is a price variance and one that rose because usage grew is a volume variance, and they require completely different responses; (2) mix as a first-class component, since moving workloads between instance families, storage classes or regions changes the blended rate without anyone consuming more, and this is a large and frequently misdiagnosed source of variance; (3) attribution to a cause rather than to a resource, joining the variance to deployments, configuration changes and business events, which is what turns a decomposition into an explanation; (4) materiality thresholds, since a bill has thousands of line items and a complete decomposition is unreadable — the useful output is the three factors that explain most of the change; and (5) a narrative output, because the consumer is preparing an explanation for an executive and a table is an input to that rather than the answer.

## Target Customer
Finance and technology business management functions, cost management vendors, and the enterprise planning vendors for whom cloud is an increasingly awkward cost line.

## Impact If Solved
A century-old decomposition answers exactly the question asked every month and is not applied. The price-versus-volume split under a variable rate structure is the genuine adaptation, and mix is the component most often misdiagnosed.
