# AI Agents & Platform Opportunities — Mobile Game Publishers

**Industry:** [[mobile-game-publishers|Mobile Game Publishers]]

---

## 1. Prototype Funnel Platform
#ai-platform #survival-analysis #bayesian-inference #confidence-intervals #gradient-boosting #causal-inference #evaluation-metrics #worker-facing

**Concept:** A platform that turns a kill funnel into a learning system. It derives advancement thresholds from the publisher's own outcome history per genre and prototype completeness rather than applying inherited folklore across the portfolio; it reports every kill decision as a probability with an interval and states plainly when a prototype missed by less than the sampling error; and it runs a funded randomised allowance advancing a small subset of below-threshold concepts, which is the only way anyone learns what the funnel is missing. It ranks on probability of being a portfolio outlier rather than on expected median outcome, because that is where the returns are and the two orderings differ sharply.

**Inputs:** Prototype early metrics with acquisition source and test geography; prototype characteristics and mechanic family; full historical prototype outcomes including killed concepts; realised long-run revenue for scaled titles; randomised advancement assignments.

**Outputs / Actions:** Genre-conditioned advancement probabilities with intervals. A measured false negative rate — the number no publisher currently has about its own funnel. Kill decisions returned to the team as a diagnosis: where players stopped, whether the core loop was reached, what the retention curve's shape says, and whether the test conditions rather than the concept produced the result. Portfolio-level findings about which mechanics and first-session structures survive, which is the craft knowledge this funnel should be producing and currently leaves in the heads of whoever has been there longest.

**Why now:** The economics changed — acquisition costs rose substantially after tracking restrictions and the industry moved to deeper hybrid-monetised games — while the three-day kill metrics designed for a shallower, cheaper era did not move with them.

**Market:** Hypercasual and hybridcasual publishers running high-volume prototype funnels, the external studios supplying them, and the publishing arms of larger operators using the same model.

---

## 2. Monetisation and Player Welfare Platform
#ai-platform #markov-decision-processes #survival-analysis #change-point-detection #causal-inference #confidence-intervals #compliance #revenue-impact

**Concept:** A platform that optimises hybrid monetisation on the objective that actually matters and reports a second number beside it. It sets ad exposure and purchase pressure jointly and per player — using the purchase propensity model publishers already run for offer targeting — against total revenue over 90 to 180 days net of the retention hazard, rather than against whichever channel a given test happened to measure. And it reports a population-level welfare metric alongside revenue for every proposed change: the share of revenue arriving through rapid escalation, unusual-hour concentration, purchases immediately following losses or progression blocks, and sharp departures from a player's own baseline.

**Inputs:** Ad and purchase events with placement, timing and response; session structure and progression state; retention and churn timing; refund and chargeback requests; self-imposed limit usage; experiment assignments varying both monetisation channels together.

**Outputs / Actions:** Per-player ad and offer configuration on a joint long-horizon objective. A welfare metric in the same review where the monetisation decision is taken, which is the mechanism by which it changes what ships. Shippable interventions that are not refusals — spend pacing, easily-found self-set limits, suppression of high-pressure offers for distress signatures — with their measured revenue cost, which is frequently smaller than assumed and is exactly the evidence an internal argument requires. The metric is population-level by construction and does not produce individual diagnoses, which this data cannot support.

**Why now:** Hybrid monetisation became the default structure without the measurement to configure it, and regulatory attention to randomised reward mechanics and offer design has been increasing in several jurisdictions. Self-regulation with a published measure is the version most likely to be credible.

**Market:** Free-to-play publishers of every size, the mediation and LiveOps platforms serving them, and the trade bodies negotiating with regulators who currently have no measurement to offer.

---

## 3. Soft Launch Readout Agent
#ai-agent #causal-inference #transfer-learning #bayesian-inference #confidence-intervals #gradient-boosting #evaluation-metrics #automation

**Concept:** An agent that makes the last checkpoint before a global launch mean what everyone assumes it means. It estimates the market-pair transfer relationship for retention, monetisation and acquisition cost from the publisher's own portfolio of titles that went through both stages, adjusts for the composition difference between a low-volume soft launch cohort and a scaled acquisition mix — which is probably where most of the current error lives — and chooses test markets to maximise information about this title's specific uncertainty rather than by convention.

**Inputs:** Soft launch cohort metrics by market, genre and acquisition source; the publisher's historical soft-launch-to-scale pairs; market covariates including device mix, payment friction and competitive landscape; planned scale acquisition mix; the title's specific open questions.

**Outputs / Actions:** A scaled-performance projection with intervals, per market and genre rather than pooled. An explicit cohort composition adjustment with its size stated, so the readout distinguishes a game that will not scale from a test that was not representative. Market recommendations chosen for what they would resolve. A clear flag on the recurring failure mode — validated in soft launch, did not scale — when the adjusted numbers predict it.

**Why now:** Soft launch precedes a publisher's largest acquisition commitments and is read against informal multipliers that have never been estimated, at a moment when acquisition costs have risen enough that getting the scale decision wrong is materially more expensive than it was.

**Market:** Mobile publishers of any scale, the studios they publish for, and the user acquisition agencies whose budget recommendations rest on the same unvalidated readout.
