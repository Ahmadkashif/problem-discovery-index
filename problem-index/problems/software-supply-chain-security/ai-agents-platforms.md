# AI Agents & Platform Opportunities — Software Supply Chain Security

**Industry:** [[software-supply-chain-security|Software Supply Chain Security]]

---

## 1. Exploitability Triage Agent
#ai-agent #graph-theory #gradient-boosting #confidence-intervals #hypothesis-testing #evaluation-metrics #compliance #worker-facing

**Concept:** An agent that turns a scan result into a work list. It establishes reachability from the application's own code to each vulnerable function, joins deployment context from infrastructure data — internet exposure, authentication, segmentation — and weighs exploitation likelihood rather than abstract severity. It estimates remediation effort alongside risk, because the decision is a trade-off. And it publishes its own reachability false negative rate, which no vendor does and which is the reason security teams still triage everything manually. Dismissals persist across scans and propagate to structurally identical cases elsewhere, so the queue stops regenerating.

**Inputs:** Dependency and call graphs; application source and configuration; deployment topology from infrastructure and observability systems; vulnerability metadata and affected ranges; exploit availability and observed exploitation data; historical dismissals with reasoning; ecosystem upgrade outcomes.

**Outputs / Actions:** A ranked work list with the reason for each ranking. Automatic refutation of mechanically determinable non-issues — unreachable paths, versions outside range, duplicates under other identifiers, components absent from the deployed artefact. Persistent, propagating dismissals. A published error rate. Suppressed findings visible on request, so nothing is silently hidden.

**Why now:** The category's output is unusable at the volume it generates, which means the critical finding is indistinguishable from a thousand irrelevant ones. Reachability has become differentiating and remains unaudited — publishing the error rate is what would make automated suppression acceptable to a security team.

**Market:** Application security teams and the software composition analysis vendors. The buyer is whoever is accountable for a backlog of thousands of findings they know they cannot work, which is every application security lead.

---

## 2. Package Integrity Agent
#ai-agent #change-point-detection #graph-neural-networks #gradient-boosting #dbscan #confidence-intervals #evaluation-metrics #compliance

**Concept:** An agent that watches how packages are published rather than only what they contain. A legitimate package's publishing behaviour is stable over years — same maintainer, cadence, build environment, code style — and a compromise produces discontinuity across several of those at once, which is detectable and is exactly what reputation-based defences miss. It also models coordinated campaigns relationally, catching the shared infrastructure, timing and code fragments that per-package analysis cannot see. And it implements the mitigation that needs no model: delaying adoption of brand-new versions for non-urgent dependencies, since most malicious releases are removed within days.

**Inputs:** Registry publishing history with maintainer identity, cadence, build provenance and attestations; code style and structure across versions; install script behaviour; declared and observed capabilities; account activity; cross-package infrastructure and code sharing; confirmed incident history.

**Outputs / Actions:** Publishing discontinuity alerts with the dimensions that shifted. Campaign clustering across the ecosystem. Graduated response — warn, delay, quarantine, block — rather than a binary verdict, because blocking a widely used package breaks builds everywhere. Adoption delay policy for non-urgent updates. Provenance verification where attestations exist.

**Why now:** The attack moved from exploiting vulnerable dependencies to publishing poisoned ones, and maintainer compromise is both the most dangerous case and the one every reputation signal is blind to. Publishing behaviour is public, complete and highly regular, which makes change detection unusually well-posed.

**Market:** Registries, supply chain security vendors and large enterprises with internal package mirrors. The graduated response is what makes it deployable — a binary blocker on this signal would be unusable.

---

## 3. Exposure Query Platform
#ai-platform #graph-theory #bert #k-nearest-neighbors #dbscan #evaluation-metrics #compliance #data-integration

**Concept:** A platform that makes bills of materials answer the question they were mandated to answer. It resolves component identity across SBOMs from many vendors in several formats with inconsistent naming and version schemes, normalises depth so a shallow document is flagged rather than trusted, and tracks which version of which vendor product is actually deployed where. Then it answers, in minutes rather than as a project: given this advisory, which products, in which versions, running in which environments, contain the affected component — and what the exposure actually is.

**Inputs:** SBOMs across SPDX and CycloneDX from vendors and internal builds; Package URL identifiers and file hashes where present; public registry metadata; asset and deployment records; vulnerability advisories.

**Outputs / Actions:** Canonical component identity across the document estate. Depth and quality scoring per received SBOM, so a superficial one is visible as such. Deployment currency joining documents to what is actually running. Exposure queries answered against a new advisory. Vendor follow-up lists where an SBOM is too shallow to answer.

**Why now:** The ecosystem built generation, mandated it, and never built consumption — so a compliance artefact accumulates while the underlying question is still answered by asking around. Identity resolution across the documents is the missing foundation and is an ordinary matching problem.

**Market:** Regulated buyers subject to SBOM mandates, large enterprises with substantial vendor software estates, and government procurement. The value proposition is the one the regulation intended and currently does not deliver.
