# Buy: Retention and Deletion From the Data Platforms

**Niche:** The Engineer Who Must Delete It
**Industry:** [[industries/privacy-tech-vendors|Privacy Tech Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Modern data platforms added time-travel, partition management and retention controls for operational reasons, and none of it is exposed as a subject-keyed deletion capability.
**Tags:** #evaluation-metrics #compliance #data-integration #automation #workflow-orchestration #graph-theory
**Contested on:** Whether deletion is a capability the systems were built with, or a script an engineer writes each time.

## The Problem

The data platforms have most of the primitives. Modern table formats support row-level deletes, merge operations and partition rewriting. Time travel and versioning exist. Retention policies can expire data automatically. Streaming platforms support compaction by key. Object stores have lifecycle rules. Search engines support document deletion.

What none of them has is a subject-keyed deletion capability: given an identifier for a person, remove everything belonging to them from this system and confirm it is gone. Every primitive needed exists and the assembly does not, so each organisation assembles it by hand in a script.

The gap is also conceptual. Time travel, which exists so that a mistaken transformation can be rolled back, is directly at odds with deletion — a row deleted today remains accessible through time travel for the retention window, and most engineers performing a deletion have not considered it. The platforms provide the feature and do not surface the interaction.

## What Already Exists

Table formats: Delta Lake, Apache Iceberg and Apache Hudi, all supporting row-level deletes, merge operations, partition evolution and time travel with configurable retention.

Warehouses: Snowflake, BigQuery and Databricks, with delete support, time travel and retention controls, and varying degrees of guidance on privacy deletion.

Streaming: Kafka with log compaction by key and tombstone records — a genuine deletion primitive keyed by identifier, used for state management rather than for privacy.

Object and file storage: lifecycle policies, versioning and object lock, the last of which is deliberate immutability.

Change data capture: Debezium and equivalents propagating deletes downstream, used for consistency and not for privacy.

Search and caches: document deletion and invalidation primitives everywhere.

## The Customization Gap

**Nothing is subject-keyed.** Every primitive operates on rows, partitions, keys or objects. Nothing operates on a person across the estate, which is the operation privacy requires and the assembly nobody provides.

**Time travel is a deletion trap.** Deleted rows remain accessible through versioning for the retention period, and the platforms do not warn about this in a privacy context. It is the most common unnoticed failure in warehouse deletion.

**Kafka compaction is the right primitive with the wrong framing.** Tombstone records delete by key and are documented for state management. The same mechanism serves privacy deletion and almost nobody uses it that way.

**CDC propagation is not wired to privacy.** Deletes propagate downstream for consistency. Connecting privacy deletion to the same mechanism would solve downstream persistence and is unbuilt.

**Verification is not offered.** No platform provides a confirm-absence operation after deletion, though the query is trivial and the assurance is what the engineer actually needs.

**Unstructured and log data is served worst.** Application logs holding identifiers in free text are among the most common places data survives, and no platform offers anything for it.

**Guidance is thin.** The platform vendors publish little on privacy deletion patterns, which is why every customer improvises.

## Target Customer

The data platform vendors — Databricks, Snowflake, Confluent and the table format communities — for whom a subject-keyed deletion capability is a natural feature their customers already build badly and repeatedly.

Data engineering leadership at request-heavy organisations, who would adopt a supported capability immediately over maintaining scripts.

The privacy platforms as integrators, calling a platform deletion capability rather than routing a ticket to a human.

## Impact If Solved

The primitives already exist; assembling them into a subject-keyed operation is the missing product, which makes this an unusually tractable gap.

Surfacing the time-travel interaction alone would prevent the most common silent failure in warehouse deletion, and it is a documentation and warning change.

And wiring change data capture to privacy deletion would handle downstream propagation with a mechanism already deployed for other reasons, closing the place where deleted data most often survives.
