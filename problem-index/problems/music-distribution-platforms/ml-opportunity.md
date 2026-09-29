# Machine Learning Opportunities — Music Distribution Platforms

**Industry:** [[music-distribution-platforms|Music Distribution Platforms]]
**Derived from:** [[problems/music-distribution-platforms/high-impact|High Impact]], [[problems/music-distribution-platforms/low-impact-1|Low Impact 1]], [[problems/music-distribution-platforms/low-impact-2|Low Impact 2]], [[problems/music-distribution-platforms/worker-life-1|Worker Life 1]], [[problems/music-distribution-platforms/worker-life-2|Worker Life 2]]

---

## 1. Recording-to-Composition Matching as Graph Entity Resolution
#graph-neural-networks #bert #word-embeddings #k-nearest-neighbors #gradient-boosting #evaluation-metrics #feature-engineering #compliance

**Problem statement:** A stream generates a recording royalty and a composition royalty administered by entirely separate systems with no authoritative link between them. Where the link is missing, the money accumulates unmatched and is eventually distributed by market share to the largest rights holders rather than to the writers who are owed it — and the writers most likely to be unmatched are the ones least able to file a claim.

**ML task:** Entity resolution over a graph of writers, works, recordings, publishers and societies, with audio-based composition identification for cases metadata cannot resolve
**Input data:** Recording metadata with ISRCs, titles, artists and contributors; composition registrations with ISWCs, writers, publishers and splits across societies; co-writing relationships and catalogue co-occurrence; publisher affiliations; audio for melodic similarity; historical confirmed matches and confirmed rejections; unmatched pool contents.
**Target:** A confidence-scored link between each recording and its underlying composition, with the writer identities resolved.
**Evaluation metric:** Precision at the auto-pay threshold is the binding constraint, because a wrong match pays the wrong writer, which is materially worse than leaving money unmatched and is the reason current processes are conservative. Report recall separately at several confidence tiers, since the value of the work is entirely in the ambiguous middle band that is currently sent straight to the pool. Validate against a held-out set of confirmed matches, stratified by catalogue size, because performance on major-label repertoire tells you nothing about the population that is actually unmatched.
**Scope:** The cheapest and highest-leverage intervention is not the model at all: capturing the link at upload, when the distributor is talking to the one person who knows both the recording and the composition, costs a better form and a validation step and is nobody's product requirement. Graph resolution on corroborating edges is far stronger than the name matching most current processes use. Audio-based identification handles covers, live versions and re-recordings that metadata cannot. Confidence tiering with a claimant review path replaces a binary matched-or-pooled outcome. 3 ML engineers, 8 months.
**Data availability:** Distributors hold the largest corpora of recordings matched to compositions in existence and use them to validate their own uploads. Society registration data is partially accessible and inconsistently formatted.

---

## 2. Distributor-Side Manipulation Signals and Targeting Separation
#graph-neural-networks #gradient-boosting #k-means-clustering #change-point-detection #autoencoders #evaluation-metrics #compliance #feature-engineering

**Problem statement:** Artificial streams draw from a fixed pool, so the fraud is a transfer from every legitimate artist. Enforcement now lands on distributors as financial penalties, which they pass to artists who may have bought promotion that turned out to be bots, may have been maliciously targeted by a competitor, or may have done nothing at all — and who cannot contest a detection they are not shown.

**ML task:** Anomaly and relationship detection over distributor-side account, upload and payout signals, with separation of participation from malicious targeting
**Input data:** Account creation patterns and cross-account relationships; upload cadence and catalogue composition; payout destinations and their clustering; promotional service usage where disclosed; stream velocity and geography patterns per release; historical penalties with what preceded them and whether they were reversed; takedown and restriction history.
**Target:** A pre-penalty risk signal per release and per account, and a classification distinguishing artist-originated manipulation from external targeting.
**Evaluation metric:** The useful measure is lead time before a service-imposed penalty, validated against the distributor's own penalty history — a warning that arrives after the charge is worthless. For the targeting separation, precision matters enormously because the output determines whether a penalty is passed to an artist or contested on their behalf, and the cost of wrongly judging an artist a participant falls on someone who may have no recourse.
**Scope:** Distributors hold signals the streaming services do not — account relationships, payout destinations, upload behaviour — and largely do not model them. The separation of targeting from participation is the part that makes the enforcement regime just rather than merely effective: artificial streams originating from accounts with no relationship to an artist's own promotional history are a different case, and the distributor holds some of that evidence. Every penalty, reversal and preceding pattern is a labelled example that accumulates and goes unused. 2 ML engineers, 5 months.
**Data availability:** Complete internally at the distributor. The streaming services' detection is opaque by necessity, which means this must be built as an independent signal rather than as a reconstruction.

---

## 3. Pre-Delivery Validation and Rejection Learning
#bert #large-language-models #object-detection #cnns #k-nearest-neighbors #evaluation-metrics #data-integration #automation

**Problem statement:** Every streaming service layers its own ingestion rules on top of DDEX, rejections arrive asynchronously with unclear reasons, and an artist who promoted a Friday release and was rejected on Wednesday has a problem measured in hours. The distributor holds a large history of rejections and their eventual corrections and uses it to write help articles.

**ML task:** Deep pre-delivery validation against per-service specifications, artwork content classification, and learning from the rejection-to-correction corpus
**Input data:** Historical deliveries with rejections, reasons and the corrections that resolved them; per-service published specifications; title, contributor and explicit-flag conventions; artwork images; rejection rates by defect type over time.
**Target:** A pre-delivery defect report with the specific correction, expressed in language a non-specialist understands, and detection of undisclosed specification changes.
**Evaluation metric:** The proportion of eventual rejections caught before delivery, measured per service, and the false positive rate — blocking a valid release costs the artist their date, so the threshold must favour delivery on anything ambiguous. For specification change detection, lead time relative to the service's own notification, which is often absent entirely.
**Scope:** Artwork content checking is a vision problem handled today by manual review or by the service's rejection: logos, text overlays, social handles, prices and prohibited imagery are all detectable. Specification drift is visible in the distributor's own rejection telemetry before any notice arrives. The highest-value output is upload-time guidance in plain language, since correcting a defect while the artist is still in the form beats every downstream process. 2 ML engineers, 4 months.
**Data availability:** Excellent and internal. Rejection histories provide a directly supervised mapping from defect to fix with no annotation cost.

---

## 4. Catalogue Integrity: Fingerprinting and Artist Disambiguation
#cnns #graph-neural-networks #bert #k-nearest-neighbors #k-means-clustering #evaluation-metrics #worker-facing #compliance

**Problem statement:** Reviewers judge impersonation, infringement and metadata fraud on very large daily upload volumes, in seconds, against patterns that change every few months. Content identification catches exact matches while re-recordings, pitch-shifted uploads and re-uploaded stems pass, and two artists can legitimately share a name.

**ML task:** Robust audio fingerprinting against the full catalogue, graph-based artist name disambiguation, and account-level fraud pattern detection
**Input data:** Full catalogue audio; upload audio; existing artist entities with catalogues, identifiers and audience data; artist name strings and their historical disambiguation decisions; artwork images; account creation, upload cadence, catalogue composition and payout destination; historical review decisions including reversals.
**Target:** Match candidates robust to pitch, tempo and re-recording; an evidenced assessment of whether a new upload's artist name conflicts with an existing entity; and account-level risk.
**Evaluation metric:** For fingerprinting, recall on deliberately transformed known tracks — pitch-shifted, tempo-adjusted, re-recorded — since exact matching is already solved and the transformations are where the gap is. For disambiguation, the metric must be reported in both directions with the asymmetry named: wrongly blocking a legitimate artist costs them a release date and their trust, wrongly approving an impersonation costs a takedown and a clawback, and both are bad in different ways.
**Scope:** Account-level detection is where the leverage is, because fraud arrives as an account with a characteristic pattern rather than as a single release, and human review is currently directed release by release. Risk-based routing that lets low-risk uploads from established accounts pass with sampling is what makes the function scale against volumes that grow every year. Precedent retrieval including reversals is the only mechanism by which this role accumulates knowledge rather than relearning it each time patterns shift. 3 ML engineers, 6 months.
**Data availability:** Catalogue audio and review histories are internal and large. Artist entity data is partly external and partly derivable from the distributor's own catalogue.
