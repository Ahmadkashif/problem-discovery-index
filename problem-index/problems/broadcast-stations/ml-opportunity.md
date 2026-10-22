# Machine Learning Opportunities — Broadcast TV & Radio Stations

**Industry:** [[broadcast-stations|Broadcast TV & Radio Stations]]
**Derived from:** [[problems/broadcast-stations/high-impact|High Impact]], [[problems/broadcast-stations/low-impact-1|Low Impact 1]], [[problems/broadcast-stations/low-impact-2|Low Impact 2]], [[problems/broadcast-stations/worker-life-1|Worker Life 1]], [[problems/broadcast-stations/worker-life-2|Worker Life 2]]

---

## 1. Learning the GSM's Sell-Out and Hold Read
#tacit-knowledge-ml #gradient-boosting #bayesian-inference #survival-analysis #time-series-forecasting #evaluation-metrics #revenue-impact

**Problem statement:** Experienced general sales managers and inventory managers "know" how fast each daypart-week will sell, what the last units will clear at and how much to hold back for late local, scatter and political money. The ML problem is to forecast sell-out and clearing rate per daypart-week and learn where the manager's historical overrides beat the forecast, so that read becomes visible, graded and transferable.

**ML task:** Time-to-sell-out survival model and clearing-rate regression per daypart-week, with a hierarchical Bayesian layer pooling across stations in a group; a second model predicting the manager's own rate and hold decisions, used to measure where they add value over the forecast
**Input data:** Traffic-system history: rate-card versions, orders with booking dates, unit rates, preemptions, makegoods and unsold units by daypart-week; ratings by daypart; category demand from occurrence data (Vivvix, MediaRadar); pacing reports; political-file orders and race calendars in even years; the managers' rate overrides with timestamps.
**Target:** Weeks-to-sell-out and final average unit rate per daypart-week; for preemption decisions, the realised cost of each choice (makegood units, advertiser churn within 12 months).
**Evaluation metric:** Calibration of sell-out probability at each horizon (Brier score by weeks-to-air), strictly out of time across at least one full election cycle, because political years behave differently. Revenue-per-available-unit uplift is measured in a holdout of daypart-weeks priced with the model's guidance against comparable ones priced as usual. Under-holding before an election costs far more than over-holding in a soft week, so report error asymmetrically on high-demand weeks.
**Scope:** The data collection challenge comes first: holds are often informal and overrides carry no reason, so the system needs a one-click capture of "expected sell-out and why" at the moment a rate or hold is set, plus reconstruction of history from rate-card versions and order timestamps. The labelling challenge is that revenue is a noisy, counterfactual label and managers disagree with themselves: the same GSM prices a November week differently after a weak October. Repeated judgements on sampled scenarios measure that consistency before overrides are treated as signal. The deployment challenge is speed: guidance must appear inside the avails and order-pricing screen, faster than the manager's own recall, or it will be ignored. 2 data scientists and 1 engineer embedded with one station group's revenue team, 6–9 months to a pilot across ~10 stations (estimate), with retrieval of comparable past weeks delivered before any rate recommendation.
**Data availability:** Traffic data is complete and owned by the station, but sits inside WideOrbit or Imagine schemas that need export agreements. Political demand is observable through the station's own political file. National demand detail sits with the rep. The managers' reasoning does not exist yet and must be captured going forward.

---

## 2. Transmitter Fault Anticipation from Remote-Control Telemetry
#tacit-knowledge-ml #autoencoders #change-point-detection #time-series-forecasting #lstms-and-grus #evaluation-metrics #worker-facing

**Problem statement:** Flag transmitter, transmission-line and site faults hours or days before they take a station off the air, and explain each alarm in terms of past incidents at the same site, using the telemetry stations already log.

**ML task:** Per-site multivariate anomaly detection (autoencoder reconstruction error on normalised telemetry) plus change-point detection on slow-moving channels (reflected power, PA temperatures, line pressure); fault-class classification for the anomalies that match historical incidents
**Input data:** Remote-control and transmitter logs at minute resolution: forward and reflected power, PA module currents and temperatures, line pressure, HVAC and room temperature, mains and generator status; weather at the site; the engineer's incident notes and parts replaced.
**Target:** Probability of an off-air or reduced-power event within 24 and 72 hours; fault class (cooling, PA module, line or antenna, power).
**Evaluation metric:** Recall on off-air events at a fixed false-alarm budget per site per month, because a missed failure costs air time and licence exposure while a false alarm costs an engineer's night. Lead time before the event is reported alongside.
**Scope:** Telemetry is plentiful but labels are sparse: real failures are rare per site, so the model pools across sites with the same transmitter family, and the engineers' incident notes provide the labels. Those notes vary by engineer and need a short structured form going forward. 1 ML engineer and 1 broadcast engineer, 6 months for one group's sites.
**Data availability:** Stations own the telemetry, but much of it is kept only as rolling logs on the remote-control unit. Incident history is in paper site logs and email. Transmitter makers hold fleet data from their remote-monitoring services under customer terms.

---

## 3. Expected Subscriber Counts for Retransmission Audit
#bayesian-inference #exponential-smoothing #change-point-detection #hypothesis-testing #feature-engineering #revenue-impact

**Problem statement:** For every distributor system in every market, predict the subscriber count it should report this month and flag reports that fall outside the expected range, so the distribution team audits the systems where money is most likely missing.

**ML task:** Hierarchical Bayesian time-series model of subscribers by system nested in distributor and DMA, with change-point detection for step drops not explained by peers
**Input data:** Historical monthly subscriber reports per system and tier; contract terms (rates, escalators, tiers counted); distributor-level subscriber disclosures from public filings; market-level pay-TV penetration trends; known events such as system sales, migrations and tier changes.
**Target:** Expected subscribers per system-month with a credible interval; flag when a report is below the lower bound or shows an unexplained step.
**Evaluation metric:** Precision of flags at the top of the ranked list against what audits recover, because each audit is costly and limited by contract. Dollars recovered per audit hour is the business metric.
**Scope:** Modest model, heavy data integration. Mapping systems to DMAs and parsing each distributor's report format is most of the work. 1 data scientist and 1 data engineer, 4 months for a group's full distribution book.
**Data availability:** Reports and contracts are held by the station group's distribution team under confidentiality. Labels come from past audit findings, which are few, so early versions rely on peer comparison.

---

## 4. Issue Tagging of Newscasts and Public-Affairs Programming
#bert #transformers #large-language-models #k-means-clustering #evaluation-metrics #compliance #automation

**Problem statement:** Tag every newscast story and public-affairs segment by community issue as it airs, and draft the quarterly issues/programs list from those tags, so the station certifies from a complete record instead of a last-week reconstruction.

**ML task:** Multi-label text classification of story-level transcripts and rundown slugs into a station-specific issue taxonomy, with clustering to propose new issues as coverage shifts; LLM drafting of list entries (issue, programme, date, time, duration, description)
**Input data:** Newsroom rundowns and scripts (ENPS, iNEWS, Ross), closed-caption or speech-to-text transcripts, public-affairs programme logs, PSA schedules, prior quarters' lists.
**Target:** Issue labels per segment; a draft list meeting the station's content expectations; gaps where an issue has no programme.
**Evaluation metric:** Agreement with the news director's final list (issues retained, programmes cited) and reviewer minutes per list. Missing a significant programme matters more than including a weak one, so recall on segments the reviewer adds is the primary metric.
**Scope:** Prior lists give weak labels; a few hundred hand-labelled segments per station type are enough to fine-tune. 1 engineer, 3 months for a group template.
**Data availability:** Rundowns and captions are the station's own. Radio clusters with little local news rely on public-affairs logs, which are shorter and simpler.

---

## 5. Copy Instruction Extraction and Log Conflict Resolution
#large-language-models #seq2seq #dynamic-programming #optimization-fundamentals #evaluation-metrics #automation #workflow-orchestration

**Problem statement:** Read agency and advertiser copy instructions from email and PDF into structured rotation rules, then place and move spots on the daily log to satisfy order windows, separations and priorities with the fewest preemptions.

**ML task:** Information extraction (instruction to structured rotation: ISCI or Ad-ID, flight dates, weights, daypart restrictions) and constrained optimisation of spot placement with a learned cost for each kind of move
**Input data:** Copy instructions, orders, the traffic system's log and inventory, separation rules, sales priority codes, and historical log edits by the traffic director.
**Target:** Structured rotation per order with confidence; a feasible log with minimal weighted moves and preemptions.
**Evaluation metric:** Field-level extraction accuracy at the auto-apply threshold, with zero tolerance for wrong copy applied silently; discrepancies per thousand spots and makegood units generated, before and after.
**Scope:** Extraction is tractable with modern language models and a few hundred labelled instructions per agency style. The optimiser must run inside or alongside the traffic system's own log engine, which is the integration risk. 2 engineers, 5 months.
**Data availability:** Instructions and logs are the station's own. The traffic director's historical edits supply the cost of each kind of move.
