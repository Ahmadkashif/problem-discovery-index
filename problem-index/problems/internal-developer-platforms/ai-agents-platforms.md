# AI Agents & Platform Opportunities — Internal Developer Platforms

**Industry:** [[internal-developer-platforms|Internal Developer Platforms]]

---

## 1. Platform Product Analytics
#ai-platform #gradient-boosting #survival-analysis #k-means-clustering #causal-inference #confidence-intervals #evaluation-metrics #compliance

**Concept:** A platform that treats an internal developer platform as the product it actually is. It measures activation, golden path completion and abandonment by step, feature retention by team cohort, and time from repository creation to production traffic decomposed into where the time goes. It detects route-arounds — teams that built their own deployment pipeline or observability setup — from infrastructure and repository signals, because those teams are the most informative users the platform has and are currently invisible. Every measurement aggregates at team level and individual-level aggregation is not implementable, which is the design requirement that makes it acceptable at all.

**Inputs:** Portal and template usage events; golden path step completion; pipeline and deployment usage; repository and infrastructure signals for bespoke tooling; time-to-production traces; team attributes and mandate status; support contact rates.

**Outputs / Actions:** An adoption funnel with drop-off by step. Team cohort retention. Route-around inventory with what each team built instead. Time-to-production decomposition. Staged rollout comparison so the platform's effect on delivery is estimable rather than asserted. It cannot report on individuals, by construction.

**Why now:** Internal platforms fail at a rate the industry openly discusses, and the cause is consistently a category error — infrastructure thinking applied to a product problem. The instrumentation requires nothing new; it requires the frame.

**Market:** Platform engineering teams and the commercial IDP vendors. The strongest hook is that a platform team currently cannot defend its headcount with evidence, and staged rollout comparison is the only thing that would let it.

---

## 2. Living Catalogue Agent
#ai-agent #graph-neural-networks #bert #gradient-boosting #k-nearest-neighbors #evaluation-metrics #data-integration #automation

**Concept:** An agent that derives the service catalogue from behaviour instead of asking people to declare it. Ownership comes from who actually commits, deploys and gets paged, which reflects today rather than two reorganisations ago. Dependencies come from runtime tracing, which already contains a more accurate graph than any hand-maintained one. Lifecycle state comes from deployment, traffic and commit recency, so dead services are identified rather than accumulating. Where declared metadata contradicts observed behaviour it raises a staleness flag rather than demanding everything be perfect, which turns an unbounded obligation into a short list.

**Inputs:** Commit and pull request activity by author and service; deployment actors; paging records; distributed tracing dependency edges; code owners; cloud resource tags and creation events; traffic and deployment recency; declared catalogue entries.

**Outputs / Actions:** Derived ownership with confidence and the evidence behind it. A dependency graph from runtime rather than declaration. Lifecycle classification identifying dead services. Staleness flags where declaration and behaviour disagree. Incident-time ownership resolution, which is the moment the catalogue is actually needed.

**Why now:** The tracing graph and the commit history have both been available for years while catalogues continued to be populated by hand. The join is an integration task, and the failure it prevents — not knowing who owns a failing service at three in the morning — is universally experienced.

**Market:** IDP vendors and platform teams running Backstage or its commercial equivalents. Catalogue accuracy is the foundation under scorecards, cost allocation, access reviews and incident response, all of which currently inherit its decay.

---

## 3. Platform Interface Agent
#ai-agent #large-language-models #bert #k-means-clustering #gradient-boosting #evaluation-metrics #automation #worker-facing

**Concept:** An agent that sits between developers and the platform's edges. It translates failures from underlying systems — an admission controller rejection, a Terraform provider error, an IAM policy denial — into platform-level explanations with the actual remedy, which is the moment the abstraction most visibly breaks its promise. It answers support questions from channel history and documentation, deflecting the repeats. It surfaces precedent, showing how another team accomplished the same thing, which is more useful than any documentation page. And it reports question frequency by topic, which is simultaneously the platform team's support metric and its product backlog, since the most-asked question is the worst interface.

**Inputs:** Support channel history with resolutions; platform documentation and configuration model; failure messages from underlying systems; historical error-to-remedy mappings; other teams' implementations as precedent; capability and permission state per service and environment.

**Outputs / Actions:** Translated errors delivered at the point of failure in the developer's own tooling. Retrieved answers from channel history and documentation. Precedent examples from other teams. Capability discovery so a developer can find out what is supported without attempting it. A weekly topic-frequency report to the platform team. Clear statements where something genuinely is not supported, with the reason and the alternative.

**Why now:** Error translation is a bounded, learnable mapping over a finite set of underlying failures, and it addresses the exact moment developers conclude the platform is obstructive. The support channel corpus needed nothing but structure.

**Market:** Platform teams, IDP vendors and internal developer experience functions. The deflection pays for it and the frequency report is what finally lets the team fix causes rather than instances.
