# Machine Learning Opportunities — Renewable Power Producers

**Industry:** [[renewable-power-producers|Renewable Power Producers]]
**Derived from:** [[problems/renewable-power-producers/high-impact|High Impact]], [[problems/renewable-power-producers/low-impact-1|Low Impact 1]], [[problems/renewable-power-producers/low-impact-2|Low Impact 2]], [[problems/renewable-power-producers/worker-life-1|Worker Life 1]], [[problems/renewable-power-producers/worker-life-2|Worker Life 2]]

---

## 1. Capturing the Interconnection Lead's Read of a Queue Position
#tacit-knowledge-ml #survival-analysis #gradient-boosting #bayesian-inference #evaluation-metrics #feature-engineering #revenue-impact

**Problem statement:** Senior interconnection people "know" which points of interconnection are saturated, which transmission owners' studies slip and which neighbouring requests are speculative, and they decide on that basis whether to post each escalating deposit. The ML problem is to predict each request's odds and timing of reaching operation from public queue history, then learn where the expert's recorded estimates add information the public covariates miss.

**ML task:** Competing-risks survival model (time to commercial operation versus time to withdrawal), calibrated probability of operation within 36, 60 and 84 months, and a disagreement score between the model and the expert's ledger estimate at each decision point
**Input data:** LBNL Queued Up data file (requests from all seven ISOs and dozens of non-ISO balancing areas, with status, dates, technology, size and location); current ISO queue files pulled with the open-source gridstatus library; EIA-860 generator operating dates; cluster study reports (assigned network upgrade cost per request, parsed from PDFs); and the developer's position ledger (expected survival, upgrade cost per kW, online date and reason at each decision).
**Target:** Ending type (operation or withdrawal) and months from request to that ending; assigned upgrade cost per kW at each study phase; agreement between model and expert.
**Evaluation metric:** Time-dependent concordance and integrated Brier score, measured strictly out of time by queue vintage (train on requests filed through 2016, test on 2017–2020 cohorts whose outcomes are mostly known), with calibration plots by grid operator. Recall on positions that withdraw after the facilities study matters most, because those carry the largest forfeited deposits; a false warning costs a review meeting. Report the expert's own estimates on the same test set as the benchmark to beat.
**Scope:** The two-week MVP is the public half: join Queued Up, gridstatus queue pulls and EIA-860, engineer substation-level features (megawatts queued at the same point, prior withdrawal rate there, study phase, vintage), fit a gradient-boosted survival model, and publish per-request odds and months-to-operation. The tacit half is harder. The data collection challenge is that the expert's estimate must be captured at the decision, inside 45-day cluster windows, so the ledger needs a one-minute confirmation drafted from the study report and committee memo. The labelling challenge is that outcomes take about five years, withdrawal can be a good call, and the same director re-rates a substation after a bad restudy, so labels need repeated estimates on a sample to measure self-consistency. The deployment challenge is that the screen must rank hundreds of candidate points faster than the director can during a window. 1 ML engineer and 1 power-systems analyst, 3 months to a trusted public model; the expert layer needs 12–18 months of ledger capture.
**Data availability:** Public data are good but incomplete: valid in-service dates exist for only 73% of operational projects and withdrawal years for 63% of withdrawn requests (LBNL). Order 2023 changed the process, so older outcomes describe a serial queue. Power-flow cases are released under non-disclosure and cannot be pooled. The expert ledger does not exist anywhere and building it is most of the work.

---

## 2. Reading Turbine SCADA the Way a Reliability Engineer Does
#tacit-knowledge-ml #autoencoders #lstms-and-grus #gradient-boosting #feature-engineering #evaluation-metrics #worker-facing

**Problem statement:** Experienced reliability engineers look at a turbine's temperature and power-curve trends and vibration spectra and judge that a main bearing or gearbox stage is failing weeks before an alarm, early enough to plan an uptower repair instead of a crane job. The ML problem is to learn that read from fleet data and their past calls.

**ML task:** Normal-behaviour modelling of each turbine (autoencoder or LSTM residuals on SCADA channels), plus classification of component failure within 30 and 90 days and of the likely fault type
**Input data:** 10-minute SCADA (power, wind speed, rotor speed, pitch angle, bearing, generator and gearbox oil temperatures); high-frequency vibration from condition monitoring systems; OEM fault and event logs; work orders and parts records; engineers' historical alarm dispositions.
**Target:** Component failure (main bearing, gearbox, generator, pitch system) within the horizon; fault type; engineer's disposition (act, watch, ignore).
**Evaluation metric:** Precision at a fixed alert budget (for example two alerts per 100 turbines per month) and median lead time before failure. Recall on main-bearing and gearbox failures carries the cost: a missed one can mean a $225,000–$400,000 replacement with a crane (search summary), while a false alert costs an inspection climb.
**Scope:** The data collection challenge is that engineers' dispositions live in email and chat, so a disposition button on each alert has to be added before labels accumulate. The labelling challenge is that work orders say "replaced bearing" without the failure mode, and engineers disagree with themselves on borderline spectra, so a reviewed sample sets the ceiling. The deployment challenge is that alerts must reach the engineer before the weekly maintenance plan is set. 2 ML engineers and a reliability engineer, 6–9 months per turbine platform.
**Data availability:** Each owner holds its own SCADA and work orders; condition monitoring data often sits with the OEM or vendor under service terms. Public research SCADA datasets from a few European wind farms exist (named from recall) and are useful for prototyping, not for fleet-specific failure modes.

---

## 3. Curtailment and Nodal Basis Forecasting for Budgets and Hedges
#temporal-fusion-transformers #time-series-forecasting #gradient-boosting #feature-engineering #evaluation-metrics #revenue-impact

**Problem statement:** Forecast, for each plant, how many megawatt-hours will be curtailed and how far its node price will sit from the hub price, hour by hour over the next one to 36 months, so budgets, PPA settlement shapes and hedges stop assuming the plant sells everything at the hub.

**ML task:** Probabilistic multi-horizon forecasting with quantile outputs, conditioned on scenarios for new capacity and transmission
**Input data:** Historical nodal and hub prices and congestion shadow prices from the ISOs; the plant's dispatch instructions and curtailment logs; ISO outage schedules and load forecasts; weather; queued and newly operating capacity near the node (from interconnection data); transmission projects and their in-service dates.
**Target:** Hourly curtailed MWh and node-to-hub basis in $/MWh at P10, P50 and P90.
**Evaluation metric:** Pinball loss and continuous ranked probability score against a seasonal-naive baseline, with coverage of the P10–P90 band. The tails matter most: a spring like CAISO's March 2025 record of 919 GWh curtailed is what breaks a budget, so the upper quantile's coverage is reported separately.
**Scope:** 2 data scientists, 4–6 months for one ISO; each further ISO adds 2–3 months. Long horizons need structural scenarios (new plants, new lines) that pure time-series models cannot invent.
**Data availability:** Prices and shadow prices are public and easy to pull; plant-level curtailment is internal to each owner. Price forecasting vendors sell curves but rarely the plant-level curtailment piece.

---

## 4. Battery Bidding Under Uncertainty
#markov-decision-processes #dynamic-programming #model-based-rl #time-series-forecasting #optimization-fundamentals #revenue-impact

**Problem statement:** Decide each day's and each interval's bids for a battery across day-ahead energy, real-time energy and ancillary services, respecting state of charge, cycle limits and warranty degradation, to capture as much of the theoretical revenue as possible.

**ML task:** Stochastic sequential decision-making: price-scenario forecasting feeding stochastic dynamic programming or model-based reinforcement learning, with a degradation cost per cycle
**Input data:** Day-ahead and real-time prices and ancillary clearing prices; load, wind and solar forecasts; the battery's telemetry (state of charge, temperature, availability); warranty cycle limits; market rule changes such as ERCOT's real-time co-optimisation.
**Target:** Bid curves and dispatch schedule per interval.
**Evaluation metric:** Capture rate: realised revenue as a share of perfect-foresight revenue on the same asset and days, net of degradation cost, compared with a rolling-intrinsic baseline. Backtests must use only forecasts available at bid time.
**Scope:** 2 quantitative engineers, 6 months to a backtested optimiser for one market; live trading adds operations, risk limits and market registration.
**Data availability:** Market data are public; telemetry is the owner's; optimiser vendors hold cross-asset histories under service agreements.

---

## 5. Certified Payroll and Begin-Construction Evidence Extraction
#large-language-models #transformers #bert #evaluation-metrics #compliance #automation

**Problem statement:** Turn subcontractors' certified payrolls, apprenticeship records and construction documents into a worker-hour ledger checked against wage determinations, apprenticeship ratios and begin-construction rules, ready for a credit buyer's diligence.

**ML task:** Document extraction (table and field extraction from PDFs and scans), classification of craft and labour category, and rule checks over the extracted ledger
**Input data:** Weekly certified payrolls, registered apprenticeship agreements and request letters, wage determinations by county and craft, contracts and invoices evidencing physical work, and equipment cost breakdowns.
**Target:** Worker-level hours, rates and classifications; per-facility apprenticeship percentage; flagged shortfalls with correction amounts.
**Evaluation metric:** Field-level accuracy on hours and rates, and recall on non-compliant worker-weeks, which is the binding metric: a missed underpayment becomes a buyer holdback or an insurer exclusion, while a false flag costs a few minutes of review.
**Scope:** 1 ML engineer and 1 tax specialist, 4 months to a working pipeline; craft classification against local wage determinations is the hard tail.
**Data availability:** Payrolls are the developer's own records held by contractors; wage determinations are public; diligence outcomes from past sales give labels.
