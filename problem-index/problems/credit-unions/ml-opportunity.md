# ML Opportunities — Credit Unions

**Industry:** [[credit-unions|Credit Unions]]
**Tags:** #gradient-boosting #large-language-models #feature-engineering #evaluation-metrics #cross-validation #probability-distributions #tacit-knowledge-ml #compliance #revenue-impact
**Derived from:** [[problems/credit-unions/high-impact|High Impact]], [[problems/credit-unions/low-impact-1|Low Impact 1]], [[problems/credit-unions/low-impact-2|Low Impact 2]], [[problems/credit-unions/worker-life-1|Worker Life 1]], [[problems/credit-unions/worker-life-2|Worker Life 2]]

---

## 1. Member Default Prediction with Behavioral Signals (Primary Opportunity — Tacit Knowledge ML)
#gradient-boosting #decision-trees #feature-engineering #cross-validation #evaluation-metrics #probability-distributions #bias-variance-tradeoff #gradient-descent #tacit-knowledge-ml #revenue-impact

**Problem statement:** Veteran CU loan officers predict member default more accurately than credit scores by reading behavioral signals in deposit patterns, account usage shifts, and member engagement history — judgment built from hundreds of observed loan outcomes that is lost when they retire and unavailable to junior lending staff.

**ML task:** Binary classification (default within 12 months: yes/no) with feature importance attribution for loan officer review
**Input data:** Member-level features extracted from core banking transaction history (Symitar/KeyStone/XP2): deposit amount trajectory (3/6/12-month rolling averages and volatility), deposit frequency changes, account balance floor trend, overdraft frequency and recovery speed, product engagement breadth (number of active CU products), credit card utilization trajectory, external transfer patterns, member tenure, and loan payment timing patterns (days-before-due-date trend). Supplemented by structured knowledge capture from veteran loan officers identifying which behavioral signals they weight in lending decisions.
**Target:** Binary default label (90+ days past due or charge-off within 12 months of origination), with secondary regression target for loss severity.
**Evaluation metric:** AUC-ROC on held-out loan vintages; recall at 5% false positive rate (critical: the model must catch defaults without over-declining); comparison to FICO-only baseline on the same member population. Fair lending audit: disparate impact analysis across protected classes to ensure behavioral features don't proxy for prohibited characteristics.
**Scope:** 2-person ML team, 4-6 months to production pilot. Requires core banking data extract pipeline, 5-10 years of loan performance history, and structured interviews with 3-5 veteran loan officers for feature engineering validation. Pilot on unsecured personal loans where relationship signals have highest marginal value over bureau scores.
**Data availability:** Core banking systems contain full transaction history; loan performance data is available through call report filings and internal loan tracking. The scarce resource is structured capture of veteran loan officer judgment — requires dedicated interview/observation sessions before retirement. NCUA fair lending review adds 1-2 months to deployment timeline.

---

## 2. Member Churn Prediction and Retention Targeting
#gradient-boosting #decision-trees #feature-engineering #cross-validation #evaluation-metrics #time-series-forecasting #probability-distributions #bias-variance-tradeoff #revenue-impact

**Problem statement:** Credit unions lose 5-8% of members annually, but identify at-risk members only after they've already moved their primary banking relationship — when the direct deposit switches to another institution and the share account balance drops to near zero.

**ML task:** Binary classification (member attrition within 6 months: yes/no) with lead time of 60-90 days before full relationship departure
**Input data:** Member engagement features from core banking: direct deposit presence and amount trend, debit card transaction frequency and volume, mobile/online banking login frequency, branch visit frequency, product holding breadth, loan payoff without replacement, external ACH transfer volume increases, bill pay deactivation, and demographic features (age, tenure, geographic proximity to branch).
**Target:** Member attrition label — defined as direct deposit departure or account balance decline below $100 sustained for 60+ days.
**Evaluation metric:** Precision at top-10% risk decile (intervention resources are limited; the model must accurately identify the members most likely to leave). Lift over baseline (tenure + balance rule).
**Scope:** Single ML engineer, 3-4 months. Requires core banking data extract and 3+ years of historical member attrition data with behavioral feature reconstruction. Integration with CRM or marketing automation for retention outreach triggering.
**Data availability:** Core banking platforms maintain complete transaction and engagement history. Attrition labeling requires matching account closure or dormancy records with preceding behavioral patterns. Most CUs have never constructed this dataset but the raw data exists.

---

## 3. Cross-Sell Propensity Scoring for Teller and Digital Channels
#gradient-boosting #decision-trees #feature-engineering #cross-validation #evaluation-metrics #conditional-probability-and-bayes-theorem #probability-distributions #worker-facing

**Problem statement:** CU tellers and digital banking platforms deliver untargeted product suggestions that convert at 1-3%, creating member friction and teller stress while missing high-propensity opportunities hidden in member transaction patterns.

**ML task:** Multi-label classification (propensity score for each CU product: auto loan, mortgage refi, credit card, certificate, HELOC, personal loan) per member
**Input data:** Current product holdings, transaction patterns (spending categories indicating auto purchase research, mortgage payment to external institution, high savings balance duration), life event signals (address change, payroll amount change, new joint account holder), member demographics, and historical product adoption sequences (members who opened product X subsequently opened product Y within N months).
**Target:** Product adoption within 90 days for each product category. Multi-label: a member may have positive propensity for multiple products simultaneously.
**Evaluation metric:** Precision@1 (the single recommendation shown to the teller must be relevant); lift over random product suggestion baseline; teller referral conversion rate before vs. after deployment.
**Scope:** Single ML engineer, 3-4 months. Requires product holding history, transaction enrichment (MX or internal categorization), and integration with teller workstation display and digital banking notification system.
**Data availability:** Product holding and adoption history is standard in core banking. Transaction categorization may require MX or similar enrichment layer. Historical referral conversion data (if tracked) provides direct training signal; otherwise, product adoption timing serves as implicit label.

---

## 4. BSA/AML Alert Prioritization for Credit Union Transaction Patterns
#gradient-boosting #decision-trees #feature-engineering #evaluation-metrics #descriptive-statistics #hypothesis-testing #probability-distributions #compliance

**Problem statement:** BSA/AML platforms generate 200-400 alerts per month at small CUs with 90%+ false positive rates because monitoring rules and ML models are calibrated for commercial bank transaction distributions, not the member-level behavioral baselines of a 15,000-member community institution.

**ML task:** Anomaly detection (genuinely suspicious transactions vs. expected member behavior) with alert risk scoring for investigation prioritization
**Input data:** Member-level transaction history establishing individual behavioral baselines: typical cash deposit amounts and frequency, wire transfer destinations and frequency, ACH patterns, and seasonal cycles. Community context features: local industry mix (cash-intensive businesses in the CU's field of membership), geographic remittance corridors, and historical SAR filing patterns. Alert metadata from existing BSA platform (Verafin/Abrigo): alert type, trigger rule, transaction details.
**Target:** BSA officer disposition label on historical alerts — investigated (SAR filed) vs. cleared (false positive). Secondary: FinCEN feedback on filed SARs (confirmed suspicious vs. no action).
**Evaluation metric:** Recall on true suspicious activity (must not miss genuine SARs); false positive reduction rate at constant recall; BSA officer review time per alert. Regulatory constraint: model must maintain or improve SAR detection rate to satisfy NCUA examination.
**Scope:** 2-person team (ML + compliance), 6-8 months including regulatory validation. Requires historical alert disposition data (2-3 years), member transaction history for baseline construction, and NCUA compliance review of model methodology before production deployment.
**Data availability:** BSA platforms maintain complete alert and disposition history. Member transaction data is in core banking. The regulatory validation requirement — demonstrating to NCUA examiners that the model maintains detection effectiveness — is the primary timeline driver, not the technical build.
