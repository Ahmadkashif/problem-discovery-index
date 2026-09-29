# Machine Learning Opportunities — SaaS Implementation Partners

**Industry:** [[saas-implementation-partners|SaaS Implementation Partners]]
**Derived from:** [[problems/saas-implementation-partners/high-impact|High Impact]], [[problems/saas-implementation-partners/low-impact-1|Low Impact 1]], [[problems/saas-implementation-partners/low-impact-2|Low Impact 2]], [[problems/saas-implementation-partners/worker-life-1|Worker Life 1]], [[problems/saas-implementation-partners/worker-life-2|Worker Life 2]]

---

## 1. Configuration Outcome Modelling Across a Delivery Portfolio
#gradient-boosting #survival-analysis #causal-inference #k-nearest-neighbors #confidence-intervals #evaluation-metrics #data-integration #tacit-knowledge-ml

**Problem statement:** A partner has configured the same platform hundreds of times and the adoption outcome of every one sits in a customer tenant the partner loses access to at hypercare. The firm's experience compounds into individuals' intuitions rather than into evidence.

**ML task:** Normalise configurations into a comparable representation, join them to post-go-live adoption telemetry, and predict which patterns are adopted or abandoned for organisations of a given shape
**Input data:** Platform configuration metadata per tenant — objects, fields, automations, approval structures, integration patterns, customisation depth; aggregated and anonymised usage telemetry under a post-go-live clause; organisation characteristics — size, industry, process maturity, prior system; implementation project characteristics.
**Target:** Adoption at 90 and 180 days per configured capability, and abandonment of specific workflows.
**Evaluation metric:** Predictive accuracy on held-out customers rather than held-out time periods, because the use is to advise a new client. Report abandonment prediction separately and prominently: the commercially uncomfortable finding is likely to be that a meaningful share of built customisation is never used, and a model evaluated only on average adoption will not surface it. Intervals matter because early on the sample is a few dozen implementations.
**Scope:** The normalised configuration representation is the bulk of the work and is ordinary but substantial engineering across heterogeneous tenants, versions and releases. Telemetry access is a contract clause plus an aggregation design that addresses the legitimate customer concern about a vendor observing their staff's system use. 2 data engineers and 1 data scientist, 12 months to a usable first model.
**Data availability:** Configuration is accessible during engagements; telemetry currently is not and is negotiable. No single customer could build this, and the platform vendor sees configuration without the delivery context.

---

## 2. Integration Mapping Proposal From a Firm-Owned Corpus
#bert #word-embeddings #k-nearest-neighbors #graph-neural-networks #gradient-boosting #large-language-models #evaluation-metrics #data-integration

**Problem statement:** The same partner has connected the same two major systems dozens of times, and each engagement re-authors the field mapping from scratch because the previous ones live in client environments under different contracts.

**ML task:** Propose field-level mappings and transformation rules between system pairs with confidence scores, inferred from schema, field values, and a corpus of the firm's prior mappings
**Input data:** Source and target schemas with field names, types and sample value distributions; the firm's historical mappings between the same system pairs, extracted into an owned corpus; transformation rules and their code-set translations; reconciliation outcomes showing which mappings later produced data quality problems.
**Target:** The mapping a consultant confirms, and downstream, whether the mapping produced reconciliation errors in production.
**Evaluation metric:** Top-1 and top-3 proposal accuracy against consultant-confirmed mappings, reported separately for fields that are obvious from the name and fields that are not — aggregate accuracy is dominated by the trivial cases and will look excellent while being useless. The more valuable metric is downstream: reconciliation error rate on mappings proposed by the model versus authored by hand.
**Scope:** Ambiguous columns must be inferred from values rather than names, which is where the human time actually goes. Extracting prior mappings into a firm-owned corpus is a contractual and process change before it is a technical one. 2 engineers, 6-9 months.
**Data availability:** Prior mappings exist in dozens of client environments and have never been consolidated. Schemas and sample values are available during an engagement.

---

## 3. Release Impact Analysis and Cross-Tenant Risk Propagation
#graph-neural-networks #gradient-boosting #large-language-models #change-point-detection #evaluation-metrics #feature-engineering #automation #workflow-orchestration

**Problem statement:** Platforms release several times a year, every customisation is a breakage candidate, and testing is a manual subset chosen by judgement. A managed services partner assesses the same release independently across dozens of tenants.

**ML task:** Map release behaviour changes to a tenant's configuration dependency graph to rank customisations by exposure, and propagate a confirmed failure in one tenant to every other tenant carrying the same pattern
**Input data:** Release notes and known-issue lists parsed as structured behaviour changes; per-tenant configuration metadata and its dependency graph; historical release-related failures with the configuration patterns involved; production exercise frequency per customisation; the partner's estate of managed tenants.
**Target:** Whether a given customisation breaks following a release.
**Evaluation metric:** Recall on actual breakages at a test-suite budget — the operational claim is narrowing eight hundred tests to forty, so the measure is what proportion of real failures the forty catch. Report the false negative cases in detail, since an undetected breakage in production is the cost this exists to avoid. For cross-tenant propagation, measure the lead time between the first tenant's failure and the proactive check reaching the others.
**Scope:** Cross-tenant propagation is the highest-value piece and only a managed services partner is positioned to do it — one customer's production failure becomes a prevented failure across the estate. Parsing release notes into structured change descriptions is the enabling step and is well within reach. 2 engineers, 6-9 months.
**Data availability:** Configuration metadata and release notes are fully available. Historical failure records exist in ticket systems and need labelling.

---

## 4. Configuration Intent Reconstruction and Accumulation Detection
#large-language-models #bert #graph-neural-networks #gradient-boosting #k-means-clustering #evaluation-metrics #worker-facing #tacit-knowledge-ml

**Problem statement:** Support engineers inherit tenants with hundreds of configuration elements and no record of why any of them exist, so every change begins with archaeology and carries risk they did not create.

**ML task:** Link configuration elements to the requirements, change requests and correspondence that produced them, and detect accumulated dead configuration with evidence
**Input data:** Configuration metadata and its dependency graph; requirements documents, change requests, project correspondence and ticket history; production exercise data — which automations fire, which fields are populated, which rules ever match; modification timestamps and authorship.
**Target:** The originating requirement or discussion for a configuration element, verified by consultant review; and whether an element is genuinely dead.
**Evaluation metric:** Retrieval precision for intent linkage on a reviewed sample, with abstention treated as a correct answer where no record exists — a fabricated rationale for a compliance-driven rule is considerably worse than admitting the reason is unrecorded, and this is the failure mode to test for hardest. For accumulation, precision on dead-element identification must be very high, since the action is deletion and a field feeding a silently-failing integration looks unused right up until it is removed.
**Scope:** The dependency graph alone removes most of the archaeology and requires no modelling. Intent reconstruction is the higher-value and riskier half. Blast-radius reporting before a change, combining dependencies with production exercise frequency, is what turns a nervous change into an assessed one. 2 engineers, 6-9 months.
**Data availability:** Configuration and production exercise data are directly available. Project correspondence is scattered across client systems and is the integration challenge.
