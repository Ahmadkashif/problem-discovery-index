# AI Agents & Platform Opportunities — Customer Data Platforms

**Industry:** [[customer-data-platforms|Customer Data Platforms]]

---

## 1. Identity Quality Platform
#ai-platform #graph-neural-networks #bayesian-inference #confidence-intervals #gradient-boosting #hypothesis-testing #compliance #evaluation-metrics

**Concept:** A platform that gives an organisation the first measurement of its own identity graph. It builds a stratified adjudicated evaluation set concentrated in the ambiguous band, reports over-merge and under-merge rates separately and continuously, and lets the operating point be chosen from the actual costs of each error rather than inherited from a vendor default. It carries match confidence downstream, so an advertising audience and an account page that displays order history no longer share one threshold — which is the specific configuration that turns a matching error into a privacy incident.

**Inputs:** All identifier-bearing records and the existing graph's merge decisions; co-occurrence structure across devices and households; the adjudicated evaluation set; downstream use registry with each use's tolerance for error.

**Outputs / Actions:** Merge precision and split rate by segment and identifier type, tracked over time with alerts on change. A per-use operating point rather than a global threshold. Confidence propagated into activation so marginal merges are usable for modelling and refused for disclosure. A comparison basis that finally lets a buyer evaluate identity vendors on something other than match rate — the metric that improves as over-merging gets worse.

**Why now:** The category has repositioned around identity as the warehouse absorbed the pipeline, which puts competitive weight on the one function that has never been validated. Privacy enforcement has also raised the cost of the over-merge error from an embarrassment to a reportable event.

**Market:** Enterprises running a CDP or a composable stack, retail and financial services above all, and the identity vendors themselves, for whom a published error rate would be a genuine differentiator if any of them dared.

---

## 2. Data Contract Agent
#ai-agent #change-point-detection #time-series-forecasting #bert #large-language-models #gradient-boosting #worker-facing #workflow-orchestration

**Concept:** An agent that makes the event stream report its own health and puts the consequences of a change where the change is made. It forecasts every event and property against its own history, correlates any departure with the deployment that caused it, and raises it the same day instead of three weeks later via a marketer's complaint. It derives the real event catalogue from what is actually arriving — owners, first-seen dates, volumes, downstream dependencies — replacing the stale tracking plan spreadsheet. It proposes semantic mappings when a second team ships the same concept under a different name. And it posts dependency information into the pull request: this event feeds these four audiences and two journeys.

**Inputs:** Event arrival volumes and property distributions; deployment and release history; event and property schemas; CDP configuration for audiences, journeys and destinations; downstream tool dependencies.

**Outputs / Actions:** Same-day drift alerts with the release identified. A live, derived catalogue that is true rather than aspirational. Proposed event equivalences for human confirmation, never auto-applied. Blast-radius comments at the moment of the code change, which is the only moment an engineer can act cheaply.

**Why now:** Silent schema drift is the most common way these systems degrade and is currently discovered by investigating a business decline. Everything needed is already in the platform's own telemetry and configuration; nobody has connected the two.

**Market:** Data and analytics engineering teams at any organisation with a customer data platform, and the platform vendors, for whom this is the obvious complement to schema validation they already sell.

---

## 3. Privacy Fulfilment Agent
#ai-agent #graph-neural-networks #bayesian-inference #confidence-intervals #large-language-models #evaluation-metrics #compliance #worker-facing

**Concept:** An agent that runs deletion and access requests end to end, with the identity uncertainty made explicit rather than hidden. It resolves the subject and partitions the matched records into confident, marginal and excluded, presenting the marginal ones for a human decision with the evidence attached — so a shared household or a partial match becomes a recorded judgement rather than a silent inclusion. It maintains a propagation record of which downstream systems received which profiles and when, turning fulfilment from broadcasting to every system into an enumerable checklist. It executes the mechanics: API deletions, tickets for systems without APIs, chasing, confirmation, and the compiled evidence pack.

**Inputs:** The identity graph with per-edge confidence; export, sync and activation logs by system and date; downstream system capabilities and retention characteristics; the statutory clock; the organisation's adjudication rubric and its precedent history.

**Outputs / Actions:** A resolved subject with its marginal band surfaced and sized, so the operator knows how many judgement calls the request contains before certifying it. An enumerated downstream checklist with completion evidence. Automated execution and chasing. A defensible record of what was decided and why — which is what a regulator asks for and what most organisations currently cannot produce.

**Why now:** Request volumes have grown steadily under state privacy laws while the tooling still assumes identity is a solved input. The propagation record is a small engineering change that has to be made at export time and cannot be reconstructed later, which makes starting now materially better than starting in a year.

**Market:** Privacy operations teams at any consumer business, the privacy platform vendors whose products stop at the request intake, and the CDP vendors whose graphs are the uncertain foundation the whole process rests on.
