# Machine Learning Opportunities — Expert Networks

**Industry:** [[expert-networks|Expert Networks]]
**Derived from:** [[problems/expert-networks/high-impact|High Impact]], [[problems/expert-networks/low-impact-1|Low Impact 1]], [[problems/expert-networks/low-impact-2|Low Impact 2]], [[problems/expert-networks/worker-life-1|Worker Life 1]], [[problems/expert-networks/worker-life-2|Worker Life 2]]

---

## 1. Expert–Request Fit Prediction From Senior Reviewer Judgement
#tacit-knowledge-ml #gradient-boosting #large-language-models #k-nearest-neighbors #causal-inference #evaluation-metrics #feature-engineering #revenue-impact

**Problem statement:** Senior project managers can read a candidate's profile and screener answers and sense whether that person actually made the decision the client is asking about. Capture that judgement and the call outcomes it predicts, and rank candidates for associates by the probability the call will address the client's question.

**ML task:** Pairwise and pointwise ranking of candidate experts against a free-text request, with a calibrated probability of a successful call, plus nearest-neighbour retrieval of comparable past experts
**Input data:** The client request text; candidate profile (employer history, titles, tenure, dates); screener questions and the candidate's answers; network history for the candidate and for prior experts from the same employer and role; outcome signals per completed call — client selection, rating, call duration versus booked, dispute or refund, rebooking of the same expert, and (with consent) the share of the transcript that addresses the stated question; senior reviewer triage decisions with a one-line reason collected on a calibration sample.
**Target:** Probability that the call is rated successful and not disputed; secondary target of the reviewer's forward/drop decision.
**Evaluation metric:** Precision at the top three to five forwarded profiles, since a client reads only the first few, measured against call outcomes. Calibration matters because associates will act on the score. Report inter-reviewer agreement (Cohen's kappa) on the calibration sample as the ceiling: a model that agrees with seniors more than seniors agree with each other is overfitting their vocabulary.
**Scope:** The difficulty is the label, not the model. Data collection requires recording senior reviewers triaging live candidates with a reason, which costs their time in a speed-driven business; run it as a weekly calibration session on a few hundred profiles rather than continuously. Labelling is noisy because a bad call can be the client's fault and because forwarded candidates are a selected population — propensity weighting on the forward decision and a small exploration budget (forwarding a few borderline candidates deliberately) are what make the outcome labels usable. Deployment has to be faster than a glance: a rank and a one-line reason inside the existing CRM, never a separate screen. 2 ML engineers and a data engineer, 6 months, with a senior project manager seconded part-time.
**Data availability:** Large networks hold hundreds of thousands of completed calls a year with ratings and disputes; profiles and screener answers are retained. Reviewer reasoning does not exist anywhere and must be collected. Transcript-derived relevance is only available where the client consented to recording.

---

## 2. MNPI Risk Detection in Expert Call Transcripts
#bert #transformers #large-language-models #evaluation-metrics #confidence-intervals #compliance #automation

**Problem statement:** Distinguish statements in an expert call that disclose specific, non-public, company-level information (contract wins and losses, unreleased results, pending deals, current pricing at a named company) from legitimate industry commentary, in near-real time during the call and in full on every transcript after it.

**ML task:** Span-level sequence classification over transcripts with a risk category and a severity score, plus a call-level escalation decision
**Input data:** Call transcripts (live streaming and post-call); expert profile with current and former employers and departure dates; the subject companies of the project; historical compliance reviewer decisions on flagged passages; the client's restricted-topic policy.
**Target:** For each passage, whether it requires compliance review and why (current-employer disclosure, specific undisclosed figure, deal information, government information).
**Evaluation metric:** Recall on reviewer-confirmed MNPI passages is the primary metric — a missed disclosure is the regulatory failure mode — reported with a confidence interval because positives are rare. Precision is tracked as reviewer workload; the operating point is set so the reviewed fraction stays within compliance capacity while recall stays above an agreed floor.
**Scope:** Positives are scarce and partly synthetic examples will be needed, written by compliance staff, to cover categories that rarely occur. Employer-awareness matters more than language: the same sentence is safe from a competitor's former employee and risky from the subject company's current one, so the expert's employment record is an input, not metadata. 2 ML engineers plus compliance reviewers for labelling, 5 months.
**Data availability:** Networks that record calls hold the transcripts and reviewer redaction history; libraries hold edited and raw versions, whose diff is a direct label for what reviewers removed.

---

## 3. Re-Identification Risk and Long-Tail Entity Resolution for Transcript Libraries
#transformers #bert #graph-theory #word-embeddings #evaluation-metrics #data-integration #automation

**Problem statement:** Anonymise transcripts by detecting combinations of details that jointly identify the expert or the client, rather than redacting named entities wholesale, and link every company, product and informal reference in the transcript to canonical identifiers including private companies and their public peers.

**ML task:** Named-entity recognition and entity linking against a company graph, plus a re-identification risk score computed against the expert's own profile and the population of possible experts
**Input data:** Raw and editor-redacted transcripts; expert profiles; company and subsidiary identifier databases; the library's existing tags; subscriber search logs.
**Target:** Linked entity mentions with confidence; a per-transcript re-identification risk with the contributing spans.
**Evaluation metric:** Entity linking F1 on the long tail (private companies, products) separately from large public names, since the head is easy; for anonymisation, the rate at which an adversarial reviewer can identify the expert from the redacted text, compared with editor-only redaction.
**Scope:** The editor diff between raw and published transcripts provides tens of thousands of labelled redaction decisions; entity linking for private companies needs a maintained company graph, which is the bulk of the effort. 2 ML engineers and a data engineer, 5 months.
**Data availability:** Good inside libraries; the company graph for private companies is partially purchasable and partially built from the library's own tags.

---

## 4. Claim Extraction and Cross-Call Agreement Mapping
#large-language-models #transformers #word-embeddings #k-means-clustering #evaluation-metrics #workflow-orchestration #worker-facing

**Problem statement:** Across all calls and library transcripts in a research project, extract the specific claims experts made, cluster them by question, and show which claims are corroborated, contradicted or unsupported, weighted by the source's relationship to the company and recency.

**ML task:** Claim extraction (sequence-to-structure), semantic clustering, and pairwise stance classification (agree / contradict / unrelated)
**Input data:** Project transcripts and analyst notes; expert metadata (role, employer, tenure, departure date, relationship to subject company); library transcripts retrieved for the same companies.
**Target:** A structured claim table with sources, clusters and stance relations.
**Evaluation metric:** Faithfulness first — every extracted claim must be traceable to transcript lines, measured by human audit of a sample, with a near-zero tolerance for unsupported claims. Then stance accuracy on pairs and analyst-judged usefulness of the clustering.
**Scope:** Achievable with current language models; the work is in faithfulness checks and in a user interface that keeps the transcript one click away. 2 engineers, 3–4 months for a usable version.
**Data availability:** Clients own their transcripts and notes; the networks and libraries own the library corpus. Labelled stance pairs need a few thousand annotations.

---

## 5. Expert Claim Accuracy Ledger
#causal-inference #bayesian-inference #logistic-regression #large-language-models #evaluation-metrics #confidence-intervals #revenue-impact

**Problem statement:** Many statements in library transcripts are forward-looking or factual claims about industries and companies that later become publicly checkable — a product launch timing, a pricing trend, a market-share shift. Score them against what happened, and estimate the reliability of claims by expert type, tenure and recency.

**ML task:** Claim extraction with checkability classification, resolution against later public data, and a hierarchical model of claim accuracy by source characteristics
**Input data:** Timestamped library transcripts; expert metadata; subsequent public disclosures, filings, earnings transcripts and news for the companies named.
**Target:** Per-claim resolution (true, false, unresolved) and per-source-type reliability estimates.
**Evaluation metric:** Agreement of automated resolution with human adjudication on a sample; for reliability estimates, calibration of predicted claim accuracy on held-out time periods.
**Scope:** Only a fraction of claims are checkable and resolution is laborious; the value is in aggregate reliability by source type (former employees versus customers, by years since departure), not per-expert scores, which raise fairness and contractual issues. 2 ML engineers and an analyst, 6 months.
**Data availability:** Libraries hold the corpus with timestamps; public resolution data is purchasable. Nobody has assembled the join.
