# Supply Chain Traceability and Chain of Custody

**Niche:** [[niches/data-marketplace-brokers/provenance-and-consent-evidence/profile|Provenance & Consent Evidence]]
**Industry:** [[industries/data-marketplace-brokers|Data Marketplace Brokers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Food safety, pharmaceuticals, conflict minerals and forensic evidence all built chain-of-custody systems that survive audit, and data provenance is a questionnaire.
**Tags:** #compliance #graph-theory #data-integration #automation #workflow-orchestration #evaluation-metrics #descriptive-statistics #quick-win
**Contested on:** Every serious competitor in this niche is fighting to replace a contractual warranty about lawful collection with evidence a buyer can rely on — and whoever does that takes the account, because the buyer now carries the regulatory risk and a warranty does not discharge it.

## The Problem
Proving that a thing came from where it is claimed to have come from, through a chain of custodians, in a form that withstands audit and litigation, is a solved institutional problem in several regulated industries. Pharmaceutical serialisation tracks a unit through the distribution chain. Food traceability supports recall to the batch. Conflict minerals schemes audit upstream suppliers. Forensic chain of custody is designed to survive cross-examination. Data provenance is a supplier-completed form.

## What Already Exists
Pharmaceutical track-and-trace with serialisation and verification; food traceability standards with batch-level recall capability; responsible sourcing schemes with upstream auditing and certification; forensic chain-of-custody procedures; software bill-of-materials formats with transitive dependency declaration; and third-party certification and audit institutions.

## The Customization Gap
The adaptation is to an asset that is copied rather than moved and that aggregates. It requires: (1) provenance that composes under merging, since a derived dataset's origins are the union of its inputs' and no physical traceability system has to handle an asset that combines — this composition is the distinctive technical requirement and is where chains break today; (2) the bill-of-materials analogy taken seriously, since a dataset assembled from four sources is structurally identical to a software artefact with dependencies and the format work is largely transferable; (3) record-level rather than batch-level granularity where consent differs between individuals, which is finer than any physical scheme requires; (4) an audit and certification institution, since every successful traceability scheme has one and this market has none — which is the missing piece that no individual participant can supply; and (5) propagation of a downstream event, such as a withdrawal, backwards and forwards through the chain, which physical recall systems do and data systems do not.

## Target Customer
Data providers, marketplaces, compliance functions, certification bodies, and regulators designing provenance obligations.

## Impact If Solved
Chain of custody is an institutional solved problem in several industries and this market has a questionnaire. Provenance that composes under merging is the distinctive requirement, and the absence of a certification institution is the gap no single participant can fill.
