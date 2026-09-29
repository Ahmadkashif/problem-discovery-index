# Machine Learning Opportunities — Audio Adtech Networks

**Industry:** [[audio-adtech-networks|Audio Adtech Networks]]
**Derived from:** [[problems/audio-adtech-networks/high-impact|High Impact]], [[problems/audio-adtech-networks/low-impact-1|Low Impact 1]], [[problems/audio-adtech-networks/low-impact-2|Low Impact 2]], [[problems/audio-adtech-networks/worker-life-1|Worker Life 1]], [[problems/audio-adtech-networks/worker-life-2|Worker Life 2]]

---

## 1. Exposure Modelling: Estimating Who Actually Reached the Advertisement
#survival-analysis #gradient-boosting #bayesian-inference #confidence-intervals #probability-distributions #time-series-forecasting #evaluation-metrics #revenue-impact

**Problem statement:** The channel's currency is the download, which is a file request. Whether a listener played the episode, and whether they reached the position where the advertisement sits, is not measured — though the telemetry to measure it is collected by every platform player.

**ML task:** Estimate the listen-through curve per show, episode type and audience segment, and convert a download into a probability of exposure at each ad position
**Input data:** Position-in-episode listening telemetry from platform players and hosting integrations; skip and seek events; completion rates; episode length, format and ad marker positions; show, category and audience segment; device and app type where observable.
**Target:** Probability that a given download resulted in the listener reaching a given ad position.
**Evaluation metric:** Calibration against direct measurement on the subset of listening where full telemetry exists, and — the more convincing test — agreement with promotional code redemption rates across shows, which are an independent signal of real exposure. Report per-position, because the entire commercial consequence is that mid-rolls and post-rolls in long episodes reach far fewer people than the download count implies, and the size of that gap is the finding.
**Scope:** The measurable share of listening is partial: platform players expose telemetry, open RSS consumption largely does not, and the platforms have a commercial reason not to publish the result. The model must therefore be explicit about what population its estimate covers and how it extrapolates to the rest — extrapolating silently is how this becomes another unverified number. 2 ML engineers, 4-6 months.
**Data availability:** Excellent inside a platform, poor outside it. This is the clearest case in the industry where the capability and the incentive sit in the same place and point in opposite directions.

---

## 2. Calibrating IP-Match Attribution
#bayesian-inference #probability-distributions #confidence-intervals #hypothesis-testing #gradient-boosting #causal-inference #evaluation-metrics #compliance

**Problem statement:** Audio conversions are attributed by matching the household IP that requested an episode against a later site visit. Carrier-grade NAT, VPNs, IPv6 rotation, cross-device and out-of-home listening all corrupt the match, and no provider publishes a false-match rate.

**ML task:** Estimate match precision and recall by segment, and replace binary attribution with a calibrated match probability
**Input data:** IP-level request and visit records with their timing; IP characteristics — carrier-grade NAT concentration, VPN and proxy indicators, address stability, geography; independent conversion signals such as promotional codes, vanity URLs and survey recall; holdout and PSA comparisons where available.
**Target:** Whether the matched visit was made by a person who actually heard the advertisement — approximated using the independent signals as partial ground truth.
**Evaluation metric:** Precision estimated against promotional code and vanity URL evidence, reported by segment, because the failure modes concentrate sharply: mobile-heavy and shared-network audiences match very differently from fixed-line ones. Publish an overall correction factor with an interval, and expect it to be uncomfortable — an attribution product that survives disclosing its own error rate is a different product from one that does not.
**Scope:** Partial ground truth is the central difficulty; promotional codes are themselves a biased sample of conversions, skewing to price-sensitive and highly-engaged listeners. The honest output is a probability with segment-specific uncertainty rather than a corrected count presented as fact. 2 ML engineers plus a measurement specialist, 6-9 months.
**Data availability:** Request and visit data exist inside measurement providers. Independent validation signals are scattered across advertisers and must be gathered deliberately.

---

## 3. Back-Catalogue Inventory Forecasting and Constrained Allocation
#time-series-forecasting #exponential-smoothing #recurrent-forecasting #convex-optimization #gradient-boosting #confidence-intervals #evaluation-metrics #revenue-impact

**Problem statement:** Dynamic insertion makes every past episode sellable, so inventory is the sum of future downloads across an entire catalogue at several positions, segmented by targeting — and most publishers forecast it with a growth assumption on last month's number.

**ML task:** Forecast download volume per episode cohort with show-specific decay and seasonality, aggregate to sellable inventory by position and targeting segment, and solve the allocation of booked campaigns against that stochastic supply
**Input data:** Historical downloads by episode and day since publication; show format, cadence and category; publication schedule; seasonality and known events; guest and topic features that drive back-catalogue spikes; booked campaign requirements including targeting and delivery obligations.
**Target:** Future download volume per episode cohort and position, and a feasible allocation that meets delivery obligations.
**Evaluation metric:** Forecast error at the horizons the yield decision actually uses — typically 30 to 90 days — with intervals, since the decision to sell forward or hold for spot is a decision under uncertainty and a point forecast makes it unreasonable. For allocation, measure make-goods and expired unsold inventory before and after, which are the two ways forecast error converts into lost margin.
**Scope:** Decay curves differ fundamentally between daily news, weekly interview and evergreen narrative formats, and a single pooled model is wrong for each differently — show-level or format-level fitting is the requirement. Back-catalogue spikes are driven by external events and are largely unforecastable, which the intervals must reflect rather than smooth over. 2 ML engineers, 4-6 months.
**Data availability:** Complete within any hosting platform. This is the most immediately tractable item in this industry.

---

## 4. Treatment-Aware Suitability and Embedding-Based Contextual Targeting
#bert #transformers #large-language-models #contrastive-learning #word-embeddings #transfer-learning #evaluation-metrics #compliance

**Problem statement:** Transcription made audio readable and the industry built keyword blocklists with it, defunding news and current affairs in a repeat of the open web's mistake. The valuable half — finding relevant inventory across a long tail of shows — is barely developed.

**ML task:** Classify content by subject and treatment against per-advertiser policy, and learn episode embeddings that support thematic targeting beyond category taxonomies
**Input data:** Episode transcripts with speaker structure; show and episode metadata; advertiser policy documents and their labelled examples; IAB and GARM suitability taxonomies; historical exclusion decisions and any appeals.
**Target:** Whether this specific advertiser's reviewer would consider the episode unsuitable — a per-advertiser label by construction — and, for targeting, thematic similarity validated against campaign performance.
**Evaluation metric:** The essential measurement is reach cost alongside risk reduction, reported together and never separately: a suitability model that blocks more is not better, and the current generation's failure is precisely that it is evaluated on risk alone. Treatment discrimination is the specific capability to test — an episode analysing a subject versus endorsing it, which keyword matching cannot distinguish and which determines nearly every real judgement.
**Scope:** Per-advertiser policy means few-shot adaptation from a brand's examples rather than a universal classifier. Every exclusion should generate an appealable record naming the brand, the passage and the reason, so publishers can see revenue loss they currently only infer from fill rate. 2 ML engineers, 6-9 months.
**Data availability:** Transcription is cheap and accurate. Advertiser policies exist as documents and reviewer judgement; converting them into labelled examples is the first and most underestimated task.
