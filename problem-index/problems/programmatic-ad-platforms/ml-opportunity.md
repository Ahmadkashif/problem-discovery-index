# Machine Learning Opportunities — Programmatic Ad Platforms

**Industry:** [[programmatic-ad-platforms|Programmatic Ad Platforms]]
**Derived from:** [[problems/programmatic-ad-platforms/high-impact|High Impact]], [[problems/programmatic-ad-platforms/low-impact-1|Low Impact 1]], [[problems/programmatic-ad-platforms/low-impact-2|Low Impact 2]], [[problems/programmatic-ad-platforms/worker-life-1|Worker Life 1]], [[problems/programmatic-ad-platforms/worker-life-2|Worker Life 2]]

---

## 1. Bid Valuation Under Delayed and Censored Conversion
#survival-analysis #gradient-boosting #maximum-likelihood-estimation #bayesian-inference #confidence-intervals #evaluation-metrics #probability-distributions #loss-functions

**Problem statement:** Conversions arrive days to weeks after the impression that caused them, so at training time most of the positive outcomes for recent impressions have not happened yet. Treating unconverted-so-far as negative systematically undervalues inventory that drives considered purchases and overvalues whatever converts within the hour, which is usually an audience the advertiser would have reached anyway.

**ML task:** Joint estimation of conversion probability and time-to-conversion under right-censoring, producing a calibrated expected outcome value per bid request
**Input data:** Bid request features (context, placement, format, geography, device, audience signals); auction outcome and price paid; observed conversions with their timestamps and the elapsed observation window per impression; advertiser vertical, product price band and historical delay distribution; campaign and creative identifiers.
**Target:** Conversion within the advertiser's stated attribution window, with the delay modelled rather than truncated — the label is a time and a censoring indicator, not a binary.
**Evaluation metric:** Calibration of the expected value is the primary criterion, since the number is used to price a bid and a miscalibrated model loses money directly rather than ranking badly. Report calibration by delay bucket, because the failure is concentrated in slow-converting segments. Rank correlation against fully-observed outcomes on a held-out cohort that has aged past the attribution window is the honest accuracy test; anything measured on fresh data is measuring the censoring.
**Scope:** The delay distribution must be fit per advertiser and product price band — a $12 impulse purchase and a $4,000 considered one share no structure. Recency matters enormously in this domain, so the model retrains continuously and the censoring correction has to be stable under retraining. 3 ML engineers plus a measurement analyst, 6-9 months to a production bidder integration.
**Data availability:** Bid logs are enormous and complete. Conversion timestamps exist for pixel-based conversions and are the binding constraint everywhere else — MMP postbacks and clean-room returns arrive aggregated, which limits the model to the advertisers willing to return event-level or windowed data.

---

## 2. Incrementality Estimation from Continuous In-Auction Holdouts
#causal-inference #bayesian-inference #hypothesis-testing #confidence-intervals #monte-carlo-methods #evaluation-metrics #variational-inference #revenue-impact

**Problem statement:** Attributed conversions cannot distinguish an ad that caused a purchase from an ad shown to someone already buying, and the bidder's targeting guarantees the two are confounded. Annual lift studies answer the question at a granularity too coarse to change any bid.

**ML task:** Hierarchical causal effect estimation from a continuous stream of small randomised auction-level holdouts, pooling across segments to produce incremental value estimates with honest uncertainty
**Input data:** Randomised holdout assignment at auction eligibility; exposure records for the treated arm; outcome records for both arms; segment covariates (audience, channel, creative, supply source, geography, frequency); campaign and advertiser hierarchy for pooling.
**Target:** Incremental conversion rate — the difference in outcome rate between eligible-and-served and eligible-and-withheld, per segment.
**Evaluation metric:** Interval coverage against a small number of large, properly-powered reference experiments is the only trustworthy validation; point-estimate accuracy alone will look fine while being wrong. Report the width of the intervals honestly — a segment-level incrementality estimate that cannot exclude zero should say so, and most of them will at first.
**Scope:** The statistical difficulty is power: at segment granularity, holdouts are small and effects are small, which is exactly the regime where hierarchical pooling earns its keep and where naive per-segment estimates produce confident nonsense. The organisational difficulty is larger — somebody must agree to withhold spend permanently, and the finding that a segment has no incremental effect is commercially unwelcome to the party being asked to fund it. 3 ML engineers plus a causal inference specialist, 9-12 months, and an executive sponsor who will accept bad news.
**Data availability:** Requires instrumenting the bidder to randomise and log the withheld arm, which most do not do. Once built, the data accumulates for free and permanently, which is what makes it a better asset than any study.

---

## 3. Supply Path and Inventory Quality Scoring from the Buyer's Own Auction Stream
#graph-neural-networks #change-point-detection #dbscan #k-means-clustering #gradient-boosting #feature-engineering #evaluation-metrics #data-integration

**Problem statement:** The same impression reaches a buyer through many resellers at many prices, and a share of available inventory exists only to carry advertising. Universal quality lists are blunt, stale, and not specific to the buyer whose money is at stake.

**ML task:** Graph learning over the declared and observed supply chain, plus clustering and change detection on domain behaviour, to score paths by realised cost efficiency and domains by quality for this buyer
**Input data:** Bid requests with SupplyChain Object, seller and publisher identifiers; `ads.txt` and `sellers.json` declarations; win rate, clearing price and fee reconciliation per path; page-level features — ad density, content volume and reuse, traffic acquisition signals, refresh behaviour; the buyer's own downstream outcome data per domain and path.
**Target:** Realised outcome per dollar by path and domain for this buyer, and a made-for-advertising classification validated against manual review.
**Evaluation metric:** For paths, cost delta at matched publisher and format — the claim is that path A costs eleven percent more than path B for the same impression, and it is checkable. For quality, precision at the top of the blocklist matters far more than recall, because a false positive removes legitimate reach from a real publisher and the known harm of blunt blocklists is defunding small and non-English publications. Measure reach lost alongside quality gained, always together.
**Scope:** The graph is the interesting part: declared chains and observed behaviour disagree, and the disagreement itself is signal. Domain behaviour drifts after ownership changes, which is a change-detection problem with a clear label once it is noticed. 2 ML engineers plus a supply analyst, 4-6 months.
**Data availability:** Entirely in the buyer's own bid stream plus public declaration files. This is the most immediately tractable item on this list.

---

## 4. Creative Performance Prediction from Asset Content
#cnns #transformers #bert #contrastive-learning #transfer-learning #gradient-boosting #evaluation-metrics #feature-engineering

**Problem statement:** Creative is the largest driver of advertising effectiveness and is optimised by rotating opaque variant identifiers, so nothing learned in one campaign transfers to the next. On day one of a flight — when the decision matters most — the system knows nothing.

**ML task:** Learn a content-level representation of creative assets (image, video, copy) and predict performance as a function of creative attributes interacted with placement context
**Input data:** Creative assets themselves — frames, layout, detected faces and objects, colour and motion statistics, copy text and its structure, brand element position; placement context (format, device, environment, content category, position); observed performance by context; advertiser vertical and objective.
**Target:** Outcome rate for the creative-in-context, using the same outcome definition as the bid valuation model rather than raw click-through.
**Evaluation metric:** Cold-start performance is the whole point — evaluate on creatives and advertisers never seen in training, because a model that only ranks well after two weeks of data has reproduced the thing it was meant to replace. Report lift over the incumbent rotation at day one, day three and day seven.
**Scope:** The transferable unit is the attribute, not the asset, and the interaction between creative attribute and placement context is where most of the exploitable signal lives. Cross-advertiser training is the advantage an independent platform holds over a single-brand optimiser and raises the same contractual questions as any cross-customer learning — abstracted attributes rather than assets is the workable form. 3 ML engineers with vision and multimodal experience, 9-12 months.
**Data availability:** Creative assets and their delivery records sit in the ad server. The constraint is outcome quality, which inherits every problem in item 1, and the fact that most advertisers ship too few variants for within-advertiser learning — which is precisely the argument for pooling across them.
