# Artefact Provenance & Integrity

**Parent Industry:** [[industries/software-supply-chain-security|Software Supply Chain Security]]
**Category:** Contested Sub-Niche
**Contested on:** Every serious competitor here is fighting to prove that what is running was built from what was reviewed, by an authorised process, from known inputs — and whoever does that takes the platform and compliance account, because regulation is now asking and nobody can answer.

## Profile
**Market Size:** ~$480M US artefact provenance, signing and integrity
**Share of Parent Industry:** ~16% of category revenue
**Digital Adoption:** Low-Medium — the infrastructure exists and adoption is partial
**Target Buyer:** Platform engineering and compliance, under regulatory pressure
**Automation Potential:** Very High — the facts are produced by the build and are discarded

## What Makes This a Distinct Niche
The provenance question is different in kind from the vulnerability question. It asks whether the artefact running in production is the one that was built from the reviewed source, by the authorised pipeline, from the dependencies that were resolved and scanned — and it is asked increasingly by regulators and by enterprise customers rather than by the security team's own risk appetite. The infrastructure to answer it exists: signing, attestation formats, provenance specifications and transparency logs are all available and open, and the build system produces every fact required as a by-product. Adoption is nonetheless partial, because signing something is easy and verifying it at the point of deployment, maintaining the trust policy, and handling the operational consequences of a failed verification are the parts nobody has made routine. The contest is end-to-end verification that an organisation can actually operate.

## Current Tools & Gaps
Signing and transparency infrastructure, provenance attestation specifications, build systems emitting attestations, and registry support of varying completeness. The gaps: signing is adopted far more widely than verification, which means artefacts are signed and nothing checks the signature at deployment — the half that provides the security; trust policy is where the difficulty is and is barely tooled, so organisations sign everything and verify nothing; the provenance chain breaks at the points where artefacts are rebuilt, re-tagged or promoted between registries; verification failure has no operational playbook, so the first genuine failure blocks a deployment nobody knows how to unblock; and the regulatory demand is stated in outcomes the technical artefacts do not obviously satisfy.

## Problems
- [[niches/software-supply-chain-security/artefact-provenance-integrity/build|🔨 Build: Everything Is Signed and Nothing Is Verified]]
- [[niches/software-supply-chain-security/artefact-provenance-integrity/buy|🛒 Buy: Attestation Infrastructure That Already Exists]]
- [[niches/software-supply-chain-security/artefact-provenance-integrity/fix|🔧 Fix: The Chain That Breaks at Promotion]]
