# AI Agents & Platform Opportunities — Observability Vendors

**Industry:** [[observability-vendors|Observability Vendors]]

---

## 1. Incident Diagnosis Agent
#ai-agent #graph-neural-networks #change-point-detection #causal-inference #large-language-models #confidence-intervals #evaluation-metrics #worker-facing

**Concept:** An agent that meets the on-call engineer at the page with a hypothesis rather than a dashboard. It establishes what moved first and how it propagated along the service dependency graph, enumerates and ranks the changes that preceded the incident — deployments, configuration, feature flags, infrastructure events, dependency releases — and matches the anomaly's shape against abstracted failure signatures from a large cross-organisational corpus. It returns three candidate explanations with the evidence for each and an explicit confidence, plus blast radius, because the first questions asked of an on-call engineer are always who is affected and how many.

**Inputs:** Metric, trace and log telemetry; service dependency graphs from tracing; change and deployment event streams; the organisation's own historical incidents with resolutions; abstracted cross-customer failure signatures.

**Outputs / Actions:** Ranked hypotheses with evidence and confidence at page time. Blast radius and affected user estimate. Prior similar incidents with what resolved them. A running timeline assembled automatically for the post-incident review. It never presents a verdict, because an engineer can evaluate a hypothesis in thirty seconds and cannot evaluate a conclusion.

**Why now:** Tracing-derived dependency graphs became widely available with OpenTelemetry adoption, which supplies the structure that earlier attempts lacked and that turned their output into correlation dressed as causation. The cross-customer corpus is the vendors' unique asset and requires the signature abstraction to be contractually usable.

**Market:** Every observability vendor and every engineering organisation with a meaningful on-call rota. Time to diagnosis is the largest component of incident duration, which makes this the moment the category's value is either delivered or not.

---

## 2. Telemetry Value Platform
#ai-platform #gradient-boosting #k-means-clustering #logistic-regression #confidence-intervals #evaluation-metrics #revenue-impact #automation

**Concept:** A platform that tells an engineering organisation which telemetry is worth its cost. It scores every stream by how often it is queried, whether it has appeared in an incident investigation, whether an alert built on it has fired usefully, and how recently — then joins that to cost to produce a value-per-dollar ranking. Retention and sampling follow the score rather than a global policy: queried signals stay hot, rare-but-interesting traces are preserved while the ordinary ones are dropped, and streams never read in a year are surfaced for deletion with the evidence attached.

**Inputs:** Query logs with the streams touched; alert definitions and firing outcomes; incident investigation traces; ingestion volume and cost per stream; stream ownership and metadata.

**Outputs / Actions:** A value-per-dollar ranking across every telemetry stream. Retention and sampling policy recommendations per stream. Regret tracking — of the streams dropped, how many were subsequently needed. Cost anomaly attribution to the specific service, metric and label. Cardinality warnings before ingestion rather than after billing.

**Why now:** Observability cost has become a board-level line and customers are cutting by volume because volume is all they can see. OpenTelemetry decoupled collection from the vendor, which makes a value-aware collector layer viable outside the incumbents — who have a clear commercial reason not to build this.

**Market:** Engineering and platform teams facing observability cost pressure, which is most of them, plus the open-source collector ecosystem. The buyer is whoever was asked why the monitoring bill exceeds the infrastructure bill.

---

## 3. Alert Health Agent
#ai-agent #change-point-detection #time-series-forecasting #gaussian-mixture-models #hypothesis-testing #evaluation-metrics #automation #worker-facing

**Concept:** An agent that maintains alerting the way it should have been maintained all along. It models each service metric's real structure — daily and weekly seasonality, deploy-related step changes, multiple regimes — and backtests candidate thresholds against the organisation's actual incident history to recommend numbers that would have caught the real events without firing on ordinary variation. It also produces the inventory no platform offers: which alerts have fired and led to action, which fired and were ignored, which have never fired, and which incidents had no alert at all.

**Inputs:** Historical metric series per service; deployment and scaling events; incident records with times; alert firing history with acknowledgement and resolution outcomes; on-call response data.

**Outputs / Actions:** An alert quality inventory in four classes with counts and examples. Backtested threshold recommendations with their historical precision and recall. Flapping and duplicate alert suppression. Retirement candidates for alerts that have never fired usefully. Coverage gaps where incidents occurred with no alert.

**Why now:** Alert fatigue is a leading contributor to on-call burnout and originates in numbers guessed once, and backtesting against incident history is entirely computable from data every platform holds. The quality inventory needs no modelling at all and is the fastest available improvement.

**Market:** Observability and incident response vendors, and SRE organisations directly. The argument is on-call sustainability rather than tooling features, which reaches engineering leadership rather than a platform budget.
