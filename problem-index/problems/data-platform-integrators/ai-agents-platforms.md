# AI Agents & Platform Opportunities — Data Platform Integrators

**Industry:** [[data-platform-integrators|Data Platform Integrators]]

---

## 1. Platform Value and Pruning Platform
#ai-platform #graph-neural-networks #gradient-boosting #k-means-clustering #confidence-intervals #evaluation-metrics #data-integration #revenue-impact

**Concept:** A platform that answers the question every mature data estate owner has and cannot prove: which of this is earning its keep. It joins query and access logs to lineage and to attributed compute cost, classifies each asset by realised purpose rather than by access count — distinguishing a regulatory extract run twice a year from a daily refresh feeding a dashboard nobody opens — and produces a value-per-dollar ranking with safe deletion candidates. For the integrator it closes the loop that has never been closed, feeding usage evidence back into how the next engagement is scoped.

**Inputs:** Query and dashboard access logs with consumer identity and type; the full lineage graph; compute cost attributed per model run; refresh schedules; delivery records from the integrator.

**Outputs / Actions:** A ranked pruning list with the rare-but-essential class explicitly protected and reported separately, because that false positive is the objection that has killed every previous attempt. Monthly cost attached to each unused asset, which is what actually gets a deletion approved. Evidence about which asset types get used in which organisational contexts, so the next platform is scoped to build what people query. And the uncomfortable aggregate — what share of delivered assets are never opened — reported rather than avoided.

**Why now:** Consumption pricing made the cost of dead assets a visible monthly number rather than an abstraction, and lineage is now standard enough that purpose-aware classification is possible. The missing piece is a post-go-live data access clause, which clients will grant because they want the answer.

**Market:** Data platform integrators, the platform owners who inherit these estates, and the catalogue vendors whose lineage products are used for compliance rather than for pruning.

---

## 2. Semantic Data Health Agent
#ai-agent #change-point-detection #time-series-forecasting #gradient-boosting #graph-neural-networks #confidence-intervals #evaluation-metrics #data-integration

**Concept:** An agent that watches for the failures that pass every structural test. It learns per-column distributional baselines and detects meaningful departures — a categorical distribution shifting, a numeric scale changing, a join relationship silently becoming one-to-many — then propagates the impact through lineage and query history to say which reports were affected and who consumed them in the interim, which is the information that determines whether anyone has to be told. It weights every alert by downstream consumption, so the monitor stays readable and therefore stays read.

**Inputs:** Column-level distributions, cardinalities and null rates over time; join relationship cardinality; upstream schema and release history; lineage; query and access logs; historical incidents with confirmed causes.

**Outputs / Actions:** Semantic drift alerts with the affected downstream assets and their consumers enumerated. Consumption-weighted prioritisation so a change in a board-report feed and one in an unqueried staging model are not presented identically. An impact statement covering the interim period, which is the part an organisation actually needs when a wrong number has been circulating. Detection lead time measured against the current mechanism, which is somebody noticing weeks later.

**Why now:** Observability tooling has matured on the structural axis and stopped there; the semantic axis needs per-column baselines that are cheap to compute and that nobody computes. Lineage coverage is now good enough for propagation to be reliable.

**Market:** Data platform teams at any organisation with a mature warehouse, integrators offering managed platform services, and the observability vendors whose products currently watch the wrong layer.

---

## 3. Analytics Engineering Agent
#ai-agent #bert #large-language-models #graph-neural-networks #k-nearest-neighbors #gradient-boosting #worker-facing #automation

**Concept:** An agent that handles the investigation preceding every piece of analytics engineering work. It answers which of four similarly-named models is the right one by searching semantically and weighting by actual usage, so a dead model that matches the name is not the answer. It reconstructs why a model exists by linking it to the pull request, ticket and discussion that created it — abstaining visibly where no record exists rather than inventing a rationale. It explains why two numbers disagree by comparing lineage and definitions and naming the divergence, and records the resolution so the next person is answered before they ask. And on the operational side it triages pipeline alerts by whether a human can act now and what depends on them, names the likely failure cause with evidence, and assembles dependency-ordered recovery with cost stated.

**Inputs:** Model SQL, metric definitions and their history; lineage and query logs; pull requests, tickets and discussion threads; prior discrepancy resolutions; pipeline failure history with causes; downstream consumption and timing requirements.

**Outputs / Actions:** Usage-weighted semantic search across the estate. Reconstructed intent with honest abstention. Named discrepancy causes with the resolution recorded once. Blast-radius assessment before a change, weighted by whether dependencies are actually queried. Overnight alert triage that removes the wakes where nothing can be done, a named diagnosis on arrival, and a publish-or-hold recommendation grounded in who actually consumes the affected data and when they need it.

**Why now:** Data teams imported software on-call practice without its mitigations, and the discovery problem has grown with estate size while lineage and query logs — everything needed to solve it — have become universally available.

**Market:** Analytics and data platform engineers everywhere, integrators running managed services across client estates, and the transformation and catalogue vendors whose tools describe structure but not usage or intent.
