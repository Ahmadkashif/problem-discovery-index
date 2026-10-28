# A Net-Income-per-Space Bridge for Every Facility

**Niche:** [[niches/parking-operators/commercial-garage-management/profile|Commercial & Mixed-Use Garage Management]]
**Industry:** [[industries/parking-operators|Parking Operators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Owners see net parking income per space move every month and get a list of reasons, not a decomposition of what the operator's decisions contributed.
**Tags:** #causal-inference #gradient-boosting #time-series-forecasting #feature-engineering #revenue-impact #data-integration
**Contested on:** Every serious competitor in this niche is fighting to return the most parking income per space to the owner after fees and expenses, and whoever delivers the highest net parking income per space against the owner's budget takes the account.

## The Problem
When a garage misses its budget the asset manager asks why. The operator answers with remote work, a lost event or a new competitor, all plausible and none quantified. The owner cannot separate what the market did from what the operator did: rate changes, monthly-contract sales, marketplace exposure, staffing hours, the move to gateless entry.

## Why Nobody Has Built This
Operators report revenue and expenses, not decisions, so there is nothing to attribute to. Data is split between PARCS, channels, billing and payroll, and at managed sites it belongs to the owner, which discourages operators from pooling it into comparisons. Owners with a handful of garages lack the analysts to do it themselves.

## What to Build
A monthly bridge per facility from last year's net income per space to this year's, split into market demand (estimated from comparable facilities and public sources such as city meter occupancy), rate effect, mix shift between transient, monthly and event, channel commissions, labour and other expenses, and contract fees. Rate effects are estimated against counterfactual days, with the operator's logged rate decisions as treatments. The owner sees which lines the operator controlled and how they moved.

## Target Customer
Regional vice presidents at national and regional operators defending renewals; asset managers at REITs, institutions and cities with 10–100 garages.

## Impact If Built
If a decomposition lets an operator correct one weak lever per facility worth 2% of net income (estimate), a region of 50 garages at ~$1M net income each gains ~$1M a year for its owners, and the operator walks into renewals with numbers instead of reasons.
