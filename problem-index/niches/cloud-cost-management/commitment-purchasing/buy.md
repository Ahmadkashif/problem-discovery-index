# Portfolio Optimisation Under Uncertainty

**Niche:** [[niches/cloud-cost-management/commitment-purchasing/profile|Commitment Purchasing]]
**Industry:** [[industries/cloud-cost-management|Cloud Cost Management]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Hedging uncertain future demand with a portfolio of instruments at different terms and discounts is a solved financial problem, and cloud commitments are chosen from a coverage percentage.
**Tags:** #convex-optimization #monte-carlo-methods #bayesian-inference #time-series-forecasting #confidence-intervals #optimization-fundamentals #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor here is fighting to turn a multi-year capacity commitment into a decision made under stated uncertainty rather than an extrapolation of last quarter — and whoever does that takes the largest single controllable lever in the category.

## The Problem
Committing to future consumption at a discount, with instruments of different durations and flexibility, against uncertain demand, with an option to wait — this is the structure of a commodity hedging problem, and energy, agriculture and airlines have all solved it with established methods. Cloud commitment purchasing has the identical structure and is decided by looking at a coverage percentage against a recommendation from the last month.

## What Already Exists
Portfolio optimisation under uncertainty with risk measures; stochastic and robust optimisation formulations; real options valuation, which prices the option to wait directly; Monte Carlo simulation for scenario evaluation; demand forecasting with distributional output; and the commodity hedging literature and practice. All established and taught.

## The Customization Gap
The adaptation is to cloud instruments and an engineering-driven demand. It requires: (1) a demand model driven by architectural plans rather than by price and season, since cloud usage changes because somebody re-architected something, which is knowable in advance and is entirely unlike a commodity demand curve; (2) accurate instrument modelling, since the flexibility rules — what a savings plan covers, how a reserved instance can be modified or exchanged, regional and family scope — determine the entire trade-off and are intricate enough that most tools simplify them away; (3) an explicit risk preference elicited from the organisation rather than assumed, because the right coverage depends on tolerance for stranded commitment and the tools currently choose on the customer's behalf; (4) option value computation, since the ability to commit at any time is a genuine option and waiting a quarter for better information is frequently worth more than the discount forgone — an insight the category does not articulate at all; and (5) laddering as a structural recommendation, which is standard practice in fixed income and is done by hand here when it is done.

## Target Customer
Cloud economics and treasury functions, cost management vendors, commitment marketplaces, and the financial planning vendors for whom this is an adjacent problem they already understand.

## Impact If Solved
An established hedging discipline maps almost exactly onto this decision and is not applied to the largest controllable lever in the category. Architectural-plan-driven demand and option valuation are the two adaptations, and the second is not even discussed in the current practice.
