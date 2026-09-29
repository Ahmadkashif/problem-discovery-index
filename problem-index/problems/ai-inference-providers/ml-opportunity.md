# Machine Learning Opportunities — AI Inference Providers

**Industry:** [[ai-inference-providers|AI Inference Providers]]
**Derived from:** [[problems/ai-inference-providers/high-impact|High Impact]], [[problems/ai-inference-providers/low-impact-1|Low Impact 1]], [[problems/ai-inference-providers/low-impact-2|Low Impact 2]], [[problems/ai-inference-providers/worker-life-1|Worker Life 1]], [[problems/ai-inference-providers/worker-life-2|Worker Life 2]]

---

## 1. Correlated Demand Forecasting and Capacity Portfolio Optimisation
#time-series-forecasting #gradient-boosting #convex-optimization #confidence-intervals #evaluation-metrics #optimization-fundamentals #markov-decision-processes #revenue-impact

**Problem statement:** Accelerators are committed in advance and depreciate quickly while demand arrives in unannounced spikes. Overprovision and the margin sits idle; underprovision and the latency guarantee fails. Capacity planning treats customers as independent when their demand is correlated — launches cluster, business hours overlap, viral moments hit everyone at once — which makes the aggregate tail far fatter than any independent model predicts.

**ML task:** Hierarchical probabilistic demand forecasting per customer and model with explicit correlation structure, feeding a stochastic optimisation over the committed, reserved and spot capacity mix
**Input data:** Request volumes per customer per model at fine granularity; token counts and sequence length distributions; customer attributes, contract type and tenure; model popularity trajectories; historical spike events and their causes where known; spot market availability and reclamation history; hardware costs by procurement channel.
**Target:** The aggregate demand distribution over the planning horizon, and the capacity mix minimising expected cost subject to a guarantee-violation constraint.
**Evaluation metric:** Calibration of the aggregate demand distribution at high quantiles, which is where every decision is actually made — average accuracy is worthless here since the entire problem is the tail. Report realised cost against the guarantee violation rate as a frontier, and compare against the provider's current provisioning as the baseline.
**Scope:** Correlation is the modelling contribution and the reason naive per-customer forecasts underestimate peak requirement. New customers and newly released models have no history, which forces a hierarchical structure borrowing from comparable cohorts. Spike prediction is genuinely limited — the driver is a customer product event the provider cannot see — so the honest framing is distributional planning rather than event prediction. 3 ML engineers plus a capacity planner, 6-8 months.
**Data availability:** Request telemetry is complete and high frequency. Spike causes are rarely recorded, which limits any attempt at causal understanding. Customer product roadmaps are the missing input and are obtainable only through a pricing structure that rewards disclosure.

---

## 2. Request Footprint Prediction for Batch Composition
#gradient-boosting #logistic-regression #confidence-intervals #evaluation-metrics #optimization-fundamentals #convex-optimization #feature-engineering

**Problem statement:** Continuous batching mixes requests from multiple tenants into the same forward pass, which is where efficiency comes from and where isolation breaks. A tenant with long sequences occupies key-value cache others need; a burst fills the batch and pushes another tenant's requests later. The affected customer sees unexplained latency variance and the provider cannot even identify the cause internally.

**ML task:** Predicting a request's resource footprint before scheduling — output token count, peak key-value cache occupancy and compute time — then composing batches under per-tenant latency constraints
**Input data:** Prompt text and token count; model identity and configuration; historical output lengths for similar prompts and for this customer; sampling parameters including stop conditions and maximum tokens; realised footprints from completed requests; batch composition records with per-request latency outcomes.
**Target:** Realised output length, peak memory occupancy and total compute time per request.
**Evaluation metric:** Quantile accuracy on output length rather than mean, since the scheduler needs an upper bound it can plan against and being wrong high is far cheaper than being wrong low. The operational metric is per-tenant latency percentile compliance at a given oversubscription ratio, which is what determines how confidently the provider can share hardware.
**Scope:** Output length prediction from the prompt is the crux and is achievable with useful accuracy — prompts asking for a summary, a code block or a single word are distinguishable, and per-customer history is strongly predictive. No serving engine attempts it, which means batch composition currently proceeds blind. Interference measurement between co-located workloads is a separate and immediately useful piece requiring no prediction at all. 2-3 ML engineers plus a serving systems engineer, 5-6 months.
**Data availability:** Request and completion telemetry is complete. Batch composition records — which requests shared a forward pass — are frequently not retained, which is what makes interference attribution impossible today and is a logging change.

---

## 3. Automated Serving Configuration Search with Cross-Architecture Transfer
#bayesian-optimization #optimization-fundamentals #gradient-boosting #transfer-learning #evaluation-metrics #hypothesis-testing #confidence-intervals

**Problem statement:** Every new model architecture requires weeks of hand tuning per hardware target — parallelism strategy, batch policy, memory allocation, quantisation scheme — and the work is redone with each release. Time to serve a new architecture is a primary differentiator and it is gated by scarce performance engineers running benchmarks and applying intuition.

**ML task:** Black-box optimisation over the serving configuration space with warm starts transferred from architecturally similar models, plus task-conditioned quantisation quality assessment
**Input data:** Configuration and measured throughput, latency and memory across historical model deployments; model architecture descriptors (attention variant, parameter count, layer structure, expert routing); hardware characteristics; quantisation schemes with measured quality on benchmarks and on customer-representative tasks.
**Target:** The configuration maximising throughput subject to a latency constraint; and for quantisation, the quality cost on a given workload.
**Evaluation metric:** Performance achieved against the hand-tuned configuration an engineer would have produced, and — the metric that matters commercially — the number of benchmark evaluations required to get there, since the whole point is collapsing weeks into hours. For quantisation, quality measured on customer-representative tasks rather than on general benchmarks, which is the gap that currently makes the trade-off implicit.
**Scope:** Bayesian optimisation is well suited: the objective is cheap to evaluate relative to the search, the space is structured, and interactions between parameters are strong. Transfer is where the leverage is — architectures are variations on a small number of patterns, and the configuration for a new model in a familiar family starts close to its predecessor's. Honest quantisation quality measurement is the piece with the clearest customer-facing value, converting an implicit trade-off into a product choice. 2 ML engineers plus a performance engineer, 5 months.
**Data availability:** Benchmark results exist across every deployment and are typically recorded in engineer notebooks and dashboards rather than as a structured corpus, so assembling the history is the first task.

---

## 4. Latency Regression Detection with Version Attribution
#change-point-detection #hypothesis-testing #confidence-intervals #descriptive-statistics #gradient-boosting #evaluation-metrics #causal-inference

**Problem statement:** Latency rises and an engineer bisects across a stack where the serving engine, driver, kernel library, model build, traffic mix, batch composition and hardware generation all change independently and none is version-locked. Many investigations end with a hypothesis rather than an answer.

**ML task:** Change point detection on latency percentiles conditioned on request mix, with attribution against the stack change log using the heterogeneous fleet as a natural control
**Input data:** Per-request latency with prompt and output token counts; serving engine, driver, kernel library and model build versions per node; hardware generation and rack; batch composition; traffic mix over time; deployment and upgrade events; thermal and utilisation telemetry.
**Target:** A genuine latency regression distinguished from a mix shift, attributed to a specific stack change.
**Evaluation metric:** Detection precision and recall against engineer-confirmed historical regressions, which exist as incident records and form a natural evaluation set. False positive rate is the operational constraint — the reason percentile alerting is currently ignored is that request mix moves constantly and naive detection fires on it.
**Scope:** Conditioning on request mix is what separates this from a dashboard alert and is the first-order requirement, since a shift toward longer prompts raises latency legitimately. The fleet is a natural experiment: nodes running different versions concurrently give a clean comparison that a controlled reproduction cannot, and this is the strongest available attribution mechanism. Canary deployment for stack changes makes the comparison deliberate rather than opportunistic and prevents most regressions from reaching the fleet. 2 ML engineers, 4 months.
**Data availability:** Telemetry is abundant. Version tracking per node is inconsistent in practice, and fixing it is the prerequisite that makes attribution possible at all.
