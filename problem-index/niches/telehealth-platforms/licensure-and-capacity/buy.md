# Buy: Workforce Management Adapted to State-Constrained Contractor Supply

**Niche:** [[niches/telehealth-platforms/licensure-and-capacity/profile|Licensure, Credentialing & Capacity Matching]]
**Industry:** [[industries/telehealth-platforms|Telehealth Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Contact centre workforce management solves forecasting and scheduling against skill-based routing; here the skill is a state licence that costs money and takes months to acquire.
**Tags:** #time-series-forecasting #convex-optimization #evaluation-metrics #confidence-intervals #data-integration #compliance #automation #revenue-impact
**Contested on:** Whether workforce management built for employed agents with trainable skills can plan a contractor pool whose eligibility is regulatory.

## The Problem

Workforce management is a mature discipline in contact centres. Demand forecasting by interval, skill-based routing, scheduling against service level targets, shrinkage modelling, intraday management and adherence tracking are all well developed, and the analytical core — forecast arrivals, staff to a service level, route by skill — maps closely onto this problem.

Two assumptions break. Skills in a contact centre are trainable in days and cost a training course; a state licence costs hundreds to thousands of dollars, takes weeks to months, and involves a regulatory body. And agents are employees who work assigned shifts; clinicians are contractors who choose their hours and can decline.

## What Already Exists

NICE, Verint, Genesys and the workforce management category, with Erlang-based and simulation staffing models, skill-based routing engines, forecasting modules and intraday management. Credentialing and licensure tracking systems. Scheduling and shift marketplace products from the healthcare staffing world.

## The Customization Gap

**Skill acquisition is a capital decision with a long lead time.** WFM tools model skills as attributes to be scheduled around, with training as an operational adjustment. Here the skill matrix itself is the strategic lever, each change costs money and months, and choosing which to acquire is a portfolio optimisation with no representation in any WFM product.

**Supply is elastic and self-scheduling.** Scheduling engines assign shifts. Here the platform posts availability and clinicians choose, so the planning object is a probability distribution over who logs on, responsive to rate. That requires a supply response model in front of the scheduler — a component WFM assumes away because employees are scheduled.

**Routing constraints are legal, not preferential.** A misrouted call is an inefficiency; a patient seen by a clinician not licensed in their state is a regulatory violation. The constraint must be hard, auditable at the encounter level, and aware of jurisdictional rules that differ by modality and by presentation — a compliance posture no routing engine provides.

**Service level is clinical, not just operational.** Contact centres target answer time. Here the target interacts with clinical urgency — some presentations should not wait — so the queue needs triage-aware prioritisation rather than a uniform service level.

**Demand is seasonal in a clinical way.** Respiratory season, allergy season, weather and school calendars drive state-level demand with patterns that contact centre forecasting modules do not anticipate but handle well once specified with the right regressors.

## Target Customer

Platform workforce operations evaluating WFM tooling, who need to know that the forecasting and staffing engine transfers and the licence portfolio and supply elasticity do not. Also the WFM vendors, for whom licensed contractor marketplaces are an adjacent vertical with a recognisable shape.

## Impact If Solved

The forecasting, staffing-to-service-level and intraday machinery gets bought, and the licence portfolio optimisation, supply response model, hard legal routing constraints and clinical prioritisation get built. The concrete result is planning that accounts for the two things that actually determine capacity here: which states each clinician can serve, and whether they will choose to work.
