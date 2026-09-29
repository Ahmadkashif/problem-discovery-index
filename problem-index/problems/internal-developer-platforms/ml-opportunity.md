# Machine Learning Opportunities — Internal Developer Platforms

**Industry:** [[internal-developer-platforms|Internal Developer Platforms]]
**Derived from:** [[problems/internal-developer-platforms/high-impact|High Impact]], [[problems/internal-developer-platforms/low-impact-1|Low Impact 1]], [[problems/internal-developer-platforms/low-impact-2|Low Impact 2]], [[problems/internal-developer-platforms/worker-life-1|Worker Life 1]], [[problems/internal-developer-platforms/worker-life-2|Worker Life 2]]

---

## 1. Platform Adoption Funnel and Route-Around Detection
#gradient-boosting #survival-analysis #k-means-clustering #causal-inference #confidence-intervals #hypothesis-testing #evaluation-metrics #workflow-orchestration

**Problem statement:** Platform teams build paved paths and cannot explain why adoption stalls, because they think of themselves as building infrastructure rather than a product and collect almost none of the measurements a product team would consider essential.

**ML task:** Funnel analysis with survival modelling of golden path completion, team-level cohort analysis, and classification of teams that have built their own alternative
**Input data:** Portal and template usage events; golden path step completion and abandonment; deployment pipeline usage; repository and infrastructure signals indicating bespoke tooling; time from repository creation to production traffic; team attributes and mandate status; support channel contacts.
**Target:** Golden path completion, sustained platform usage over time, and route-around as evidenced by team-owned equivalents of platform capabilities.
**Evaluation metric:** Standard product metrics — activation, completion, retention by cohort — reported at team level with individual-level aggregation architecturally impossible. The outcome measure is time-to-production decomposed by step, which is what identifies where the path actually costs time rather than where the team assumed it did.
**Scope:** The team-level boundary is not a policy choice but a design requirement: any instrumentation of engineering activity can become performance surveillance, engineers are correctly alert to it, and a platform team that crossed that line would destroy the trust adoption depends on. Route-around detection is the most informative signal available and comes from infrastructure and repository inspection rather than from telemetry. Staged rollouts designed to permit comparison are what would let a platform team defend its existence with evidence. 2 ML engineers plus a product analyst, 4-5 months.
**Data availability:** All of it exists in platform, CI and infrastructure systems and is almost never collected for this purpose.

---

## 2. Catalogue Derivation from Observed Behaviour
#graph-neural-networks #bert #word-embeddings #gradient-boosting #k-nearest-neighbors #evaluation-metrics #data-integration

**Problem statement:** The service catalogue underpins everything and is maintained by asking teams to update metadata files that are accurate on the day they are written. Within a year a meaningful share of ownership entries are wrong, and the failure surfaces during an incident.

**ML task:** Inference of ownership, dependencies and lifecycle state from commit, deployment, paging and runtime signals, plus staleness scoring against declared metadata
**Input data:** Commit and pull request activity by service and author; deployment actors; on-call paging records; runtime dependency edges from distributed tracing; repository structure and code owners; cloud resource tags and creation events; traffic and deployment recency; declared catalogue metadata.
**Target:** Actual ownership as confirmed during incidents or by team leads, and actual dependencies as observed at runtime.
**Evaluation metric:** Ownership accuracy against confirmed cases, and — more usefully — the staleness detection rate: of declared entries that were wrong, what proportion did the system flag before someone needed them. Dependency recall against tracing ground truth.
**Scope:** Runtime tracing already contains a more accurate dependency graph than any catalogue, and joining it is an integration rather than a modelling task. Ownership inference from commit and deployment activity reflects who is working on the service today rather than who was assigned it two reorganisations ago, which is exactly the distinction that matters at three in the morning. Lifecycle detection — no deployments, no traffic, no commits — stops the catalogue growing monotonically. 2 ML engineers, 4 months.
**Data availability:** Strong across version control, CI, paging and tracing systems. The catalogue itself provides declared values to compare against.

---

## 3. Template Drift Measurement and Propagation
#bert #word-embeddings #gradient-boosting #dbscan #graph-theory #evaluation-metrics #automation

**Problem statement:** Golden paths deliver value once at generation, and every subsequent template improvement reaches only new services. This caps what a platform can achieve on an existing estate, and it is the single largest limit on the category's value.

**ML task:** Measurement of divergence between each service and its template, classification of divergence as deliberate customisation or neglect, and prioritisation of which drift matters
**Input data:** Template versions and their change history; generated services and their subsequent commit history; file-level differences between service and current template; the nature and coherence of local modifications; security and compliance requirements; incident history associated with configurations.
**Target:** Whether a divergence was an intentional customisation, and whether it is one that should be converged, as judged by the owning team.
**Evaluation metric:** For classification, agreement with team judgement on a sample. For prioritisation, whether the ranked list precedes the problems that occur — a missing security configuration ranking above an old logging format. For propagation, the acceptance rate of automatically opened convergence pull requests, which is the operational outcome.
**Scope:** Dependency updating already solves this problem shape for version strings and the generalisation to templates has never been packaged, because a template change must be merged into a locally modified file rather than substituted. That is a three-way merge with conflict handling — well-understood technology, unpackaged for this use. Drift measurement is independently valuable before any propagation exists. 2 ML engineers, 4-5 months.
**Data availability:** Template and service repositories are fully available. Intent labels for customisation versus neglect require team input and do not exist as a corpus.

---

## 4. Support Channel Structuring and Error Translation
#bert #word-embeddings #k-means-clustering #large-language-models #gradient-boosting #evaluation-metrics #automation #worker-facing

**Problem statement:** Platform support runs in an unstructured chat channel with no ticketing, categorisation or metrics, so a load consuming half a team's week is invisible to everyone including the team. The questions repeat, and each repetition is evidence of a design or documentation failure that nobody has time to fix.

**ML task:** Classification and clustering of support questions, retrieval-based answering from channel history and documentation, and mapping of low-level system errors to platform-level explanations
**Input data:** Support channel history with questions and resolutions; platform documentation; deployment and pipeline failure messages from underlying systems; the platform's own configuration model; historical error-to-remedy mappings; question frequency over time.
**Target:** Question topic and its eventual answer; and for errors, the platform-level remedy that resolved the underlying failure.
**Evaluation metric:** Deflection rate — questions resolved without a platform engineer — and, equally important, the topic-frequency report, which is simultaneously the support metric and the product backlog. For error translation, whether the translated message enabled the developer to resolve it unaided.
**Scope:** Error translation is the highest-value component and the most bounded: underlying systems produce a finite set of failures, the mapping to platform-level explanations is learnable, and receiving a raw admission controller rejection is the moment the abstraction most visibly breaks its promise. The frequency report requires no modelling and is what makes the invisible load arguable. 2 ML engineers, 3-4 months.
**Data availability:** Channel history is complete and unstructured. Error corpora from underlying systems are abundant. Resolution labels are implicit in the conversation and require extraction.
