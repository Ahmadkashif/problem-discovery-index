# Machine Learning Opportunities — Software Supply Chain Security

**Industry:** [[software-supply-chain-security|Software Supply Chain Security]]
**Derived from:** [[problems/software-supply-chain-security/high-impact|High Impact]], [[problems/software-supply-chain-security/low-impact-1|Low Impact 1]], [[problems/software-supply-chain-security/low-impact-2|Low Impact 2]], [[problems/software-supply-chain-security/worker-life-1|Worker Life 1]], [[problems/software-supply-chain-security/worker-life-2|Worker Life 2]]

---

## 1. Contextual Exploitability Ranking
#graph-theory #gradient-boosting #logistic-regression #confidence-intervals #hypothesis-testing #feature-engineering #evaluation-metrics #compliance

**Problem statement:** Scans return thousands of findings ranked by a severity score computed by an analyst who has never seen the application. A minority are reachable, fewer are exploitable given the deployment, and fewer still justify interrupting a release — and the tools report the count anyway, so the critical finding sits in a backlog with a thousand irrelevant ones.

**ML task:** Ranking of findings by realistic risk, combining static reachability, deployment exposure and exploitation likelihood, with remediation effort estimated alongside
**Input data:** Dependency graphs and call graphs across language boundaries; application source and configuration; deployment topology including internet exposure, authentication and network segmentation from infrastructure data; vulnerability metadata and affected version ranges; exploit availability and observed exploitation data; historical dismissals with recorded reasoning; ecosystem-wide upgrade outcomes.
**Target:** Findings that were genuinely acted on and, where available, findings implicated in actual incidents.
**Evaluation metric:** Recall on findings that were actually exploited or required urgent action, which must be very high because a suppressed real vulnerability is the failure that ends the product. Report the suppression rate achieved at that recall, which is the efficiency delivered. Reachability false negative rate must be published — no vendor currently does, and that omission is why teams still triage manually.
**Scope:** Reachability defeats static analysis at exactly the constructs ordinary code uses: dynamic dispatch, reflection, dependency injection, configuration-driven wiring. Honest error rates matter more than headline accuracy. Deployment context is a join to infrastructure data that no scanner performs and that changes the answer substantially. Remediation effort estimation from ecosystem upgrade history is the missing half of every prioritisation decision. 3-4 ML engineers plus security researchers, 8 months.
**Data availability:** Dependency graphs across large customer bases are held by the vendors. Deployment context requires integration. Exploitation labels are scarce, late and biased toward what gets publicised.

---

## 2. Maintainer Compromise Detection from Publishing Discontinuity
#change-point-detection #graph-neural-networks #gradient-boosting #bert #dbscan #confidence-intervals #evaluation-metrics #compliance

**Problem statement:** The most dangerous supply chain attack is a compromised legitimate package, because it carries reputation, download history and existing trust — which is precisely where reputation-based defences fail. Behavioural scanning looks for known-bad patterns that attackers test against before publishing.

**ML task:** Change point detection on a package's publishing behaviour across multiple simultaneous dimensions, plus relational clustering of coordinated publishing campaigns
**Input data:** Package release history with cadence, maintainer identity, build environment and provenance attestations; code style and structural characteristics across versions; install script behaviour; declared and observed capabilities such as network and filesystem access; account activity patterns; cross-package infrastructure, timing and code fragment sharing; confirmed malicious package incidents.
**Target:** Packages subsequently confirmed malicious or compromised.
**Evaluation metric:** Detection lead time before removal from the registry — most malicious packages are removed within days, so value is measured in hours, not accuracy. False positives are extremely costly, since blocking a widely used package breaks builds across an ecosystem, so precision must be very high and the response should be graduated: warn, delay, quarantine, block.
**Scope:** Publishing behaviour is stable over years and a compromise produces discontinuity in several dimensions at once — maintainer, cadence, build environment, code style — which is exactly the shape change point detection handles and reputation cannot. Campaign-level relational modelling catches what per-package analysis misses. The simplest effective mitigation needs no model at all: delaying adoption of brand-new versions for non-urgent dependencies eliminates much of the exposure, since most malicious releases are removed quickly. 3 ML engineers plus security researchers, 6 months.
**Data availability:** Registry publishing data is public and complete. Confirmed malicious labels exist from incident disclosures and are rare relative to the population.

---

## 3. Component Identity Resolution Across Bills of Materials
#graph-theory #bert #word-embeddings #k-nearest-neighbors #dbscan #evaluation-metrics #data-integration #compliance

**Problem statement:** SBOMs are mandated, generated at scale and functionally inert. When a vulnerability appears in a widely used component, the question the mandate exists to answer — are we affected and in what — cannot be answered from the accumulated documents without a project, because component naming, version formats and depth all vary across vendors.

**ML task:** Entity resolution of components across heterogeneous SBOMs into canonical identities, with depth normalisation and currency tracking
**Input data:** SBOMs across formats and vendors with component names, versions, suppliers and hashes; Package URL identifiers where present; public package registry metadata; file hashes and binary fingerprints where available; vendor product and version deployment records.
**Target:** Canonical component identity, validated against registry ground truth and against hash matches where both are available.
**Evaluation metric:** Resolution precision and recall against hash-verified matches, reported separately for documents with and without Package URL identifiers, since the latter is the actual difficulty. The operational metric is query latency for the exposure question: given a new advisory, how quickly can affected products and deployments be enumerated.
**Scope:** Hashes resolve identity definitively where present and are frequently absent, which is what makes this a matching problem rather than a lookup. Depth normalisation matters because a shallow SBOM listing only direct dependencies creates false confidence that the recipient cannot detect without inspection. Currency — which version of which vendor product is actually deployed where — is a separate join to asset management that nobody performs. 2 ML engineers, 4-5 months.
**Data availability:** SBOMs accumulate at organisations subject to the mandate and are largely unexploited. Registry metadata is public.

---

## 4. Upgrade Path Computation and Risk Estimation
#graph-theory #gradient-boosting #large-language-models #confidence-intervals #k-nearest-neighbors #evaluation-metrics #automation #worker-facing

**Problem statement:** A developer is told to fix a vulnerability in a transitive dependency four levels deep, with no indication of what has to change. Resolving it may require upgrading an intermediate dependency across a major version with breaking changes, and the ticket says none of that.

**ML task:** Constraint solving over the dependency graph for the minimal upgrade set, combined with prediction of breaking-change risk from ecosystem upgrade history
**Input data:** Dependency graphs with version constraints; package version histories and their declared compatibility; ecosystem-wide records of upgrades attempted, succeeded, reverted and their associated failures; changelogs and release notes; API surface differences between versions; the application's own usage of the affected APIs.
**Target:** Whether an upgrade succeeded without code changes, required changes, or was reverted.
**Evaluation metric:** Accuracy of the breaking-risk prediction, with under-prediction weighted heavily since a supposedly safe upgrade that breaks a build costs developer trust immediately. For the upgrade path, minimality and correctness verified by resolving and building.
**Scope:** The constraint solving is deterministic and the risk estimation is the learned component, drawn from a large public record of how upgrades in each ecosystem actually go. The application's own usage of the changed APIs is what makes the prediction specific rather than generic, and it requires call graph analysis the reachability work already needs. Automated pull requests for confidently safe transitive resolutions extend what dependency bots already do for direct version bumps. 2-3 ML engineers, 5 months.
**Data availability:** Public ecosystem upgrade history is enormous and freely available. Private outcomes across a vendor's customer base are richer still and are a genuine proprietary advantage.
