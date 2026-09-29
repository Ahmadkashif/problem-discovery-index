# AI Agents & Platform Opportunities — Digital Forensics Firms

**Industry:** [[digital-forensics-firms|Digital Forensics Firms]]

---

## 1. Scope Determination Platform
#ai-platform #bayesian-inference #confidence-intervals #graph-neural-networks #probability-distributions #hypothesis-testing #compliance #evaluation-metrics

**Concept:** A platform that makes the determination governing notification into an explicit, defensible inference rather than a narrative. Given the evidence actually available, it bounds what the attacker could have reached, estimates access probability per system and data store from observed artefacts, the known capabilities of the tooling involved and the firm's corpus of comparable intrusions, and partitions the result into established, probable with a stated probability, and cannot be excluded. The evidence chain behind every probability is inspectable, because the output has to survive lawyers, regulators and potentially a court.

**Inputs:** Available artefacts and the specific gaps; the attacker's tooling and its documented capabilities; environment topology and access paths; the firm's corpus of prior intrusions with what was eventually established; cases where ground truth later emerged.

**Outputs / Actions:** A bounded scope with per-system probabilities, in which the cannot-be-excluded category is prominent rather than buried in a limitations section readers skip. A calibration record built from the cases where litigation, disclosure or leak sites later established the truth — the field's only available validation and one nobody collects systematically. An explicit statement of what the evidence cannot support, which is frequently the most valuable line in a forensic report.

**Why now:** Both error directions carry real cost — over-scoping alarms people whose data was unaffected, under-scoping fails people whose data was — and the current practice resolves that under diffuse pressure toward a cleaner narrative than the evidence supports. A firm that states bounds and can show its calibration is in a stronger position, not a weaker one.

**Market:** Incident response firms, the cyber insurers reserving against scope determinations, and the legal teams making notification decisions on the basis of them.

---

## 2. Investigation Acceleration Agent
#ai-agent #change-point-detection #graph-neural-networks #gradient-boosting #bert #confidence-intervals #automation #worker-facing

**Concept:** An agent that compresses the acute phase, which is the most direct way to reduce both the client's period of uncertainty and the responder's period of not stopping. It builds an environment baseline from retained data mid-incident, surfaces the anomalous and pattern-matching events out of millions, correlates the same action across endpoint, authentication, network and cloud sources into single narrative units, and reconciles clock skew while carrying the residual ordering uncertainty into the findings rather than assuming it away. Everything remains available and auditable, because a filter that hides is unusable in a forensic context.

**Inputs:** Parsed events across all sources; retained historical data for baselining; known intrusion patterns from the corpus; events observable in multiple sources for skew estimation; the examiner's own marks and queries.

**Outputs / Actions:** A reduced candidate set with recall on examiner-relevant events as the binding constraint. Cross-source correlated actions, which is where the narrative actually comes from. Reported clock uncertainty rather than a silent correction, since sequence is what is being established and a misalignment can reverse a causal reading in a document used for a legal determination. And a defensible record generated from the work itself — every action, query and artefact examined — which removes the documentation burden without weakening it, at exactly the point in a deadline where it is currently compressed.

**Why now:** Endpoint telemetry has made rich evidence available where it is deployed, which has moved the constraint from collection to reduction — and reduction is still manual.

**Market:** Incident response firms, corporate internal investigation teams, and the forensic tooling vendors whose timeline products currently produce volume rather than reduction.

---

## 3. Readiness and Capacity Platform
#ai-platform #graph-neural-networks #gradient-boosting #time-series-forecasting #confidence-intervals #large-language-models #compliance #worker-facing

**Concept:** A platform that moves this industry's value before the incident and staffs for the waves. On readiness, it maps an organisation's evidence posture against plausible intrusion paths and names the specific gaps that would make a future scope determination unanswerable — this system's logs expire in seven days, it has access to this data store, so an intrusion discovered after a week could not be scoped for that data. That is a named consequence, which changes a retention decision in a way that a maturity rating does not. On capacity, it forecasts incident demand from exploitation activity against widely-deployed software, which produces a predictable wave with a known lag that firms currently absorb rather than staff for.

**Inputs:** Client log retention configuration and actual retained volumes, monitoring coverage, cloud audit settings, asset inventory and data location; access paths; the firm's corpus of investigations with the gaps that proved decisive; public exploitation activity and installed-base estimates; the firm's own staffing and engagement history.

**Outputs / Actions:** A gap assessment expressed as named systems, named data and named unanswerable questions, validated retrospectively against whether it would have predicted the gaps that actually mattered in past cases. A demand forecast with lead time, so senior capacity can be rotated rather than exhausted. Report assembly from the investigation record with the limitations section generated from the actual evidence gaps, which removes the post-engagement work that currently overlaps the next engagement. And a corpus that makes less experienced responders more capable, which is the only real answer to a labour pool this small.

**Why now:** The field has acknowledged its working pattern is unsustainable for a decade without changing it, and its attrition removes exactly the senior judgement that scope determinations depend on. The rotation question is a cost comparison — utilisation against attrition — that nobody has actually made.

**Market:** Incident response firms and their insurer panels, enterprise security teams buying readiness rather than response, and the cyber insurers whose losses depend on both.
