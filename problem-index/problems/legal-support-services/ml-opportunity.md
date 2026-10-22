# Machine Learning Opportunities — Legal Support Services

**Industry:** [[legal-support-services|Legal Support Services]]
**Derived from:** [[problems/legal-support-services/high-impact|High Impact]], [[problems/legal-support-services/low-impact-1|Low Impact 1]], [[problems/legal-support-services/low-impact-2|Low Impact 2]], [[problems/legal-support-services/worker-life-1|Worker Life 1]], [[problems/legal-support-services/worker-life-2|Worker Life 2]]

---

## 1. Learning the Veteran Server's Attempt Plan
#tacit-knowledge-ml #gradient-boosting #survival-analysis #feature-engineering #evaluation-metrics #worker-facing #revenue-impact

**Problem statement:** Experienced process servers choose when to attempt, when to stake out, when to distrust an address and when to stop and document diligence, from cues they cannot fully state. The ML problem is to learn that plan from veteran servers' GPS-stamped attempt histories and outcomes, and recommend the next attempt window and an address-validity score for every open job.

**ML task:** Time-to-successful-service survival model with time-varying covariates, plus binary classification of address validity, combined into a ranked next-attempt recommendation
**Input data:** Attempt logs with GPS, timestamp, photo and outcome (served, no answer, occupant denies, moved, refused) from server-management software and national networks; job metadata (case type, plaintiff type, papers, deadline); address features (dwelling type, gated access, prior jobs at the address, skip-trace hit age and source); one-tap reason codes captured going forward; server identity and tenure.
**Target:** Hazard of successful service per attempt window; address-good probability; and, for evaluation, agreement between the model's ranked windows and the windows veteran servers chose.
**Evaluation metric:** Attempts per completed serve and days to service on a prospective holdout of jobs, against servers' unassisted performance — the operational metric the server is paid on. Concordance index for the survival model; calibration of the address-validity score, where a false "dead address" costs a missed serve and a false "good" costs one drive, so precision on the dead-address call matters more. Report veteran-versus-junior lift separately: the point is to give juniors the veteran's plan.
**Scope:** The data collection challenge comes first: GPS logs record where and when, not why, so the system needs a near-zero-effort reason code at the curb and must reconstruct sequences across the several networks a server subcontracts for. The labelling challenge is that "served" is a noisy label for a good plan — lucky fourth attempts and evasive subjects at good addresses abound — and experts are inconsistent with themselves, so a repeated-rating sample of veteran calls is needed to set the ceiling. The deployment challenge is that the recommendation must be on the phone before the server pulls away and beat their own instinct, or veterans will ignore it. 2 ML engineers and 1 product engineer embedded with one national network, 6–9 months, starting with retrieval ("last three attempts at this complex succeeded before 7 a.m.") before any model ranks windows.
**Data availability:** National networks and server-software vendors hold millions of geotagged attempts (estimate); NYC-licensed servers must already keep tamper-proof electronic logs. Outcomes are recorded per job. Reason codes do not exist yet and must be captured prospectively.

---

## 2. Grading the Patent Searcher's Relevance Calls
#tacit-knowledge-ml #transformers #bert #contrastive-learning #evaluation-metrics #feature-engineering #revenue-impact

**Problem statement:** A senior patent searcher knows which classification groups, conference proceedings and foreign utility models hold the closest art, and rates each reference's relevance to each claim element by a judgement developed over thousands of searches. Learn those calls from the search house's archive of charted references, and grade them against what examiners and the PTAB later relied on.

**ML task:** Claim-element-to-passage retrieval and learning-to-rank, with a calibrated relevance category per reference (closest, combinable, background)
**Input data:** The house's archive of claim charts and reference ratings by analyst; target patents' claims and specifications; full-text patent and non-patent literature with classification codes; examiner citations, PCT search report categories (X, Y, A) and PTAB institution and final written decisions, which are public and dated.
**Target:** Passage-level relevance to each claim element; reference category; and the downstream outcome — cited by the examiner, relied on in an instituted ground, or claims found unpatentable on it.
**Evaluation metric:** Recall at k of references later relied on by the PTAB or the examiner, on patents held out by date — a search beaten by art found later is the failure the client pays to avoid, so recall dominates precision. Agreement with held-out analyst ratings, reported against senior analysts' own test-retest agreement as the ceiling.
**Scope:** Collection: the archive exists in Word and Excel charts and must be parsed into structured element-passage pairs, and the analyst's search path (queries, classes visited, documents rejected) is rarely saved. Labelling: analysts disagree on "closest", and PTAB outcomes are a biased label (only petitions filed and decided). Deployment: suggestions must surface inside the search session, faster than the analyst's own next query. 2 ML engineers, 1 data engineer and a senior searcher, 8–12 months.
**Data availability:** Patent literature, examiner citations, IPR petitions and PTAB decisions are public and can seed a model on their own. The decisive asset — the house's charted relevance calls — is client work product delivered under confidentiality, so training on it needs client consent or must stay inside each client's own matters; invalidity contentions are served rather than docketed, often under protective order, so they are not a public label.

---

## 3. Affidavit Plausibility Against the Device Trail
#gaussian-mixture-models #dbscan #hypothesis-testing #feature-engineering #evaluation-metrics #compliance

**Problem statement:** Score every affidavit of service, before it is filed, for the patterns that indicate fabricated or careless service, using the server's own device trail and the population of other serves.

**ML task:** Unsupervised anomaly detection on spatio-temporal attempt sequences, with rule-based impossibility checks and a supervised layer where outcomes exist
**Input data:** GPS traces and timestamps for all attempts by a server in a day; affidavit text (time, place, person served, physical description); subject's known schedule signals where lawful; historical traverse-hearing outcomes and vacated defaults.
**Target:** Plausibility score per affidavit and named reason (impossible travel, simultaneous serves, recycled descriptions, attempts outside plausible windows).
**Evaluation metric:** Precision at a fixed review budget, because every flag is a human review and a false accusation damages a server's livelihood; recall measured on seeded synthetic violations and on the rare adjudicated cases.
**Scope:** Labels are scarce and biased (traverse hearings are rare), so the model is anomaly-first with transparent rules. 1 data scientist and 1 engineer, 4–5 months, with a network or a volume filer as the buyer.
**Data availability:** Networks hold the device trails; affidavits are filed with courts. Adjudicated outcomes must be collected from court records.

---

## 4. Predicting Clerk Rejections of E-Filings
#gradient-boosting #logistic-regression #large-language-models #feature-engineering #evaluation-metrics #automation

**Problem statement:** Predict, before submission, whether a court's clerk will reject an electronic filing envelope, and why, so the filer fixes it while the deadline still allows.

**ML task:** Binary classification of rejection plus multiclass rejection reason; LLM extraction of reasons from historical clerk rejection notices
**Input data:** Envelope metadata (court, case type code, filing code, fees, party data), document properties (page size, signatures, bookmarks, redaction), historical rejection notices and their free-text reasons.
**Target:** Accept/reject and the rejection category.
**Evaluation metric:** Recall on rejections at a modest false-alarm rate — a missed rejection near a deadline can cost the case, while a false alarm costs a minute of checking.
**Scope:** 1 ML engineer, 3–4 months per e-filing system; rules vary by county, so the model must learn per-court patterns from enough volume.
**Data availability:** E-filing service providers and attorney-service companies hold years of envelopes and rejection notices.

---

## 5. Service-of-Process Intake Extraction
#large-language-models #transformers #seq2seq #evaluation-metrics #automation #compliance

**Problem statement:** Read every document served on a registered agent or corporate legal department and extract the entity served, court, case type, plaintiff, and the computed answer deadline, routing it the same day.

**ML task:** Document classification and structured extraction, with rule-based deadline computation from extracted court and service method
**Input data:** Scanned summonses, complaints, subpoenas, garnishments and agency notices; jurisdiction rules for response periods.
**Target:** Structured intake record with answer date and routing.
**Evaluation metric:** Field-level accuracy, with zero tolerance for a wrong or missing answer date — a silent error is a default judgment.
**Scope:** 2 engineers, 4 months; the long tail is garnishments and agency notices with unusual formats.
**Data availability:** Registered agents hold the corpus, though the documents belong to the client entities served.
