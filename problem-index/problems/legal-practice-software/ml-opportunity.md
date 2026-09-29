# Machine Learning Opportunities — Legal Practice Software

**Industry:** [[legal-practice-software|Legal Practice Software]]
**Derived from:** [[problems/legal-practice-software/high-impact|High Impact]], [[problems/legal-practice-software/low-impact-1|Low Impact 1]], [[problems/legal-practice-software/low-impact-2|Low Impact 2]], [[problems/legal-practice-software/worker-life-1|Worker Life 1]], [[problems/legal-practice-software/worker-life-2|Worker Life 2]]

---

## 1. Billable Time Entry Reconstruction from Device Activity
#transformers #bert #large-language-models #word-embeddings #gradient-boosting #feature-engineering #evaluation-metrics #tacit-knowledge-ml #revenue-impact

**Problem statement:** Small-firm lawyers lose fifteen to thirty per cent of billable time by failing to record it. Existing tools present raw activity — documents opened, emails sent, calls made — and ask the lawyer to convert it into billable entries, which is the hard part and the part nobody has automated. The three judgements required are matter attribution, billable duration, and a narrative that survives client review.

**ML task:** Multi-stage — sequence segmentation of activity into work sessions, multiclass classification of session to matter, regression on billable duration, and conditional text generation for the narrative
**Input data:** Local device activity (application focus intervals, document open and edit events with file paths, email metadata and subject lines, calendar entries, call logs), the firm's matter list with parties and keywords, and the lawyer's own historical time entries as paired examples of activity to entry.
**Target:** The confirmed time entry — matter, duration in the firm's increment convention, and narrative text — with the lawyer's edits treated as the correction signal.
**Evaluation metric:** Fraction of proposed entries accepted without edit; matter attribution accuracy; mean absolute error on duration in tenths of an hour; and for narratives, edit distance from the lawyer's final text. The business metric is recovered hours per lawyer per week against a pre-deployment baseline.
**Scope:** Per-user personalisation is essential — matter vocabulary, rounding habits and narrative style are individual, and a global model will underperform a lightly fine-tuned personal one. Privileged content must not leave the device, so inference runs locally with a small model and only approved entries synchronise. 3 ML engineers plus a practising-lawyer advisor, 6-8 months.
**Data availability:** Historical time entries are abundant and clean in every platform. The activity side must be collected prospectively and consented to explicitly. The pairing between past activity and past entries does not exist retrospectively, so the first cohort trains on weak supervision from calendar and document timestamps before genuine paired data accumulates.

---

## 2. Court Rule Change Monitoring and Draft Rule Extraction
#large-language-models #bert #transformers #word-embeddings #change-point-detection #transfer-learning #compliance

**Problem statement:** Deadline calculation is only as good as the rule content behind it, and that content spans thousands of courts, divisions and standing orders that change without notification. Maintaining the long tail by hand is not fundable at any per-seat price the market supports, so coverage is deep where customers concentrate and untrustworthy elsewhere.

**ML task:** Document change detection over a large crawled corpus, plus information extraction converting rule text into structured deadline rules (trigger event, offset, counting convention, exclusions)
**Input data:** Crawled court websites, rule amendment notices, standing orders and judge-specific pages, versioned over time. Existing structured rule sets as extraction training pairs. Court holiday calendars. Secondarily, observed filing behaviour from the platform's own customers in each court.
**Target:** A detected material change with the affected rule, plus a structured draft rule for human verification.
**Evaluation metric:** Change detection recall against a manually tracked set of known amendments, with false positive rate per court per month as the operational constraint. For extraction, exact-match accuracy on trigger, offset and counting convention against the existing curated rule sets.
**Scope:** Distinguishing a material rule change from a website redesign is most of the difficulty and is best handled by extracting first and diffing the structure rather than diffing the text. Nothing publishes automatically — the output is a review queue for the content team. 2 ML engineers plus a rules attorney, 4-6 months.
**Data availability:** Court websites are public and highly heterogeneous, with some jurisdictions publishing only PDFs and a few only in print. Existing curated rule sets are the training asset and are typically licensed rather than owned, which constrains what may be used.

---

## 3. Template Induction from a Firm's Own Document Corpus
#large-language-models #transformers #bert #word-embeddings #k-means-clustering #transfer-learning #evaluation-metrics

**Problem statement:** Document assembly works and is unadopted at small firms because converting existing documents into templates with variables and conditional logic is a project lawyers start and abandon. Meanwhile every firm holds hundreds of past examples of each document it produces, which contain the template implicitly.

**ML task:** Document clustering by type, followed by multi-document alignment to separate invariant boilerplate from variable slots, plus slot typing and conditional-section detection
**Input data:** The firm's historical document corpus with matter metadata attached (matter type, parties, jurisdiction, dates, amounts). Across the customer base, the same corpus segmented by practice area and jurisdiction.
**Target:** A proposed template per document type: fixed text, typed variable slots mapped to matter fields, and conditional sections with the condition inferred from which matters included them.
**Evaluation metric:** Reconstruction accuracy — can the induced template regenerate held-out historical documents from their matter data — plus the proportion of slots a lawyer accepts without modification. Reconstruction is a strong proxy and is measurable without human review.
**Scope:** Multi-document alignment on legal text is the technical core and is well suited to it, because legal drafting is unusually repetitive. Jurisdiction and practice-area segmentation must come first or alignment produces mush. 2-3 ML engineers, 5 months. Firm documents are confidential and cross-customer training requires explicit permission that most firms will refuse, so the realistic design is per-firm induction with a shared architecture.
**Data availability:** Excellent within a firm and legally constrained across firms. Matter metadata linking documents to their variables is present in the platform for documents created inside it and absent for the migrated back catalogue, which is most of it.

---

## 4. Continuous Trust Account Anomaly Detection
#descriptive-statistics #change-point-detection #hypothesis-testing #confidence-intervals #evaluation-metrics #naive-bayes #compliance #automation

**Problem statement:** Trust accounting errors are detected at reconciliation, often months after the causing transaction, by which time dependent activity has accumulated and the discovery is frequently prompted by a bar audit. The errors themselves are mundane and would be trivial to correct on the day they occur.

**ML task:** Primarily deterministic rule evaluation with a statistical anomaly layer over transaction patterns; the interesting modelling is prioritisation, not detection
**Input data:** Trust transaction ledger (deposits, disbursements, fee transfers, bank fees) per client per account, invoice records, bank feed transactions, and the firm's historical pattern of transaction types, amounts and timing.
**Target:** A flagged transaction or ledger state with a rule violation or an anomaly score, and an assessment of whether it is likely a data entry error, a timing artefact, or a genuine compliance problem.
**Evaluation metric:** Detection latency measured in days from the causing transaction, and false positive rate per firm per month — the binding constraint, because a noisy trust alert is switched off immediately and this is the one alert that must never be ignored. Precision must be very high before any alert ships.
**Scope:** The deterministic checks — negative client ledger, disbursement exceeding client balance, fee transfer without invoice, operating expense against trust — deliver most of the value and require no modelling at all. The statistical layer handles the residual: unusual amounts, unusual timing, unusual counterparties for this firm. 1-2 engineers, 3 months, with a compliance attorney defining the rule set.
**Data availability:** Complete and internal. Bank feed integration quality is the main variable; firms without a connected feed reconcile against imported statements and detection latency inherits that cadence.
