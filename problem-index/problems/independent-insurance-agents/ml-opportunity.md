# Machine Learning Opportunities — Independent Insurance Agents

**Industry:** [[independent-insurance-agents|Independent Insurance Agents]]
**Derived from:** [[problems/independent-insurance-agents/high-impact|High Impact]], [[problems/independent-insurance-agents/low-impact-1|Low Impact 1]], [[problems/independent-insurance-agents/low-impact-2|Low Impact 2]], [[problems/independent-insurance-agents/worker-life-1|Worker Life 1]], [[problems/independent-insurance-agents/worker-life-2|Worker Life 2]]

---

## 1. Carrier Appetite Prediction for Commercial Lines Submissions
#gradient-boosting #ranking #tabular-ml #tacit-knowledge-ml #revenue-impact

**Problem statement:** Experienced producers carry a mental model of which carriers are actively writing which classes of commercial business in which geographies — knowledge built from years of submissions, declinations, and underwriter conversations. This tacit knowledge determines whether a submission gets quoted in 3 days or declined after 2 weeks of waiting. The goal is to capture and encode this expertise into a model that ranks carriers by likelihood of quoting competitively for a given risk profile.

**ML task:** Learning-to-Rank (pairwise or listwise) on carrier-risk pairs
**Input data:** Risk profile features (NAICS code, state, revenue band, employee count, years in business, loss history summary, coverage lines requested, prior carrier), carrier features (recent bind rate by class/state, average premium for class, loss ratio in segment, published appetite indicators), and historical submission metadata (submission date, market cycle phase)
**Target:** Carrier ranking by composite outcome: P(quote) * P(competitive premium) * P(bind), derived from historical submission-to-outcome records. Primary label is a 3-class outcome per submission: {declined, quoted-not-bound, bound}
**Evaluation metric:** NDCG@5 (Normalized Discounted Cumulative Gain at top 5 carriers) — the model succeeds if the carriers most likely to quote and bind appear in the producer's top 5 recommendations. Secondary: Mean Reciprocal Rank of the carrier that ultimately bound the policy
**Scope:** Requires a multi-agency data consortium or partnership with an aggregator (Bold Penguin, Tarmika, or an AMS vendor) to assemble sufficient submission-outcome pairs. A minimum viable dataset needs 50,000+ commercial lines submissions with outcomes across 20+ carriers. A team of 2-3 ML engineers plus an insurance domain expert could build an MVP in 6-9 months, with the data partnership being the longest lead-time item. Cold-start for new carriers or rare classes will require fallback to structured appetite guide data.
**Data availability:** Individual agencies have hundreds to low thousands of submissions per year — insufficient alone. AMS vendors (Applied, Vertafore) sit on aggregated data but have not productized it for ML. Carrier appetite guides are semi-structured PDFs, parseable but noisy. The critical gap is outcome data: most agencies track whether a policy was bound but not which carriers declined or quoted uncompetitively on the same account.

---

## 2. Client Retention Risk Scoring
#gradient-boosting #binary-classification #tabular-ml #revenue-impact

**Problem statement:** Agencies lose 8-15% of their book annually to competitor agencies, direct carriers, or insurtechs, but the signals of impending departure — rate shopping, reduced communication, competitor quote requests — are scattered across emails, phone notes, and AMS activity logs. A model that identifies at-risk accounts 90-120 days before renewal enables proactive retention outreach.

**ML task:** Binary classification — will this client leave at their next renewal?
**Input data:** Client tenure, premium trajectory (3-year), claims history and frequency, communication frequency (emails, calls logged in AMS), payment behavior (late payments, autopay status), coverage complexity (number of lines, endorsements), rate change history, NPS or survey scores if available, market-level pricing trends for their class
**Target:** Binary label: {retained, lost} at renewal, derived from historical policy records where a client either renewed with the agency or did not
**Evaluation metric:** AUC-ROC as primary metric; precision at top-decile for operational deployment (account managers can only proactively outreach 10-15% of the book). Recall is important but false negatives are less costly than false positives — calling a happy client isn't harmful
**Scope:** A single mid-to-large agency with 5+ years of AMS history and 2,000+ client records can build a usable model. Feature engineering from AMS data (Applied Epic ODBC export or Vertafore reporting) is the main effort. A solo ML engineer with insurance domain access could ship an MVP in 3-4 months. The model improves dramatically with communication sentiment analysis but can launch with structured features only.
**Data availability:** AMS systems contain policy history, premium data, and activity logs. The challenge is extracting and structuring communication data — emails and call notes are unstructured text in AMS activity records. Client loss labels are available retrospectively from policy expiration records.

---

## 3. Cross-Sell Opportunity Scoring
#gradient-boosting #binary-classification #tabular-ml #recommendation #revenue-impact

**Problem statement:** The average independent agency client holds 1.4 policies with the agency despite needing 3-5 coverage types. Producers lack a systematic way to identify which clients are most likely to purchase additional lines (umbrella, cyber, EPLI, inland marine) based on their existing coverage profile and business characteristics.

**ML task:** Multi-label binary classification — for each client x coverage-line pair, predict P(purchase within 12 months)
**Input data:** Client industry, revenue, employee count, existing coverage lines, current carrier mix, policy vintage, claims history, geographic risk factors (e.g., coastal = flood potential), recent business changes (revenue growth, new locations from publicly available data), and comparable-client coverage profiles within the agency's book
**Target:** Binary label per coverage line: {purchased, not purchased} within 12-month window, using historical cross-sell records
**Evaluation metric:** AUC-ROC per coverage line, with lift-at-top-decile as the operational metric (producers will act on a prioritized list). Weighted by line-level commission revenue to optimize for dollar impact
**Scope:** Requires an agency with 1,000+ commercial clients and 3+ years of coverage history. Feature engineering is straightforward from AMS data. Comparable-client clustering adds significant lift but is optional for MVP. A data scientist with AMS access could deliver in 2-3 months. Main risk is label sparsity for niche lines (cyber, EPLI) where few historical purchases exist.
**Data availability:** Strong within individual agencies — AMS systems track all policy lines per client. Cross-agency data would improve coverage of rare lines but is not required for a useful MVP.

---

## 4. Claim Frequency Prediction for Risk Consulting
#gradient-boosting #regression #tabular-ml #revenue-impact

**Problem statement:** Forward-thinking agencies are building risk consulting practices — advising commercial clients on loss prevention to reduce premiums and strengthen carrier relationships. But identifying which clients would benefit most from risk consulting (i.e., which are likely to experience above-average claim frequency) requires actuarial-level analysis that small agencies cannot perform manually.

**ML task:** Regression — predict expected claim count over next 12 months per commercial client
**Input data:** Client industry (NAICS), years in business, employee count, revenue, prior 3-year claims history (count, severity, type), safety program indicators (OSHA citations, experience modification rate for WC), geographic risk factors, carrier loss control report findings if digitized, policy coverage structure (deductible levels, coverage limits as proxies for risk tolerance)
**Target:** Integer count of claims filed in the next policy year; secondary target is aggregate claim severity
**Evaluation metric:** Mean Absolute Error on claim count; Poisson deviance as the distributional metric since claims follow a count distribution. Calibration (predicted vs. actual decile alignment) matters more than point accuracy for consulting use cases
**Scope:** Requires partnership with a carrier or access to agency cluster loss data — individual agencies see only their own clients' claims. A dataset of 10,000+ commercial accounts with 3-year claims history is the minimum. An ML engineer with actuarial or insurance analytics background could build this in 4-6 months. The model's value increases when paired with interpretable risk factors that the agent can present to the client as actionable recommendations.
**Data availability:** Carriers hold the deepest claims data but rarely share it at the account level with agencies. Agency-side data includes claims reported through the AMS and loss runs requested from carriers (typically PDF format requiring parsing). Experience modification rates for workers' comp are publicly available and serve as strong predictive features.
