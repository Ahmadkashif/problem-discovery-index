# Machine Learning Opportunities — BNPL Providers

**Industry:** [[bnpl-providers|BNPL Providers]]
**Derived from:** [[problems/bnpl-providers/high-impact|High Impact]], [[problems/bnpl-providers/low-impact-1|Low Impact 1]], [[problems/bnpl-providers/low-impact-2|Low Impact 2]], [[problems/bnpl-providers/worker-life-1|Worker Life 1]], [[problems/bnpl-providers/worker-life-2|Worker Life 2]]

---

## 1. Cashflow-Primary Underwriting and Accumulation Inference
#gradient-boosting #logistic-regression #survival-analysis #bert #causal-inference #confidence-intervals #evaluation-metrics #feature-engineering #compliance

**Problem statement:** Each provider underwrites a consumer it models as having one obligation while the consumer may hold six across six providers, because pay-in-four furnishing is partial by construction. The provider's own outcome — did this plan repay — is a much narrower thing than the capacity it is trying to estimate.

**ML task:** Repayment and capacity modelling on connected bank cashflow, with explicit inference of concurrent instalment obligations from transaction descriptors
**Input data:** Connected account transaction feeds including income timing and amount, recurring debits, balance troughs and overdraft events; other providers' auto-debits identifiable by descriptor; bureau and alternative file data where present; device and behavioural signals; the provider's own plan and repayment history; merchant and basket context.
**Target:** Probability of repayment without consumer harm — defined to include not triggering an overdraft and not requiring a further plan to service this one — and an estimated count of concurrent obligations.
**Evaluation metric:** Loss rate at a fixed approval rate is the commercial metric, but it is insufficient on its own and using it alone is what produces the sector's worst outcomes. Report alongside it the rate at which approved plans were serviced through an overdraft or a subsequent plan, stratified by predicted capacity band. A model that reduces charge-offs while increasing that rate has made the business better and the consumers worse, and only a two-metric frame makes that visible.
**Scope:** Connected-account coverage is the highest-leverage lever available and costs conversion, which is exactly why the tradeoff should be measured rather than assumed — a randomised test of connection prompts against downstream loss and harm metrics is a small, decisive experiment. Descriptor-based detection of competitors' debits is straightforward string and pattern work with very high value, since it solves the accumulation problem unilaterally without requiring anyone to cooperate. 3 ML engineers and 1 data engineer, 7 months.
**Data availability:** Connected feeds exist for the minority of consumers who link an account, which is the constraint. Everything else is internal. Competitor descriptors are learnable from any connected population and then applied to inference elsewhere.

---

## 2. Distress Signal and Collections Treatment Selection
#gradient-boosting #survival-analysis #bert #large-language-models #causal-inference #evaluation-metrics #worker-facing #compliance

**Problem statement:** Collections agents work small delinquent balances belonging to people in genuine difficulty, choosing between retry, payment plan, hardship arrangement and placement, with no way to distinguish a consumer who is temporarily short from one in a spiral. Automated card retries into an empty account generate overdraft fees larger than the instalment.

**ML task:** Distress classification separating temporary from structural shortfall, plus uplift modelling on treatment choice
**Input data:** Decline patterns and retry outcomes; connected balance and payroll timing where available; other instalment debits; consumer message text and channel responsiveness; plan and purchase history; prior arrangements and whether they held; eventual recovery and re-delinquency.
**Target:** A capacity state for the consumer, and the expected outcome of each available treatment conditioned on it.
**Evaluation metric:** Treatment selection must be evaluated as uplift rather than as outcome — a payment plan offered to someone who would have paid anyway is a cost, not a success, and only randomised or quasi-experimental assignment separates the two. The secondary metric that matters is overdraft events triggered by the provider's own retries, which is measurable in connected accounts and is currently nobody's number.
**Scope:** Retry timing alone is a large, cheap win: timing against observed payroll cycles instead of a fixed schedule reduces both failed retries and the overdraft fees they cause. The uplift work requires deliberate randomisation of treatment within policy bounds, which is defensible here precisely because the current assignment is effectively arbitrary. Proactive hardship identification matters because the consumers most at risk are the least likely to call. 2 ML engineers, 6 months.
**Data availability:** Retry and recovery histories are complete internally. Arrangement outcomes are recorded. Overdraft consequences are visible only in connected accounts, which makes that population the measurement sample.

---

## 3. Return Prediction and Refund-to-Plan Reconciliation
#gradient-boosting #bert #k-nearest-neighbors #large-language-models #evaluation-metrics #feature-engineering #data-integration #workflow-orchestration

**Problem statement:** A consumer returns an item, the merchant processes it over three weeks, and the instalment schedule keeps debiting for a product in a warehouse. Matching a merchant's refund file back to the right plan is manual when references do not align, and the choice of how to adjust the schedule is a default nobody has tested.

**ML task:** Return probability estimation at plan origination, plus entity matching between merchant refund records and instalment plans
**Input data:** Merchant category, item type, price point and basket composition; consumer return history; merchant return policy and historical processing latency; refund files with order references, amounts and dates; plan and payment state; consumer complaint records tied to refund handling.
**Target:** Probability and expected timing of return at origination; and a confident plan match for each incoming refund line.
**Evaluation metric:** Matching precision is the operative number, with unmatched lines routed to operations rather than force-matched — a refund applied to the wrong plan creates two consumer problems instead of one. For return prediction, calibration by merchant matters more than aggregate accuracy, since the use is per-merchant scheduling policy. Downstream, measure complaints per thousand refunded plans under each schedule-adjustment policy.
**Scope:** Matching is the mechanical majority of the value and needs little learning beyond fuzzy reference resolution and amount-date reconciliation. Return prediction enables differentiated scheduling on high-return merchant categories, which is a product change rather than a model output. Complaint classification on consumer narratives is worth adding because complaint themes identify a merchant whose returns handling is failing before that merchant knows. 2 ML engineers, 4 months.
**Data availability:** Good. Refund files, plan records and complaint text are all held; merchant processing latency is derivable from history.

---

## 4. Placement Incrementality and Integration Verification
#causal-inference #gradient-boosting #bert #large-language-models #confidence-intervals #hypothesis-testing #evaluation-metrics #revenue-impact

**Problem statement:** The provider's commercial argument to merchants is incremental revenue, asserted from a dashboard comparing BNPL and non-BNPL orders, which is not a comparison of like with like. Meanwhile placements break silently — wrong page, wrong position, absent on mobile, shown on ineligible baskets — and are discovered when volume drops.

**ML task:** Randomised incrementality measurement on offer exposure, plus automated verification and classification of merchant storefront placements
**Input data:** Session-level exposure and conversion data; basket composition and eligibility; merchant storefront pages fetched across device types; placement position and rendering; historical placement configurations and their measured conversion; merchant category and basket size distributions.
**Target:** Incremental conversion and basket size attributable to the offer; and a verified statement of where and how the offer renders on each merchant.
**Evaluation metric:** Incrementality requires withholding the offer from a randomised share of sessions, and the metric is the difference in conversion and order value between arms with a confidence interval a merchant's analytics team can check. Anything short of randomisation produces a number that sophisticated merchants correctly discount. For verification, the metric is broken placements detected before the merchant or the account manager notices.
**Scope:** Verification is unglamorous and immediately valuable: fetching a merchant's own product pages and checking that the messaging renders in the right place, on mobile, only on eligible baskets, is a crawler and a classifier. Incrementality is the harder sell internally because it requires giving up a small amount of volume, and it is the only thing that converts the merchant negotiation from assertion to evidence. Placement recommendations drawn from thousands of merchants' measured results replace a best-practice guide. 2 ML engineers, 5 months.
**Data availability:** Session and conversion data are held by the provider; storefronts are publicly fetchable. Randomisation requires merchant agreement, which is easier to obtain than it appears when framed as proving the provider's own claim.
