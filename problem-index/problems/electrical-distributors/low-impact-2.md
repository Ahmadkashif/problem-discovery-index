# Wire Quotes Priced Off Yesterday's Copper

**Industry:** [[electrical-distributors|Electrical Distributors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Price optimisation software sets customer prices by segment and elasticity; wire and cable need a price tied to the day's copper, a hold period the contractor accepts, and a check on every open quote when the metal moves.
**Tags:** #time-series-forecasting #exponential-smoothing #linear-regression #feature-engineering #revenue-impact #automation #data-integration

## The Problem
Building wire, MC cable, feeder cable and bare copper are some of the largest categories an electrical distributor sells (~15–25% of sales, estimate), and copper is most of their cost (~60–80% for building wire, estimate). Wire manufacturers reprice off COMEX copper as often as daily and publish price sheets; distributors carry reels bought at one cost and quote contractors at another. A contractor's bid price for a job's wire is set weeks before the wire is bought, so every wire quote carries a hold period — hours for a counter price, days for a project quote — and every order placed after that window should be repriced.

In practice, wire quotes are priced by a few people who watch copper, and open quotes are rarely revisited when the metal moves. A quote held for a week at the old price loses its margin if copper jumps; an order released months later against a stale quote is filled at a loss, or the contractor disputes the reprice. Copper has been unusually volatile: a 50% Section 232 tariff on semi-finished copper and derivatives, including wire and cable, took effect on 1 August 2025 and moved to full value in April 2026, and COMEX copper set a record settlement of ~$6.9/lb in September 2026 (search summary).

## What Already Exists
Price optimisation software such as Zilliant, PROS and Vendavo sets customer-specific prices from segment, elasticity and margin targets; Epicor Eclipse and other ERPs apply matrix pricing and cost updates; manufacturers publish copper-based price sheets; commodity brokers and hedge advisors serve firms large enough to hedge, as mapped under [[commodity-brokers|Commodity Brokers]].

## The Customisation Gap
Wire needs cost-plus pricing indexed to a live copper reference with the manufacturer's adder, explicit hold periods per quote type and customer, escalation clauses written into project quotes, reel and cut-length handling (a 2,500-foot reel versus 500 feet cut at the counter), tariff pass-through on imported cable, and a sweep that flags every open quote and unreleased project order whose margin has fallen below floor since copper moved. Generic optimisers treat wire as just another product class with a stable cost, which is exactly what it is not.

## Impact If Solved
Holding wire margin through copper swings protects a category worth tens of millions of dollars a year at a mid-size distributor (estimate), and replaces a few people's watchfulness with a rule that applies to every quote, branch and salesperson.
