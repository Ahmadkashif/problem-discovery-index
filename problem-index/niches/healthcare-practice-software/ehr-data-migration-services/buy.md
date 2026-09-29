# Data Quality Tooling Adapted to Clinical Fidelity

**Niche:** [[niches/healthcare-practice-software/ehr-data-migration-services/profile|EHR Data Migration & Conversion]]
**Industry:** [[industries/healthcare-practice-software|Healthcare Practice Software]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Data profiling and reconciliation tooling is a mature commodity from the data engineering world, and migration validation in healthcare is still done by counting rows and spot-checking twenty charts.
**Tags:** #descriptive-statistics #hypothesis-testing #evaluation-metrics #confidence-intervals #dimensionality-reduction #data-integration #compliance #automation
**Contested on:** Every serious competitor in EHR migration is fighting to map an unfamiliar legacy database to a target schema with clinical fidelity and without a consultant hand-reading tables — and whoever maps fastest with the fewest post-go-live surprises takes the account.

## The Problem
Validation of a completed migration is typically a row count per table and a manual review of a small sample of charts chosen by the practice. Row counts prove nothing about fidelity: a medication list can migrate with the right number of rows and the wrong discontinued flags, so a chart shows a patient still on a drug they stopped two years ago. Sample review finds only what is in the sample. The defects that matter are systematic and confined to a subpopulation — the patients whose records predate a workflow change, the allergies entered as free text — which is exactly the shape a small random sample misses.

## What Already Exists
Great Expectations, dbt tests, Soda, Monte Carlo and the general data-observability category provide column profiling, distributional comparison, null and cardinality checks, referential integrity validation and assertion frameworks, all mature and mostly open source. Healthcare integration engines provide transformation and logging. The generic tooling covers every structural check a migration needs and none of the clinical ones.

## The Customization Gap
The adaptation is to define fidelity clinically and then let the commodity tooling test it. It requires: (1) a clinical assertion library — active medication counts per patient must match, allergy severity must survive, problem list onset dates must not drift, encounter counts per provider per month must reconcile — expressed as testable properties rather than as row counts; (2) distributional comparison by cohort rather than in aggregate, since the systematic defects live in subpopulations and vanish in a total; (3) stratified sampling for the human review, deliberately oversampling the old, the complex and the structurally unusual records instead of sampling uniformly; (4) reconciliation of the financial side to the cent, because a migrated A/R that is close is not migrated; and (5) a signed-off fidelity report the practice can read, which is what converts go-live from an act of faith into an accepted deliverable.

## Target Customer
EHR vendors and conversion firms performing migrations, and the practices themselves, who currently accept a migration on the basis of a spot check and discover the defects in clinic.

## Impact If Solved
Cohort-level distributional testing finds systematic defects before go-live rather than in the first week of clinic, which is the difference between a correction and a crisis. Most of the tooling is free; the investment is in writing the clinical assertions once, and they are reusable across every migration the vendor ever performs.
