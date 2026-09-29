# Machine Learning Opportunities — AP Automation Vendors

**Industry:** [[ap-automation-vendors|AP Automation Vendors]]
**Derived from:** [[problems/ap-automation-vendors/high-impact|High Impact]], [[problems/ap-automation-vendors/low-impact-1|Low Impact 1]], [[problems/ap-automation-vendors/low-impact-2|Low Impact 2]], [[problems/ap-automation-vendors/worker-life-1|Worker Life 1]], [[problems/ap-automation-vendors/worker-life-2|Worker Life 2]]

---

## 1. Exception Cause Capture, Prediction and Semantic Matching
#bert #large-language-models #k-nearest-neighbors #gradient-boosting #word-embeddings #evaluation-metrics #feature-engineering #automation

**Problem statement:** Fifteen to thirty percent of invoices fail automated matching and go to a human, whose resolution is recorded as a status change rather than as a labelled cause. The same exceptions recur monthly from the same handful of root causes, and nobody computes that distribution, so the remedy is always more clerks.

**ML task:** Exception cause classification from invoice, purchase order and resolution context; semantic line matching across differing descriptions and units; and prediction of exception likelihood at invoice receipt
**Input data:** Invoices with extracted headers and line items; purchase orders and receipts; vendor history and invoicing patterns; the ERP changes that accompanied each resolution; clerk correspondence; historical matched line pairs from the customer's ERP; requisitioner and buyer identity.
**Target:** A structured cause per exception with a proposed resolution, a probabilistic line-level match, and a pre-match exception likelihood.
**Evaluation metric:** For matching, precision at the auto-clear threshold dominates — a wrongly matched line releases a payment for goods not received, which is a real loss rather than a review cost. For cause classification, accuracy against clerk-confirmed causes, measured after the structured field exists, since today there is no ground truth at all. The business metric is exceptions per thousand invoices and days to resolve, both of which customers already track and neither of which has improved much across a decade of extraction accuracy gains.
**Scope:** The single most important change is not a model: adding one structured cause field that the clerk selects on resolution converts a queue into a dataset, and everything else depends on it. Root cause analytics on top — the distribution of causes by vendor, buyer, category and requisitioner — is the report no customer currently receives and usually shows that a third of exceptions trace to two or three fixable upstream habits. Semantic line matching replaces tolerance-band arithmetic inherited from paper processes. 2 ML engineers, 6 months.
**Data availability:** Invoices, purchase orders and ERP states are complete. Resolution causes do not exist today, which is the gap and the first deliverable.

---

## 2. Cross-Customer Vendor Corroboration and Bank Change Fraud Detection
#graph-neural-networks #bert #gradient-boosting #k-nearest-neighbors #word-embeddings #evaluation-metrics #compliance #data-integration

**Problem statement:** A request to change a vendor's bank details, arriving by email, is the mechanism of business email compromise, and the control is a callback to a number that may have come from the attacker. Meanwhile the platform can see that the same vendor invoices four hundred other buyers whose records show different bank details.

**ML task:** Graph-based vendor entity resolution across customers, corroboration scoring for bank detail changes, and authenticity classification of change requests
**Input data:** Vendor records across the customer base including tax identifiers, addresses, bank accounts, contact domains and invoice templates; bank detail change requests with full email headers, domain age and similarity, phrasing and timing; historical confirmed fraudulent requests; vendor communication history and style; payment and invoicing patterns per vendor across buyers.
**Target:** A resolved vendor identity spanning customers, a corroboration score for any proposed bank change, and an authenticity assessment of the request.
**Evaluation metric:** Recall on confirmed fraud is what matters, evaluated against the platform's own historical incidents and near-misses — a missed case is a large unrecoverable wire, while a false positive is a delayed payment and an awkward phone call. Corroboration should be reported as evidence rather than as a score: "this bank account is not used by any of the other 412 buyers of this vendor" is more actionable and more defensible than a number.
**Scope:** Cross-customer corroboration is the highest-value unexploited asset in this category and needs almost no modelling — it is a join the platform can already perform and does not. Graph entity resolution on tax identifiers, bank accounts, remittance addresses and contact domains is far stronger than the name-and-address fuzzy matching that ships with ERPs today, and the same resolution fixes duplicate payments and a large share of exceptions. Network intelligence sharing, where a confirmed fraudulent request immediately protects every other buyer of that vendor, is the clearest collective-defence case in the domain. 3 ML engineers, 6 months.
**Data availability:** Complete across the platform. The obstacle is contractual and governance-related — using one customer's vendor data to protect another requires terms that many platforms have not written — and should be settled before building.

---

## 3. Correspondence Generation and Reply Interpretation
#large-language-models #bert #k-nearest-neighbors #gradient-boosting #evaluation-metrics #workflow-orchestration #worker-facing #automation

**Problem statement:** The AP clerk's day is writing emails to requisitioners, receivers and vendors about blocked invoices, following up, and manually translating prose replies — "yes we only got half, the rest ships next week" — into receipt adjustments and released invoices.

**ML task:** Generation of exception-specific correspondence, and extraction of actionable facts from free-text replies
**Input data:** Exception type and full invoice, purchase order and receipt context; recipient identity, role and prior responsiveness; historical correspondence with replies and the resolutions that followed; vendor and internal communication norms; ERP actions taken after each reply.
**Target:** A drafted, context-complete message; and a structured interpretation of the reply with the proposed ERP action.
**Evaluation metric:** For generation, the proportion sent without edit and the reply rate compared with the clerk's own baseline — a generated message that is ignored has saved nothing. For interpretation, precision on the proposed action, with anything ambiguous routed to the clerk: acting on a misread reply adjusts a receipt wrongly and releases a payment, which is worse than asking.
**Scope:** This is the largest single time saving available in the role and the least technically demanding, since the messages are formulaic functions of exception type and context. Reply interpretation is the higher-value half because it closes the loop without the clerk re-entering the conversation. Consequence-based prioritisation — discount expiry, payment run timing, vendor supply criticality — needs no learning and should ship alongside, since the queue is currently ordered by whoever complained most recently. 2 ML engineers, 5 months.
**Data availability:** Correspondence lives in email and is accessible where the platform has inbox integration, which many do. Historical replies joined to subsequent ERP actions are the training signal and require a small amount of assembly.

---

## 4. Coding from ERP History with Cross-Customer Chart Alignment
#bert #word-embeddings #k-nearest-neighbors #transfer-learning #large-language-models #evaluation-metrics #data-integration #workflow-orchestration

**Problem statement:** Posting an invoice requires an account, dimensions, tax codes and sometimes customer-invented fields, mapped bespoke per customer over a six-week implementation, and coded thereafter by rules that break on anything ambiguous.

**ML task:** Invoice-to-coding classification trained on the customer's historical ERP postings, with semantic alignment of charts of accounts and dimension structures across customers
**Input data:** Years of the customer's existing AP journal entries with full coding; vendor, line item, amount, requisitioner and category; chart of accounts and dimension names, hierarchies and descriptions across the platform's customer base; custom field names, value distributions and usage; historical corrections.
**Target:** A complete coding assignment with confidence, plus a discovered mapping between the customer's configuration and the platform's model.
**Evaluation metric:** Accuracy at the auto-post confidence threshold, reported separately for the long tail of rarely used accounts and dimensions, where aggregate figures hide exactly the failures a controller notices. Mapping discovery should be validated by replaying historical transactions through the proposed configuration and comparing against what the ERP actually recorded — a direct, decisive test that catches silent misposting before go-live rather than in a month-end variance investigation.
**Scope:** The customer's own posting history is a directly supervised training set for that customer's exact conventions, available on day one of every implementation and used by almost nobody. Cross-customer chart alignment lets a new customer start informed rather than cold, since charts differ in vocabulary far more than in meaning. Implementation length is the binding growth constraint in this category, which makes mapping discovery commercially more important than coding accuracy. 2 ML engineers, 5 months.
**Data availability:** Available at onboarding with customer permission, complete, and routinely left untouched.
