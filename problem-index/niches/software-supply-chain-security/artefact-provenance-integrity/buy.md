# Attestation Infrastructure That Already Exists

**Niche:** [[niches/software-supply-chain-security/artefact-provenance-integrity/profile|Artefact Provenance & Integrity]]
**Industry:** [[industries/software-supply-chain-security|Software Supply Chain Security]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Signing, transparency logs, attestation formats and provenance specifications are all open, mature and free, and the gap between them and a verified deployment is policy and operations.
**Tags:** #graph-theory #descriptive-statistics #evaluation-metrics #confidence-intervals #compliance #automation #data-integration #workflow-orchestration
**Contested on:** Every serious competitor here is fighting to prove that what is running was built from what was reviewed, by an authorised process, from known inputs — and whoever does that takes the platform and compliance account, because regulation is now asking and nobody can answer.

## The Problem
The cryptographic and format layer of this problem is solved and given away: keyless signing with identity-based certificates, public transparency logs, a standard attestation envelope, a provenance specification with defined levels, and policy engines to evaluate the result. An organisation can obtain every component for nothing. What they cannot obtain is the policy that expresses their trust decisions, the operational process around verification failure, and the coverage across an estate that was not built with this in mind.

## What Already Exists
Keyless signing and transparency log infrastructure; the attestation envelope and provenance specification with graded levels; policy engines with declarative languages; admission controllers that enforce at deployment; and build system support emitting attestations natively in several ecosystems.

## The Customization Gap
The adaptation is to a heterogeneous estate with legacy and third-party artefacts. It requires: (1) policy expression for a real estate, which includes artefacts built by systems that will never emit attestations, vendor images with their own signing, and emergency paths — and a policy language that cannot express the exceptions will be replaced by no policy at all; (2) incremental adoption by scope, so an organisation can verify one environment or one class of artefact and expand, rather than facing an all-or-nothing switch; (3) provenance across rebuilds and promotions, which is where the chain breaks in practice and is addressed in the fix note; (4) mapping to the regulatory questions, since the demand is expressed as outcomes — can you show what is in your software and where it came from — and the answer is a set of attestations that somebody must translate into that language, which is the piece the compliance buyer actually needs; and (5) operational tooling for the failure path, since the technical layer assumes verification either passes or blocks and the organisation needs a third option that is not simply switching it off.

## Target Customer
Platform engineering and compliance functions, supply chain security vendors, and the open infrastructure projects whose adoption stalls at verification.

## Impact If Solved
The cryptographic layer is free and complete and adoption stalls at policy and operations, which is where a product belongs. Policy that can express a real estate's exceptions is what determines whether verification is turned on at all.
