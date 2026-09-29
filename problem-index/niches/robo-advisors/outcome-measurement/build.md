# What the Platform Actually Added

**Niche:** [[niches/robo-advisors/outcome-measurement/profile|Outcome Measurement]]
**Industry:** [[industries/robo-advisors|Robo-Advisors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every input needed to say what this client gained from being here rather than in a single index fund is in the platform's own records, and no client has ever been told.
**Tags:** #causal-inference #monte-carlo-methods #evaluation-metrics #confidence-intervals #revenue-impact #descriptive-statistics #hypothesis-testing #gradient-boosting
**Contested on:** Every serious competitor in this niche is fighting to tell each client what the platform actually delivered for them, net of fees, taxes and their own behaviour, against a stated alternative — and whoever publishes that number first makes every competitor's marketing average look like what it is.

## The Problem
A client wants to know whether this was worth it. The platform shows them a return, which is mostly the market. The question they are actually asking — what did I get from being here rather than buying a total market fund and doing nothing — requires decomposing the outcome into rebalancing, harvesting, allocation, fees and the client's own timing decisions. Every component is computable from records the platform holds. None of it is computed, because the answer would be uncomfortable for some clients and the marketing average is easier.

## Why Nobody Has Built This
Reporting was built to show performance, which is what brokerage statements show, so the frame was inherited rather than chosen — and a value-added frame requires stating a counterfactual, which invites a comparison nobody wanted to invite. The behaviour cost component implicates the client, which is delicate. The components sit across investment, tax and product. And no competitor has done it, so there is no pressure.

## What to Build
Decompose the outcome and report it honestly. Define the counterfactual explicitly — a simple index portfolio bought and held — since a value-added number means nothing without one and stating it is the decision the category has avoided. Attribute the return to rebalancing, allocation, harvesting, fees and client timing, which is the core and is standard attribution arithmetic over complete records. Quantify the client's own timing cost in dollars, because it is usually the largest single component and no client has ever seen theirs. Net the fee against the contribution plainly, as a value figure that excludes the fee is not a value figure. Express uncertainty where components are estimates, particularly the tax benefit, rather than asserting precision. Report the distribution across clients internally, since the average conceals that the platform adds a great deal for some and little for others. Use the finding to target the product, because the clients where value is low are where the product should change. Deliver the number to the client in a form they can act on, which is the retention argument and the trust argument at once. Accept that it will be negative for some clients, as publishing an honest number including the bad cases is precisely what makes it credible. And replace the marketing average with a measured distribution, which is a durable competitive position.

## Target Customer
Investment and marketing leadership, clients asking whether the fee is justified, regulators interested in value disclosure, and competitors relying on simulated averages.

## Impact If Built
Reporting inherited the brokerage performance frame and a value-added frame requires naming a counterfactual nobody wanted to name. The attribution is standard arithmetic over records the platform already holds.
