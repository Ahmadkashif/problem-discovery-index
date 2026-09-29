# A System That Survives the Handover

**Niche:** [[niches/product-design-studios/design-system-durability/profile|Design System Durability]]
**Industry:** [[industries/product-design-studios|Product Design Studios]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The deliverable starts decaying the week it is delivered and nobody is there to see it.
**Tags:** #automation #workflow-orchestration #data-integration #evaluation-metrics #compliance #graph-theory #descriptive-statistics #change-point-detection
**Contested on:** Every serious competitor in this niche is fighting to deliver a design system that does not begin drifting from the client's production code the week the studio leaves — and whoever makes it durable takes the account.

## The Problem
A design system is delivered as two artefacts that must stay in agreement with a third: a design library, a documentation site, and the client's production code. Nothing keeps them aligned. Developers approximate components under deadline, designers create one-off variants, the documentation is updated by nobody. The system degrades continuously and invisibly, and the product it was meant to unify slowly reverts to what it was.

## Why Nobody Has Built This
The studio's engagement ends at handover and maintenance was not sold. Design tools and code have no shared representation of a component. Drift is gradual and nobody owns noticing. And the client has no design system function to hand it to.

## What to Build
Make drift visible and give the client something they can run. Detect divergence between the design library and the production implementation automatically, which is the core and turns an invisible decay into a reported number. Measure component adoption in the live product — which parts use the system and which do not — since that is the honest measure of whether the system is working. Generate the documentation from the implementation rather than maintaining it separately, which removes the fastest-decaying artefact entirely. Provide a governance process the client can operate without the studio, as the absence of ownership is the actual cause. Support token and primitive synchronisation between design and code, which is the layer where alignment is achievable. Flag one-off components created outside the system so they can be absorbed or rejected deliberately. Report system health on a schedule to a named owner, which is what makes decay a decision rather than an accident. Design for contribution by the client's developers, since a system only they can consume and never extend will be abandoned. Sell a maintenance relationship on the evidence of measured drift, which is a far easier sale than a speculative retainer. And make the handover a transfer of ownership rather than a delivery of files.

## Target Customer
Design studios and consultancy design arms, client design system teams, in-house design organisations, and design tooling vendors.

## Impact If Built
The system degrades continuously and invisibly and the product reverts, which is the commonest way a studio's work is judged to have failed. Automatic drift detection with adoption measurement turns that into a reported number with an owner.
