# What It Was Actually Worth to This Client

**Niche:** [[niches/robo-advisors/tax-loss-harvesting/profile|Tax-Loss Harvesting]]
**Industry:** [[industries/robo-advisors|Robo-Advisors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The headline benefit is an average from a simulation, and no client has ever been told what harvesting did for them.
**Tags:** #monte-carlo-methods #confidence-intervals #evaluation-metrics #gradient-boosting #revenue-impact #descriptive-statistics #hypothesis-testing #compliance
**Contested on:** Every serious competitor in this niche is fighting to prove what harvesting actually delivered for this specific client after wash-sale exposure they cannot see — and whoever can state a per-client realised number replaces an industry-wide average that applies to almost nobody.

## The Problem
The marketing says harvesting adds some number of basis points a year. That number comes from a backtest over a market path that did not happen, at a tax rate that is not this client's, assuming a realisation pattern that may never occur. For a client in a low bracket who never sells, harvesting may be worth nothing or less than nothing after the basis reduction. For a high-bracket client with regular gains it may be worth a great deal. The platform harvests identically for both and reports the same average to each.

## Why Nobody Has Built This
The average is a marketing asset, so measuring per client creates a number that will be smaller for many of them — and there is no commercial pressure to produce it. Realised value depends on future events, which makes it feel unmeasurable rather than estimable. Marginal rate is not reliably known. And the accounting required to attribute the benefit properly sits between investment, tax and product functions.

## What to Build
Attribute the benefit per client. Track realised harvesting activity per client — losses harvested, basis reduced, offsets used, carryforwards — which is the core and is bookkeeping the platform can do today from its own records. Estimate the client's marginal rate rather than assuming one, since it is the single largest determinant and can be inferred or simply asked. Model the deferral value explicitly, because the benefit is a timing benefit and reporting gross harvested losses as a gain is misleading. Project realisation scenarios rather than asserting one, as the honest answer is a range conditioned on what the client eventually does. Report the number to the client with its assumptions visible, which is the deliverable and is what no competitor offers. Identify the clients for whom harvesting is not worth doing, since harvesting them anyway costs them basis and costs the platform trading. Measure the substitute security's tracking cost against the tax benefit, because the cost side is currently uncounted. Detect when a client's situation changes the calculation, such as a bracket change or a large expected gain. Feed the realised numbers back into the marketing claim, so the published figure is an observation rather than a simulation. And report distribution rather than average, which is the honest form and is a differentiator in itself.

## Target Customer
Investment and product leadership, clients who have never seen a figure that applies to them, tax preparers reconciling the activity, and competitors whose marketing rests on the same untested average.

## Impact If Built
The average is a marketing asset and measuring per client produces a smaller number for many, so nothing drove it. The activity is already recorded, and attributing it per client is bookkeeping rather than research.
