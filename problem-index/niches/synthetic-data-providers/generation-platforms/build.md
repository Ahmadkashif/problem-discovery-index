# A Platform Claim That Does Not Survive the Modality Split

**Niche:** [[niches/synthetic-data-providers/generation-platforms/profile|Generation Platforms]]
**Industry:** [[industries/synthetic-data-providers|Synthetic Data Providers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Vendors sell a general generation platform and the thing that determines whether the output works differs completely between tabular and sensor data, so the general claim is never the thing being bought.
**Tags:** #gans #diffusion-models #vaes #evaluation-metrics #transfer-learning #data-integration #cross-validation #probability-distributions
**Contested on:** Not terminal — the contest differs by data modality, and the decomposition is recorded in the profile.

## The Problem
A vendor positions as a synthetic data platform and demonstrates on both a customer table and a rendered street scene. A buyer with a forty-table warehouse asks whether foreign keys and business rules survive generation. A buyer training a perception model asks whether a model trained on the renders will work on the real camera. Both questions are the whole purchase, neither is answered by the platform claim, and the engineering required to answer them shares nothing. The general platform is a packaging decision and the contest is one level down.

## Why Nobody Has Built This
The general positioning is commercially useful — it addresses a larger market and supports a higher valuation than either modality alone. The two modalities require genuinely different expertise, so a vendor strong in one is usually weak in the other and prefers not to invite the comparison. And the field's benchmarks are modality-general, which lets a general claim be evidenced with numbers that do not reach either question.

## What to Build
Build for the modality and say so. The honest platform is a shared substrate — orchestration, connectors, versioning, access control, evaluation harness plumbing — under two genuinely different generation engines, each competing on its own terms. What is missing at the platform layer proper is the connective tissue that is modality-independent and that nobody treats as a product: lineage from synthetic record back to the generation run, the configuration and the source snapshot, which is what an auditor asks for and what almost no vendor can produce. Reproducibility, so that a dataset can be regenerated identically two years later when a regulator asks, which requires pinning the model, the seed, the source state and the library versions. Versioning and drift detection on the source, since a generator trained on last year's data silently stops representing this year's and nothing in the category notices. Evaluation as a pipeline stage that gates the release rather than a report attached to it. And a change log on the generator itself, since customers frequently cannot tell whether an output difference came from their data or from a vendor model update.

## Target Customer
Data platform teams licensing generation, the vendors building it, and the audit and compliance functions who will eventually ask where a record came from.

## Impact If Built
The general platform claim is never what is bought and the substrate that genuinely is modality-independent — lineage, reproducibility, source drift — is the part nobody has productised.
