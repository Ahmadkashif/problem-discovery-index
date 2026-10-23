# Module Findings Forecast at Induction

**Niche:** [[niches/aircraft-mro-shops/llp-workscope-planning/profile|LLP & Workscope Planning]]
**Industry:** [[industries/aircraft-mro-shops|Aircraft MRO & FBO Shops]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A shop quotes a workscope from hours, cycles and the removal reason, and learns at teardown that a module it planned to inspect needs full restoration.
**Tags:** #gradient-boosting #survival-analysis #feature-engineering #confidence-intervals #revenue-impact #tacit-knowledge-ml
**Contested on:** Every serious competitor in this niche is fighting to build each engine to the cheapest workscope that still delivers the on-wing life the owner needs, with every life-limited part proven back to birth, and whoever predicts module findings and remaining part lives most accurately at induction takes the account.

## The Problem
Senior powerplant engineers carry a feel for what a given engine will show when opened: this operator's hot-and-high routes eat high-pressure turbine blades, this thrust rating cracks combustor liners at a certain cycle count, an engine that was "quick-turned" last time will need more now. That judgement drives the initial workscope and the quote, and it is rarely written down or checked against what teardown later found.

## Why Nobody Has Built This
Shops keep teardown findings in inspection reports and non-conformance records, coded inconsistently by module and cause. The OEMs that hold fleet-wide findings use them inside their own programmes. Independent shops have seen workscope prediction as engineering craft, and the data cleaning looked bigger than the payoff until turn times and parts scarcity made surprises expensive.

## What to Build
A findings model trained on the shop's own history: for each module, the probability of each finding class (within limits, repairable, scrap) and the expected restoration cost, given engine type, thrust rating, cycles since last visit, operator and route environment, on-wing borescope findings and trend margins. It pairs with an LLP build planner that chooses which parts to replace so the engine reaches a target interval at the lowest cost. The engineer sees the forecast with the past engines it is based on, then adjusts and records why. Those adjustments are the senior engineers' tacit judgement, captured for the first time.

## Target Customer
Powerplant engineering directors at independent engine shops; technical managers at lessors and operators who specify workscopes and want to check a shop's quote.

## Impact If Built
Halving unplanned workscope growth on ~200 visits a year (estimate) would cut quote-change rounds and late parts orders. At ~$100,000–$200,000 a month in spare-engine cost, every week saved per affected visit is worth ~$25,000–$50,000 to the owner and a stronger renewal case for the shop.
