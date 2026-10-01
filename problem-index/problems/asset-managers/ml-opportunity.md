# Machine Learning Opportunities — Asset Managers

**Industry:** [[asset-managers|Asset Managers]]
**Derived from:** [[problems/asset-managers/high-impact|High Impact]], [[problems/asset-managers/low-impact-1|Low Impact 1]], [[problems/asset-managers/low-impact-2|Low Impact 2]], [[problems/asset-managers/worker-life-1|Worker Life 1]], [[problems/asset-managers/worker-life-2|Worker Life 2]]

---

## 1. Capturing the Analyst's Read of Management
#tacit-knowledge-ml #large-language-models #transformers #gradient-boosting #change-point-detection #evaluation-metrics #worker-facing

**Problem statement:** An experienced buy-side analyst notices when management language on an earnings call or in a meeting departs from what she expected — guidance hedged differently, a metric quietly dropped, a capital allocation priority reordered — and acts on it before it shows in the numbers. The aim is to capture that read as structured, timestamped judgments and train a model that flags the same departures for every company in coverage.

**ML task:** Pairwise change detection between successive management communications conditioned on the analyst's recorded expectation, plus a learned ranking of which detected shifts experienced analysts treat as material
**Input data:** Earnings call transcripts, investor day materials and filings for covered companies (licensed from the firm's data vendors); the analyst's own meeting notes in the research management system; short structured post-meeting ratings (credibility, direction of change, what would change the view) captured at the time; the recommendation ledger and subsequent returns.
**Target:** For each new communication, a ranked list of language shifts versus the prior period and versus the analyst's recorded expectation, each scored for materiality; secondarily, the analyst's own post-meeting rating as a supervised label.
**Evaluation metric:** Precision at the top five flagged shifts per call, judged blind by senior analysts — the deployment constraint is that a list with two irrelevant items at the top will not be read again. Secondary: whether flagged shifts precede estimate revisions or abnormal returns more often than unflagged ones, measured as an event study with confidence intervals, not as a trading backtest.
**Scope:** This is the hardest entry and the most valuable. **Data collection** is the bottleneck: the judgment is formed in meetings that compliance often forbids recording, so the only scalable capture is a ninety-second structured prompt after each meeting, which must be designed with the analysts and enforced lightly or it will be skipped. **Labelling** is noisy: analysts re-rating old meetings with outcomes hidden often disagree with their original scores, and the outcomes themselves are delayed and confounded by the market, so inter-rater and intra-rater agreement must be measured before any model is trusted. **Deployment** must beat the alternative of asking the analyst: the flag list has to be ready before the PM's morning meeting, scoped to the reader's information-barrier permissions, and never present a judgment as the model's own. 1 ML engineer, 1 NLP specialist, 1 data engineer and two senior analysts at 20% for 9–12 months before results are trustworthy.
**Data availability:** Transcripts and filings are licensed and complete. The analyst notes exist but are inconsistent in length and discipline. The structured judgment labels do not exist anywhere and must be collected going forward; a backfill from historical notes using language models is possible but should be treated as weak labels.

---

## 2. Recommendation Ledger and Research Hit-Rate Estimation
#causal-inference #gradient-boosting #logistic-regression #confidence-intervals #hypothesis-testing #evaluation-metrics #data-integration #revenue-impact

**Problem statement:** Analysts issue recommendations and target prices; PMs act, partly act or ignore them; returns follow. The firm never joins the three, so it cannot say which analysts, sectors or recommendation types carry information, or what the PM's overrides cost or saved.

**ML task:** Construction of a decision–outcome dataset, then estimation of per-analyst and per-recommendation-type predictive value with explicit adjustment for confounders, plus a calibrated model of which recommendations PMs act on
**Input data:** Recommendation and rating history with timestamps from the research management system or email; portfolio holdings and trades from the order management system; security returns and factor exposures from the risk system; sector and market regime labels.
**Target:** Factor-adjusted forward return on each recommendation over defined horizons; the probability a recommendation is acted on; the counterfactual return of acted versus non-acted recommendations.
**Evaluation metric:** Information coefficient of recommendations against factor-adjusted forward returns, reported with confidence intervals per analyst — most analysts will have too few independent calls for a significant individual estimate, and stating that honestly is part of the product. For the action model, calibration rather than accuracy.
**Scope:** The ledger is data engineering, not research: 2 data engineers for 3–4 months, mostly spent reconstructing timestamps from systems that record state rather than events. The estimation is a quant's job for a further 2–3 months. Factor adjustment is essential; without it the analysis rewards whoever covered the sector that rallied.
**Data availability:** Fully internal. Trades and returns are clean. Recommendations are the weak link — they exist in the research system for disciplined firms and in emails and models elsewhere, and backfilling them is the main cost.

---

## 3. Strategy-Aware RFP and DDQ Answer Retrieval
#large-language-models #word-embeddings #k-nearest-neighbors #bert #evaluation-metrics #compliance #automation

**Problem statement:** RFP and due diligence questions repeat with varied wording across consultants; the right answer depends on strategy, vehicle, date and what was told to the same consultant before, and the numbers must tie to the book of record.

**ML task:** Semantic retrieval of approved answers conditioned on strategy and vehicle metadata, with numeric slot-filling from the performance system and cross-response consistency checking
**Input data:** Historical RFPs and DDQs with submitted answers; the approved content library; consultant database submissions by quarter; performance, AUM and characteristics data by strategy and composite; compliance edits on past drafts.
**Target:** For each incoming question, the best approved answer adapted to the strategy and date, with numeric fields filled from source and a flag where the answer conflicts with a prior submission to any consultant.
**Evaluation metric:** Share of questions answered with no substantive edit by the RFP writer, and — weighted more heavily — the rate of factual inconsistencies caught versus missed in a seeded test set, since a wrong number in a submitted RFP costs more than a slow one.
**Scope:** A retrieval-augmented system on a well-defined corpus; 2 engineers for 4–5 months. The metadata model (strategy, vehicle, share class, composite, date) is the real work.
**Data availability:** Good. Managers retain every submitted RFP. Compliance edits are often tracked in documents and can be mined as preference data.

---

## 4. Attribution-Grounded Commentary Drafting
#large-language-models #transformers #evaluation-metrics #descriptive-statistics #worker-facing #compliance #automation

**Problem statement:** Quarterly commentary must explain performance using attribution, trades and the team's rationale, then be cut into many formats; drafts are slow to produce and errors are client-facing.

**ML task:** Data-to-text generation grounded in attribution tables and trade records, with claim-level source linking and a factual consistency checker
**Input data:** Brinson or factor attribution by strategy; top contributors and detractors; trades with sizes; analyst rationales from the research system; prior quarters' approved commentary as style reference; compliance-approved phrasing.
**Target:** A draft commentary in which every quantitative claim links to a source figure, plus derived short-form versions for fact sheets and database narratives.
**Evaluation metric:** Unsupported-claim rate measured by automated checking against source tables and confirmed by the specialist; secondary, PM edit distance on the narrative. Any unsupported performance claim is a hard failure because of marketing-rule exposure.
**Scope:** 2 engineers, 3–4 months to a useful draft for equity strategies; fixed income attribution is less standardised and adds time.
**Data availability:** Excellent; attribution and approved past commentary are archived by every manager.

---

## 5. Proxy Ballot Triage and Vote Consistency
#large-language-models #bert #k-nearest-neighbors #gradient-boosting #evaluation-metrics #compliance #workflow-orchestration

**Problem statement:** Thousands of ballot items must be voted in a compressed season according to the firm's own policy, with divergences from proxy adviser recommendations justified and votes consistent across similar items.

**ML task:** Multiclass classification of ballot items into policy outcomes, nearest-neighbour retrieval of similar past votes with rationales, and anomaly flagging where a proposed vote departs from precedent
**Input data:** Proxy statements and ballot items; proxy adviser research and recommendations; the firm's voting policy; historical votes with rationales; engagement records; Form N-PX categories.
**Target:** Proposed vote per item with a confidence score; routing to human review when confidence is low, when the item is contested, or when it departs from the firm's precedent.
**Evaluation metric:** Recall on items that a senior analyst would route to human review — a missed contested item is the costly error — at an acceptable review volume.
**Scope:** 1–2 engineers, 4 months. The voting policy must be formalised enough to be tested, which is itself valuable to the stewardship team.
**Data availability:** Good. Vote histories and rationales are retained for N-PX and client reporting; proxy adviser research is licensed but its reuse terms must be checked.
