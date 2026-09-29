# The Chain That Breaks at Promotion

**Niche:** [[niches/software-supply-chain-security/artefact-provenance-integrity/profile|Artefact Provenance & Integrity]]
**Industry:** [[industries/software-supply-chain-security|Software Supply Chain Security]]
**Type:** Fix (Pain Point)
**One-liner:** An artefact is signed at build, re-tagged when promoted between registries, and arrives in production with a provenance chain that no longer resolves.
**Tags:** #graph-theory #descriptive-statistics #evaluation-metrics #confidence-intervals #hypothesis-testing #compliance #quick-win #data-integration
**Contested on:** Every serious competitor here is fighting to prove that what is running was built from what was reviewed, by an authorised process, from known inputs — and whoever does that takes the platform and compliance account, because regulation is now asking and nobody can answer.

## The Problem
A build produces a signed image with a provenance attestation. The image is promoted from the development registry to the staging registry, re-tagged, then promoted to production, then mirrored into an air-gapped environment. At each step the digest is preserved or it is not, the attestation is copied or it is not, and the tag no longer corresponds to what was signed. In production the verification either fails, which blocks a deployment for a reason nobody can explain, or is not attempted, which is the common resolution. The chain broke at a promotion nobody thought of as a security event.

## Why It's Still Broken
Promotion is a registry operation performed by a pipeline step that predates the signing initiative, and it moves an image without any awareness that attestations are attached elsewhere. Attestations are stored alongside artefacts in ways that vary by registry, so a copy operation that preserves the image may not preserve the attestation. Mirroring into constrained environments is a bulk operation with its own tooling. And the break is silent until somebody verifies, which — as the build note describes — is frequently nobody.

## What a Fix Looks Like
Make promotion provenance-aware. Preserve the digest through every promotion and never rebuild for promotion, which is the single most important practice and is frequently violated by pipelines that rebuild per environment — a rebuilt artefact is a different artefact and its provenance is a different chain. Copy attestations with the artefact as an atomic operation, which requires the promotion tooling to know they exist and is a straightforward change to a pipeline step. Verify at each promotion rather than only at the end, so a break is detected at the step that caused it rather than three environments later. Handle mirroring and air-gapped transfer explicitly, since the bulk import path is where attestations are most often lost and is also where verification matters most. Attest the promotion itself, so the chain records who promoted what to where, which is a question auditors ask and which the existing chain does not answer. Report chain integrity across the estate — what proportion of production artefacts have a resolvable chain back to a reviewed source — which is the honest coverage measure and is usually much lower than the signing adoption suggests. And make rebuild-for-promotion visible, since it is common, it destroys the property, and the teams doing it usually do not know.

## Who Feels the Pain
Platform teams whose verification fails for reasons that are not security problems; compliance functions who cannot demonstrate a chain they were told existed; and organisations whose signing initiative produced a property that breaks at the third registry.

## Impact If Fixed
Preserving the digest and copying attestations through promotion are pipeline changes that keep the chain intact, and verifying at each step localises a break to its cause. Chain integrity coverage is the honest measure and is typically far below the signing adoption number that is reported instead.
