# Completed Job Actuals as Validation on Published Labour Units

**Niche:** [[niches/electrical-contractors/electrical-labor-unit-publishers/profile|Electrical Labour Unit & Estimating Database Publishers]]
**Industry:** [[industries/electrical-contractors|Electrical Contractors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Contractors bid against the published labour units and then record what the work actually took, and none of that returns — so a database of installation times is validated by the studies that produced it and by nothing else.
**Tags:** #gradient-boosting #feature-engineering #evaluation-metrics #cross-validation #causal-inference #confidence-intervals #hypothesis-testing #time-series-forecasting #data-integration #revenue-impact

## The Problem
A labour unit asserts that a task takes this long under these conditions. Contractors estimate against it, win or lose the bid, execute the work, and record actual hours in their job costing — generating, collectively, an enormous body of evidence about whether the assertion holds. The publisher sees none of it. Units are set and revised by study and by expert review, validated against the same process that produced them. The weakest entries are consequently the unusual conditions and infrequent tasks where no researcher has recently looked, which is also where a contractor is most likely to lose money on a bid and least able to check the number.

## Why Nobody Has Built This
Actual labour hours are the most commercially sensitive data a contractor has — they reveal productivity and margin to a market of competitors — so voluntary contribution needs a reason. The analysis is genuinely confounded as well: an actual reflects one crew's productivity, one site's conditions, and one project's management, so naive comparison to a national published unit mixes four things. And a database that drifted toward whatever its contributors experience would be worse rather than better, which is a real risk rather than a hypothetical.

## What to Build
A contribution programme structured so that participating is rational, with the confounders modelled rather than ignored. Contractors contribute estimated-versus-actual hours at task level and receive their own productivity benchmarked against the contributed population — which is something no contractor can get any other way and is the only credible reason to share. Contributions carry site, crew, and condition metadata so that crew productivity, project conditions, and scope variance are separable from the unit's own accuracy. The publisher's output is not an adjusted unit but a validation report per entry: dispersion of observed hours around the published figure, systematic bias where it exists, and identification of entries where dispersion is wide enough that the unit should carry a range. Research effort then concentrates where the evidence shows the database is weak. And the derivative product falls out naturally — published units with an empirical confidence band, which is what an estimator most wants on a tight bid and which no competitor offers.

## Target Customer
VPs of content at estimating database publishers, and the chief estimators at electrical contractors who bid against these units with no measure of their reliability.

## Impact If Built
Converts a database validated by its own method into one validated by outcomes. Confidence bands change what the product is worth on a bid, and the contribution corpus is a moat that deepens with subscriber base — the one asset a competitor entering with better software cannot replicate.
