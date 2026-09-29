# The Customer Who Quietly Stopped Buying

**Niche:** [[niches/b2b-commerce-platforms/purchasing-pattern-intelligence/profile|Purchasing Pattern Intelligence]]
**Industry:** [[industries/b2b-commerce-platforms|B2B Commerce Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A customer who ordered every three weeks for nine years stops, and the distributor notices eleven months later when someone runs an annual report.
**Tags:** #change-point-detection #survival-analysis #time-series-forecasting #revenue-impact #evaluation-metrics #confidence-intervals #quick-win #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to predict what a business customer will order next from the cleanest repeat-purchase record in commerce — and whoever does it accurately enough to act on owns the reorder before the customer initiates it.

## The Problem
B2B attrition is silent. There is no cancellation, no notice, no negative event — the orders simply become less frequent, then smaller, then stop. A line item that was reordered monthly for six years moves to a competitor and everything else continues, so the account total barely moves and nobody looks. By the time an annual review surfaces it the relationship has been rebuilt elsewhere and the customer has no reason to come back. The signal was in the data from the first missed cycle, and the distributor's reporting is built on totals and periods, which is precisely the shape that hides it.

## Why It's Still Broken
Reporting aggregates by month and by account, and gradual erosion is invisible at that resolution. Nobody defines what a missed cycle is, because nobody has modelled the cycle. Reps cover too many accounts to notice per-line changes. And the loss is attributed to market conditions at review time, which closes the question.

## What a Fix Looks Like
Detect the break in the pattern at the line level. Establish an expected reorder interval per customer and part, then alert when an order is overdue by a meaningful multiple of it — which is the entire mechanism and needs only the interval estimate the build note produces. Watch line-level erosion rather than account totals, since partial defection is the common case and totals conceal it completely. Distinguish a paused customer from a lost line, because a contractor between projects and an account that switched supplier need opposite responses and conflating them wastes the rep's attention. Alert the rep with the specific evidence — this part, this cycle, this many weeks late — rather than a churn score, which is what makes the call happen. Trigger at the first missed cycle rather than at a quarterly review, since recovery probability falls sharply with elapsed time and the whole value is in earliness. Correlate breaks across customers to detect a competitor's move or a supply problem, which turns individual alerts into a market signal. Track recovery outcomes so the organisation learns which interventions work. And report attrition as a first-class number alongside new business, because it is currently the only major revenue movement nobody measures.

## Who Feels the Pain
Distributors losing accounts they never noticed leaving; reps blamed for erosion they had no visibility of; and customers whose growing dissatisfaction produced no response until it was final.

## Impact If Fixed
Monthly account totals are exactly the shape that hides line-level erosion, and the signal was present from the first missed cycle. Alerting with the specific part and the specific overdue interval is what turns a churn score nobody calls on into a call the rep makes.
