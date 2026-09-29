# Software Supply Chain Security

## Profile
**Category:** Developer Tools & Infrastructure
**Market Size:** ~$3B US software composition analysis, artefact security and supply chain integrity
**Tech Maturity:** Rapidly funded, poorly calibrated — Snyk, Sonatype, Chainguard, JFrog, Socket, Endor Labs and GitHub's native tooling scan dependencies, generate bills of materials and enforce policy. The category detects far more than any organisation can act on, and the ratio between what it reports and what actually matters is its central unresolved problem.
**Workforce:** Security researchers, vulnerability analysts, policy engineers, developer advocates, remediation engineers, compliance specialists

## Key Pain Themes
The category's defining failure is a signal-to-noise ratio that guarantees its findings are ignored. A scan of a typical application returns hundreds or thousands of vulnerability findings, of which a small fraction are reachable from the application's own code, a smaller fraction are exploitable in its configuration, and a smaller fraction still are worth interrupting a release for. Everyone in the field knows this and the tools report the raw count anyway. Around it sit two hard problems: malicious package detection, which is genuinely adversarial and where the attack has shifted from vulnerable dependencies to deliberately poisoned ones; and bills of materials, which regulation increasingly mandates and which are generated, filed and never used because nothing consumes them. Security engineers spend their days on triage that a better model would have done, and developers experience the category as a stream of tickets about code they did not write.

## Current Tech Landscape
Software composition analysis is mature and commoditised, with the national vulnerability database as the shared substrate and its known limitations widely acknowledged. Reachability analysis is the current differentiator and is offered by several vendors with varying rigour. SBOM generation is standardised through SPDX and CycloneDX and mandated in federal procurement. Sigstore and provenance attestation address artefact integrity. Malicious package detection has become urgent as typosquatting, dependency confusion and maintainer account compromise have all been used at scale. Exploit prediction scoring provides a probabilistic prioritisation signal that few tools use well.

## Problems
- [[problems/software-supply-chain-security/high-impact|🔴 High Impact: Findings Nobody Can Act On]]
- [[problems/software-supply-chain-security/low-impact-1|🟡 Low Impact: Malicious Package Detection]]
- [[problems/software-supply-chain-security/low-impact-2|🟡 Low Impact: Bills of Materials Nothing Consumes]]
- [[problems/software-supply-chain-security/worker-life-1|🟢 Worker Life: Security Engineer Triaging Noise]]
- [[problems/software-supply-chain-security/worker-life-2|🟢 Worker Life: The Developer Handed Someone Else's Vulnerabilities]]
- [[problems/software-supply-chain-security/ml-opportunity|🧠 ML Opportunities]]
- [[problems/software-supply-chain-security/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
These vendors observe the dependency graph of a large share of commercial software, joined to which vulnerabilities were fixed, which were dismissed, which were exploited and how upgrades actually went. That is the corpus from which real exploitability, real upgrade risk and real remediation effort could be estimated — the three questions every finding raises and none of the tools answer. The category instead ships severity scores computed by someone who has never seen the application, which is why its output is filed rather than acted upon.
