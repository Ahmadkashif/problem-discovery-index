# Machine Learning Opportunities — Executive Search Firms

**Industry:** [[executive-search-firms|Executive Search Firms]]
**Derived from:** [[problems/executive-search-firms/high-impact|High Impact]], [[problems/executive-search-firms/low-impact-1|Low Impact 1]], [[problems/executive-search-firms/low-impact-2|Low Impact 2]], [[problems/executive-search-firms/worker-life-1|Worker Life 1]], [[problems/executive-search-firms/worker-life-2|Worker Life 2]]

---

## 1. Learning the Consultant's Read of a Candidate
#tacit-knowledge-ml #large-language-models #transformers #survival-analysis #gradient-boosting #evaluation-metrics #revenue-impact

**Problem statement:** Experienced search consultants read an interview or a reference and "know" that a career story is too polished, that a candidate depends on a particular founder, or that a reference's praise is code for weak execution. The ML problem is to capture those reads from the consultant's own notes and annotations, join them to what happened to the executive afterwards, and surface the patterns that predicted early failure to whoever runs the next assessment.

**ML task:** Passage-level multi-label classification of interview and reference text into the firm's assessment vocabulary (derailer types, evidence strength, motivation to move), plus a time-to-departure survival model conditioned on those signals, the role, the ownership type and the consultant's confidence
**Input data:** Interview notes and transcripts, off-list and on-list reference notes, candidate reports, psychometric scores where used, the consultant's recommendation and confidence, the brief; outcomes from Form 8-K Item 5.02 filings (departures and demotions within four business days), press releases, sponsor portfolio pages and biography changes, coded for reason where inferable.
**Target:** Passage labels in the consultant's own terms; hazard of involuntary departure within 18 and 36 months, with takeover- and restructuring-driven exits censored rather than counted as failure; agreement between model and consultant.
**Evaluation metric:** Concordance and time-dependent AUC at 18 months, strictly out of time — a model validated on random splits will learn the firm's recent client mix. For passage labels, agreement with held-out consultant annotations reported against the consultant's own test-retest agreement as the ceiling. Recall on true early failures matters more than precision: a missed derailer costs a replacement search, a false flag costs one more reference call.
**Scope:** The data collection challenge comes first: consultants' doubts are spoken in debriefs rather than written in reports, so the system needs a near-zero-effort capture surface — a one-minute voice debrief after each interview, transcribed and structured — and historical notes must be aligned to outcomes after the fact. The labelling challenge is that consultants disagree with themselves and each other, so a sample needs repeated blind annotation to measure intra- and inter-rater reliability, and tenure must be adjusted for departures unrelated to the hire. The deployment challenge is speed: the signal must appear before the debrief and the shortlist, quicker than the consultant's recall, or it will be ignored. 2 ML engineers and a research lead embedded with one practice, 9–12 months, with value arriving first as retrieval ("the last three placements with this pattern") before any score is trusted.
**Data availability:** Interview and reference notes exist in CRMs and document stores at every established firm, unevenly. Public-company outcomes are free and dated; private-company outcomes need monitoring. Presented-but-not-hired candidates must be followed too, or the model learns only the firm's selection. Client consent and data-protection terms for reusing assessment notes must be settled before any modelling.

---

## 2. Candidate Move-Propensity Scoring
#gradient-boosting #logistic-regression #survival-analysis #feature-engineering #evaluation-metrics #revenue-impact

**Problem statement:** Predict, before the first approach and again before the shortlist, the probability that a sitting executive will engage, progress and finally accept a move, so consultants spend scarce conversations on candidates who will actually come.

**ML task:** Multi-stage binary classification (responds; progresses to interview; accepts offer) plus time-to-move survival modelling on the general population of mapped executives
**Input data:** Tenure in role and company; vesting calendar inferred from proxies and Form 4 filings for public-company officers; company events (new CEO, acquisition, restructuring, share-price drawdown); prior approach history and responses in the firm's CRM; stated motivations from conversations; relocation requirements; counteroffer history.
**Target:** Response to approach; progression; offer acceptance; withdrawal after acceptance.
**Evaluation metric:** AUC and calibration per stage, with lift in the top decile of the longlist as the business metric. Calibration matters more than ranking for the final stage: a consultant deciding whether to present a candidate needs a believable probability, not an order.
**Scope:** A gradient-boosted baseline on CRM history is achievable in a quarter with 1 data scientist and 1 engineer; the survival layer on mapped-but-never-approached executives needs public career-move data. The honest difficulty is that the most predictive signals (a candidate's private reasons) are in free text and must be extracted.
**Data availability:** Approach and response history is in the firm's own CRM and is the firm's data; vesting and event data are public for listed companies and thin for private ones.

---

## 3. Title Levelling and Market Map Resolution
#bert #word-embeddings #k-nearest-neighbors #graph-theory #evaluation-metrics #data-integration #automation

**Problem statement:** Turn a target company list into a correctly levelled map of who holds which role, resolving inconsistent titles to a common function and level and resolving employer names to corporate families for off-limits checks.

**ML task:** Title-to-function-and-level classification with embedding nearest-neighbour retrieval against the firm's past levelled maps; entity resolution of employers to ultimate parents and sponsor portfolios; reporting-line inference from filings and announcements
**Input data:** Titles and descriptions from company sites, filings, press releases and the firm's CRM; company size and structure; corporate hierarchy data; historical maps levelled by researchers; client off-limits terms.
**Target:** Function and level per person; employer-to-family links; off-limits status per name with the rule that triggered it.
**Evaluation metric:** Accuracy of level assignment against researcher-levelled held-out maps, with "one level off" reported separately; for off-limits, recall on true conflicts is the binding metric because a missed conflict loses a client, with precision tracked so researchers trust the flags.
**Scope:** The firm's past maps are the training set and are larger than firms realise. 1 ML engineer and 1 researcher for labelling, 4–5 months to a first version for one practice.
**Data availability:** Historical maps sit in spreadsheets attached to closed mandates and need consolidation; corporate hierarchy data is licensable.

---

## 4. Make-Whole Valuation With Payout Simulation
#monte-carlo-methods #probability-distributions #large-language-models #feature-engineering #revenue-impact #automation

**Problem statement:** Estimate the value a candidate forfeits by moving — unvested restricted stock, performance shares, options, in-year bonus, tenure-vested deferred pay — with uncertainty bands, early enough to know whether the client can afford them.

**ML task:** Document extraction of grant terms from statements and plan documents; Monte Carlo simulation of performance-share payouts and option values under share-price and metric uncertainty
**Input data:** Candidate-provided grant statements (shared under confidentiality); proxy and Form 4 data for named officers; plan documents; peer metric histories; share-price volatility.
**Target:** Distribution of forfeited value by component and date; recommended make-whole structures within the client's plan limits.
**Evaluation metric:** Extraction accuracy on grant terms (zero tolerance for a missed tranche); calibration of simulated performance-share payouts against realised payouts for disclosed named officers; the business metric is the share of offers that do not collapse on make-whole.
**Scope:** The simulation is standard quantitative finance; the work is extraction across messy statements and plan rules. 1 engineer and 1 quantitative analyst, 3–4 months.
**Data availability:** Realised payouts for named officers are public in proxies; candidate statements are personal and confidential and must not be retained beyond the search without consent.

---

## 5. Candidate Report and Progress Report Drafting
#large-language-models #seq2seq #transformers #evaluation-metrics #worker-facing #workflow-orchestration

**Problem statement:** Draft client-ready candidate reports and weekly progress updates from interview notes, call transcripts and CRM activity, with every claim traceable to its source and confidential remarks kept out.

**ML task:** Grounded summarisation into a firm's report templates, with claim-to-source attribution and a classifier for confidential or non-shareable content
**Input data:** Interview transcripts and notes, references, CVs, the brief and competency framework, CRM status history, prior reports as style examples.
**Target:** Report sections with source links; a progress summary per mandate; flagged passages needing consultant review.
**Evaluation metric:** Unsupported-claim rate (any sentence not grounded in a source) and leakage rate of confidential remarks, both with near-zero tolerance; consultant edit distance and time-to-send as adoption measures.
**Scope:** Write-ups are already the most common generative AI use in search (73% in a Cluen survey reported in early 2026), so the gap is grounding and confidentiality rather than fluency. 2 engineers, 3 months, building on prior reports as supervision.
**Data availability:** Prior reports and notes are the firm's own; transcripts exist only where interviews are recorded with consent, which many senior candidates refuse.
