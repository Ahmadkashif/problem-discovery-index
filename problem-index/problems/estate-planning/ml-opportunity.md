# Machine Learning Opportunities — Estate Planning Law Firms

**Industry:** [[estate-planning|Estate Planning Law Firms]]
**Derived from:** [[problems/estate-planning/high-impact|High Impact]], [[problems/estate-planning/low-impact-1|Low Impact 1]], [[problems/estate-planning/low-impact-2|Low Impact 2]], [[problems/estate-planning/worker-life-1|Worker Life 1]], [[problems/estate-planning/worker-life-2|Worker Life 2]]

---

## 1. Estate Plan Staleness Risk Scoring from Life Event Detection
#gradient-boosting #binary-classification #tabular-ml #tacit-knowledge-ml

**Problem statement:** Experienced estate planning attorneys have internalized which client life events (marriage, divorce, death of a named party, business acquisition, tax law change, state domicile move) trigger a plan update and how urgently. This judgment can be formalized as a staleness risk model that scores each client's plan for update urgency based on detectable events — combining internal client record changes with publicly available external data.

**ML task:** Binary classification (plan update recommended: yes/no) + urgency score (routine / priority / urgent) per client, triggered by event detection from internal and external sources
**Input data:** Client profile data (plan execution date, plan type, named parties, asset categories, state of domicile), event triggers (obituary monitoring for named parties, marriage/divorce public records in client's state, IRS tax law change announcements with applicable exemption amount changes, client-reported address change), time since last plan review
**Target:** Update recommendation flag per client, with reason code (beneficiary deceased / tax law change / address change suggesting domicile shift / plan age > configurable threshold) and recommended engagement type
**Evaluation metric:** Recall on genuinely stale plans (attorney agreement that the flagged clients actually need updates); precision (fraction of flags that result in actual update engagements); revenue from update engagements triggered by the system vs. baseline
**Scope:** The event detection infrastructure (obituary monitoring, public records monitoring) is available via services like Whitepages API, public records databases, and state vital records. Linking public record events to client names requires probabilistic matching. The scoring model trains on attorney judgments of past re-engagement cases. 8-12 week project.
**Data availability:** Client data is in the case management system. External public records monitoring requires API integration (DataZapp, Melissa Data, state vital records). The primary challenge is probabilistic matching of public records to client names — manageable with fuzzy matching and manual review of ambiguous cases.

---

## 2. Tax Law Change Impact Analysis for Active Client Plans
#bert #text-classification #nlp #compliance

**Problem statement:** When estate and gift tax law changes (TCJA sunset provisions, annual exclusion adjustments, state estate tax threshold changes), automatically identify which clients in the firm's active database have plans that reference the changed provisions and classify the severity of the impact — enabling targeted client outreach and update recommendations.

**ML task:** Text classification of estate planning document provisions by legal concept + impact assessment when a legal change is detected
**Input data:** Estate plan document text (trust instruments, wills, tax apportionment clauses), tax law change announcements (IRS Publications, state revenue department notices), prior mapping of document provisions to relevant legal thresholds (applicable exclusion amount, annual exclusion amounts, state estate tax thresholds)
**Target:** Per-client impact classification (no impact / minor review recommended / significant impact requiring update) when a specific tax law change is input; explanation of the specific provision affected in each client's plan
**Evaluation metric:** Attorney agreement rate on impact classifications; false negative rate on significant-impact flags (missing a genuinely impactful change is the critical error); coverage of tax change types handled
**Scope:** The document provision classification step requires fine-tuning a legal BERT model on estate planning document text. The tax law change monitoring component is rule-based (mapping change type to affected provision types) on top of the classification. 10-14 week project including document corpus annotation.
**Data availability:** Estate planning document libraries (Wealth Counsel, WealthDocx) provide standardized provision text for initial training. The firm's executed plan archive provides practice-specific document variation. Tax law change monitoring requires ongoing maintenance as law evolves.

---

## 3. Estate Administration Duration and Complication Prediction
#gradient-boosting #regression #tabular-ml

**Problem statement:** Predict the expected duration and complexity of a new estate administration at intake, based on estate size, asset types, jurisdiction, number of beneficiaries, and presence of complicating factors — enabling accurate scope estimates for fee quotes and resource planning.

**ML task:** Regression (expected months to close administration) + multiclass classification (complication tier: routine / moderate / complex / contested)
**Input data:** Estate size (total asset value), asset types (real property: how many states? business interests? retirement accounts? life insurance?), number and relationship of beneficiaries, presence of a will vs. intestacy, whether a trust was funded, jurisdiction (state probate law complexity), family relationship complexity (blended family, disinherited parties, minor beneficiaries), prior billing data from similar administrations
**Target:** Expected duration in months with prediction interval; complication tier classification
**Evaluation metric:** MAE of duration prediction; accuracy of complication tier classification; comparison of fee estimate accuracy with and without the model
**Scope:** A firm with 100+ completed administrations with consistent intake data logging can build a useful model in 4-6 weeks. Complication classification is the more valuable output — the model doesn't need to predict duration precisely, just identify the estates that will require significantly more attorney involvement than a routine administration.
**Data availability:** Estate administration billing data provides duration (file open date to close date) and total fee (a proxy for complexity). Asset type and beneficiary data is captured at intake. A firm with 3+ years of administration history has sufficient volume for a first model.

---

## 4. Charitable Planning Opportunity Identification
#gradient-boosting #binary-classification #tabular-ml #revenue-impact

**Problem statement:** Identify which clients in the firm's existing base are candidates for charitable planning strategies (Charitable Remainder Trusts, Donor Advised Funds, Qualified Charitable Distributions) based on their financial profile, estate size, and tax situation — enabling targeted recommendations that create client value and additional fee engagements.

**ML task:** Binary classification (charitable planning opportunity present: yes/no) per client, with ranked strategy recommendation
**Input data:** Client age, estimated estate value, income sources (retirement distributions, business income, appreciated assets), existing charitable intentions documented in estate plan, IRA/retirement account balances, state income tax rate (affects QCD vs. DAF attractiveness), prior charitable giving history if documented
**Target:** Opportunity flag per client with recommended strategy type and estimated tax benefit to quantify the recommendation
**Evaluation metric:** Conversion rate of flagged clients to charitable planning engagements; attorney agreement with opportunity classifications; average additional fee per identified engagement
**Scope:** Charitable planning recommendations are primarily rule-based with a scoring layer — the conditions for each strategy (CRT: client has appreciated assets + charitable intent + income need; QCD: client is 70.5+ with IRA + charitable intent) are well-defined. A simple scoring model on structured client data is a 3-4 week project. The challenge is data completeness — many clients' financial profiles are partially unknown to the attorney.
**Data availability:** Client intake data and plan documents capture some financial information, but estate planning attorneys often don't have full financial account visibility. A client financial data sharing form or annual questionnaire improves data quality significantly over time.

---

## 5. Beneficiary Conflict and Dispute Risk Prediction
#gradient-boosting #binary-classification #tabular-ml

**Problem statement:** Predict which estates, based on family structure and plan characteristics visible at administration intake, are at elevated risk of beneficiary disputes — enabling proactive attorney intervention (beneficiary meetings, clearer communication protocols) before conflict escalates to litigation.

**ML task:** Binary classification (dispute risk: elevated / routine) from estate intake characteristics
**Input data:** Family relationship complexity (blended family, prior marriages, unequal distributions, disinherited parties), estate size (larger estates generate more conflict), type of assets (family business, personal property with sentimental value, real estate are higher-risk asset types), decedent communication patterns (was there a family meeting before death?), executor/trustee being a family member vs. corporate trustee, prior family conflict indicators documented in file
**Target:** Dispute risk flag with primary contributing factors; recommended proactive actions (request family meeting, appoint independent co-trustee, document distribution decisions with supporting rationale)
**Evaluation metric:** Recall on estates that resulted in actual disputes; precision (fraction of elevated-risk flags that result in genuine conflict); attorney agreement with risk classifications in case review
**Scope:** A firm with 3+ years of administration history, including disputed administrations, has sufficient signal. The feature set is largely categorical. A gradient boosting classifier on 100-200 completed administrations (including both routine and disputed) is achievable in 4-6 weeks. Key challenge: disputed administrations are rare events (maybe 5-10% of administrations), creating class imbalance that requires SMOTE or class weighting.
**Data availability:** Administration case files contain family structure data and outcome (disputed vs. routine). Consistent documentation of dispute occurrence is necessary for labeling — firms that don't systematically record "this case was disputed" need a labeling audit before model training.
