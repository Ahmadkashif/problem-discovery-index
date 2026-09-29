# Machine Learning Opportunities — Streaming Video Platforms

**Industry:** [[streaming-video-platforms|Streaming Video Platforms]]
**Derived from:** [[problems/streaming-video-platforms/high-impact|High Impact]], [[problems/streaming-video-platforms/low-impact-1|Low Impact 1]], [[problems/streaming-video-platforms/low-impact-2|Low Impact 2]], [[problems/streaming-video-platforms/worker-life-1|Worker Life 1]], [[problems/streaming-video-platforms/worker-life-2|Worker Life 2]]

---

## 1. Incremental Title Value and Substitutability
#causal-inference #survival-analysis #gradient-boosting #confidence-intervals #hypothesis-testing #evaluation-metrics #feature-engineering #revenue-impact

**Problem statement:** A platform spends billions annually on content and substitutes hours viewed for value, which rewards long series watched by loyal subscribers who were never going to leave and undervalues the narrow title that holds a segment nobody else serves — precisely the content a differentiated service depends on.

**ML task:** Causal estimation of a title's contribution to acquisition and retention, with explicit modelling of substitutability, using the randomisable levers and the natural experiments the business already generates
**Input data:** Complete individual viewing histories with timing, abandonment and rewatch; subscription tenure, signup and cancellation events; randomised recommendation placement, artwork, homepage promotion and notification targeting; staggered international release dates and regional rights variations; title removals and rights expirations; catalogue composition over time; marketing spend by title and region.
**Target:** Incremental subscribers acquired and cancellations prevented per title, by segment, and the estimated substitutability of each title within the catalogue.
**Evaluation metric:** Estimates must be reported as intervals with the identifying assumption stated, because a contestable number that measures the right quantity beats a precise number that measures consumption. The strongest available validation is the title removal event: when a title leaves the catalogue, what happens to the subscribers who watched it is close to a clean natural experiment and occurs constantly. Segment-level results matter more than aggregate ones, since the aggregate is exactly what conceals the value of narrow content.
**Scope:** Randomising a title's availability is impossible, but randomising exposure is not — placement, artwork, promotion and notification are assignable without withholding content from anyone, and they generate real variation in who watches what. Substitutability is the question that separates a popular title from a valuable one and is estimable from what viewers watch when a similar title is unavailable. The organisational obstacle is real and should be acknowledged in the project framing: the executives who would be judged by this number usually decide whether it gets built. 4 ML engineers and 2 econometricians, 10 months.
**Data availability:** The best in any industry for volume and completeness, and among the worst for experimental design. The natural experiments are plentiful and unanalysed.

---

## 2. Content-Derived Metadata and Artwork Generation
#cnns #object-detection #large-language-models #bert #transfer-learning #semantic-segmentation #evaluation-metrics #automation

**Problem statement:** Every title needs synopses, genres, mood and theme tags, advisories, and artwork in many aspect ratios and languages, mostly produced by humans working from a supplier's synopsis against a controlled vocabulary that lags how audiences actually search. A title tagged poorly is invisible to the recommendation system regardless of its quality.

**ML task:** Multimodal tag and description generation from video, audio and subtitles, plus generation of artwork candidate variants from the title's own footage targeted at audience segments
**Input data:** Video, audio and subtitle tracks; scripts where available; existing human-assigned metadata as supervision; search query logs showing how audiences actually describe content; artwork variants and their measured click-through by segment; content advisories and their territory-specific definitions.
**Target:** Themes, tone, setting, narrative shape and advisory-relevant content tags; synopses at multiple lengths; and candidate artwork variants per aspect ratio and segment.
**Evaluation metric:** Tags are judged by downstream discovery — whether titles tagged by the system are surfaced and watched more than those tagged by the existing process — not by agreement with the existing human labels, which are the thing being improved on. For artwork, click-through against the supplier-provided variants in the platform's existing personalisation test harness, which already exists and makes this directly measurable.
**Scope:** Artwork generation is a natural extension of a capability platforms already have: they test among supplied variants, and generating candidates from the title's own footage simply widens the pool being tested. Advisory verification from the video is a classification task currently performed by a person watching with a checklist against territory-specific definitions. Subtitle quality checks — timing, reading speed, line breaks, character limits — are mechanical and are done by watching. 3 ML engineers, 7 months.
**Data availability:** Excellent. Content, existing metadata and artwork performance are all internal, and the personalisation test harness provides the evaluation loop.

---

## 3. Event Demand Forecasting and Device-Cohort Anomaly Detection
#time-series-forecasting #change-point-detection #gradient-boosting #k-means-clustering #confidence-intervals #evaluation-metrics #worker-facing #workflow-orchestration

**Problem statement:** A premiere or live event concentrates demand into minutes across a delivery chain the platform only partly controls, and alerting cannot distinguish a successful surge from a degradation. Most incidents affect a subset of device types — one manufacturer's older firmware — and are detected only once they become a general alarm.

**ML task:** Concurrent stream forecasting per event with uncertainty, and quality-of-experience anomaly detection segmented by device cohort, CDN and region
**Input data:** Historical event traffic curves by title type, region and device; marketing spend and pre-release engagement; comparable prior titles; time zone patterns; per-device-cohort quality-of-experience telemetry including startup time, rebuffer ratio and bitrate; CDN and origin health; DRM and ad server latency; client version distribution; historical incidents with causes and resolutions.
**Target:** Forecast peak concurrency with intervals by region and device, and early detection of quality degradation localised to a layer and a cohort.
**Evaluation metric:** For forecasting, quantile accuracy at the upper tail rather than mean error, since capacity planning needs a bound it can provision against. For anomaly detection, lead time before customer-visible impact and before social media reporting — the latter being the real-world detection benchmark this function is measured against, and one it frequently loses to.
**Scope:** Device-cohort monitoring as a first-class dimension is the highest-value change: a quality divergence in one manufacturer's cohort is the earliest available signal and is currently buried in aggregates. Modelling normal per event type rather than applying a global threshold is what makes alerting usable during a premiere. Automated root cause localisation across CDN, origin, DRM, ad server and client — inferable from correlated telemetry — replaces engineers on a call comparing dashboards. 2 ML engineers, 5 months.
**Data availability:** Excellent. Quality-of-experience telemetry is collected at enormous volume; incident history exists in ticketing and chat and requires structuring.

---

## 4. Ad Inventory Forecasting and Cross-Source Frequency Management
#time-series-forecasting #convex-optimization #gradient-boosting #confidence-intervals #evaluation-metrics #feature-engineering #workflow-orchestration #revenue-impact

**Problem statement:** Ad-supported tiers must forecast impressions by segment weeks ahead against a content calendar that changes, then allocate them under guarantee, pacing, competitive separation and frequency constraints. Frequency capping fails visibly because each demand source caps within its own view, and viewers see the same advertisement repeatedly in a single session.

**ML task:** Segment-level impression forecasting coupled to content release schedules, plus constrained allocation with unified cross-source frequency state
**Input data:** Historical viewing by segment, daypart and device; content release calendar and prior title audience sizes; guaranteed campaign commitments, pacing and targeting; programmatic demand and clearing prices; competitive separation rules; per-viewer exposure across platform-sold, programmatic and third-party demand; ad load and completion by pod position; retention and viewing outcomes at different ad loads.
**Target:** Impressions available by segment and period with uncertainty, and an allocation satisfying constraints while maximising yield under a unified frequency cap.
**Evaluation metric:** Forecast accuracy at the segment level where guarantees are made, since aggregate accuracy hides the segments that under-deliver and trigger make-goods. For frequency, the honest metric is viewer-level exposure distribution — the proportion of sessions where a viewer saw the same creative more than a stated number of times — which is currently unmeasurable because no single system holds the full view and is the entire problem.
**Scope:** Unified cross-source frequency state is architecturally possible and organisationally awkward, and is the most visible viewer experience failure in ad-supported streaming. Inventory forecasting is coupled to the title audience question from the first opportunity, one layer removed. Ad load optimisation against long-run retention rather than immediate revenue requires an experiment spanning months, which is why the industry consistently measures the immediate effect and not the deferred one. 2 ML engineers and 1 operations researcher, 6 months.
**Data availability:** Viewing and delivery data are complete internally. Cross-source exposure requires an identity join the platform can perform and has not prioritised.
