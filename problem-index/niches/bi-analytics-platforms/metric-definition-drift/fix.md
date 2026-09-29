# The Glossary Nobody Connected to the Queries

**Niche:** [[niches/bi-analytics-platforms/metric-definition-drift/profile|Metric Definition Drift]]
**Industry:** [[industries/bi-analytics-platforms|BI & Analytics Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Every organisation has a business glossary stating what churn means, written once, and nothing checks whether any query computes it that way.
**Tags:** #descriptive-statistics #word-embeddings #evaluation-metrics #confidence-intervals #hypothesis-testing #data-integration #quick-win #compliance
**Contested on:** Every serious competitor in this niche is fighting to guarantee that two things called revenue are the same number, and to detect it from the query logic when they are not — and whoever does that takes the account, because the meeting that reconciles instead of deciding is the category's most visible failure.

## The Problem
A data governance initiative produces a glossary: ninety business terms, each with a careful prose definition agreed across departments over several months. It is published in the catalogue. It is read during onboarding and never again, because it describes intent while every dashboard implements logic, and nothing connects the two. Two years later the glossary says churn is measured on a rolling ninety-day basis and the three dashboards that report churn use thirty, sixty and ninety, and the glossary is not wrong so much as inert.

## Why It's Still Broken
Glossaries are produced by governance programmes whose deliverable is the document, and the document is the point at which the programme ends. Connecting a prose definition to query logic requires someone to map each term to the assets implementing it, which is manual, large and never budgeted. Catalogues support the linkage as a feature and leave the population of it to the customer, which means it is populated for the first twenty terms and abandoned. And no one is accountable for the glossary being true, only for it existing.

## What a Fix Looks Like
Connect the glossary to the estate and report conformance. Map each glossary term to the assets that claim to implement it, proposed automatically from names, aliases, descriptions and column references and confirmed by a person — which turns an impossible manual mapping into an afternoon of review. Report per term how many assets implement it, how many implementations differ, and which ones diverge from the stated definition, which converts the glossary from a document into a measurement. Show the definition in context, so the person looking at the dashboard sees what the metric is supposed to mean at the moment they are reading the number, rather than in a catalogue they will not visit. Flag orphaned terms that nothing implements and orphaned metrics that no term defines, both of which are informative — the first suggests governance describing work nobody does, the second names the metrics that most need a definition. And measure staleness, because a glossary whose terms have not been reviewed since the business changed is worse than none, since it is cited.

## Who Feels the Pain
Governance teams whose central artefact is ignored; analysts who inherit a metric with no authoritative definition; and executives making decisions on numbers whose meaning nobody has checked against the agreed one.

## Impact If Fixed
Glossaries are near-universal, near-universally inert, and the conformance report is the smallest change that makes one consequential. Proposed mapping with human confirmation is what makes the linkage feasible at all, and the orphaned-metric list is a governance backlog derived from evidence rather than from a workshop.
