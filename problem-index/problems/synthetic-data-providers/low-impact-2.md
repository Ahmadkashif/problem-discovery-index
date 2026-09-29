# Domain-Specific Generation Constraints

**Industry:** [[synthetic-data-providers|Synthetic Data Providers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** General-purpose generators produce statistically faithful nonsense in regulated domains, because a clinician or an underwriter can spot an impossible record instantly and no generic model knows what is impossible.
**Tags:** #large-language-models #bayesian-inference #hypothesis-testing #evaluation-metrics #feature-engineering #transfer-learning #compliance

## The Problem
Synthetic healthcare data must contain plausible clinical trajectories: a diagnosis, then the tests that follow it, then treatments consistent with the diagnosis, at intervals that reflect how care actually happens, with lab values inside physiological ranges and moving in directions the condition implies.

A generic generator matches marginal distributions and pairwise correlations. It produces records where a patient receives a treatment before the diagnosis that indicates it, where lab values are individually normal and jointly impossible, where a medication appears with a contraindicated comorbidity.

The same holds elsewhere. Synthetic financial transaction data with no merchant category coherence, no realistic recurring payment structure and no plausible balance evolution is useless for testing fraud systems. Synthetic industrial sensor data that ignores physical conservation laws is useless for testing anomaly detection.

The domain expert reviewing the output rejects it in minutes, and the vendor's solutions engineer begins encoding domain rules by hand — for that customer, for that schema, again.

## What Already Exists
Clinical terminology systems (SNOMED, ICD, LOINC, RxNorm) encode relationships between diagnoses, procedures, medications and observations, and are machine readable. Clinical quality measure logic encodes care pathways explicitly. Financial data standards define transaction structures. Physical simulation is mature in industrial domains. Rule engines can enforce constraints once someone writes them. Several vendors offer healthcare-specific configurations.

## The Customisation Gap
The knowledge exists in ontologies and the generators do not use it. SNOMED encodes that a procedure is indicated for a condition; nothing connects that to the generation process, so the model must learn clinical coherence from the training data alone and learns it incompletely from any realistic sample size.

Temporal pathway structure is the sharper gap. Real clinical data is a sequence of events with dependencies — this test follows that symptom, this medication is titrated over these intervals — and generic tabular synthesis treats a patient's record as a set of correlated fields rather than as a trajectory. Sequence models handle this naturally and are not what most tabular products use.

Validation by domain rule is entirely missing. Whether generated records violate known clinical, financial or physical constraints is checkable automatically against the same ontologies, and the check is not run, which is why the domain expert becomes the validation step.

The reusability gap compounds it. The same clinical constraints apply at every healthcare customer, and each engagement encodes them again because nothing accumulates them as a shared asset.

## Impact If Solved
Regulated domains are where synthetic data is most needed, because the real data cannot be shared, and they are where generic generation fails most visibly. Grounding generation in existing domain ontologies and validating against them converts repeated bespoke rule-writing into a domain module that improves with every engagement.
