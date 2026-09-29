# Machine Learning Opportunities — Digital BPO Operations

**Industry:** [[digital-bpo-operations|Digital BPO Operations]]
**Derived from:** [[problems/digital-bpo-operations/high-impact|High Impact]], [[problems/digital-bpo-operations/low-impact-1|Low Impact 1]], [[problems/digital-bpo-operations/low-impact-2|Low Impact 2]], [[problems/digital-bpo-operations/worker-life-1|Worker Life 1]], [[problems/digital-bpo-operations/worker-life-2|Worker Life 2]]

---

## 1. Full-Coverage Resolution Assessment and Repeat Contact Measurement
#transformers #bert #large-language-models #gradient-boosting #confidence-intervals #causal-inference #evaluation-metrics #hypothesis-testing

**Problem statement:** Quality is estimated from a low single-digit sample and a survey almost nobody answers, while handle time is measured to the second — and the two metrics conflict on exactly the contacts where resolution matters most.

**ML task:** Assess resolution across every contact from transcripts and subsequent behaviour, and compute case-mix-adjusted repeat contact rate as the primary quality metric
**Input data:** Full contact transcripts and dispositions; subsequent contacts by the same customer within defined windows and whether they concern the same issue; downstream account activity indicating whether the problem persisted; issue type, complexity and channel; agent identity and tenure; existing human quality scores for calibration.
**Target:** Whether the customer's stated issue was resolved, validated against human quality review and against observed repeat contact.
**Evaluation metric:** Agreement with human reviewers on a calibration set, and — the more important check — whether the automated assessment predicts repeat contact better than the human sampled score does, which is the practical claim. Case-mix adjustment is essential and its absence would be actively harmful: an agent receiving harder contacts will show worse raw resolution, and an unadjusted ranking would penalise exactly the agents handling the difficult work.
**Scope:** Repeat contact rate needs no model at all and is the single most informative number available, computable today from data every operation holds. The governance question is unavoidable: this replaces a two percent sample with total assessment of a workforce already monitored to the second, and whether that improves or worsens working life depends entirely on whether the output is used for coaching or for discipline. 2 engineers plus a quality lead, 6-9 months.
**Data availability:** Complete. Transcripts, dispositions and subsequent contacts all sit in the contact centre platform.

---

## 2. Demand and Deflection Forecasting With Decision-Aware Staffing
#time-series-forecasting #exponential-smoothing #convex-optimization #confidence-intervals #gradient-boosting #evaluation-metrics #optimization-fundamentals #worker-facing

**Problem statement:** Forecasts model human contact volume, which conflates underlying customer demand with a deflection rate that is itself changing, so accuracy has degraded and the error is paid in breached service levels or unpaid sent-home hours.

**ML task:** Forecast total demand and deflection rate separately by issue type and interval, then solve staffing against the resulting distribution with the cost asymmetry made explicit
**Input data:** Contact volume by interval, channel and issue type; automation deflection rates and their changes; underlying demand drivers — product releases, billing cycles, outages, marketing, seasonality; staffing, service level and abandonment outcomes; the contract's service level penalties and the cost of idle time.
**Target:** Human contact volume by interval, decomposed into demand and deflection components.
**Evaluation metric:** Forecast accuracy at the horizons that matter — schedule publication, typically two to four weeks, and intra-day — rather than day-ahead. Decomposition value is demonstrated by whether the separated model degrades less when deflection performance shifts, which is the specific failure of the current approach. Report staffing outcomes as service level and paid-idle hours together, since improving one at the other's expense is not an improvement and sent-home hours are currently invisible in operational reporting.
**Scope:** Schedule stability should enter the optimisation as an objective rather than being left as a residual — variable schedules are the operational practice that most damages this workforce, and the trade-off against coverage has never been explicitly priced at most operations. 1-2 data scientists, 4-6 months.
**Data availability:** Complete within contact centre and workforce management platforms.

---

## 3. Knowledge Staleness Detection and Calibrated Assist
#bert #large-language-models #transformers #change-point-detection #k-nearest-neighbors #confidence-intervals #evaluation-metrics #data-integration

**Problem statement:** Agents answer from a knowledge base they have learned not to trust, and generative assist tooling now delivers whatever is in it with uniform confidence — which is worse than no suggestion when the article is stale.

**ML task:** Detect stale and contradictory articles from downstream contact outcomes, measure divergence between documented process and what experienced agents actually say, and calibrate assist confidence with genuine abstention
**Input data:** Knowledge article content, versions and dates; article retrieval and usage during contacts; contact outcomes following a suggestion — escalation, correction, repeat contact; transcripts of how experienced agents answer the same questions; team chat as a source of current informal answers; agent feedback on suggestions.
**Target:** Whether an article is currently correct, adjudicated by the content owner on a reviewed sample.
**Evaluation metric:** Precision on staleness flags governs adoption, since the remediation is manual and a noisy flag list is ignored. For assist, the critical measure is calibration and abstention rate: an agent under handle-time pressure will use what they are given, so the burden of declining sits entirely with the tool, and a confidently wrong suggestion should be counted as a distinct and heavily weighted error rather than folded into an accuracy figure.
**Scope:** The divergence between what articles say and what experienced agents actually tell customers is the most direct available evidence that documented and real process have separated, and it is derivable from transcripts the operation already records. The feedback loop from agent report to article owner is nearly free and is the mechanism the knowledge function has always lacked. 2 engineers, 4-6 months.
**Data availability:** Excellent — transcripts, article usage and outcomes are all captured.

---

## 4. Case-Mix Adjusted Target Setting and Emotional Load Routing
#gradient-boosting #transformers #confidence-intervals #hypothesis-testing #convex-optimization #evaluation-metrics #worker-facing #time-series-forecasting

**Problem statement:** Handle time targets were calibrated on a contact mix that deflection has removed the easy half of, and the remaining work is harder and more emotionally difficult while the target has not moved — a squeeze agents absorb without acknowledgement.

**ML task:** Derive expected handle time per issue type and complexity from the current contact distribution, and route with an account of recent emotional load per agent
**Input data:** Contact transcripts with issue type, complexity indicators and resolution requirements; realised handle times by type before and after deflection changes; escalation and abuse markers in transcripts; agent contact history within a shift; existing targets and their provenance.
**Target:** Expected handle time for a contact of this type and complexity, and a measure of contact difficulty for routing purposes.
**Evaluation metric:** For targets, the proportion of agents meeting a case-mix-adjusted expectation compared with the global average target, which should reveal how much of apparent underperformance is mix rather than performance. For emotional load routing, the outcome measures are agent-reported strain and attrition rather than efficiency — a routing change that reduces exposure and costs a little handle time has succeeded, and an efficiency-only evaluation would reject it.
**Scope:** Difficulty and abuse detection in transcripts must be evaluated for differential performance across customer accents, dialects and languages, since misclassification would systematically misroute work from particular customer populations. This is deliberately a workforce-protective use of the same analysis that could be used punitively, and framing it that way is the point. 1-2 engineers, 4-6 months.
**Data availability:** Complete. Transcripts and handle time histories including the pre-deflection period are all retained.
