# Machine Learning Opportunities — Heavy Civil Contractors

**Industry:** [[heavy-civil-contractors|Heavy Civil Contractors]]
**Derived from:** [[problems/heavy-civil-contractors/high-impact|High Impact]], [[problems/heavy-civil-contractors/low-impact-1|Low Impact 1]], [[problems/heavy-civil-contractors/low-impact-2|Low Impact 2]], [[problems/heavy-civil-contractors/worker-life-1|Worker Life 1]], [[problems/heavy-civil-contractors/worker-life-2|Worker Life 2]]

---

## 1. Learning the Chief Estimator's Production Rates From Field Actuals
#tacit-knowledge-ml #gradient-boosting #bayesian-inference #feature-engineering #large-language-models #evaluation-metrics #revenue-impact

**Problem statement:** Chief estimators "just know" how much a crew and spread will drive, place, dredge or lay per shift in a given material, site and owner, and they adjust the firm's standard rates by feel. The ML problem is to predict achieved production per crew-shift for each bid item from the job conditions the estimator reads, with an honest uncertainty band, and to learn the estimator's adjustments from their overrides and from the firm's own field actuals.

**ML task:** Hierarchical regression of log production rate (units per crew-hour) by item family (pile driving, stone placement, sheet pile, mass concrete, track laying, dredging), with partial pooling across jobs, crews and owner districts. Gradient boosting with quantile loss serves as the high-capacity comparison. A language-model extraction stage turns geotechnical reports, boring logs and specifications into structured condition features: material classes, depth to refusal, water depth, access, environmental work windows and inspection regime.
**Input data:** Historical estimates from HeavyBid, B2W or InEight (item, quantity, crew, equipment, assumed rate); field cost-code time cards and quantity reports from HeavyJob-type apps; daily diaries; change orders and weather days for cleaning; geotechnical reports and specs as PDFs; the estimator's override log once a capture screen exists. Public bid tabulations on the same items serve as a market prior for jobs the firm lost.
**Target:** Achieved production rate per item and crew-shift, with a 10th to 90th percentile interval, and the estimator's adjustment factor relative to the firm's standard rate.
**Evaluation metric:** Interval coverage and pinball loss on held-out jobs split by time, so later jobs are tested on earlier training. Mean absolute percentage error on the items that make up most of each bid's value, reported beside the spread between two estimators pricing the same historical job as the human ceiling. Under-predicting difficulty is the costly error, because it wins a money-losing job, so coverage of the low tail matters more than the median.
**Scope:** The data collection challenge comes first: the estimator's reasons exist nowhere, so the estimating screen must log each departure from standard with a one-tap reason (soil, water, access, owner, crew, strategy), and field actuals must be cleaned of miscoded hours and change work. The labelling challenge is that the firm only observes outcomes on jobs it won (a selection bias the bid-tab prior partly corrects), and estimators disagree with themselves across hungry and full years, so the target must separate the production rate from the bid-strategy markup. The deployment challenge is bid week: the suggestion has to appear inside the estimating system as the item is built, with the three most similar past jobs and their actuals, faster than the estimator can recall them. 2 ML engineers, a data engineer for estimating and field-system integration, and a senior estimator as domain lead, 6–9 months. A single-firm prototype on 5–10 years of won jobs is feasible; cross-firm pooling is a trust problem, not a technical one.
**Data availability:** Estimates and cost-code actuals sit in every mid-size firm's estimating and field systems, unjoined. Geotech reports come with every bid package. The override reasons don't exist until a workflow captures them.

---

## 2. Unit-Price Outliers and Low-Bid Ranges From Public Bid Tabulations
#bayesian-inference #linear-regression #hypothesis-testing #gaussian-mixture-models #feature-engineering #revenue-impact #quick-win

**Problem statement:** Public owners publish who bid what after each letting: bidder totals at minimum, and line-item unit prices where the owner posts the full tabulation. Scoped to Corps districts, port authorities, transit agencies and railroad owners plus DOT marine, structures and rail items (DOT road-and-bridge items belong to the queued highway contractors build), the ML problem is to model the market price of each standard pay item conditional on quantity, location, date and project context, flag a draft bid's items that sit far outside it (too cheap to be credible, or unbalanced), and forecast the distribution of the low bid for a letting before bid day.

**ML task:** Bayesian hierarchical regression of log unit price on log quantity (economies of scale), region, letting date (cost escalation), item family and project size, with bidder random effects. A two-component mixture separates ordinary bids from unbalanced front-loaded or back-loaded items. A posterior predictive gives each item's outlier score and, summed over the bid schedule, the low-bid distribution. Item descriptions differ by owner, so a text-matching stage maps each owner's item codes to a shared taxonomy.
**Input data:** Corps dredging bid abstracts (bidder totals against the government estimate) and past contracts awarded from the Navigation and Civil Works Decision Support Center (search summary); line-item abstracts where districts post them on SAM.gov or district sites; SAM.gov award records; state DOT bid tabulations filtered to structures, marine and rail items (TxDOT publishes 24 months on a dashboard, and other DOTs publish files or license Oman Systems' Bid Tabs Professional; both via search summary); transit and port authority bid results; engineer's estimates where published; the contractor's own draft bid schedule.
**Target:** Item market-price distribution; outlier score per item in the contractor's draft; low-bid distribution per letting; probability that each known competitor bids.
**Evaluation metric:** Interval coverage of item prices on later lettings (time-split). Rank correlation between predicted and actual low bids. For outlier flags, precision at the top of the list as judged by an estimator, since a false flag costs a minute and a missed mis-key can cost a job. Note that the Corps cannot award above 125% of its estimate, so on dredging the useful target is also the probability a letting goes unawarded.
**Scope:** The owner's MVP shape and the most buildable entry: one engineer, two weeks for a demo on Corps dredging results plus one state's DOT tabs filtered to structures, marine and rail items; 2–3 people for 4–6 months to cover 10–20 owners with clean item mapping. The hard parts are item-code normalisation across owners, the small number of comparable lettings per item (which is why pooling matters), and quantities that are estimates subject to variation clauses.
**Data availability:** Public, free and under-used, though line-item detail is uneven outside DOTs (Corps line items only where districts post full abstracts). The work is in scraping, parsing PDFs and mapping item codes. Engineer's estimates are often published after award. The Corps' independent government estimates stay sealed until bid opening, and its CEDEP dredging estimating program is not released.

---

## 3. Pipeline Plug and Production Forecasting From Dredge Sensor Streams
#time-series-forecasting #lstms-and-grus #change-point-detection #gradient-boosting #worker-facing #revenue-impact

**Problem statement:** Forecast, minutes ahead, whether a cutter suction dredge's pipeline is heading for a plug, and what swing speed and ladder depth hold production highest without one, from the sensor stream the dredge already records for Dredging Quality Management.

**ML task:** Multivariate sequence forecasting of line velocity and slurry density 2–10 minutes ahead (LSTM or temporal convolution baseline, gradient boosting on lagged features as a strong tabular comparison). Change-point detection on vacuum, discharge pressure and cutter load flags material changes, and a plug-event classifier is calibrated as a hazard.
**Input data:** One-second to one-minute sensor logs (vacuum, discharge pressure, density, velocity, pump speeds, cutter and swing motor loads, ladder depth, swing angle, GPS position, line length and elevation); plug and stoppage logs from the dredge's daily reports; survey and boring data for the reach.
**Target:** Velocity and density trajectories; plug probability within the horizon; production per hour.
**Evaluation metric:** Plug recall at a fixed false-alarm rate per watch (operators ignore an alarm that cries wolf). Lead time before the event. Forecast error on velocity near the critical value, where accuracy matters most.
**Scope:** 2 ML engineers and a dredging engineer, 6–9 months, mostly data cleaning and event labelling. Plugs are rare events, so labels come from stoppage logs and need verification with crews. Must run on the dredge, offline from shore.
**Data availability:** Owned by the dredging contractor and recorded continuously, with a copy sent to the Corps' DQM office under the contract. Event labels need hand curation.

---

## 4. Drafting Delay Notices and Time Impact Fragnets From the Field Record
#large-language-models #transformers #bert #graph-theory #compliance #workflow-orchestration

**Problem statement:** Detect, in daily reports, RFIs, emails and survey notes, the events that start a contractual notice clock (differing site condition, owner-caused delay, high water, environmental work-window loss, late owner-furnished item). Then draft the notice and a fragnet tied into the current P6 schedule in the format the owner's spec demands.

**ML task:** Event extraction and classification over project documents (a fine-tuned encoder for event type and date, a language model for drafting). Retrieval of the governing clause from the contract and schedule spec. Graph operations on the schedule network to propose fragnet logic and compute the impact on the critical path.
**Input data:** Daily reports and diaries, RFIs and responses, correspondence, survey and inspection reports, the contract and its schedule specification, P6 .xer files or SDEF exports, past TIAs and the owner's responses.
**Target:** Event type, start date and responsible party; the notice deadline under the contract; a draft notice; a draft fragnet with predecessors and successors; the computed delay to the "End Project" milestone.
**Evaluation metric:** Recall of notice-worthy events against a scheduler's labels (a missed notice forfeits the claim). Share of drafted fragnets accepted with minor edits. Days from event to notice.
**Scope:** 2–3 engineers including one who knows P6's data model, 6 months. The schedule-graph side is deterministic; the risk is extraction recall on messy field text.
**Data availability:** All contractor-held. Labelled examples come from past TIAs and claim files, which are often under legal hold or privilege, so the first training set must be built from closed jobs with counsel's agreement.

---

## 5. Equipment Idle Time and Fleet Right-Sizing From Mixed-Fleet Telematics
#survival-analysis #k-means-clustering #time-series-forecasting #optimization-fundamentals #data-integration #automation

**Problem statement:** From hour-meter, fuel and location feeds across a mixed-OEM fleet, estimate each machine's true working time and idle share by job, predict when it will be released from a job, and recommend which units to sell, rent instead, or move between jobs.

**ML task:** Clustering of engine-state sequences into work, idle and travel modes where the feed lacks a work/idle split. Survival models of time-on-job and time-to-release. Utilisation forecasting by job phase, and an assignment optimisation across jobs.
**Input data:** AEMP 2.0 / ISO 15143-3 feeds from each OEM (location, cumulative hours, fuel used), aftermarket trackers for older units, HeavyJob-type equipment hour entries, job schedules, rental invoices, maintenance records.
**Target:** Working hours and idle share per machine-day; release date per machine-job; a recommended fleet mix.
**Evaluation metric:** Agreement of inferred work hours with foreman-entered hours on audited days. Release-date error. Realised rental spend and owned-fleet utilisation against the prior year.
**Scope:** 1–2 engineers, 3–4 months on a single firm's fleet. The difficulty is inconsistent OEM feeds and units without telematics, not modelling.
**Data availability:** Contractor-owned feeds from the OEMs' portals and fleet platforms. Equipment cost and rate data sits in the estimating and accounting systems.
