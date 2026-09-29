# Niche Analysis — Software Supply Chain Security

**Parent Industry:** [[industries/software-supply-chain-security|Software Supply Chain Security]]

## Niche Selection

Applied four-axis niche discovery: Market Share, Digital Adoption, Underserved Audience, Automation Potential, then held every candidate against the standing filter — terminal only when *"every serious competitor here is fighting to solve X, and whoever solves X best takes the account"* can be written without generality.

| # | Niche | Category | Est. Market Size | Digital Adoption | Target Buyer |
|---|---|---|---|---|---|
| 1 | Finding Prioritisation | 🔵 High Market Share | $780M | Low — severity scores computed by strangers | Application security leadership |
| 2 | Scanning & Analysis | 🔵 High Market Share | $1.1B | Very High and commoditised | Security and platform engineering |
| 3 | Malicious Package Detection | 🟠 Low Digitized | $420M | Low — signature matching against an adaptive adversary | Security functions and registries |
| 4 | SBOM Consumption | 🟠 Low Digitized | $310M | Very Low — generated, filed and never read | Procurement, compliance and security |
| 5 | The Security Engineer | 🟣 Underserved Audience | $260M | None — triage is manual and regenerated nightly | Application security leadership |
| 6 | The Developer With Tickets | 🟣 Underserved Audience | $190M | None — tickets about code they did not write | Every developer receiving findings |
| 7 | Remediation & Upgrade Risk | ⚡ Highly Automatable | $340M | Low — the fix is proposed and its risk is unstated | Platform and application engineering |
| 8 | Dependency Corpus Intelligence | ⚡ Highly Automatable | $290M | None — the corpus ships severity scores | The vendors themselves |

## Why These Niches

The category's defining failure is a signal-to-noise ratio that guarantees its findings are ignored. A scan returns thousands, a handful matter, and the tools report a severity score computed by somebody who has never seen the application. Everyone in the field knows this and the raw count is reported anyway. Prioritisation is therefore the largest contested surface and the one that determines whether the category's output is acted on at all.

Scanning **failed the filter as one niche**. Composition analysis is mature, commoditised and contested on nothing that matters — the differentiation has moved to reachability and exploitability, which is about whether a finding applies to this application, and to artefact provenance and integrity, which is about whether what was built is what is running. These are different techniques, different buyers within security, and different competitive sets. Decomposed below.

The two underdigitised areas are the adversarial frontier and the mandated artefact nobody uses. Malicious package detection faces an adversary who adapts and is served by signature matching. And bills of materials are standardised, automated and increasingly mandated, and are generated, filed and never read, because the tooling produces them and nothing consumes them.

The two underserved constituencies are the security engineer, establishing one at a time that findings do not apply in a queue the scanner regenerates nightly, and the developer, receiving tickets about transitive dependencies they never chose with no indication of whether it matters.

The automation niches are remediation risk — the three questions every finding raises and none of the tools answer — and the corpus that would answer them.

## Niches
- [[niches/software-supply-chain-security/finding-prioritisation/profile|🔵 Finding Prioritisation]]
- [[niches/software-supply-chain-security/scanning-and-analysis/profile|🔵 Scanning & Analysis]]
  - [[niches/software-supply-chain-security/reachability-and-exploitability/profile|🎯 Reachability & Exploitability]]
  - [[niches/software-supply-chain-security/artefact-provenance-integrity/profile|🎯 Artefact Provenance & Integrity]]
- [[niches/software-supply-chain-security/malicious-package-detection/profile|🟠 Malicious Package Detection]]
- [[niches/software-supply-chain-security/sbom-consumption/profile|🟠 SBOM Consumption]]
- [[niches/software-supply-chain-security/security-engineer-triage/profile|🟣 The Security Engineer]]
- [[niches/software-supply-chain-security/the-developer-with-tickets/profile|🟣 The Developer With Tickets]]
- [[niches/software-supply-chain-security/remediation-and-upgrade-risk/profile|⚡ Remediation & Upgrade Risk]]
- [[niches/software-supply-chain-security/dependency-corpus-intelligence/profile|⚡ Dependency Corpus Intelligence]]

## Filter Notes

Seven of the eight level-1 niches are terminal. **Scanning & Analysis** is not: composition analysis itself is commoditised and nobody competes on it, so the label names a mature capability rather than a contest, and the two live contests underneath it are unrelated. Reachability and exploitability is won by establishing whether a known vulnerability is actually reachable and exploitable in this application's code and configuration — a program analysis contest bought by application security to reduce a queue. Artefact provenance and integrity is won by establishing that what is running was built from what was reviewed, by whom, with what inputs — an attestation and signing contest bought by platform and compliance functions under regulatory pressure. Decomposed into two contested sub-niches.

Two candidates were rejected. *Licence compliance* was rejected because its contest belongs to the open-source commercial vendors industry covered separately in this vault, where the obligation question sits. *Container image scanning* was folded into the scanning sub-niches, since it is the same analysis applied to a different artefact type rather than a separate market.
