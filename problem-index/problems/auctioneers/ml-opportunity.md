# Machine Learning Opportunities — Auctioneers

**Industry:** [[auctioneers|Auctioneers]]
**Derived from:** [[problems/auctioneers/high-impact|High Impact]], [[problems/auctioneers/low-impact-1|Low Impact 1]], [[problems/auctioneers/low-impact-2|Low Impact 2]], [[problems/auctioneers/worker-life-1|Worker Life 1]], [[problems/auctioneers/worker-life-2|Worker Life 2]]

---

## 1. Learning the Auctioneer's Estimate
#tacit-knowledge-ml #gradient-boosting #cnns #transformers #confidence-intervals #evaluation-metrics #feature-engineering #revenue-impact

**Problem statement:** Experienced auctioneers look at an item, or a shed full of them, and "know" what it will bring in this market, this season and this sale format, and whether it will sell at all. The ML problem is to learn that judgement from the firm's own recorded estimates, condition notes and hammers, and return a calibrated price range and sell-through probability per lot fast enough to use in a walkthrough.

**ML task:** Conditional quantile regression of hammer price (10th, 50th and 90th percentiles) per lot, plus binary classification of sold versus passed, with an auxiliary model of the auctioneer's own estimate so the gap between the expert and the model can be reported
**Input data:** Lot photographs; cataloguer titles and descriptions; category, maker and model fields; serial numbers and hours for equipment; sale context (platform, format, absolute or reserve, closing day and hour, lot position, photo count, preview attendance, region, season); the auctioneer's pre-sale low and high estimates where captured; reserves; public price-realised comparables retrieved for each lot (entry 3).
**Target:** Hammer price for sold lots; sold or passed for every lot; estimate error (hammer over midpoint estimate) per estimator and category.
**Evaluation metric:** Pinball loss and interval coverage on lots from future sales only, split by time, because random splits leak market moves. The headline is calibration: the 80% interval should contain ~80% of hammers. Passed lots are censored observations, not missing data, and must be modelled, since excluding them flatters every estimate. Report model versus auctioneer on the same lots; the auctioneer's own test-retest agreement on repeated items is the realistic ceiling. Overestimates cost more than underestimates when they set reserves that cause passes, so report error asymmetrically.
**Scope:** The data collection challenge comes first: estimates must be captured by the expert during the walkthrough, which needs voice-and-video capture that drafts an item list for the auctioneer to adjust, and estimates must then be carried through lotting so each lot inherits the estimates of the items in it. The labelling challenge is that the hammer is noisy (a rained-out preview, a weak closing night) and that auctioneers disagree with themselves across seasons and when they badly want a consignment, so a sample of items should be re-estimated blind to measure intra-rater consistency. The deployment challenge is speed and defensibility: the range must appear in seconds, from a phone, with the comparables that justify it, faster than the auctioneer's own recall. 2 ML engineers and a domain lead embedded with 5–10 partner firms, 9–12 months, with value arriving first as estimator bias reports ("your glassware estimates run high") before any model output is shown to a seller.
**Data availability:** Hammers and lot data sit in clerking software and bidding platforms and are the firm's own. Estimates at lot level barely exist and must be captured prospectively. Public price results (LiveAuctioneers ~29M, Artnet ~18M, WorthPoint ~1B records) supply comparables but not estimates.

---

## 2. Photo-to-Lot Cataloguing
#large-language-models #transformers #cnns #object-detection #transfer-learning #evaluation-metrics #automation #worker-facing

**Problem statement:** From photographs of an item or a group of items, propose the lot boundaries, title, maker, pattern or model, period, material, condition note in the firm's house style, platform category and restricted-item flags, for a cataloguer to confirm.

**ML task:** Object detection and grouping for lotting; fine-grained visual identification of maker's marks and model plates; multimodal generation of titles and condition text constrained to a controlled vocabulary; multi-label classification of restricted items
**Input data:** Cataloguer photo sets; the firm's historical catalogues with their final edited text; platform category trees; maker's-mark and pattern reference images; serial-plate images for equipment; restricted-item lists (firearms, ivory, hazardous materials, titled vehicles).
**Target:** Lot groupings; structured fields; drafted title and condition text; category per platform; restricted-item flags.
**Evaluation metric:** Share of lots accepted with no edit or a minor edit, and time per lot against a stopwatch baseline. Category accuracy per platform. Restricted-item recall is the binding metric: a missed firearm or ivory piece is a legal problem, while a false flag costs seconds. Condition text is checked for invented claims ("works", "original") the photos cannot support; any fabricated claim counts as a severe error.
**Scope:** Commercial vision-language models already draft acceptable descriptions for mass-produced goods; the work is house-style adaptation, controlled condition vocabulary, lotting suggestions and platform mapping. 2 engineers, 4–6 months to a usable tablet workflow with a few partner firms.
**Data availability:** Each firm's past catalogues are a ready supervised corpus of photo-to-text pairs written in its own style; platforms hold far larger corpora but share them only in their own tools.

---

## 3. Comparable Lot Retrieval Across Price-Realised Archives
#contrastive-learning #transformers #word-embeddings #k-nearest-neighbors #evaluation-metrics #data-integration #revenue-impact

**Problem statement:** Given a lot's photos and description, retrieve the most similar previously sold lots, with hammer prices and dates, across the firm's own history and public archives, ranked the way an expert would choose comparables.

**ML task:** Joint image-text embedding trained contrastively on lots, with approximate nearest-neighbour retrieval and a learned re-ranker tuned to expert comparable choices
**Input data:** Lot photos and text from the firm's history; public price results the firm is permitted to use; expert-selected comparable sets gathered from appraisers and auctioneers during normal work.
**Target:** A ranked list of comparable sold lots with similarity scores and price adjustments for condition and date.
**Evaluation metric:** Recall at 10 and mean reciprocal rank against comparables experts chose independently, and the spread of comparable prices, since a tight, relevant set is more useful than a long, noisy one. Measure downstream: does entry 1's interval coverage improve when retrieved comparables are added as features?
**Scope:** Retrieval is a mature technique; the hard parts are licensing access to archives, deduplicating the same lot listed on several platforms, and adjusting for date and region. 1–2 engineers, 3–4 months on the firm's own data, longer with external archives.
**Data availability:** The firm's own sales are free to use. Public archives are browsable but not bulk-licensable on equal terms; the platforms that hold them (ATG, Invaluable, WorthPoint, Artnet) are the natural builders or partners.

---

## 4. Non-Paying Bidder and Shill-Bid Risk
#gradient-boosting #logistic-regression #graph-theory #evaluation-metrics #feature-engineering #compliance #automation

**Problem statement:** Score each bidder registration and each winning bid for the risk that the buyer will not pay or not collect, and flag bidding patterns that suggest shill bidding (consignor or associates bidding up their own lots), so deposits, pre-authorisations or reviews are applied before the sale closes.

**ML task:** Binary classification of payment default per winning bid; graph-based anomaly scoring of bidder-consignor relationships using shared devices, addresses, payment instruments and repeated bidding on one consignor's lots
**Input data:** Registration details, platform history and ratings, payment outcomes across the firm's sales, bid timing and increments, consignor-bidder shared identifiers, pickup no-show history.
**Target:** Paid within terms or not; collected or not; reviewer-confirmed shill pattern.
**Evaluation metric:** Precision at the recall level the firm chooses for requiring deposits, because a false positive annoys a real buyer and can cost a bid. For shill detection, reviewer-confirmed precision in the top flagged cases matters most, since accusations are serious and confirmed cases are rare. Report outcomes by sale format, because timed online sales and live simulcasts behave differently.
**Scope:** Payment-default scoring is a modest tabular project once several sales' outcomes are joined to registrations: 1 data scientist, 2–3 months. Shill detection needs cross-sale identity linkage and careful review protocols and is harder to evaluate because labels are scarce.
**Data availability:** Each firm holds its own payment outcomes; platforms hold cross-firm bidder histories and grade bidders already (Auction Flex lets firms grade bidders for non-payment).

---

## 5. Sale-Level Proceeds Forecast for Guarantees and Reserves
#monte-carlo-methods #gradient-boosting #time-series-forecasting #bayesian-inference #confidence-intervals #revenue-impact

**Problem statement:** Aggregate lot-level price distributions into a distribution of total sale proceeds for a whole consignment, adjusted for market conditions on the sale date, so the auctioneer can price a guarantee or advance and advise on reserves and sale timing.

**ML task:** Monte Carlo simulation over lot-level quantile forecasts (entry 1) with correlated market shocks; time-series forecasting of category price indices (used equipment by class, farmland by county) to the sale date
**Input data:** Lot-level forecasts; historical category indices from the firm's and public results; seasonality of sale calendars; commodity prices and interest rates for farm equipment; the consignor's reserve and guarantee terms.
**Target:** Distribution of gross and net proceeds; probability that proceeds fall below a proposed guarantee; expected cost of each reserve.
**Evaluation metric:** Calibration of the sale-total interval across many sales, and realised loss on guarantees against the forecast expected loss. A guarantee priced off an overconfident interval loses money in exactly the weak markets when many guarantees fail together, so tail coverage matters more than the mean.
**Scope:** Simple once entry 1 exists; correlated shocks are the hard part. 1 data scientist, 3 months. Most valuable to equipment and farm auctioneers who offer guarantees; small estate firms rarely do.
**Data availability:** Firms hold their own sale totals; equipment price indices are sold by valuation guides, and farmland comparables by land data providers.
