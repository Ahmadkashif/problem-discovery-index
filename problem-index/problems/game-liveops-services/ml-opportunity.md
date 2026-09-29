# Machine Learning Opportunities — Game LiveOps Services

**Industry:** [[game-liveops-services|Game LiveOps Services]]
**Derived from:** [[problems/game-liveops-services/high-impact|High Impact]], [[problems/game-liveops-services/low-impact-1|Low Impact 1]], [[problems/game-liveops-services/low-impact-2|Low Impact 2]], [[problems/game-liveops-services/worker-life-1|Worker Life 1]], [[problems/game-liveops-services/worker-life-2|Worker Life 2]]

---

## 1. Economy Simulation and Drift Forecasting
#monte-carlo-methods #markov-chains #time-series-forecasting #bayesian-inference #confidence-intervals #gradient-boosting #evaluation-metrics #revenue-impact

**Problem statement:** Faucets and sinks are balanced in a spreadsheet against a representative player, in economies where the aggregate currency stock is the sum of millions of heterogeneous accumulation histories — and the resulting drift compounds for a quarter before it is visible.

**ML task:** Simulate the economy forward under a proposed change, projecting currency stock by cohort, effective price level and progression distribution, calibrated on observed heterogeneous player behaviour
**Input data:** Complete transaction telemetry — every grant, sink, purchase and consumption with player and source; player cohort composition by tenure, spend and progression; historical configuration changes and the economic response that followed; event schedules; price and reward parameters.
**Target:** Currency stock, price level and progression distribution at 30, 90 and 180 days under a given configuration.
**Evaluation metric:** Backtest against the game's own history — project forward from a past date under the configuration that actually shipped and compare to what happened. The bar is lower than it looks and should be stated honestly: the simulation does not need to be accurate in detail, it needs to reliably distinguish a change that stabilises the economy from one that compounds drift, and it should be evaluated on that discrimination rather than on point accuracy. A simulation presented as precise would be worse than the spreadsheet, because it would be believed.
**Scope:** The behavioural response model is the hard part — how heterogeneous players react to changed prices and rewards — and getting it wrong yields confident nonsense, so it should be fitted from observed responses to past changes rather than assumed. Cohort-based simulation is usually sufficient and is far more tractable than agent-based. 2-3 ML engineers plus an economy designer, 9-12 months.
**Data availability:** Complete and exceptionally rich. This is among the best-instrumented economic systems anywhere and the tooling around it is a spreadsheet.

---

## 2. Event Net Effect With Delayed Churn Cost
#causal-inference #survival-analysis #bayesian-inference #confidence-intervals #hypothesis-testing #gradient-boosting #evaluation-metrics #revenue-impact

**Problem statement:** An event's revenue is measured in the week it runs and its cost — players who found it exhausting or unfair and reduced engagement — appears over the following months attributed to nothing. Every reporting incentive favours the more aggressive event.

**ML task:** Estimate per-event net effect on revenue and retention over a long horizon using staggered or randomised exposure, with overlapping events disentangled
**Input data:** Event exposure assignment including staggered or held-out cohorts; participation and completion behaviour; revenue during and after; engagement and churn with timing; the overlapping event calendar; player cohort covariates.
**Target:** Revenue and retained engagement at 90 and 180 days attributable to the event, net of its churn cost.
**Evaluation metric:** The horizon is the whole point — an evaluation window shorter than the churn cost measures only the benefit, systematically, which is precisely how the current practice misleads. Report the net effect with intervals and separately report the revenue and retention components, because an event that is net positive by raising revenue more than it costs in retention is a different decision from one that is positive on both. Overlap handling must be validated: events almost never run alone and attributing a whole period to one event is the standard error.
**Scope:** Building holdouts into the live calendar rather than running special studies is what makes this affordable, and it accumulates a per-event net-effect library that becomes the planning input the discipline lacks entirely. 2 ML engineers plus a causal specialist, 9-12 months including the observation horizon.
**Data availability:** Complete except for the holdout assignment, which must be deliberately introduced and is the gating requirement.

---

## 3. Engagement Absorption Capacity and Obligation-Driven Departure
#survival-analysis #hidden-markov-models #time-series-forecasting #gradient-boosting #confidence-intervals #change-point-detection #evaluation-metrics #worker-facing

**Problem statement:** Calendar cadence ratchets because each season is targeted against the last, and the variable it is implicitly trading against — how much a given audience can absorb — is modelled nowhere. Players who leave after sustained obligation-driven engagement do not resemble ordinary churn risk beforehand.

**ML task:** Model engagement capacity as a depleting resource consumed by required activity and restored by gaps, and detect the obligation signature that precedes abrupt departure after high engagement
**Input data:** Session frequency, duration and timing; required-activity completion under time pressure; number of concurrent limited-time systems a player is engaged with; reward-miss events; the abrupt-departure outcome; tenure and historical baseline per player.
**Target:** Permanent disengagement following sustained high engagement — a distinct outcome from gradual decline and the one standard churn models miss.
**Evaluation metric:** Performance must be reported on the abrupt-departure class specifically, because it is rare relative to ordinary churn and an aggregate churn metric will look fine while missing all of it — and these are among the most valuable departures. Lead time matters: a prediction in the final week is useless, so measure accuracy at 30 and 60 days before departure. For capacity, validate the model against observed response to actual cadence changes rather than against itself.
**Scope:** Absorption capacity is game-specific — a short-daily-session broad-audience game and a long-session committed-audience one differ completely, and the industry's habit of copying pass structures across genres means most games run a cadence derived from a different audience. The model's purpose is to give a live team evidence for a smaller calendar, which is currently an argument with no numbers behind it. 2 ML engineers, 6-9 months.
**Data availability:** Complete. The outcome labels are unambiguous.

---

## 4. Configuration Blast Radius and Community Reaction Forecasting
#change-point-detection #graph-neural-networks #gradient-boosting #bert #large-language-models #confidence-intervals #evaluation-metrics #automation

**Problem statement:** A live game is controlled by thousands of configuration values, many producing irreversible effects — a drop rate that ran for an hour has permanently distributed items — and the tooling is designed for reversible software flags. Separately, balance changes generate community reactions that are forecastable and are instead discovered.

**ML task:** Project the economic and population blast radius of a configuration change before release, detect overlapping segment conflicts, and forecast the magnitude and character of community reaction from the game's own history
**Input data:** The configuration graph with targeting rules and layering; recent telemetry for grant volumes and economy flows; historical configuration changes with their realised effects; the game's history of community reactions to change categories, with sentiment and volume; patch note wording and its association with reception.
**Target:** Projected grant volume, currency inflow, affected segment size; conflicting segment assignments; and the magnitude and category of community reaction.
**Evaluation metric:** For blast radius, accuracy against realised effect on shipped changes — but the operative test is whether it catches order-of-magnitude errors before release, which is the failure mode that damages economies and which a system need only be roughly right to prevent. For reaction forecasting, calibration on held-out changes, and a clear statement that it predicts reaction rather than justifying or avoiding it — the purpose is to communicate properly in advance, which demonstrably changes reception.
**Scope:** Distinguishing reversible from irreversible changes and applying different controls to each is the central design idea and is mostly product work rather than modelling. Community feedback should be delivered to designers as extracted substantive criticism separated from abuse, which is both a filtering task and a duty of care. 2 ML engineers, 6-9 months.
**Data availability:** Configuration and telemetry are complete. Community history requires collection from forums and platforms and is straightforward.
