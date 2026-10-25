# Machine Learning Opportunities — Landfill Operators

**Industry:** [[landfill-operators|Landfill Operators]]
**Derived from:** [[problems/landfill-operators/high-impact|High Impact]], [[problems/landfill-operators/low-impact-1|Low Impact 1]], [[problems/landfill-operators/low-impact-2|Low Impact 2]], [[problems/landfill-operators/worker-life-1|Worker Life 1]], [[problems/landfill-operators/worker-life-2|Worker Life 2]]

---

## 1. Learning the Senior Technician's Wellfield Tuning
#tacit-knowledge-ml #gradient-boosting #model-based-rl #time-series-forecasting #feature-engineering #compliance #revenue-impact

**Problem statement:** Senior landfill gas technicians set each wellhead valve from patterns in a well's readings that they cannot fully specify — air intrusion, watering-in, cover cracks, early heating — and the outcome is how much methane reaches the plant or escapes through the surface. The ML problem is to learn that judgement from tuning histories and recommend the next adjustment per well, with its predicted effect.

**ML task:** Per-well classification of the well's state (normal, air intrusion, liquid-impaired, surface leakage, heating) plus a dynamics model that predicts next-month oxygen, methane, balance gas, temperature and flow from the current reading, the valve change and covariates; the recommendation is the valve change that maximises predicted methane recovery subject to oxygen, temperature and pressure constraints (constrained model-based policy)
**Input data:** Monthly or more frequent wellhead readings from portable analysers and automated wellheads (methane, CO2, O2, balance gas, temperature, static and differential pressure, flow, valve position); well construction, depth, waste age and position relative to the cap edge; liquid levels and pump-outs; rainfall and barometric pressure; surface emission monitoring results; RNG or flare inlet gas quality and flow; cover inspection notes; the technician's tapped reason for each change.
**Target:** Well-state labels confirmed by what happened next (oxygen falling after a closure, flow recovering after a pump-out, a surface exceedance clearing, temperature continuing to rise); next-reading values for the dynamics model; a ranked adjustment per well.
**Evaluation metric:** For the dynamics model, error on next-reading oxygen and methane against a "no-change" baseline; for state classification, recall on heating and surface-leakage cases at a precision that keeps flags to a few per technician-day, because a missed heating event is far costlier than a false flag. The business metric is field-level methane delivered per ton of waste in place and the number of 5-day and 10-day corrective actions triggered, compared between sites using recommendations and matched sites that do not. Agreement with the senior technician is reported against the senior technician's own month-to-month consistency as the ceiling.
**Scope:** The data collection challenge comes first: the technician's reasoning has to be captured at the wellhead with a one-tap reason code, and the covariates (rain, liquids, cover condition) have to be joined from systems that were never linked. The labelling challenge is that valve outcomes are confounded by the whole field and the weather, experts set the same well differently, and the same expert changes their mind seasonally, so labels must come from the well's subsequent behaviour, not the expert's stated diagnosis. The deployment challenge is that a recommendation must be faster than the technician's own read at the wellhead and must never push a well into a regulatory exceedance; every suggestion also becomes part of a compliance record. 2–3 ML engineers with a landfill gas engineer, 9–12 months, starting on a network of 10–20 landfills with years of readings; rare heating cases need pooled data across owners.
**Data availability:** Readings exist at every regulated landfill, held by the operator, its O&M contractor or the analyser and wellhead vendor's database; the consolidators hold the deepest histories. Reason codes do not exist anywhere and must be collected. Vendor terms decide whether readings can be pooled; Loci Controls says it trained its 2026 AI features on anonymised monitoring data.

---

## 2. Early Warning of Subsurface Heating
#change-point-detection #gaussian-processes #survival-analysis #feature-engineering #compliance

**Problem statement:** Detect the onset of an elevated-temperature event or subsurface oxidation weeks before it produces odour violations, settlement, leachate surges and gas-quality collapse, from the slow joint drift of wellhead temperature, carbon monoxide, methane-to-CO2 ratio, settlement and leachate chemistry.

**ML task:** Multivariate change-point detection on per-well and per-area time series, with a spatial Gaussian process to share evidence across neighbouring wells, and a hazard model estimating the probability that an area progresses to a confirmed heating event within 90 days
**Input data:** Wellhead temperature and gas composition, carbon monoxide samples, downhole temperature where installed, settlement surveys from drone or ground elevation models, leachate volume, temperature and chemistry, odour complaints, and the site's history of confirmed events.
**Target:** Change-point times per well; area-level risk score; time-to-event for confirmed heating events.
**Evaluation metric:** Lead time gained at fixed false-alarm rate (alarms per site-month), measured on historical events held out by site; recall dominates because a missed event can end a landfill's working life, as at Chiquita Canyon, but more than about one false alarm a month at a site will be ignored.
**Scope:** Confirmed events are rare, so the model must be trained across many sites and rely on physically motivated features; 2 ML engineers and a landfill engineer for 6–9 months, with an expert panel to adjudicate historical cases.
**Data availability:** Wellhead data is plentiful; carbon monoxide and downhole temperature are sampled irregularly; confirmed events are documented in agency orders and operator files, few of which are public.

---

## 3. In-Place Density and Airspace Consumption from Drone Surveys
#semantic-segmentation #cnns #bayesian-linear-regression #feature-engineering #revenue-impact

**Problem statement:** Estimate in-place waste density and airspace consumed by area and by period from drone photogrammetry or lidar, scale tonnage and compactor telemetry, separating waste from cover soil, and attribute density differences to lift thickness, pass count, waste mix and weather.

**ML task:** Semantic segmentation of orthomosaics and point clouds into waste, daily cover, intermediate cover and roads; volume differencing between surveys; a hierarchical Bayesian regression of density on operating variables with uncertainty per area
**Input data:** Weekly to quarterly drone surveys; compactor GNSS tracks and pass counts; scale tickets by material and time; cover-soil hauls; rainfall.
**Target:** Waste versus cover volume per area per period; density with a credible interval; effect sizes for operating levers.
**Evaluation metric:** Absolute error of density against quarterly control surveys and annual engineering airspace reports; calibration of the credible intervals; the operational test is whether density moves when operators act on the levers.
**Scope:** Segmentation of drone imagery is well understood; the hard part is attributing scale tonnage to the right area and time. 1–2 ML engineers and a survey engineer for 4–6 months per landfill network.
**Data availability:** Drone vendors and consolidators hold surveys; compactor telemetry exists on newer machines; small public landfills survey once a year, so the method needs a sparse-survey mode.

---

## 4. Leachate Generation Forecasting
#temporal-fusion-transformers #time-series-forecasting #exponential-smoothing #data-integration #compliance

**Problem statement:** Forecast daily leachate volume for 1–21 days ahead from weather forecasts and site conditions, so that tanks, haulers and treatment outlets are booked before the head on the liner approaches the 30 cm limit.

**ML task:** Multi-horizon probabilistic time-series forecasting with known future inputs (forecast rainfall, temperature) and static and slowly changing covariates (open, intermediate and final-cover areas, cell ages, recirculation)
**Input data:** Daily or hourly leachate flow meters or haul logs, tank levels, sump head readings, rainfall and evapotranspiration, cell construction and capping dates, recirculation volumes.
**Target:** Daily volume quantiles (P50, P90) per collection system for each horizon.
**Evaluation metric:** Quantile loss and P90 coverage over 7 and 14 days, because the cost is asymmetric: under-forecasting a storm means emergency hauling and head exceedances, over-forecasting means idle booked trucks. Compared against an exponential-smoothing baseline.
**Scope:** A modest project: 1 ML engineer for 3–4 months per site group; most of the work is cleaning flow records and haul tickets. Generalising across sites needs site-level covariates.
**Data availability:** Every landfill records leachate volumes for state reports, though many as daily haul tallies; weather data is public.

---

## 5. Methane Hotspot Mapping from Aerial and Surface Surveys
#cnns #object-detection #gaussian-processes #data-integration #compliance

**Problem statement:** Combine quarterly walking or drone surface readings, aerial and satellite plume detections and wellfield data into a map of where methane is escaping, which collection deficiency explains each hotspot, and where to send the technician or drill a well.

**ML task:** Plume detection and source localisation in aerial hyperspectral or drone concentration maps; spatial Gaussian process interpolation of surface concentrations between survey lines; classification of hotspot cause (working face, cracked cover, failed boot or penetration, under-vacuum area, leachate cleanout)
**Input data:** Surface emission monitoring traverses with GPS; drone concentration maps; plume detections and emission rates from aerial and satellite providers; wind data; well readings and header layout; cover and construction maps.
**Target:** Gridded concentration and emission-rate estimates with uncertainty; hotspot locations; cause labels from the repair that cleared them.
**Evaluation metric:** Recall on exceedance locations found by the next regulatory survey, and agreement between estimated site totals and independent aerial quantification, given that aerial rates averaged 1.4 times reported rates in the Carbon Mapper study. Precision matters for field time: each false hotspot costs a technician visit.
**Scope:** 2 ML engineers with a remote-sensing specialist for 6–9 months; the integration of external plume data with site records is the main work.
**Data availability:** Surface monitoring records exist at every regulated landfill; drone data at fewer; aerial and satellite detections come from providers whose site-level results are commissioned or licensed, so rights must be checked.
