# Machine Learning Opportunities — Marketing Attribution Vendors

**Industry:** [[marketing-attribution-vendors|Marketing Attribution Vendors]]
**Derived from:** [[problems/marketing-attribution-vendors/high-impact|High Impact]], [[problems/marketing-attribution-vendors/low-impact-1|Low Impact 1]], [[problems/marketing-attribution-vendors/low-impact-2|Low Impact 2]], [[problems/marketing-attribution-vendors/worker-life-1|Worker Life 1]], [[problems/marketing-attribution-vendors/worker-life-2|Worker Life 2]]

---

## 1. Continuous Model Validation Against Experimental Ground Truth
#causal-inference #cross-validation #bayesian-inference #hypothesis-testing #confidence-intervals #evaluation-metrics #monte-carlo-methods #revenue-impact

**Problem statement:** Attribution and mix models produce numbers that reallocate budgets and are validated, if at all, by historical fit — which measures whether the model explains past revenue, not whether its causal decomposition is correct. Only an experiment discriminates, and experiments are treated as occasional supplements rather than as the standard.

**ML task:** Score every model's channel-level predictions against subsequent randomised experiments it did not see, maintain the error record over time, and use it to correct and recalibrate
**Input data:** Model predictions of channel incremental effect at a point in time; geo holdout, staggered launch and matched-market experiment results run afterwards; channel, vertical, spend level and season covariates; the specification used for each prediction.
**Target:** The experimentally measured incremental effect, treated as ground truth with its own measurement error.
**Evaluation metric:** Prediction error against held-out experiments, reported per channel and per vertical, and — the number that matters — how often the experiment's result falls outside the model's stated interval. A model whose 80% intervals contain the truth 40% of the time is miscalibrated, and that fact is currently unmeasured everywhere in this category. Track it over time and publish it.
**Scope:** Experimental measurement error must be modelled rather than assumed away, since many geo tests are themselves underpowered — treating a noisy experiment as exact ground truth produces a validation record that is itself noise. The commercial obstacle is larger than the technical one: this makes error visible, which is why no incumbent has done it and why doing it is a positioning strategy as much as an engineering project. 2 ML engineers plus a causal specialist, 6-9 months to a working record.
**Data availability:** Requires that experiments be run systematically and their results retained alongside the predictions that preceded them. Most vendors have neither the experiment cadence nor the archive; building both is the project.

---

## 2. Specification Ensembles and Identifiability Diagnostics
#bayesian-inference #mcmc-sampling #variational-inference #regularization #confidence-intervals #cross-validation #hypothesis-testing #evaluation-metrics

**Problem statement:** With collinear channel spends and two years of weekly data, the likelihood is close to flat across a wide region and the posterior is substantially the prior. Different defensible specifications give different contributions, and the output reports one of them as though the data chose it.

**ML task:** Fit an ensemble across the space of defensible specifications — adstock forms, saturation curves, control sets, pooling levels, priors — and report the distribution of contributions, plus diagnostics on which parameters the data actually informs
**Input data:** Spend and impressions by channel and geography; conversions and revenue; price, promotion, distribution and competitive covariates; seasonality; the client's own contaminating events — migrations, stockouts, rebrands — gathered explicitly rather than left implicit.
**Target:** Not a point estimate but the distribution of channel contributions across specifications, and per-parameter prior-to-posterior contraction.
**Evaluation metric:** Simulation-based calibration is the right instrument: generate data from known effects and ask whether the procedure recovers them at this sample size and collinearity structure. Where it cannot, the product should say so for that channel rather than report a number. External validation still comes from item 1 — the ensemble narrows what is defensible, it does not establish truth.
**Scope:** The computational cost of an ensemble over hundreds of specifications is real but modest with modern samplers and variational approximations. The design question is which specifications count as defensible, which is a judgement that should be explicit and documented rather than buried. 2 ML engineers with Bayesian modelling depth, 6-9 months.
**Data availability:** The same data the single model already uses. The client's contaminating-event history is the missing input and is obtained by asking, which currently happens in interviews and is then lost.

---

## 3. Empirical Priors from a Pooled Experimental Base
#bayesian-inference #variational-inference #causal-inference #confidence-intervals #hypothesis-testing #evaluation-metrics #transfer-learning #revenue-impact

**Problem statement:** Priors carry much of the identification in mix modelling and are set by analyst judgement. A vendor with hundreds of advertisers could derive them from its own accumulated experimental results instead, which would be both more defensible and the one thing a client cannot build alone.

**ML task:** Hierarchical model over pooled experimental estimates producing channel effect priors conditioned on vertical, spend level, purchase cycle and business model, used to inform each client's model
**Input data:** Every experimental result across the client base with its design, power and measurement error; client covariates; channel and platform taxonomy; spend levels and saturation region; season.
**Target:** A predictive distribution for a channel's incremental effect given a new client's characteristics, before that client has run any experiment of their own.
**Evaluation metric:** Out-of-client predictive accuracy — held out entire advertisers, not held out weeks — because the question is whether the pooled prior helps a business the model has never seen. Report how much the prior shrinks a small advertiser's estimate and be explicit that for small accounts the prior is doing most of the work, which is defensible when the prior is empirical and indefensible when it is an analyst's intuition.
**Scope:** Cross-client pooling raises legitimate confidentiality questions and the workable form aggregates to covariate cells rather than exposing any advertiser's results. Heterogeneity is the modelling risk — a prior pooled too coarsely imports a competitor's economics into a business that does not share them, so the hierarchy's structure matters more than its sophistication. 2 ML engineers, 6-9 months once an experimental base exists.
**Data availability:** Depends entirely on item 1's experiment programme. Without a systematic experiment cadence there is nothing to pool, which is why these three items are one programme in sequence.

---

## 4. Conversion Completeness Modelling and Finance Reconciliation
#bayesian-inference #gradient-boosting #probability-distributions #confidence-intervals #change-point-detection #evaluation-metrics #data-integration #compliance

**Problem statement:** The conversion record is partial and its missingness correlates with browser, region, consent state and device — and therefore with channel. Models fed that record attribute the pattern of missingness to whichever channels correlate with it, and platform-modelled conversions are ingested as if they were observations.

**ML task:** Estimate conversion record completeness by segment and correct for it; separate observed from platform-modelled conversions and carry the latter as estimates with uncertainty; reconcile the corrected total against finance
**Input data:** Observed conversion events with browser, region, device, consent state and channel; consent rates by segment; the client's finance order and revenue totals; platform-reported conversions with modelling disclosure where available; deduplication logic between browser and server events.
**Target:** True conversion counts by segment, with the observed record treated as a biased sample of them.
**Evaluation metric:** Reconciliation error against finance totals is the primary check and the only external truth available here. Report the correction's size by segment — if the correction is large for exactly the segments that differentiate channels, the uncorrected model was substantially wrong and that should be stated plainly to the client rather than absorbed silently into a new number.
**Scope:** Unglamorous, fast, and changes answers by more than most modelling refinements. Deduplication faults between browser and server events are a common silent doubling for one channel and should be detected as part of this work. 1-2 ML engineers, 3-4 months.
**Data availability:** Good. Consent rates and segment composition are observable; finance totals are available if asked for; platform modelling disclosure is partial and improving.
