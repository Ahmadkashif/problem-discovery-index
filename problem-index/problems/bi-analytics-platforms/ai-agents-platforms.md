# AI Agents & Platform Opportunities — BI & Analytics Platforms

**Industry:** [[bi-analytics-platforms|BI & Analytics Platforms]]

---

## 1. Semantic Integrity Platform
#ai-platform #bert #graph-neural-networks #dbscan #large-language-models #hypothesis-testing #evaluation-metrics #data-integration

**Concept:** A platform that finds where an organisation disagrees with itself. It fingerprints every computed field across the asset estate from the query logic, clusters by business term, and surfaces the cases where the same name maps to materially different logic — ranked by combined usage, so the divergences appearing in executive reporting come first and the two hundred in unused dashboards do not. For each it proposes a canonical definition, names an owner, and shows the migration impact: which assets change and by how much, which is the number that determines whether the change can actually happen.

**Inputs:** Query and dashboard definitions with parsed SQL; lineage graphs; usage telemetry by viewer and role; semantic layer definitions where present; certification status.

**Outputs / Actions:** A ranked divergence list with both definitions side by side. Proposed canonical definitions with owners. Migration impact analysis per divergence. Ongoing monitoring so new drift is caught at creation rather than in a meeting. A gate for natural language querying, so generated queries compute canonical definitions rather than inventing new ones.

**Why now:** Natural language querying makes the definition choice invisible, which turns a chronic problem into an accelerating one. The detection has always been possible from stored query logic and was never attempted because the problem was framed as governance discipline rather than as detection.

**Market:** BI vendors, data catalogue vendors, and enterprise data platform teams. Definition drift is why organisations do not trust their dashboards, and distrust is what keeps the analyst request queue full — which makes this the upstream fix for the category's most persistent complaint.

---

## 2. Estate Curation Agent
#ai-agent #gradient-boosting #bert #dbscan #evaluation-metrics #automation #workflow-orchestration

**Concept:** An agent that keeps the analytics estate manageable. It classifies every asset as archive, duplicate, broken or certified, using usage telemetry, lineage, query semantics and execution outcomes. Archival is reversible by design, which removes the fear that made deletion impossible. It detects silently broken assets — zero-row results, deprecated source tables, filters bounded to a date range that ended two years ago — which are actively harmful because people still read them. And it certifies on evidence rather than on volunteers: widely used, built on governed sources, consistent with canonical definitions, not broken.

**Inputs:** Asset definitions and query logic; usage telemetry; lineage and downstream dependencies; execution results and error rates; source table deprecation; authorship and edit history.

**Outputs / Actions:** Reversible archive proposals with usage evidence. Duplicate clusters with a suggested survivor. Brokenness alerts routed to the asset owner. Evidence-based certification badges that update automatically. A monthly estate health report showing what grew, what decayed and what is now trusted.

**Why now:** Every platform has collected this telemetry for years without acting on it, and reversible archival is the small design change that resolves the rational fear keeping eleven thousand dashboards alive.

**Market:** BI platform vendors and enterprise analytics teams. Sprawl is universal past a certain deployment size and is the reason discovery fails, which is the reason people ask an analyst instead.

---

## 3. Pipeline Reliability Agent
#ai-agent #change-point-detection #gradient-boosting #bert #time-series-forecasting #evaluation-metrics #automation #worker-facing

**Concept:** An agent that handles the pipeline failures that repeat. It classifies each failure from the log and context into the small set of recurring causes, attempts the deterministic remedy where one exists — retry with backoff, wait-and-rerun for a late dependency, backfill a known gap — and pages a human only when the automated attempt fails or the cause is genuinely novel. It monitors upstream source schemas before the run rather than discovering a change when the transform breaks, and it models each data series with its real seasonality so the quality alerts stop crying wolf. It keeps a recurrence register: which failure classes consume on-call time, ranked.

**Inputs:** Pipeline execution logs and error traces; job dependency graphs and schedules; upstream source schemas; historical failures with their eventual remedies; per-table volume, freshness and distribution history; downstream asset usage for consequence routing.

**Outputs / Actions:** Automated remediation for known deterministic classes. Pages carrying the likely cause and the historical remedy rather than a stack trace. Pre-run schema change alerts. Series-aware quality anomalies routed by downstream consequence. A ranked recurrence register for the reliability investment conversation.

**Why now:** Failure classification from logs is straightforward and the remedies are already known to every engineer on the rota — the automation simply lost every prioritisation contest against delivery work. The recurrence register is what changes that argument.

**Market:** Data platform teams, data observability vendors and orchestration vendors. On-call load is a leading cause of data engineering attrition, and most of it is the eleventh instance of a known failure.
