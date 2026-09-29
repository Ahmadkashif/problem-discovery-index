# The Warehouse Took the Middle Out

**Niche:** [[niches/customer-data-platforms/the-platform-architecture/profile|The Platform Architecture]]
**Industry:** [[industries/customer-data-platforms|Customer Data Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The warehouse became where customer data lives and activation now runs from it directly, which removed the packaged platform's reason to exist and left its vendors repositioning onto the function nobody has validated.
**Tags:** #data-integration #workflow-orchestration #evaluation-metrics #compliance #automation #graph-theory #descriptive-statistics #revenue-impact
**Contested on:** This niche is not terminal — the packaged platform and the warehouse-native stack compete on different things for different buyers, and they are stated separately in the sub-niches.

## The Problem
A packaged customer data platform collects events, stores them, resolves identity and activates to downstream tools. Organisations then built warehouses containing the same customer data, modelled better, governed centrally and joined to everything else the business knows. Activating from there directly is cheaper, avoids a second copy and keeps the data inside the governance boundary. The packaged platform's middle layer — storage and modelling — became redundant, and its vendors repositioned onto identity resolution, which is the function with no accuracy metric. The category is now competing on its least validated component while buyers cannot tell the two architectures apart.

## Why Nobody Has Built This
Incumbents cannot credibly advocate the architecture that removes their product, so nobody with authority in the category will state the choice plainly — the repositioning is commercially rational and leaves buyers unadvised. Warehouse-native vendors are newer and lack identity capability, so neither side offers a complete answer. Buyers compare feature lists across incompatible models. And the category name covers both, which prevents the comparison being framed correctly.

## What to Build
State the architectural choice and serve both sides of it well. Publish a clear account of which organisations should use which model — data team maturity, warehouse presence, governance requirements, activation breadth, time to value — which is the guidance nobody with standing will give and is immediately valuable to every buyer. Build identity as a component usable in either architecture, since it is the genuinely hard part and is currently bundled into one model and missing from the other. Make governance work across the boundary, because the split architecture leaves consent, retention and access controls in two places and that is where the failures will be. Support migration in both directions, as organisations are moving and the migration is currently a project with no tooling. Keep the customer's data in their own boundary where they want it, which is an increasing requirement and is a structural advantage for one model that the other can partially adopt. Match the packaged model's time to value in the composable one, since that is its real weakness and is why smaller organisations still buy packaged. Handle real-time activation from a warehouse, which is the composable model's genuine technical gap. Make the activation destination catalogue a commodity both models share, since breadth is a maintenance burden rather than a differentiator. Price to the architecture rather than to volume, because volume pricing is what the warehouse-native model undercuts. And measure what an organisation actually gains from each, since the decision is currently made on vendor narrative.

## Target Customer
Data platform leadership choosing an architecture, packaged and composable vendors, and the organisations running both while paying for one twice.

## Impact If Built
Incumbents cannot advocate the architecture that removes their product, so buyers compare incompatible models with no disinterested guidance. Building identity as a component usable in either architecture serves the genuinely hard part that one model bundles and the other lacks.
