# Versioning and Provenance Infrastructure

**Niche:** [[niches/mlops-platforms/experiment-tracking-platforms/profile|Experiment Tracking Platforms]]
**Industry:** [[industries/mlops-platforms|MLOps Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Source control, content-addressed storage and build provenance solved identity and reproducibility decades ago, and ML tracking reimplements weaker versions of all three.
**Tags:** #graph-theory #data-integration #compliance #automation #workflow-orchestration #evaluation-metrics #quick-win
**Contested on:** Not terminal — the contest differs by workload scale, and the decomposition is recorded in the profile.

## The Problem
The question a tracking platform exists to answer — what produced this artefact, and can I get back to it — is the question build systems, package managers and source control answer rigorously. Content addressing gives an artefact an identity derived from its contents. Build provenance attestations record what produced what, verifiably. Hermetic builds make reproduction a guarantee rather than an aspiration. Tracking platforms record a run identifier, a git hash if someone remembered to commit, and a directory of files.

## What Already Exists
Content-addressed object storage and data versioning tools; source control with immutable commit graphs; build provenance and attestation frameworks with a defined supply chain format; hermetic and reproducible build systems; package managers with lock files pinning full transitive dependency sets; and container image registries with immutable digests.

## The Customization Gap
The adaptation is to an artefact produced by a stochastic, long-running, distributed computation. It requires: (1) content addressing for datasets at a scale where hashing the whole thing is expensive, which pushes toward chunk-level or manifest-level identity and is where the existing data versioning tools are weakest; (2) provenance that spans a distributed run with heterogeneous accelerators, since the attestation formats assume a build rather than a thousand-rank job; (3) honest handling of non-determinism, because bit-identical reproduction is frequently impossible on accelerator hardware and the useful guarantee is that the inputs and the procedure were identical rather than that the output matches — stating that distinction clearly is more valuable than pretending otherwise; (4) lock files for the full environment including accelerator libraries and driver versions, which are the dependencies that actually break reproduction and which no ML tool pins; and (5) making provenance capture automatic rather than a call the researcher must remember, since anything optional is absent from exactly the run that later matters.

## Target Customer
Tracking vendors, ML platform teams, regulated organisations needing model provenance, and the supply chain and reproducibility tooling communities.

## Impact If Solved
Provenance and reproducibility are solved rigorously one field over and reimplemented weakly here. Pinning accelerator libraries and driver versions, and stating honestly what reproducibility means under non-determinism, are the two adaptations that would matter most.
