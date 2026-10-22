# Machine Learning Opportunities — Satellite Operators

**Industry:** [[satellite-operators|Satellite Operators]]
**Derived from:** [[problems/satellite-operators/high-impact|High Impact]], [[problems/satellite-operators/low-impact-1|Low Impact 1]], [[problems/satellite-operators/low-impact-2|Low Impact 2]], [[problems/satellite-operators/worker-life-1|Worker Life 1]], [[problems/satellite-operators/worker-life-2|Worker Life 2]]

---

## 1. Capturing the Fleet Engineer's Read of Telemetry
#tacit-knowledge-ml #autoencoders #lstms-and-grus #change-point-detection #survival-analysis #k-nearest-neighbors #worker-facing #revenue-impact

**Problem statement:** Senior spacecraft engineers look at trend plots of wheel currents, battery cell voltages or amplifier helix currents and "know" months ahead that a component is degrading, a judgement built over a decade of watching one fleet that sits inside the alarm limits and leaves with them. The ML problem is to learn which telemetry departures the engineer treats as precursors, surface them as a ranked shortlist with comparable historical cases, and estimate time to failure.

**ML task:** Per-subsystem multivariate anomaly scoring (autoencoder or sequence-model reconstruction error conditioned on season, eclipse, load and commanding), change-point detection on driver-response relationships, nearest-neighbour retrieval of similar historical signatures, and survival modelling of time to failure or switch to redundancy
**Input data:** Archived housekeeping telemetry at native rates for every satellite in the fleet (thousands of channels each, years of history); command and event logs; eclipse and season calendars; anomaly reports, shift logs and correspondence with the manufacturer; component switch-overs, failures and insurance claims; bus type and design data.
**Target:** Engineer-confirmed precursor flags per channel window (precursor, benign, seasonal, unknown); the eventual outcome (recovered, switched to redundancy, failed); time from first flag to outcome.
**Evaluation metric:** Lead time gained over the limit alarm at fixed false-alert budget per console shift, because controllers will mute a detector that pages them more than a few times a week. Event-level recall on the fleet's known component failures, scored by leave-one-satellite-out and strictly out of time. For retrieval, the share of surfaced cases the engineer rates as relevant. For survival models, concordance and calibration of remaining-life estimates, reported with wide intervals given the few failures per bus type. Agreement with held-out engineer annotations is reported against the engineers' own test-retest agreement as the ceiling.
**Scope:** The data collection challenge comes first: the expert's read must be captured as it happens, so the console needs a two-click flag-and-tag surface, and history must be reconstructed by interviewing engineers against old anomaly reports and aligning their recollections to telemetry timestamps. The labelling challenge is that experts disagree with themselves (a signature called "going" one year and "seasonal" the next) and that successful early calls never produce a failure label, so labels must record the engineer's confidence and the action taken, and intra-rater reliability must be estimated on re-annotated samples. The deployment challenge is that the console already has too many alarms; the model must arrive as a quiet ranked shortlist with evidence, faster than the engineer can search the archive. 2 ML engineers and 1 spacecraft systems engineer, 9–12 months for one bus type, with value appearing first as similar-case retrieval before any detector is trusted to page.
**Data availability:** The operator holds the full telemetry archive and its anomaly reports; engineer annotations are the missing asset and building them is most of the work. Manufacturers hold cross-operator data for each bus type but share it under contract and export control. Public benchmarks (the ESA anomaly dataset, NASA's SMAP and MSL telemetry sets) are useful for method development but not for a specific fleet.

---

## 2. Interference Signature Classification from Spectrum Traces
#cnns #transfer-learning #k-nearest-neighbors #evaluation-metrics #automation #worker-facing

**Problem statement:** Classify the type of interference on a transponder (cross-polarisation, adjacent-satellite, intermodulation, terrestrial leakage, unmodulated or swept carrier, deliberate jamming) from carrier monitoring traces as soon as it appears, and retrieve the most similar past cases with their sources, so the payload engineer starts with a likely cause instead of a blank screen.

**ML task:** Multi-class classification of spectrogram and trace images plus carrier parameters, with similar-case retrieval over the operator's interference history
**Input data:** Carrier monitoring captures (spectrum traces and spectrograms over time, carrier parameters, Carrier ID where present) from Kratos Monics-type systems; interference case records with confirmed causes and sources; satellite, beam, transponder and frequency plans; customer terminal databases.
**Target:** Interference type; probable source class (own customer, other operator's customer, terrestrial, unknown); similar historical cases.
**Evaluation metric:** Top-2 accuracy on confirmed case types, because the engineer needs the right cause on the shortlist rather than a single guess; time from detection to correct source identification before and after. Precision on the "deliberate" class matters most, since a false jamming call escalates to regulators and governments.
**Scope:** Confirmed case labels exist in case records but are inconsistently coded; a relabelling pass with senior engineers on a few thousand cases is needed. Transfer from pretrained image models works for trace images. 1 ML engineer and 1 RF engineer, 5–6 months for a first version on one fleet.
**Data availability:** Operators keep monitoring captures and case logs, often only for the duration of a case; retention policies must change before history accumulates. Industry interference groups hold anonymised case statistics but not traces.

---

## 3. Manoeuvre-or-Not Decisions on Conjunction Warnings
#gradient-boosting #monte-carlo-methods #probability-distributions #evaluation-metrics #automation

**Problem statement:** For each conjunction warning, estimate the probability that the event is still high-risk at the manoeuvre decision point, after re-screening with the operator's own ephemeris and planned burns and correcting for the reporting source's covariance realism, so analysts act on the few events that will truly need a manoeuvre.

**ML task:** Binary classification and probability calibration of event outcome at decision time, with Monte Carlo re-estimation of collision probability under corrected covariance
**Input data:** Conjunction data message histories per event from Space-Track, TraCSS and commercial providers; the operator's own orbit determination solutions and planned manoeuvres; later tracking that reveals each prediction's error; space weather indices; object type and manoeuvrability of the secondary.
**Target:** Whether the event's collision probability at the decision deadline exceeds the operator's threshold; the corrected probability itself.
**Evaluation metric:** Recall on events that truly required a manoeuvre must be near one, because a missed event can end a satellite and add debris; precision then measures avoided burns. Calibration of the corrected probability against later tracking-based estimates. The European Space Agency's Collision Avoidance Challenge showed how hard late-event prediction is, so a persistence baseline is the bar to beat.
**Scope:** The operator's own CDM history, joined to later tracking, provides labels. Covariance realism scoring per source is the most valuable piece. 1 flight dynamics engineer and 1 data scientist, 4–6 months.
**Data availability:** CDMs are free from Space-Track for operators; commercial data is licensed. The operator's own ephemerides and manoeuvre plans are internal.

---

## 4. Beam-Level Capacity Demand Forecasting for Mobility and Broadband
#temporal-fusion-transformers #time-series-forecasting #gradient-boosting #feature-engineering #revenue-impact

**Problem statement:** Forecast demand per beam (GEO spot beam or LEO cell) by hour for the coming weeks and months, combining subscriber growth, airline schedules and shipping routes, so capacity can be sold, priced and steered without busy-hour congestion.

**ML task:** Multi-horizon hierarchical time-series forecasting with quantiles
**Input data:** Historical throughput per beam and terminal; subscriber and terminal activations; airline flight schedules and seat counts for connected fleets; vessel positions and routes; events and seasonality; planned capacity additions.
**Target:** Hourly busy-period demand per beam with 10th and 90th percentile bands; probability of exceeding capacity.
**Evaluation metric:** Weighted quantile loss at the busy hour, which is what determines congestion; reconciliation error between beam, region and fleet forecasts; the share of congestion events forecast a week ahead.
**Scope:** Data is internal and plentiful for operators with live networks. Mobility demand depends on partner schedules, which must be ingested from airline and shipping sources. 2 data scientists, 4 months.
**Data availability:** Network telemetry is complete; partner schedules are licensable; subscriber pipeline data sits in sales systems.

---

## 5. Filing Relevance Triage for ITU Circulars
#large-language-models #transformers #k-nearest-neighbors #compliance #workflow-orchestration #automation

**Problem statement:** For each fortnightly ITU space circular and each FCC public notice, rank filings by how likely they are to require the operator's comment or coordination, explain why, and compute the response deadline.

**ML task:** Ranking of filings by relevance with structured parameter extraction and similar-case retrieval over past coordinations
**Input data:** BR IFIC special sections and the ITU space network database; the operator's own filings and coordination agreements; FCC public notices; past decisions to comment or not; correspondence.
**Target:** Comment, coordinate, monitor or ignore, with the overlapping parameters and deadline.
**Evaluation metric:** Recall on filings the regulatory team historically commented on must be near one, because a missed window weakens coordination rights for years; workload reduction at that recall.
**Scope:** Most of the relevance test is rule-based on bands, orbits and service areas; models add value on free-text notes and in ranking borderline cases. 1 engineer and 1 regulatory engineer, 3–4 months.
**Data availability:** ITU and FCC data are available to administrations and subscribers; the operator's own comment history is the label.
