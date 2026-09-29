# Machine Learning Opportunities — Live Commerce Platforms

**Industry:** [[live-commerce-platforms|Live Commerce Platforms]]
**Derived from:** [[problems/live-commerce-platforms/high-impact|High Impact]], [[problems/live-commerce-platforms/low-impact-1|Low Impact 1]], [[problems/live-commerce-platforms/low-impact-2|Low Impact 2]], [[problems/live-commerce-platforms/worker-life-1|Worker Life 1]], [[problems/live-commerce-platforms/worker-life-2|Worker Life 2]]

---

## 1. Real-Time Stream Understanding for Matching
#cnns #transformers #contrastive-learning #gradient-boosting #evaluation-metrics #confidence-intervals #k-nearest-neighbors #revenue-impact

**Problem statement:** A stream is a permanent cold start — no interaction history, a title typed before it began, and content that changes continuously as the host moves between items. Recommendation machinery built for persistent catalogues has nothing to match on, and an unwatched stream is not a delayed sale but a seller who does not return.

**ML task:** Continuous extraction of stream state from video, audio and chat into a live feature representation, feeding a matching model that re-evaluates as the stream changes
**Input data:** Video frames and audio transcription at low latency; chat text and volume; the host's stated product list and historical catalogue; viewer session behaviour including entry, dwell and exit; purchase events with timing relative to stream content; host historical performance by category.
**Target:** Viewer engagement and purchase given a match, evaluated within the stream's lifetime.
**Evaluation metric:** Purchase conversion per surfaced stream rather than watch time, since the inherited short-form video objective optimises the wrong thing and the two diverge. Report seller-side outcomes separately — the share of streams reaching a viewership floor, and new seller retention — because engagement-optimised ranking starves small sellers and destroys the supply the marketplace depends on.
**Scope:** The latency budget is the engineering constraint: understanding must run within seconds across thousands of concurrent streams, which forces choices about sampling rate and model size. Matching on current stream state rather than on stream identity is the design shift, and it creates a natural re-entry recommendation when a stream moves to something a viewer wants. Session-level intent inference — shopping for something specific versus browsing — should modulate what is surfaced and is inferable from the first few interactions. 3-4 ML engineers, 7 months.
**Data availability:** Streams, chat and purchase events are captured completely and constitute the richest behavioural commerce data anywhere. Frame-level content is expensive to retain and is usually sampled, which limits retrospective training.

---

## 2. Commerce-Specific Live Violation Detection
#cnns #transformers #bert #object-detection #evaluation-metrics #confidence-intervals #compliance #worker-facing

**Problem statement:** General content classifiers cover general harms and not the violations that matter in live commerce — counterfeits held to a camera, prohibited health or safety claims in speech, manufactured scarcity, undisclosed promotional relationships. Detection must run continuously at low latency, and a violation between samples is broadcast to the full audience.

**ML task:** Multimodal detection of commerce-specific violations across video, audio and chat, with risk-adaptive sampling and human queue prioritisation
**Input data:** Video and transcribed audio; chat text and sentiment; product listings and claims; host history and prior flags; confirmed violations with moderator decisions; category-specific prohibited claim taxonomies; regulatory claim rules by product category.
**Target:** A confirmed policy violation as adjudicated by a moderator, with its type and timestamp.
**Evaluation metric:** Recall on serious violations at a false positive rate that does not repeatedly interrupt legitimate sellers — the trade-off is sharper here than in recorded moderation because a false positive stops someone's income live in front of an audience. Report detection latency from utterance to flag, since the whole value is acting before the violation reaches its full audience.
**Scope:** Risk-adaptive sampling is the practical lever: analysing every frame of every concurrent stream is uneconomic, and increasing sample rate on higher-risk hosts, categories and moments — a chat sentiment shift, an unusual claim — covers far more of the actual risk at the same cost. Graduated interventions must exist for detection to be useful, since a system that can only recommend ending a stream will be tuned so conservatively that it catches little. Prohibited claim detection is genuinely category-specific and regulatory, which makes it a taxonomy problem before a modelling one. 3 ML engineers plus a trust and safety specialist, 6 months.
**Data availability:** Confirmed violations with moderator decisions exist and are heavily skewed toward what current detection already catches, which biases training toward known patterns.

---

## 3. Burst Prediction and Fair Allocation
#time-series-forecasting #gradient-boosting #optimization-fundamentals #confidence-intervals #evaluation-metrics #hypothesis-testing #workflow-orchestration

**Problem statement:** A host announces a limited item and hundreds of purchase attempts arrive within seconds against an absolute inventory constraint. Ticketing solved this for scheduled events with preparation; live commerce has thousands of unannounced micro-drops a day, and allocation fairness is currently decided implicitly by whose request arrives first.

**ML task:** Predicting an imminent demand burst from stream signals, and defining allocation policy explicitly under contention
**Input data:** Chat volume and sentiment trajectory; the host's spoken introduction and framing; item characteristics including scarcity and price; current viewer count and its trend; the host's history with comparable items; historical burst events with realised attempt volume and timing.
**Target:** Purchase attempt volume in the seconds following a drop announcement.
**Evaluation metric:** Lead time on correctly predicted bursts — even a few seconds is enough to pre-warm capacity and pre-authorise — and precision, since unnecessary pre-warming costs infrastructure. For allocation, the operational measures are oversell rate, which should be zero, and viewer-perceived fairness, which is measurable through complaint and chat sentiment following drops under different policies.
**Scope:** Allocation fairness is a policy choice with real consequences that is currently made by default. Speed-based allocation rewards network latency and bots; randomising among those who acted within a window is defensible and testable; loyalty weighting is possible and contentious. The platform should choose deliberately and be able to explain the choice to an audience watching in real time, because perceived unfairness in a live chat is corrosive in a way a failed checkout elsewhere is not. Bot resistance matters more here than in ordinary commerce. 2 ML engineers plus a platform engineer, 4 months.
**Data availability:** Attempt-level telemetry around drops is captured. Historical burst events are abundant. Chat and audio signals preceding drops are available where retained.

---

## 4. Host Assistance — Chat Triage and Show Guidance
#large-language-models #bert #transformers #gradient-boosting #time-series-forecasting #evaluation-metrics #automation #worker-facing

**Problem statement:** A host presents, sells, reads a fast-moving chat, tracks inventory, runs auctions and moderates simultaneously for hours, usually alone. Most chat is repetitive — price, size, shipping, availability — and is answered by the person who is also performing.

**ML task:** Chat classification and automated response from product data, plus next-item recommendation conditioned on current audience and remaining inventory
**Input data:** Chat messages with timing; product listings, prices, shipping terms and stock; the host's own prior answers as style reference; live viewer composition and arrival patterns; item-level sell-through during the show; comparable historical shows by this host and by similar hosts; auction state.
**Target:** Correctly answered routine questions without host involvement, and the next item that maximises engagement and sell-through given who is watching now.
**Evaluation metric:** The proportion of chat handled without host attention at an accuracy level that does not create wrong-answer incidents — a mis-stated price or shipping term in a live chat is a commitment the host has to honour. For show guidance, sell-through and viewer retention against the host's own baseline, measured across comparable shows.
**Scope:** Accuracy on commitments is the binding constraint: automated answers must draw strictly from structured product data and escalate anything requiring judgement, because an incorrect stated price in front of an audience is a real obligation. Next-item recommendation is where the platform genuinely knows more than the host mid-show, since it can see who is watching now and what comparable audiences bought. Live inventory presented on the host's own view removes the hand-written note that most hosts actually use. 2 ML engineers, 4-5 months.
**Data availability:** Chat, product data and purchase events are complete. The host's own prior answers provide a natural style corpus. Comparable-show benchmarking requires cross-host data the platform holds and individual hosts cannot see.
