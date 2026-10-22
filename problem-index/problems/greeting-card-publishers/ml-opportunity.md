# Machine Learning Opportunities — Greeting Card Publishers

**Industry:** [[greeting-card-publishers|Greeting Card Publishers]]
**Derived from:** [[problems/greeting-card-publishers/high-impact|High Impact]], [[problems/greeting-card-publishers/low-impact-1|Low Impact 1]], [[problems/greeting-card-publishers/low-impact-2|Low Impact 2]], [[problems/greeting-card-publishers/worker-life-1|Worker Life 1]], [[problems/greeting-card-publishers/worker-life-2|Worker Life 2]]

---

## 1. Learning the Editor's Pick for a Pocket
#tacit-knowledge-ml #transformers #contrastive-learning #gradient-boosting #evaluation-metrics #feature-engineering #revenue-impact

**Problem statement:** Experienced card editors and line planners choose, from a set of candidate designs for one pocket (occasion, recipient, tone), the ones that will outsell the incumbent card, using a feel for the buyer that they cannot specify. Learn that judgement from their recorded picks and from pocket-level sell-through, and surface it at the review table before the design is printed.

**ML task:** Pairwise ranking of candidate designs within a pocket brief (learning to rank), plus regression of a sell-through index relative to the incumbent by store cluster; multimodal inputs embedded with an image-text model fine-tuned contrastively on the publisher's own card history
**Input data:** Card front and inside images (final art and sketches), caption text front and inside, finish attributes (foil, emboss, glitter, die cut), price point, pocket brief (occasion, recipient, tone), fixture position; weekly units by store and pocket under scan-based trading; store attributes (channel, region, shopper demographics); the selection ledger of each reviewer's picks, confidence and reason codes, including rejected candidates.
**Target:** (a) The reviewers' pick within each candidate set; (b) 26-week sell-through index versus the incumbent in the same pocket, adjusted for fixture position and out-of-stock weeks, per store cluster.
**Evaluation metric:** For the pick model, top-2 agreement with held-out editor choices, reported against the editors' own test-retest agreement on repeated sets, which is the realistic ceiling. For the sales model, rank correlation between predicted and realised index within pocket, measured strictly on later seasons than training, with precision at the top of the ranking weighted most: promoting a loser costs a pocket for a full cycle, while missing a modest winner costs less.
**Scope:** The data-collection challenge comes first: the experts' judgements must be captured while they perform the task, so the review meeting needs a tablet ledger that records picks, confidence and reason codes in one tap per design, and historical rejected candidates must be recovered from creative archives where they exist. The labelling challenge is that experts disagree with themselves and sales are confounded by fixture position, shrink and season, so labels need repeated annotation on a sample of candidate sets to measure intra-rater reliability, and the sales target must be position-adjusted. The deployment challenge is speed: scores must appear in the meeting, on sketches and draft captions, faster than the editors' own discussion, and must explain themselves through similar past cards rather than a bare number. 2 ML engineers, 1 data engineer and a senior editor as product owner, 9–12 months; retrieval of similar past designs and their sales is useful in month three, well before any ranking model is trusted.
**Data availability:** Sell-through by pocket is rich at publishers with scan-based trading accounts, but the scan data is the retailer's, shared under supply agreements that may limit its use. Design images and captions sit in creative archives with inconsistent metadata. The selection ledger does not exist anywhere and building it is most of the work.

---

## 2. Pocket Allocation and Refresh by Store Cluster
#time-series-forecasting #bayesian-inference #k-means-clustering #optimization-fundamentals #feature-engineering #revenue-impact

**Problem statement:** Decide, for each store cluster, which designs fill which pockets and which pockets to refresh next season, by forecasting each design's weekly demand in each cluster and allocating fixed fixture space to maximise department sales per linear foot net of shrink.

**ML task:** Hierarchical demand forecasting (design × pocket × store cluster × week) with partial pooling for sparse, low-volume series; store clustering on sales mix; constrained assignment of designs to pockets
**Input data:** Weekly scans by UPC and store; planograms and pocket positions; store attributes and local demographics; seasonality and holiday calendars; shrink estimates; refresh history.
**Target:** Weekly units per design per store cluster; the allocation that maximises expected sales per linear foot subject to fixture constraints.
**Evaluation metric:** Weighted absolute percentage error on held-out weeks at cluster level, because individual stores sell too few units per pocket for store-level error to be meaningful; then lift in department sales per linear foot in A/B store tests against the current planogram. Under-forecasting a winner leaves an empty pocket; over-forecasting a loser holds inventory the publisher owns under scan-based trading, so both errors cost money but the second is more visible to the retailer.
**Scope:** Most series are intermittent (a few units a week), so partial pooling and clustering do the heavy lifting. A testable version for one retail account takes 2 data scientists about 5 months; store tests need the retailer's cooperation at reset time.
**Data availability:** Held by the publisher for its scan-based accounts; planograms are in space-planning files that need parsing.

---

## 3. Seasonal Quantity and Returns Forecasting
#gradient-boosting #time-series-forecasting #loss-functions #monte-carlo-methods #evaluation-metrics #automation

**Problem statement:** Set store-level quantities for each seasonal program (Valentine's Day, Easter, Mother's Day, Father's Day, graduation, boxed Christmas cards) so that cards sell through in the final days before the holiday with the fewest returns and destroys afterwards.

**ML task:** Quantile regression of store-level seasonal demand by design and day, with a newsvendor-style allocation that prices stock-outs against returns
**Input data:** Prior seasons' daily scans by store and design; set dates and pull dates; the calendar position of the holiday (day of week, days after a preceding season); weather and local events; store traffic proxies; return and destroy records.
**Target:** Daily seasonal demand quantiles per store and design; recommended initial and replenishment quantities.
**Evaluation metric:** Pinball loss on the relevant quantile, plus the realised return rate and lost-sales estimate per season against the prior allocation method. The asymmetry is explicit: a sold-out pocket on the day before Mother's Day loses the year's biggest sales day, while an excess card becomes a credit, so the target quantile is set from the publisher's own margin and return cost.
**Scope:** Each holiday has only one observation a year per store, so pooling across stores and seasons is essential and the model must handle holidays that fall on different weekdays. 1–2 data scientists, 4 months for one program.
**Data availability:** Scan and return records are held by the publisher; set and pull dates are often in merchandiser logs rather than systems.

---

## 4. Fixture Photo Compliance for Merchandisers
#cnns #object-detection #transfer-learning #evaluation-metrics #worker-facing #automation

**Problem statement:** From a merchandiser's phone photo of a card fixture section, identify every card face and pocket, flag misfiled cards with their correct pocket, empty and low pockets, out-of-season cards, and deviations from the current planogram.

**ML task:** Object detection of card faces and pocket tags, fine-grained recognition of each card against the publisher's design catalogue, and matching to the planogram
**Input data:** Fixture photos under store lighting with occlusion and glare; the full catalogue of card front images; planogram files with pocket coordinates; merchandiser corrections.
**Target:** Bounding boxes with design IDs; pocket-level status (correct, misfiled, empty, low, off-season).
**Evaluation metric:** Recall on misfiled and empty pockets at the precision that keeps false alerts below a few per section, since a merchandiser who is sent to fix correct pockets stops trusting the app. Recognition top-1 accuracy across tens of thousands of visually similar designs, and seconds per section on a mid-range phone.
**Scope:** Fine-grained recognition is the hard part: many designs share palettes and layouts, and only a slice of each card is visible in a pocket. Transfer from general retail shelf models helps with detection but not with identity. 2 engineers, 6 months, with catalogue images as the main training asset.
**Data availability:** Catalogue images exist at every publisher; labelled fixture photos must be collected from merchandisers, which their visit logs already partly provide.

---

## 5. Embellishment Mask Proposal for Prepress
#semantic-segmentation #cnns #transfer-learning #evaluation-metrics #worker-facing #automation

**Problem statement:** Given an approved card design and a rough mark-up of which elements receive foil, emboss, glitter or spot gloss, propose press-ready separation masks and die lines that a production artist corrects rather than draws.

**ML task:** Semantic segmentation of artwork into effect layers, followed by vectorisation and rule checks (minimum line weight, trap, distance from fold and die)
**Input data:** Flattened approved art; production artists' finished separation files from past seasons (the paired supervision); printer proof rejection notes; stock and process specifications.
**Target:** Per-pixel effect masks converted to editable vector paths, plus rule violations.
**Evaluation metric:** Intersection-over-union against the artist's final mask, and more importantly minutes of correction per design and proof rejection rate against the hand-built baseline.
**Scope:** Years of paired art and separation files exist in production archives, which makes this unusually well supervised for a creative task. 1–2 engineers, 4–5 months to a plug-in that drafts foil and emboss masks; die lines and glitter follow.
**Data availability:** Held entirely by the publisher and its printers; needs file-format clean-up rather than labelling.
