# Machine Learning Opportunities — Email & SMS Marketing Platforms

**Industry:** [[email-sms-marketing-platforms|Email & SMS Marketing Platforms]]
**Derived from:** [[problems/email-sms-marketing-platforms/high-impact|High Impact]], [[problems/email-sms-marketing-platforms/low-impact-1|Low Impact 1]], [[problems/email-sms-marketing-platforms/low-impact-2|Low Impact 2]], [[problems/email-sms-marketing-platforms/worker-life-1|Worker Life 1]], [[problems/email-sms-marketing-platforms/worker-life-2|Worker Life 2]]

---

## 1. Inbox Placement Inference from Engagement Differentials
#bayesian-inference #gradient-boosting #confidence-intervals #change-point-detection #hypothesis-testing #probability-distributions #evaluation-metrics #feature-engineering

**Problem statement:** Mailbox providers do not disclose placement and never will, because publishing it would let bulk senders optimise against the filter. The industry's proxy, the open rate, was rendered unreliable by pre-fetching privacy features and is still used for segmentation, sunsetting and reporting everywhere.

**ML task:** Estimate inbox placement rate per sender, provider and recipient cohort from click-conditional-on-delivery differentials, calibrated against every partial ground truth available
**Input data:** Delivery and click events segmented by mailbox provider and recipient engagement cohort; seed-list placement results; Postmaster reputation and complaint data; sender authentication status; volume, content and template features; the platform's cross-brand corpus including senders whose placement demonstrably collapsed.
**Target:** Placement rate, treated as a latent variable inferred from observable engagement differences rather than as a label.
**Evaluation metric:** Calibration against seed-list placement on the subset where it exists, and — more convincing — agreement with the known collapses in the corpus, where placement unambiguously fell and the model should detect it without being told. Report intervals, and resist collapsing the estimate into a score out of 100; a sender making a volume decision needs to know whether the estimate is precise, and for small senders it will not be.
**Scope:** This is only tractable at platform scale, because calibration requires many senders including failures — no individual brand has the data. The cohort segmentation matters enormously: placement differs sharply between highly-engaged and dormant recipients at the same provider, and an aggregate number hides exactly the degradation that matters. 3 ML engineers plus a deliverability specialist, 9-12 months.
**Data availability:** Engagement and delivery data is complete. Ground truth is sparse, partial and biased, which is why calibration design is the hard part rather than the modelling.

---

## 2. Causal Diagnosis of Placement Degradation
#causal-inference #change-point-detection #gradient-boosting #hypothesis-testing #confidence-intervals #time-series-forecasting #evaluation-metrics #tacit-knowledge-ml

**Problem statement:** When a sender's placement degrades, the candidate causes — volume ramp, a new acquisition source, a template change, authentication, a shared IP neighbour, a blocklist entry, an ageing list — are confounded, and the specialist diagnoses by hypothesis and waits weeks for feedback.

**ML task:** Change-point detection on provider-segmented engagement plus cause attribution learned from a cross-brand corpus of incidents with confirmed causes and remedies
**Input data:** Provider-segmented engagement time series; sender behaviour events — volume changes, list source additions, template and content changes, authentication configuration, IP and domain changes; historical incidents with the cause identified and the remedy that worked; cross-brand contemporaneous data to distinguish provider-wide filter changes from sender-specific faults.
**Target:** The cause as confirmed by the specialist who resolved the incident, and the time the degradation began.
**Evaluation metric:** Detection lead time against when the incident was actually noticed is the headline — the value is entirely in the weeks between degradation starting and revenue making it obvious. For attribution, top-3 cause accuracy rather than top-1, since a specialist can evaluate three hypotheses quickly and a confidently wrong diagnosis wastes a fortnight of remediation on the wrong lever.
**Scope:** The cross-brand view is what distinguishes a provider-wide filter change from a sender's own fault, which is the first question in every incident and the one no single sender can answer. Incident labels come from deliverability teams' own case histories, which exist as tickets and notes rather than structured data — extracting them is the first project. 2 ML engineers plus a deliverability specialist, 6-9 months.
**Data availability:** Behaviour and engagement data is complete inside the platform. Labelled incidents require mining support and consulting records, which is tedious and entirely feasible.

---

## 3. Contact Frequency as a Lifetime Value Optimisation
#survival-analysis #causal-inference #markov-decision-processes #gradient-boosting #confidence-intervals #hidden-markov-models #evaluation-metrics #revenue-impact

**Problem statement:** Each message generates immediate measurable revenue and contributes to attrition that accumulates over months and is attributed to nothing. Every incentive — campaign reporting, quarterly targets, volume-based pricing — points toward sending more, and the cost shows up later as a dead list.

**ML task:** Per-recipient contact policy optimising expected lifetime value, with attrition modelled as a hazard rising with recent contact pressure and recovering with time
**Input data:** Full contact history across channels including push and paid retargeting where visible; engagement, purchase and attrition events with timing; unsubscribe and complaint events; product purchase cycle; recipient tenure and acquisition source; randomised frequency variation where it can be introduced.
**Target:** Expected revenue over a 12-month horizon net of the attrition hazard, per recipient, as a function of contact schedule.
**Evaluation metric:** This must be validated with a genuine randomised frequency holdout over a long horizon, because the observational version is severely confounded — brands send more to engaged people, so naive analysis concludes that more messages cause engagement. Report the immediate revenue cost of the policy alongside the lifetime gain, honestly, because the policy will reduce this quarter's number and anyone adopting it needs to see the trade rather than discover it.
**Scope:** The depleting-resource framing — attention consumed by contact, restored by time — is the right structure and makes the problem a policy over states rather than a global cap. Cross-channel pressure must be included or the model optimises email while SMS and push exhaust the same person. 3 ML engineers plus a causal specialist, 12 months including the holdout period.
**Data availability:** Contact and outcome histories are complete and long. Cross-channel visibility is partial. Randomised frequency variation must be deliberately introduced and is the gating requirement.

---

## 4. Flow Health Monitoring and Branch-Level Effect Estimation
#time-series-forecasting #change-point-detection #causal-inference #hidden-markov-models #gradient-boosting #confidence-intervals #evaluation-metrics #automation

**Problem statement:** Mature programmes run fifty interacting automated journeys that nobody fully understands; flows stop firing silently when an upstream event is renamed, and flow revenue is reported per flow when the meaningful unit is the branch.

**ML task:** Forecast each flow and branch's expected firing volume to detect silent failures, and estimate per-branch incremental effect using holdouts and observed journey sequences
**Input data:** Flow definitions and their trigger events; per-branch traversal volumes over time; message-level engagement and order outcomes; upstream event schema and its change history; per-branch holdout assignment where implemented; customer journey sequences across flows.
**Target:** For monitoring, whether observed traversal volume is consistent with its own forecast. For effect, incremental orders attributable to each branch rather than orders following a click within a window.
**Evaluation metric:** For monitoring, detection lead time on historical silent failures and a false-alarm rate low enough that alerts get read — seasonality and promotions produce legitimate step changes and must not fire. For branch effects, the comparison that matters is attributed revenue versus incremental revenue per branch; the gap will be large for abandonment flows, which recover carts that would substantially have recovered themselves, and reporting that gap is the point.
**Scope:** Monitoring is straightforward, immediately valuable and should ship first. Branch-level holdouts are supported by most platforms and almost never used; the modelling is easy and the adoption is hard, because the finding reduces a number everyone likes. Journey-sequence modelling to induce a better contact policy is the ambitious extension and should output an editable flow rather than a black box, since marketers need to see what is sent. 2 ML engineers, 4-6 months for monitoring and branch effects.
**Data availability:** Complete within the platform. Holdout data must be generated by turning on a feature that already exists.
