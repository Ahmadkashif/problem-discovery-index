# Machine Learning Opportunities — Web Data Extraction Firms

**Industry:** [[web-data-extraction-firms|Web Data Extraction Firms]]
**Derived from:** [[problems/web-data-extraction-firms/high-impact|High Impact]], [[problems/web-data-extraction-firms/low-impact-1|Low Impact 1]], [[problems/web-data-extraction-firms/low-impact-2|Low Impact 2]], [[problems/web-data-extraction-firms/worker-life-1|Worker Life 1]], [[problems/web-data-extraction-firms/worker-life-2|Worker Life 2]]

---

## 1. Semantic Breakage Detection Without Ground Truth
#change-point-detection #hypothesis-testing #confidence-intervals #descriptive-statistics #evaluation-metrics #k-nearest-neighbors #bert #revenue-impact

**Problem statement:** An extraction that returns nothing is caught immediately; one that returns the wrong field with the right shape passes every structural check and feeds corrupted data into customer pricing and research systems for weeks. At the scale these firms operate this is continuous, and nobody knows what fraction of delivered data is currently wrong.

**ML task:** Distributional change detection per field per source, combined with cross-source consistency checking on entities that appear in multiple places
**Input data:** Extracted field values over time per source; field type and semantics; cross-source records referring to the same entities; page structure snapshots and diffs; redundant extractions from a sampled subset using a second method; historical confirmed breakages with their onset dates.
**Target:** A field whose extraction has become semantically incorrect, with an estimated onset time.
**Evaluation metric:** Detection recall against historical confirmed breakages with their known onset dates — a natural labelled set that exists in every firm's incident history. False positive rate per source per week is the binding operational constraint, since the queue is already full and a noisy detector will be switched off within a fortnight.
**Scope:** Distributional monitoring catches the highest-value case immediately — a price field switching to the strikethrough original changes the distribution's shape, not just its mean, and requires only that per-field distributions be tracked. Cross-source consistency needs no external truth at all and is strongest exactly where the firm collects the same entities from many sites. Redundant extraction on a small sample gives a direct correctness estimate at bounded cost and is the only method that produces an absolute number rather than a change signal. 2-3 ML engineers, 5 months.
**Data availability:** Extracted values are complete and retained. Historical breakage incidents with onset dates exist in ticketing systems and are the labels. Page snapshots are frequently not retained, which limits diff-based approaches and is a storage decision.

---

## 2. Self-Healing Extraction Repair
#large-language-models #bert #cnns #transfer-learning #evaluation-metrics #hypothesis-testing #confidence-intervals #feature-engineering

**Problem statement:** Maintenance engineers work a queue of broken extractions that never empties, re-anchoring selectors against pages that will change again. The fix is usually mechanical: the field is still on the page, the semantics are known, and the element moved.

**ML task:** Locating a target field on a changed page given its semantic description and prior extraction history, then validating the proposed extraction before deployment
**Input data:** The current page in rendered and raw form; the prior working extraction with its selector and recent output values; the field's semantic description; page structure and visual layout; historical repairs across all targets as training pairs; recent known-good output distributions for validation.
**Target:** A working extraction rule producing values consistent with the field's recent history.
**Evaluation metric:** Proportion of breakages repaired without engineer intervention, and — critically — the rate at which an automatic repair produces semantically wrong values, since a bad auto-repair is worse than a failure because it is silent. The repair must validate against the recent value distribution before deployment and abstain when validation fails.
**Scope:** Validation before deployment is what makes this safe: a proposed extraction can be checked against the distribution of recent known-good values, and a proposal that produces out-of-distribution output should abstain rather than deploy. Repeat-breakage identification is a separate and valuable output — a target breaking weekly needs a structurally different approach, not a weekly repair, and identifying those targets is the difference between treating symptoms and causes. 2 ML engineers, 4-5 months.
**Data availability:** Historical repairs are recorded as configuration changes in version control and form a large natural training set. Paired before-and-after pages are frequently not retained, which is the main gap.

---

## 3. Terms and Robots Change Monitoring Against Active Collections
#large-language-models #bert #transformers #change-point-detection #word-embeddings #evaluation-metrics #compliance

**Problem statement:** Permission is assessed once at onboarding and recorded in a ticket while the collection runs for years. Terms of service change, robots directives change, sections move behind authentication, and privacy law shifts — none of which triggers re-review, because nothing connects the approval to the live collection.

**ML task:** Change detection over crawled terms of service and robots files, with extraction of provisions bearing on automated access, and matching against the active collection inventory
**Input data:** Terms of service and acceptable use pages per target, crawled and versioned; robots.txt histories; authentication state per path; the firm's active collection inventory with paths and purposes; recorded permission assessments; page content classified for personal data presence.
**Target:** A material change to a target's stated position on automated access, or a newly authenticated path, matched to the collections it affects.
**Evaluation metric:** Recall on material changes against a manually tracked set — a missed change leaves a collection running on a lapsed basis, which is the exposure. False positives per target per month determine reviewer load, and terms pages change frequently for immaterial reasons, so distinguishing material from cosmetic change is the actual task.
**Scope:** Extracting provisions specifically about automated access, scraping and data reuse from a terms document is a narrow and tractable extraction problem. Personal data detection within collected content determines which privacy regimes attach and is currently assessed by category rather than by content, which is both over- and under-inclusive. This assists a legal judgement and does not make one — the output is a re-review trigger. 2 ML engineers plus counsel, 4 months.
**Data availability:** Terms pages and robots files are public and cheap to crawl. The active collection inventory exists in the scheduler. Recorded permission assessments live in tickets and are unstructured, which is the integration obstacle.

---

## 4. Cross-Site Product and Entity Resolution
#bert #word-embeddings #k-nearest-neighbors #dbscan #large-language-models #evaluation-metrics #data-integration #feature-engineering

**Problem statement:** Extraction from hundreds of sites produces hundreds of shapes of the same entity with inconsistent identifiers, incompatible units and per-retailer taxonomies. Normalisation is dumped on the customer or rebuilt as professional services per engagement, and none of it accumulates even though the firm sees more of it than any customer ever will.

**ML task:** Entity resolution across sources without reliable shared identifiers, plus unit normalisation and taxonomy mapping
**Input data:** Extracted records across sources with names, descriptions, attributes, images and prices; identifiers where populated; per-site taxonomies; historical resolutions confirmed in prior engagements; unit and pack-size expressions in free text.
**Target:** A canonical entity identity spanning sources, with normalised units and a mapped category.
**Evaluation metric:** Pairwise precision and recall on a manually adjudicated sample, with precision weighted heavily — a false merge combines two different products and corrupts a price comparison, which is the customer's primary use. Report results separately for identifier-bearing and identifier-absent records, since the latter is the real problem and the aggregate hides it.
**Scope:** The hard cases are own-brand, long-tail and fast-moving goods where universal identifiers are absent — precisely the products where competitive monitoring is most valuable. Images add substantial signal for physical goods and are usually captured already. Taxonomy mapping between two retailers is stable once established and is re-established per engagement, which makes it the clearest accumulation opportunity. 2-3 ML engineers, 5-6 months.
**Data availability:** Extraction output is abundant. Confirmed resolutions from prior professional services engagements exist as delivered artefacts and are not retained as a corpus, which is the first thing to fix.
