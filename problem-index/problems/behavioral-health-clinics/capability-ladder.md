# ML Capability Ladder — Behavioral Health Clinics

**Industry:** [[behavioral-health-clinics|Behavioral Health Clinics]]

Sequenced from the easiest “ship in a sprint” wins to the hardest “multi-quarter build.” Each rung references the existing problem cards so a novice can start small and progress toward the toughest impact areas.

---

## 0) Foundation — Data, Privacy, and Labels
- **Ties to:** [[problems/behavioral-health-clinics/high-impact|Unified Behavioral Health Record Fragmentation]] (data sharing), [[problems/behavioral-health-clinics/worker-life-1|Documentation Burden]]
- **Do first:** Map where PHQ/GAD/PCL scores, scheduling, and credentialing timestamps live; set up consent flags for 42 CFR Part 2/psychotherapy notes; create a small labeled sample (50–100 notes) for risk terms.
- **Exit criteria:** Tables/exports exist for outcome scores and credentialing events; a redacted note set is available for downstream models.

## 1) Novice Quick Wins — Structured Signals
- **Ties to:** [[problems/behavioral-health-clinics/low-impact-1|Outcome Measurement Automation]], [[problems/behavioral-health-clinics/low-impact-2|Credentialing Workflow]]
- **Projects:**  
  - PHQ-9 / GAD-7 deterioration alerts (rule baseline → simple change-point model).  
  - Credentialing SLA risk flag (logistic/gradient-boosted trees on payer, state, completeness).
- **Why start here:** Fully structured data, small samples (a few hundred rows) are enough. Lets a novice practice data cleaning, train/val splits, and monitoring without heavy ML.
- **Exit criteria:** 90%+ recall on deterioration alerts with tolerable precision; MAE within ~10 days on credentialing timelines.

## 2) Practitioner Productivity — LLM Note Drafting
- **Ties to:** [[problems/behavioral-health-clinics/worker-life-1|Documentation Burden]], [[problems/behavioral-health-clinics/ml-opportunity|Progress Note Auto-Structuring]]
- **Projects:** Prompt an LLM to turn 2–3 minute post-session dictations into DAP/BIRP drafts; add guardrails for medical-necessity language.
- **Skills:** Prompt engineering, eval-by-checklist, small fine-tune on ~1k note pairs when ready.
- **Exit criteria:** >70% clinician acceptance with minimal edits; charting time cut by 30–50%.

## 3) Tacit Knowledge Capture — Risk Signal Extraction
- **Ties to:** [[problems/behavioral-health-clinics/high-impact|Unified Record]], [[problems/behavioral-health-clinics/ml-opportunity|Clinical Risk Signal Extraction from Therapy Notes]]
- **Projects:** Fine-tune NER + risk classifiers (BioClinicalBERT-family) on the redacted note set for suicide ideation, substance use, mood direction, med side-effects.
- **Skills:** Annotation protocol design with clinicians, handling class imbalance, high-recall tuning, PHI scrubbing.
- **Exit criteria:** F1 ≥0.85 overall with recall ≥0.95 on suicide/risk entities; zero PHI leakage in outputs.

## 4) Intermediate — Patient↔Clinician Matching
- **Ties to:** [[problems/behavioral-health-clinics/ml-opportunity|Patient-Clinician Match Prediction]]
- **Projects:** Train a ranking/recommendation model using intake fields, clinician specialties, and retention past session 3 as the target.
- **Skills:** Feature engineering on small-tabular data, NDCG evaluation, bias/eligibility checks (licensure, payer panels).
- **Exit criteria:** Top-3 recall/precision lift vs. manual routing; reduction in transfers/no-shows for early sessions.

## 5) Advanced — Unified Behavioral Health Record Layer
- **Ties to:** [[problems/behavioral-health-clinics/high-impact|Unified Behavioral Health Record Fragmentation]]
- **Projects:** Orchestrate outputs from stages 2–4 into a consent-aware patient status board: structured risk signals, outcome trend alerts, note drafts, and match recommendations gated by 42 CFR Part 2/HIPAA rules.
- **Skills:** Data orchestration, policy enforcement by design, human-in-the-loop review, monitoring drift/false negatives in safety-critical flags.
- **Exit criteria:** Clinicians no longer chase siloed notes; measurable drop in adverse interactions and 15–20 minutes/day saved in cross-provider coordination.

---

### How to Use This Ladder
1. Ship one artifact per rung (alert, model, dashboard) before advancing.  
2. Keep evaluation lightweight but strict (precision/recall for safety, NDCG for matching, acceptance-rate for LLM).  
3. Reuse the same data pipelines as you climb; only the models and oversight deepen.
