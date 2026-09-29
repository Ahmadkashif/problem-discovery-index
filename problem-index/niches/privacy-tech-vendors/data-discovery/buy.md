# Buy: Data Catalogues and Lineage, Privacy-Aware

**Niche:** Data Discovery & Mapping
**Industry:** [[industries/privacy-tech-vendors|Privacy Tech Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Data catalogue and lineage tooling already traces where data comes from and goes across the modern stack, built for analytics engineers, with no privacy semantics attached.
**Tags:** #graph-theory #bert #word-embeddings #evaluation-metrics #data-integration #compliance #automation
**Contested on:** Whether the record of where personal data lives and flows is observed from the systems or compiled by asking people.

## The Problem

Tracing data through an organisation's systems is a solved problem in the analytics world. Data catalogues inventory every table and column across warehouses, lakes and pipelines. Lineage tooling traces a column back through every transformation to its source and forward to every dashboard and model that consumes it. Column-level lineage is now standard, and it is exactly the capability a privacy data map requires.

It is built for and sold to data engineering. The catalogue's purpose is helping an analyst find a table and understand where a number came from. Nothing in it knows that a column contains personal data, whose, under what lawful basis or for what purpose, and nothing connects it to a record of processing or to a deletion request.

Meanwhile privacy vendors build their own discovery, which scans for patterns in stores they are pointed at and has no lineage at all — so it can tell you a table contains email addresses and not where those email addresses go next.

The two halves of the map are in different products serving different buyers.

## What Already Exists

Data catalogues and lineage: Collibra, Alation, Atlan, DataHub, OpenMetadata, Amundsen, and the lineage features in Snowflake, Databricks and dbt. Column-level lineage, automated metadata harvesting, ownership and glossary management.

Open lineage standards: OpenLineage, providing a common format for lineage events across tools.

Privacy discovery: BigID, Securiti, and the discovery modules in the larger privacy platforms — pattern-based scanning with classification and some cloud coverage.

Cloud data security posture: Cyera, Sentra, Dig and the DSPM category, which discovers and classifies data across cloud estates and is the closest convergence point between the two worlds.

Application-level tracing: distributed tracing and service mesh telemetry, which describe service-to-service flows and are unused for privacy purposes.

## The Customization Gap

**Catalogues stop at the warehouse boundary.** Lineage within the analytics stack is excellent. Personal data also lives in operational databases, application logs, caches, object storage, SaaS applications and third-party processors, and the catalogue sees none of it. Privacy needs the whole estate and the catalogue covers the well-governed part.

**No privacy semantics.** A catalogue records that a column is a string named `user_email`. It does not record that this is personal data of a data subject, processed under a stated basis for a stated purpose, subject to a retention period and included in three processing activities. That overlay is the adaptation.

**Lineage does not cross the organisational boundary.** The most important privacy flows leave the organisation — to processors, to advertising platforms, across borders. Lineage tooling ends where the data leaves, and that is precisely where privacy obligations begin.

**Purpose is absent everywhere.** Privacy law is built on purpose limitation. No catalogue models purpose, because analytics has no equivalent concept, and mapping observed flows to declared purposes is the hardest and most valuable part of the overlay.

**DSPM is converging from the other direction.** Cloud data security posture products discover and classify data across cloud estates with genuine breadth. They are sold to security, lack lineage depth and privacy semantics, and are the most likely place this convergence actually happens.

**Retention and deletion are unmodelled.** A catalogue tracks where data is. Privacy needs to know how long it should stay and whether it can be removed, which is metadata nothing currently carries.

## Target Customer

The data catalogue vendors — Collibra and Atlan in particular already position around governance — for whom a privacy overlay opens a legal buyer inside accounts they already hold.

DSPM vendors are the more likely adapters on current trajectory, having the estate breadth privacy needs and requiring the lineage and semantics.

The privacy platforms themselves should be consuming lineage rather than rebuilding discovery badly, and the OpenLineage standard makes that integration straightforward.

## Impact If Solved

The two halves of the map stop being in separate products. Lineage without privacy semantics and privacy discovery without lineage each solve part of a problem that neither solves alone.

Extending lineage past the organisational boundary — to processors, advertising destinations and cross-border transfers — is where the privacy value concentrates and where all current tooling stops.

And attaching purpose and retention to catalogue entries would make the record of processing a view over live metadata rather than a document assembled by interview, which is the whole transformation this niche needs.
