# Machine Learning Opportunities — Credit Card Issuers

**Industry:** [[credit-card-issuers|Credit Card Issuers]]
**Derived from:** [[problems/credit-card-issuers/high-impact|High Impact]], [[problems/credit-card-issuers/low-impact-1|Low Impact 1]], [[problems/credit-card-issuers/low-impact-2|Low Impact 2]], [[problems/credit-card-issuers/worker-life-1|Worker Life 1]], [[problems/credit-card-issuers/worker-life-2|Worker Life 2]]

---

## 1. Learning the Investigator's Read of a Bust-Out
#tacit-knowledge-ml #lstms-and-grus #transformers #gradient-boosting #evaluation-metrics #feature-engineering #revenue-impact

**Problem statement:** Experienced fraud investigators look at an account's recent history and "know" a bust-out is forming — a pattern of payment sources, line changes, merchant mix and contact behaviour they cannot write down, and which today reaches the label set only as a thin case note on accounts already referred by rules. The ML problem is to learn that read from structured investigator reviews and from outcomes, and score every account on its event stream before the line is drawn.

**ML task:** Sequence classification over account event histories (payments, returns, line changes, authorisations, contacts, bureau inquiries) producing a calibrated probability of first-party fraud within 60 days, plus multi-class cause attribution for charged-off accounts (credit loss, first-party fraud, synthetic identity, third-party fraud, ambiguous)
**Input data:** Authorisation and posting streams with merchant category and channel; payment records with source account, return codes and timing relative to line changes; line management history; contact-centre events and call reasons; address, phone and device changes; bureau inquiry and new-trade triggers; investigator case outcomes and the evidence fields they recorded.
**Target:** Investigator-assigned cause on reviewed accounts; for unreviewed charge-offs, a re-review sample labelled under a fixed protocol; the time from first risk signal to bust.
**Evaluation metric:** Dollars of loss prevented at a fixed daily review capacity, measured out of time, is the operating metric; precision in the top alert band matters because each hold or line freeze is an adverse action on a possibly innocent cardholder. Report agreement with held-out investigator labels against the investigators' own test-retest agreement as the ceiling, and lead time before the first post-warm-up draw.
**Scope:** The data collection challenge comes first: the investigator's read must be captured on accounts they clear as well as those they flag, so the build starts with a review surface that records which signals were examined, and with a protocol to re-review a stratified sample of historical charge-offs. The labelling challenge is that the cause of many no-contact charge-offs is unknowable and investigators drift with recent cases, so labels need repeat review on a subsample and an explicit "ambiguous" class rather than forced choices. The deployment challenge is latency: the score has to run on each payment and authorisation, faster than the investigator queue, and every action needs a Reg B reason. A team of 2 ML engineers, 1 data engineer and 2 seconded investigators, 9–12 months; value appears first as a ranked investigator queue before any automated hold is trusted.
**Data availability:** The event data sits inside the issuer and is clean. The labels are the project: investigator notes exist, but structured, cleared-case labels and a re-reviewed historical sample have to be created. Consortium signals (bureau triggers, synthetic-identity scores) are licensable.

---

## 2. Measuring What a Line Increase Actually Earns
#causal-inference #gradient-boosting #survival-analysis #hypothesis-testing #confidence-intervals #evaluation-metrics #revenue-impact

**Problem statement:** Line increases and decreases are evaluated on challenger cells, but most strategies are judged on raw performance of accounts that were selected for the treatment. Estimate, for each account, the incremental revolving balance, interchange and loss that a given line change causes over 12–24 months, using the issuer's history of randomised test cells.

**ML task:** Heterogeneous treatment-effect estimation (uplift modelling) with time-to-default survival modelling for the loss component
**Input data:** Historical line-change decisions with test-cell assignment; account behaviour before and after; bureau attributes at decision time; macro conditions; later delinquency and charge-off.
**Target:** Incremental net revenue (interest + interchange − loss − funding cost) per account per line action, with intervals.
**Evaluation metric:** Out-of-time Qini or uplift curves on held-out randomised cells, and the realised profit of model-targeted versus rule-targeted increases in a fresh test. Uncertainty matters as much as point estimates: the loss tail arrives 12–18 months after the action, so the model must say how sure it is.
**Scope:** The randomised history is the asset; issuers that have run disciplined test cells for years can do this well, those that have not must start testing first. 2 data scientists and 1 credit strategist, 6 months to a first model, with a live validation test running another 12 months.
**Data availability:** Fully internal; quality depends on whether test-cell assignment was recorded and preserved.

---

## 3. Dispute Narrative Classification and Chargeback Outcome Prediction
#transformers #bert #large-language-models #logistic-regression #evaluation-metrics #compliance #automation

**Problem statement:** Map each cardholder's dispute narrative and transaction record to the correct network reason code and evidence request at intake, and estimate the probability that a chargeback on that code will survive merchant representment.

**ML task:** Multi-class text classification over network reason codes, with a calibrated win-probability model for the chargeback decision
**Input data:** Call transcripts, app and web dispute forms, chat logs; transaction details (card-present, recurring, merchant category, authorisation data, 3-D Secure results); historical dispute cases with reason code, evidence, representment outcome and write-off.
**Target:** Reason code and condition; evidence checklist; probability of chargeback success; flag for likely first-party misuse.
**Evaluation metric:** Macro-F1 on reason codes against expert-coded cases, weighted toward the confusions that cost money (fraud versus consumer dispute). For the win model, calibration and dollars recovered at the operating threshold. Wrongly denying a genuine claim is a regulatory harm, so first-party flags route to a human check and never auto-deny.
**Scope:** Historical cases provide supervised labels, but the reason-code taxonomy changes with network rule releases, so the model needs a maintained mapping layer. 2 engineers and a dispute SME, 4–5 months.
**Data availability:** Internal case data is plentiful; narratives in call recordings need transcription. Outcome labels are reliable because the network records the result.

---

## 4. Cardholder-Level Redemption and Breakage Forecasting
#survival-analysis #bayesian-inference #time-series-forecasting #gradient-boosting #evaluation-metrics #revenue-impact

**Problem statement:** Forecast, for each outstanding point balance, the probability and timing of redemption by channel (statement credit, portal travel, transfer partner, merchandise) and the resulting cost per point, so the rewards liability and its quarterly true-up can be estimated by cohort.

**ML task:** Competing-risks survival modelling of redemption events by channel, with hierarchical Bayesian pooling across products and partners for thin cohorts
**Input data:** Earn and burn ledgers, account attributes and tenure, revolving status, attrition events, transfer-partner cost tables, promotion and devaluation calendars.
**Target:** Expected cost of outstanding points by cohort and quarter; breakage by product.
**Evaluation metric:** Error in the forecast liability against realised redemption cost over the following four quarters, reported by cohort; bias matters more than variance because systematic under-forecasting surfaces as an earnings miss.
**Scope:** Modest technically; the work is joining the ledger to account and partner data at cardholder level. 1–2 data scientists with rewards finance, 4 months.
**Data availability:** Internal; partner cost tables sit with partnership finance and change on renewal.

---

## 5. Hardship Treatment That Cures Rather Than Delays
#gradient-boosting #causal-inference #survival-analysis #evaluation-metrics #worker-facing #workflow-orchestration

**Problem statement:** For a delinquent cardholder eligible for several hardship programmes, estimate the probability that each programme returns the account to current and keeps it there for 12 months, so agents can choose the treatment most likely to cure rather than the one that defers the charge-off.

**ML task:** Treatment-effect estimation across multiple arms with survival outcomes (time to re-default)
**Input data:** Past programme offers and acceptances, account and payment history at offer, stated hardship reason from call notes, bureau data, later payment performance.
**Target:** Cure probability and expected recovered balance per programme.
**Evaluation metric:** Cure rate and dollars recovered for model-recommended versus agent-chosen programmes in a randomised pilot; programme assignment in the history was not random, so offline estimates must correct for selection and are validated only by the pilot.
**Scope:** 2 data scientists and a collections strategist, 5 months to a pilot; the pilot itself runs 6–9 months to observe re-default.
**Data availability:** Internal; the hardship reason is mostly in free-text notes and call recordings and needs extraction.
