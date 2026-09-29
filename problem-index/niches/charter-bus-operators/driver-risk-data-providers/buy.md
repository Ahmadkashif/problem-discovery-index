# Record Normalization Adapted to Fifty State Violation Codes

**Niche:** [[niches/charter-bus-operators/driver-risk-data-providers/profile|Commercial Driver Risk Data Providers]]
**Industry:** [[industries/charter-bus-operators|Charter Bus Operators]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** ETL and data quality platforms normalize schemas; the problem here is semantic — the same driving behaviour is a different offence code with different severity in every state, and the mapping is maintained by hand.
**Tags:** #bert #transformers #word-embeddings #contrastive-learning #random-forests #evaluation-metrics #feature-engineering #automation #data-integration #workflow-orchestration

## The Problem
Every score depends on translating a state motor vehicle record into a common violation taxonomy, and that translation is where the errors live. Each state maintains its own offence codes, its own severity conventions, its own abbreviations, and its own reporting formats, and revises them without coordination or notice. Analysts maintain the mapping by hand, state by state, and a code that changes meaning quietly produces a silently wrong score for every driver in that state until someone notices. Because the mapping sits upstream of everything, an error here is both the most consequential and the least visible failure the product has, and the maintenance backlog never closes.

## What Already Exists
Data integration tooling is mature and cheap. Fivetran, dbt, Airbyte, and the cloud ETL services handle ingestion, schema evolution, and transformation testing well; the data quality platforms detect format and distribution anomalies; reference data management products handle code list versioning competently. For moving and reshaping records, everything needed exists.

## The Customization Gap
All of these treat a code as a value to be mapped. The mapping problem here is semantic and evidential: deciding that a state's newly introduced code corresponds to an existing severity tier requires reading the statutory description, comparing it to how equivalent conduct is coded elsewhere, and — the part no tool supports — checking whether drivers receiving it behave like drivers receiving the codes it was mapped to. The adaptation is a violation ontology with statutory descriptions attached, semantic matching that proposes a mapping for a new or changed code from its text and from how comparable codes are mapped in other states, and empirical validation that compares the outcome profile of a newly mapped code against its assigned tier — which is the only way to catch a mapping that is textually plausible and behaviourally wrong. Change detection has to watch state code lists continuously rather than on a refresh schedule, since the failure mode is a mapping that silently stops being correct. And every mapping decision needs a versioned record, because a score computed last year must remain explicable when it is challenged.

## Target Customer
Heads of data operations and taxonomy leads at driver monitoring bureaus, and the analysts who currently maintain fifty state mappings by hand against a permanent backlog.

## Impact If Solved
Closes the largest silent error source in the product and removes a permanent manual burden at the same time. Empirical mapping validation also produces something genuinely new — evidence that the taxonomy is behaviourally coherent across states, which is the assumption every multi-state risk score makes and none currently tests.
