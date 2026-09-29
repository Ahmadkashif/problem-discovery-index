# Machine Learning Opportunities — Procurement & Spend Platforms

**Industry:** [[procurement-spend-platforms|Procurement & Spend Platforms]]
**Derived from:** [[problems/procurement-spend-platforms/high-impact|High Impact]], [[problems/procurement-spend-platforms/low-impact-1|Low Impact 1]], [[problems/procurement-spend-platforms/low-impact-2|Low Impact 2]], [[problems/procurement-spend-platforms/worker-life-1|Worker Life 1]], [[problems/procurement-spend-platforms/worker-life-2|Worker Life 2]]

---

## 1. Line-Item Spend Classification and Supplier Entity Resolution
#bert #word-embeddings #large-language-models #dbscan #k-nearest-neighbors #feature-engineering #evaluation-metrics #data-integration

**Problem statement:** Spend is classified by rules keyed off supplier name, so a distributor selling four categories lands entirely in one. The supplier master holds the same vendor eleven times. Every negotiation, consolidation analysis and savings claim rests on both, and both are wrong in ways that are invisible to the executive reading the spend cube.

**ML task:** Multiclass classification of invoice lines into a category taxonomy from description, supplier, price and unit; plus entity resolution over supplier records with asymmetric merge cost
**Input data:** Invoice and purchase order lines across the customer base with free-text descriptions, supplier identifiers, unit prices, quantities and units; existing category assignments as noisy labels; supplier master records with names, addresses, tax identifiers and remit-to details; confirmed merges and reversals.
**Target:** Category assignment per line as confirmed by a category manager; and canonical supplier identity per record.
**Evaluation metric:** For classification, accuracy on held-out enterprises rather than held-out lines — generalising to a customer never seen is the actual product. For resolution, merge precision weighted far above recall, with merge reversal rate as the operational metric, because a false merge corrupts payment routing and that is an incident rather than an inconvenience.
**Scope:** Cross-customer training is the entire advantage and the entire obstacle: the same line description recurs across thousands of enterprises, and using it requires contractual terms most platforms have but few have exercised. Existing category labels are inconsistent between customers and need reconciliation before they can serve as training data. 3 ML engineers plus a category management expert, 6 months.
**Data availability:** Enormous volume of line items across customer bases. Labels are plentiful and noisy. Supplier master records are messy in exactly the way entity resolution expects.

---

## 2. Contract Term Extraction and Invoice Price Verification
#large-language-models #bert #transformers #word-embeddings #hypothesis-testing #evaluation-metrics #compliance #revenue-impact

**Problem statement:** Three-way match verifies quantity and total and never checks the price against the contract, because the contract is a document nothing reads. Prices erode, volume tiers go unapplied and rebates go unclaimed, which is why a recovery audit industry exists to find this retrospectively for a share of the proceeds.

**ML task:** Clause and table extraction from executed agreements into structured pricing terms, followed by deterministic verification of each invoice line
**Input data:** Executed supplier agreements with price schedules, tier structures, rebate terms, freight and adjustment mechanisms; invoice and purchase order lines; historical recovery audit findings as validation; cross-customer price observations for the same supplier and item.
**Target:** Structured contract terms; and per invoice line, whether the price complies.
**Evaluation metric:** Extraction accuracy on unit prices and tier thresholds specifically, since those drive the check. The business metric is recovered or prevented overcharge measured against what a recovery audit firm subsequently finds on the same period — a direct and unusually honest benchmark that is available because those audits already happen.
**Scope:** Price schedules are frequently attachments in inconsistent spreadsheet formats rather than contract prose, which makes this partly a table extraction problem and partly a document one. Tier and rebate tracking has the most money attached and requires stateful accumulation across a period rather than a per-invoice check. Cross-customer benchmarking is a separate output and is where the platform's unique leverage sits. 2-3 ML engineers plus a contract compliance analyst, 5 months.
**Data availability:** Contracts and invoices are both held by the platform or its customer and are rarely joined. Recovery audit findings provide a validation set that is uniquely well suited and is never requested.

---

## 3. Behavioural Supplier Distress Detection
#change-point-detection #gradient-boosting #survival-analysis #confidence-intervals #hypothesis-testing #feature-engineering #evaluation-metrics

**Problem statement:** Supplier risk is monitored through external scores that describe suppliers in isolation and update slowly. Distress is visible in behaviour the platform observes directly — slipping delivery performance, requests for accelerated payment terms, rising invoice disputes, lengthening quoted lead times — months before a credit rating moves.

**ML task:** Change point detection on per-supplier behavioural series with survival modelling of time to disruption, pooled across the platform's customer base
**Input data:** Delivery performance against promised dates; payment term change requests; invoice dispute and correction rates; quoted lead time trends; order acceptance and rejection; spend concentration per buyer; external financial and news signals; confirmed disruption or insolvency events.
**Target:** A supply disruption, insolvency or material delivery failure within a horizon.
**Evaluation metric:** Lead time against the external risk provider's rating change is the comparison that matters — beating a credit rating by a month is the entire value proposition. Precision at a realistic review capacity, since each flag triggers a supplier conversation with commercial consequences.
**Scope:** Pooling across buyers is what makes this work: one enterprise sees a supplier's behaviour toward itself, and the platform sees it toward hundreds, which is a genuinely different observation. Confirmed disruption labels are rare and must be assembled from support records and news. The buyer-side exposure model — criticality, single-source status, inventory cover, qualification time — is separable, requires ERP data rather than modelling, and is what converts a flag into a decision. 2-3 ML engineers plus a supply risk specialist, 5-6 months.
**Data availability:** Behavioural data is complete within the platform and unused for this purpose. Exposure inputs sit in customer ERP systems and are the main integration obstacle.

---

## 4. Intake Classification and Bid Response Normalisation
#large-language-models #bert #word-embeddings #transformers #gradient-boosting #evaluation-metrics #workflow-orchestration #automation

**Problem statement:** Intake arrives as a sentence in Slack and an analyst extracts the rest by conversation, hundreds of times. Separately, sourcing bid responses arrive in whatever structure each supplier chose despite the template, and normalising them into a comparable frame is the largest single task in a sourcing event and is done in a spreadsheet under deadline.

**ML task:** Classification and slot filling from unstructured requests to determine purchase type, applicable reviews and routing; plus structured extraction from heterogeneous bid response documents into a common frame
**Input data:** Historical intake requests with their eventual classification, routing and approvals; attached quotes and supplier materials; the company's contract and supplier registry; historical sourcing events with supplier responses and the normalised comparison the category manager built.
**Target:** Purchase classification, required reviews and routing as ultimately determined; and normalised bid line items with assumptions and exclusions identified.
**Evaluation metric:** For intake, routing accuracy and the reduction in clarifying exchanges per request, which is the metric the analyst experiences. For bid normalisation, agreement with the manager's own spreadsheet, with unflagged scope assumptions counted as the severe error class since an absorbed assumption selects the wrong supplier for a multi-year agreement.
**Scope:** Duplicate detection at intake — this tool is already owned under an existing agreement — needs no modelling and is the highest-value single check. Bid normalisation must surface assumptions rather than silently reconcile them, which is a design constraint more than a technical one. 2 ML engineers, 4-5 months.
**Data availability:** Intake history is well captured in the newer orchestration tools and poorly captured where intake happens in Slack, which is most places. Prior sourcing events exist as documents and spreadsheets in project folders rather than as structured records.
