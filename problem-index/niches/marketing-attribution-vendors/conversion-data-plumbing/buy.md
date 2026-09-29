# Data Integration Practice

**Niche:** [[niches/marketing-attribution-vendors/conversion-data-plumbing/profile|Conversion Data Plumbing]]
**Industry:** [[industries/marketing-attribution-vendors|Marketing Attribution Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Data engineering solved reusable ingestion, testing and lineage years ago, and measurement pipelines are hand-built per client with no tests.
**Tags:** #data-integration #workflow-orchestration #automation #evaluation-metrics #compliance #descriptive-statistics #quick-win #confidence-intervals
**Contested on:** Every serious competitor in this niche is fighting to build the conversion record once instead of rebuilding it at every client — and whoever does that owns the input every model in the category depends on.

## The Problem
Modern data engineering has reusable connectors, declarative transformation, automated testing of data quality, lineage tracking, freshness monitoring and orchestration with retries and alerting. The tooling is mature, widely adopted and mostly inexpensive. Measurement vendors' conversion pipelines are frequently hand-written per client, untested, undocumented, unmonitored, and maintained by whoever built them.

## What Already Exists
Reusable ingestion connectors; declarative transformation frameworks with testing; data lineage and documentation generation; freshness and quality monitoring; and orchestration with alerting and retries.

## The Customization Gap
The adaptation is to a pipeline whose correctness is a modelling question rather than a data quality one. It requires: (1) tests that check semantic correctness rather than schema validity, since a conversion pipeline can be technically perfect and count the wrong events — this semantic layer is what generic tooling has no concept of and is where the errors actually are; (2) consent and privacy state propagated through every transformation, which most frameworks treat as a column rather than as a constraint on use; (3) reconciliation against an external financial truth as a standing test, which is unusual in analytics pipelines and is the strongest available check; (4) handling of platform sources that are themselves partly modelled, requiring provenance tracking at the row level; and (5) deployment into client environments the vendor does not control, which constrains the tooling that can be used.

## Target Customer
Measurement vendors, client data teams, and data engineering vendors for whom marketing measurement pipelines are an unserved application.

## Impact If Solved
The tooling is mature and inexpensive and these pipelines are hand-written and untested. Semantic tests that catch counting the wrong events, and financial reconciliation as a standing check, are what generic data quality frameworks do not supply.
