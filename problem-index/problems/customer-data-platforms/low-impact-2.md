# Event Schema Governance

**Industry:** [[customer-data-platforms|Customer Data Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** The whole system depends on product teams sending consistent events, product teams ship weekly, and the tracking plan is a spreadsheet nobody updates.
**Tags:** #change-point-detection #bert #word-embeddings #gradient-boosting #time-series-forecasting #evaluation-metrics #data-integration #workflow-orchestration

## The Problem
A CDP's value rests on an event stream produced by engineers who are shipping product features, not maintaining an analytics contract. Events get renamed in a refactor. A property changes type from string to integer. A new platform team implements checkout tracking with its own naming convention. A release removes an event entirely because the component that fired it was replaced.

Nothing breaks loudly. The pipeline accepts whatever arrives. Downstream, an audience returns fewer people each week, a lifecycle journey stops triggering, a conversion metric drifts, and a report shows a decline that gets investigated as a business problem for a fortnight before someone checks the events.

The same problem appears as inconsistency rather than absence. Three teams send a purchase event with three different names, or one name with different property sets per platform, so a single analysis requires knowing the history of who implemented what. That knowledge exists in one or two people.

## What Already Exists
Segment Protocols provides tracking plans with schema validation and violation reporting; Avo offers design-time schema management with CI integration; mParticle and Tealium have their own data quality features. Warehouse-native stacks lean on dbt tests and contracts. Schema registries are standard practice in event-streaming infrastructure generally. Most organisations have a tracking plan document, and most of those documents are out of date.

## The Customisation Gap
Validation tools check conformance to a declared schema, which helps only where the schema is declared, current and enforced — and the binding failure is that the declaration and reality drift apart continuously. What is needed sits earlier and later: detecting that reality has changed, and inferring what the change means.

Detection is a monitoring problem with a clear shape. Every event has an expected arrival rate with known seasonality; a departure is an incident, and correlating it with deployment history usually names the cause. Property-level distribution shifts — a field that was always populated becoming half null, a categorical gaining a new value — are equally detectable and equally unmonitored.

Semantic mapping is the harder half. When one team ships `order_completed` and another ships `purchase`, something must recognise they are the same concept, propose a mapping, and let a human confirm. That is inference over event names, property structure and behavioural position in the session, and it is what makes governance survivable in an organisation where enforcement across every product team is not politically achievable.

The blast radius view is the third piece: before an engineer renames an event, they should be able to see which audiences, journeys and reports depend on it. That lineage exists in the CDP's own configuration and is not exposed where the change is being made.

## Impact If Solved
Silent schema drift is the most common cause of customer data systems degrading, and its cost is paid in misdiagnosed business declines and campaigns that stopped working without anyone knowing. Arrival monitoring with deployment correlation catches it the same day; semantic mapping makes a heterogeneous organisation's data usable without winning a governance argument first; and dependency visibility at the moment of change prevents the breakage rather than detecting it.
