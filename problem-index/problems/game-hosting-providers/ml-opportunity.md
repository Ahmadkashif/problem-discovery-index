# Machine Learning Opportunities — Game Hosting Providers

**Industry:** [[game-hosting-providers|Game Hosting Providers]]
**Derived from:** [[problems/game-hosting-providers/high-impact|High Impact]], [[problems/game-hosting-providers/low-impact-1|Low Impact 1]], [[problems/game-hosting-providers/low-impact-2|Low Impact 2]], [[problems/game-hosting-providers/worker-life-1|Worker Life 1]], [[problems/game-hosting-providers/worker-life-2|Worker Life 2]]

---

## 1. Launch and Event Concurrency Forecasting Under Asymmetric Loss
#time-series-forecasting #recurrent-forecasting #bayesian-inference #confidence-intervals #probability-distributions #convex-optimization #gradient-boosting #evaluation-metrics

**Problem statement:** Concurrency can multiply within an hour in specific regions, capacity must be committed in advance, and the forecast is a studio's business estimate multiplied by a margin someone chose. Under-provisioning at launch is close to unrecoverable; over-provisioning is merely expensive.

**ML task:** Predict the distribution of concurrency by region and hour for a launch from pre-release signals pooled across many titles, and for events from the title's own history
**Input data:** Wishlist volume and velocity, preorder counts, genre, platform mix, marketing spend, announced streamer participation, regional interest indicators; realised concurrency curves from previous launches across the provider's customer base; for events, the title's own event history with type, promotion, rewards and timing.
**Target:** The concurrency distribution by region and hour, not the peak.
**Evaluation metric:** The evaluation must be against an asymmetric loss reflecting the real cost ratio — a queued player at launch and an idle instance are not commensurable, and a symmetric error metric will select the wrong model. Report quantile calibration specifically in the upper tail, since that is the region the provisioning decision reads. Regional calibration matters as much as total: correct aggregate capacity distributed wrongly produces a queue in one region and idle fleets in another, and latency constraints mean it is not fungible.
**Scope:** No single studio has enough launches to fit this; a provider hosting many titles is the natural builder and this is its structural advantage. The event-level version is a within-title forecasting problem that is immediately achievable and that most teams currently approach as a lookup of the last comparable event. 2 ML engineers, 6-9 months.
**Data availability:** Realised concurrency is complete inside the provider. Pre-launch signals sit with studios and storefronts and require a structured ask nobody currently makes.

---

## 2. Measured Exchange Rates Between Match Quality, Wait and Latency
#causal-inference #bayesian-inference #markov-decision-processes #confidence-intervals #convex-optimization #gradient-boosting #hypothesis-testing #evaluation-metrics

**Problem statement:** Every matchmaker trades quality against wait against latency using hand-set weights, and the currency of that trade — whether the player has a good session and queues again — is measured by almost nobody. Queue length is visible and complained about; churn from bad matches is not.

**ML task:** Estimate the causal effect of additional queue time, skill mismatch magnitude and latency on session quality and requeue behaviour, and use the resulting exchange rates to set matchmaking weights per title and mode
**Input data:** Match assignment records with wait time, skill estimates and their uncertainty, allocated region and measured latency; match outcomes including closeness, early quits and completion; subsequent requeue and session behaviour; player tenure and history; randomised or naturally varying assignment where available.
**Target:** Probability the player queues again in the same session and in the following days, and session-level quality indicators.
**Evaluation metric:** This requires genuine experimental variation — observational analysis is severely confounded, since players who wait longer are matched differently for reasons that predict their behaviour. Report the exchange rates with intervals and per mode, because tolerance for mismatch and sensitivity to latency differ enormously between a competitive shooter and a cooperative title, and a single weighting is wrong in most modes. Evaluate the new-player segment separately; they are the population the current bias toward short queues damages most and the one whose first sessions determine retention.
**Scope:** Rating uncertainty should enter the matching rather than be discarded — matching on the distribution rather than the point, and being conservative where estimates are uncertain, is the direct fix for the new-player case. Low-population hours and small regions need the exchange rates rather than a static rule tuned at peak. 2 ML engineers plus a causal specialist, 9-12 months.
**Data availability:** Complete and exceptionally detailed. The missing ingredient is deliberate experimental variation.

---

## 3. Cross-Title Network Degradation Detection and Path Attribution
#change-point-detection #graph-neural-networks #gradient-boosting #bayesian-inference #confidence-intervals #evaluation-metrics #data-integration #time-series-forecasting

**Problem statement:** A degradation anywhere in a long chain produces the same player experience, each party can show its own component is healthy, and problems affecting thousands of players on one network in one city at one hour persist for weeks as individually unresolvable tickets.

**ML task:** Detect correlated quality anomalies across unrelated titles by network, geography and time, and localise degradations to a component by joining client, server and path telemetry
**Input data:** Client-side network telemetry — jitter, tail latency, packet loss patterns — across every title the provider hosts; server-side metrics; allocated region and route; network identity and geography; independent path measurements; support ticket text and timing.
**Target:** The component responsible for a degradation, validated against confirmed root causes.
**Evaluation metric:** Detection lead time against when the problem was actually identified, which today is frequently by the player community rather than by any operator — that gap is the entire value. For localisation, accuracy against confirmed causes, reported by component, and with an explicit "insufficient evidence" outcome that the system uses rather than guessing, because a confident wrong attribution sends a support team in the wrong direction for days.
**Scope:** Cross-title population detection is achievable by a provider alone and is the immediately valuable half: a degradation on one internet provider in one metropolitan area appears as a correlated anomaly across unrelated games, a signal no individual studio can see. Full path attribution requires cooperation across companies and is the version that ends the dispute. Existing web performance tooling does not transfer — it measures throughput and completion, not jitter and tail latency at interactive timescales. 2 ML engineers plus a network specialist, 6-9 months.
**Data availability:** Client telemetry exists in most modern titles and is not pooled. Path measurement can be added. The layers belong to different companies, which is the structural barrier.

---

## 4. Fleet Placement and Cost Optimisation Under Uncertain Demand
#convex-optimization #bayesian-optimization #markov-decision-processes #time-series-forecasting #confidence-intervals #gradient-boosting #evaluation-metrics #revenue-impact

**Problem statement:** Compute is the dominant cost in this business, capacity is held across dozens of regions against uncertain demand, and placement decisions are made with static rules and safety margins rather than against the forecast distribution.

**ML task:** Optimise fleet placement, instance mix and buffer sizing across regions against the predictive demand distribution, the latency constraints on cross-region play, and the availability of spot and preemptible capacity
**Input data:** Demand forecasts by region and hour with uncertainty; instance pricing including spot markets and their interruption rates; provisioning and allocation latency by region and instance type; latency matrices between regions and player populations; graceful degradation options and their experience cost.
**Target:** Total cost subject to a stated service level on queue time and latency.
**Evaluation metric:** Cost at a fixed service level, compared against the incumbent static-margin policy — and the service level must be defined in player terms, not server terms, since idle capacity in the wrong region satisfies a utilisation target and fails a player. Report the frequency and duration of service level breaches, not just the average, because the entire risk in this domain is in the tail. Spot interruption handling must be evaluated under realistic interruption patterns rather than average rates.
**Scope:** Reducing the cost of being wrong — faster provisioning, multi-region buffering, graceful degradation, a queue that manages expectations rather than failing — often delivers more than a better forecast, because it shortens the exposure window and changes the loss asymmetry itself. 2 ML engineers plus an infrastructure specialist, 6-9 months.
**Data availability:** Complete inside the provider. Pricing and interruption data is available from the underlying cloud providers.
