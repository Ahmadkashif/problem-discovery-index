# The Report Says What Happened and Never What It Is Worth

**Niche:** [[niches/auto-dealers-independent/vehicle-history-report-providers/profile|Vehicle History Report Providers]]
**Industry:** [[industries/auto-dealers-independent|Independent Auto Dealers]]
**Type:** Fix (Pain Point)
**One-liner:** The provider holds decades of vehicle histories and the resale outcomes that followed, and still hands the dealer a list of events with no estimate of what any of them did to the price.
**Tags:** #gradient-boosting #causal-inference #feature-engineering #evaluation-metrics #cross-validation #confidence-intervals #survival-analysis #revenue-impact #data-integration #worker-facing

## The Problem
An independent dealer looking at a history report is asking one question: what should I pay. The report answers a different one. It lists events — an accident of unspecified severity, a branded title, four owners, a gap in service records — and leaves the dealer to convert that into a number using instinct developed over years of buying. Instinct is what the report was supposed to replace. Two dealers reading the identical report reach materially different bids, and neither can say which is right, because the translation from history to value has never been made available to them. The provider is uniquely positioned to make it: it observes the same vehicles again at subsequent transactions and can see what histories did to price, at a scale no dealer ever accumulates.

## Why It's Still Broken
The product was conceived as disclosure rather than valuation, and disclosure has a defensible boundary — reporting what a source said carries much less liability than asserting what a vehicle is worth. That boundary has hardened into product strategy. Attribution is also genuinely hard: the price effect of an accident depends on severity, repair quality, and how the market reads the disclosure, and severity is the field the underlying records most often lack. And there is a channel consideration, in that valuation is the territory of the guide publishers, some of whom are partners. The result is that the party holding the best history-to-outcome data in the industry publishes none of the analysis.

## What a Fix Looks Like
An impact layer over the existing report that estimates the price effect of the vehicle's actual history, with uncertainty stated. Built from the provider's own longitudinal data — vehicles observed at multiple transactions, with histories known between them — and controlled for the obvious confounders, since vehicles that get damaged are not a random sample. The output is not a value but a delta against an otherwise-comparable vehicle, expressed as a range: what this history is worth, on this configuration, in this market, with this much confidence. Severity, the field that most limits the estimate, is inferred where records are silent using the signals that do exist — claim amount bands, repair operation counts, structural versus cosmetic indicators — with the inference explicit rather than hidden. The layer stays advisory and clearly separated from the reported facts, which preserves the disclosure product's position while finally answering the question the buyer is actually asking.

## Who Feels the Pain
Dealers converting history to price by feel and dispersing bids accordingly; consumers who cannot tell whether a disclosed accident should cost the seller two hundred dollars or two thousand; lenders taking collateral whose history discount is guessed at; and the provider, which holds the data to settle all of it and ships a list.

## Impact If Fixed
Moves the product from disclosure to decision support, which is a different and much larger budget — a dealer pays a few dollars for a report and would pay considerably more for a defensible acquisition delta. The underlying analysis is also the strongest possible demonstration of the corpus's value, and it is the one thing a competitor with comparable event coverage but shallower history cannot reproduce.
