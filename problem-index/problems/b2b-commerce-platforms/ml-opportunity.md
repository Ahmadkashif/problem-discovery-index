# Machine Learning Opportunities — B2B Commerce Platforms

**Industry:** [[b2b-commerce-platforms|B2B Commerce Platforms]]
**Derived from:** [[problems/b2b-commerce-platforms/high-impact|High Impact]], [[problems/b2b-commerce-platforms/low-impact-1|Low Impact 1]], [[problems/b2b-commerce-platforms/low-impact-2|Low Impact 2]], [[problems/b2b-commerce-platforms/worker-life-1|Worker Life 1]], [[problems/b2b-commerce-platforms/worker-life-2|Worker Life 2]]

---

## 1. Predictive Price Precomputation and ERP Reconciliation
#gradient-boosting #optimization-fundamentals #confidence-intervals #hypothesis-testing #evaluation-metrics #data-integration #k-nearest-neighbors #revenue-impact

**Problem statement:** Customer-specific pricing must resolve a rule hierarchy across customers, products, quantities and dates in milliseconds at page load. The full space is too large to materialise, calling the ERP is slow, and caching risks staleness on a number that must be exactly right — which is why B2B storefronts feel slow and why large customers bypass them for inside sales.

**ML task:** Predicting the product set each customer is likely to view, to guide selective precomputation, plus systematic reconciliation between storefront and ERP prices
**Input data:** Customer purchase history with reorder cycles; browse and search history; contract terms and entitlement definitions; catalogue structure and product relationships; pricing rule evaluation logs; storefront prices served and ERP invoice prices for the same orders.
**Target:** The products a customer will view or order in the next period, and any divergence between quoted and invoiced price.
**Evaluation metric:** Cache hit rate on the precomputed set at a given precomputation budget — the direct operational measure, since the goal is covering the overwhelming majority of requests cheaply rather than predicting perfectly. For reconciliation, detection rate on injected discrepancies, and the true divergence rate, which no distributor currently knows.
**Scope:** B2B purchasing is unusually predictable — customers buy a small, stable set of parts on recognisable cycles — which is precisely why selective precomputation works here and would not in consumer retail. The reconciliation half needs no modelling and delivers immediate value: sampling storefront prices against ERP invoices converts a silent commercial error into a monitored one. Pricing rule hierarchy analysis from evaluation logs identifies dead, conflicting and shadowed rules in hierarchies that have accreted for a decade. 2 ML engineers, 4-5 months.
**Data availability:** Purchase and browse history is complete. Pricing rule evaluation logs are frequently not retained at the detail needed for hierarchy analysis, which is a logging change.

---

## 2. Attribute Extraction from Manufacturer Datasheets
#large-language-models #bert #cnns #word-embeddings #transfer-learning #evaluation-metrics #confidence-intervals #data-integration

**Problem statement:** Industrial catalogues run to hundreds of thousands of items whose technical attributes arrive as manufacturer PDFs, and structuring them is manual — so it is done for top sellers and the long tail stays a part number and a price, which means customers cannot filter to the specification they need and call inside sales instead.

**ML task:** Extracting structured technical attributes from datasheets into a category attribute schema, with mapping from manufacturer terminology to standard classifications
**Input data:** Manufacturer datasheets in PDF and spreadsheet form with highly variable layout; existing enriched product records as labelled pairs; industry classification schemas (UNSPSC, ETIM, eCl@ss); manufacturer-published structured data where available; catalogue images; historical corrections by catalogue staff.
**Target:** Populated attributes per product as confirmed by the catalogue team.
**Evaluation metric:** Per-attribute accuracy weighted by findability impact rather than uniformly — a wrong thread specification causes a returned part and a wrong marketing description does not. Report precision separately from coverage, since an unextracted attribute is a gap and a wrongly extracted one is a customer ordering the wrong part for a job site.
**Scope:** Datasheets are highly variable in layout and highly consistent in content within a category, which suits retrieval-augmented extraction with schema conditioning. Confidence gating is essential — the review queue should contain what the model is unsure about, not a random sample. Cross-reference generation between functionally equivalent parts from different manufacturers is the commercially valuable downstream output and is entirely gated on this extraction. 2-3 ML engineers plus a catalogue specialist, 5-6 months.
**Data availability:** Datasheets are abundant and already collected. Enriched records for top-selling items provide a substantial labelled set, biased toward the categories that were prioritised.

---

## 3. Quote Win Probability and Substitute Recommendation
#gradient-boosting #logistic-regression #confidence-intervals #k-nearest-neighbors #evaluation-metrics #hypothesis-testing #revenue-impact #worker-facing

**Problem statement:** Inside sales reps price quotes from memory and instinct, without knowing whether a quote will be accepted at a given price, what comparable customers paid, or how their own discounting has performed. Quote outcomes are frequently not tracked at all, so win rate by product, customer or discount level is unknown.

**ML task:** Acceptance probability prediction conditional on quoted price, plus specification-based substitute recommendation for unavailable or discontinued items
**Input data:** Historical quotes with line items, quantities, quoted prices, discounts and accepted or lost outcomes; customer purchase history and price sensitivity; competitor presence where recorded; product margin; stock position and lead times; structured product specifications for substitution.
**Target:** Quote acceptance, ideally at line level, and the substitute a rep actually offered and the customer accepted.
**Evaluation metric:** Calibration across the discount range, since the model is used to choose a price and must be trustworthy at levels other than the one quoted. Business metrics are realised margin and win rate against the rep's own baseline — and the model should be evaluated for the failure mode where it raises win rate simply by recommending deeper discounts.
**Scope:** The prerequisite is outcome tracking, which a remarkable number of distributors do not do, so instrumenting quote outcomes is the first project and everything else follows. Substitute recommendation is gated on structured specifications and is the clearest argument for funding the catalogue extraction work. Line-level rather than quote-level outcome data is substantially more useful and is rarer. 2 ML engineers, 4-5 months.
**Data availability:** Order history is complete in the ERP. Quote history is often incomplete or lives in email and spreadsheets, which is the binding constraint and is a process problem.

---

## 4. Procurement Connection Configuration and Part Cross-Referencing
#bert #word-embeddings #large-language-models #k-nearest-neighbors #transfer-learning #evaluation-metrics #data-integration #workflow-orchestration

**Problem statement:** Every large customer's procurement integration is a multi-week project despite standardised protocols, because the variation is in fields, conventions and expectations rather than in the protocol. Separately, customers order by their own part numbers and the crosswalk to the supplier catalogue is built manually per account.

**ML task:** Proposing connection configurations from prior integrations to the same procurement platform, plus automated cross-reference matching between customer part numbers and catalogue items
**Input data:** Historical integration configurations by procurement platform and customer; the customer's specification documents; field mappings and unit-of-measure conventions; customer part number lists with their eventual catalogue matches; product descriptions and specifications; historical order lines showing which customer part number resolved to which item.
**Target:** A working connection configuration accepted without modification, and the correct catalogue item for a given customer part number.
**Evaluation metric:** For configuration, the reduction in integration days per customer and the proportion of proposed mappings accepted unchanged. For cross-referencing, precision weighted heavily over recall — matching a customer's part number to the wrong item ships the wrong part to a job site, which is far worse than leaving it unmatched for a human to resolve.
**Scope:** Configurations for the same procurement platform are largely repeats across customers, which makes retrieval from prior integrations the natural approach and requires only that configurations be retained as a corpus rather than as per-project artefacts. Cross-reference matching benefits enormously from historical order lines, where a customer's part number has already resolved to a catalogue item through human effort — that is a large, free, high-quality labelled set that nobody exploits. 2 ML engineers, 4 months.
**Data availability:** Prior configurations exist in project files. Historical order lines linking customer part numbers to catalogue items are complete in the ERP and are the strongest available asset for this problem.
