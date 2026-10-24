# Machine Learning Opportunities — Oil & Gas Producers

**Industry:** [[oil-and-gas-producers|Oil & Gas Producers]]
**Derived from:** [[problems/oil-and-gas-producers/high-impact|High Impact]], [[problems/oil-and-gas-producers/low-impact-1|Low Impact 1]], [[problems/oil-and-gas-producers/low-impact-2|Low Impact 2]], [[problems/oil-and-gas-producers/worker-life-1|Worker Life 1]], [[problems/oil-and-gas-producers/worker-life-2|Worker Life 2]]

---

## 1. Capturing the Asset Team's Analog and Spacing Judgement
#tacit-knowledge-ml #gradient-boosting #gaussian-processes #bayesian-inference #feature-engineering #evaluation-metrics #revenue-impact

**Problem statement:** Experienced reservoir engineers pick analog wells and apply spacing, timing and completion haircuts to build the type curve for an undrilled location, a judgement formed over hundreds of wells that they cannot fully specify and that leaves with them. The ML problem is to predict a new well's normalised production from its geology and the geometry and timing of its neighbours with calibrated uncertainty, and to learn from the engineers' own recorded analog choices and haircuts which adjustments carry information.

**ML task:** Regression of 12- and 24-month normalised cumulative oil and gas (per 1,000 ft of lateral) with quantile outputs, plus a learned analog-ranking model trained on the engineers' inclusion and exclusion decisions
**Input data:** Well headers, landing bench, lateral length, proppant and fluid per foot and stage spacing (state completion filings and FracFocus); horizontal and vertical distance to every neighbour and each neighbour's months on production at the child's first production; parent-well production before and after child completions; mapped geology (thickness, porosity, pressure gradients) from the operator's or a vendor's grids; the operator's type curves and approval-time analog sets; monthly production by well from state commissions.
**Target:** Normalised cumulative production at 12 and 24 months; the parent wells' change in decline after the child's completion; agreement between the model's analog ranking and the engineers' choices; the engineer's haircut against the realised shortfall.
**Evaluation metric:** Out-of-time error and calibration: wells approved in later years are predicted from models trained on earlier ones, because random cross-validation leaks neighbour information through space and time. Report P10–P90 coverage (an 80% interval should contain about 80% of outcomes) and the mean signed error against the operator's own type curves, since the economically dangerous error is systematic optimism. Measure analog agreement against the engineers' test-retest agreement on re-presented locations as the ceiling.
**Scope:** Data collection is the hardest part. The analog set and haircut must be captured as the engineer works, so the system needs a near-zero-effort capture surface inside the planning tool, and history has to be rebuilt from saved projects and decks for a few hundred locations. Labelling is noisy: engineers disagree with themselves after good and bad pads, so a sample of locations should be re-presented blind to estimate intra-rater reliability, and outcomes must be normalised for completion size, choke and downtime and tagged with post-approval changes. Deployment needs speed: the model must propose analogs and a haircut in seconds inside the planning cycle and show which neighbours drove the answer, or engineers will override it. A team of 2 ML engineers, 1 reservoir engineer and 1 data engineer embedded with one asset team, 6–9 months, with value first appearing as analog retrieval and a calibration report on past type curves.
**Data availability:** Production, permits and completions are public by state with lags (EIA reports six to eight months on average between first production and reported data, and uses Enverus as its source), and vendors sell the normalised panel. The decisive asset, the engineers' dated analog sets and haircuts, exists only in fragments inside planning tools, spreadsheets and decks, and building it is most of the work.

---

## 2. Probabilistic Decline Forecasting for Producing Wells
#temporal-fusion-transformers #lstms-and-grus #bayesian-inference #time-series-forecasting #confidence-intervals #evaluation-metrics #automation

**Problem statement:** Engineers re-fit decline curves to thousands of producing wells for reserves, budgets and borrowing bases, mostly by hand-tuned Arps parameters. Forecast each well's monthly oil, gas and water for the next 36 months with uncertainty that holds up, flagging wells whose behaviour has changed.

**ML task:** Multivariate probabilistic time-series forecasting across a panel of wells, with physics-constrained decline (Arps or stretched-exponential) as a prior and a learned residual
**Input data:** Monthly production by well and stream; days on production and downtime; artificial-lift changes and workovers; offset-well completions nearby (frac hits); choke and line-pressure data where SCADA exists; well age, completion size and bench.
**Target:** Monthly volumes per stream for the next 36 months, as quantiles.
**Evaluation metric:** Out-of-time weighted absolute percentage error on 12-month cumulative volumes, plus quantile coverage. The asymmetric cost is overstatement: a proved-developed forecast that runs high inflates reserves and the borrowing base and has to be written down. Compare against the engineers' own year-end forecasts, not only against a naive Arps fit.
**Scope:** The models are mature; the work is data cleaning, event tagging and fitting into the reserves workflow. 2 data scientists and 1 reservoir engineer, 4–6 months to a forecast that runs monthly across the operator's producing wells, with engineers reviewing the flagged exceptions rather than every well.
**Data availability:** Every operator holds its own monthly production. Public state data covers offsets with a lag and variable lease-level allocation (Texas reports oil by lease, not by well, recalled). Workover and downtime events need tagging from field notes.

---

## 3. Title Instrument and Division Order Extraction
#large-language-models #bert #transformers #feature-engineering #evaluation-metrics #compliance #automation

**Problem statement:** Division order analysts and landmen read deeds, probate orders, affidavits of heirship, leases and title opinions to work out who owns what share of a unit. Extract each instrument's parties, legal description, interest conveyed and reservations, and propose the resulting change to the decimal interest schedule.

**ML task:** Document classification, named-entity and relation extraction over scanned and handwritten instruments, plus constrained calculation of decimal changes that must still sum to the unit total
**Input data:** County-recorded instruments (scanned PDFs, many handwritten before the mid-20th century), drilling and division order title opinions, existing decimal schedules, lease forms, unit designations.
**Target:** Structured instrument records (grantor, grantee, interest type and fraction, tract, depth limits, reservations); a proposed decimal schedule with each change linked to the instrument and clause that caused it.
**Evaluation metric:** Field-level exact match on interest fractions and tract descriptions, and exact match of the resulting decimals to the analyst's final schedule. Precision matters more than recall for automated changes: a wrong decimal pays the wrong person, so the system proposes and the analyst approves, and anything below a confidence threshold goes to review with the source highlighted.
**Scope:** 1 ML engineer and 1 experienced division order analyst or landman as subject-matter lead, 5–6 months to a reviewer-in-the-loop tool on one county set. Handwritten older instruments and inconsistent legal descriptions are the hard tail, and per-county indexing quirks matter.
**Data availability:** County records are public but scattered across county websites, title plants and vendors such as Enverus Courthouse. Labelled examples sit in operators' land files and title opinions written by counsel, which are privileged or client-owned and need permission to use.

---

## 4. Owner Matching for Suspense and Escheat
#k-nearest-neighbors #word-embeddings #logistic-regression #feature-engineering #data-integration #compliance

**Problem statement:** Royalty payments pile up in suspense because an owner is unknown, has moved or has died. Match suspended interests to the right person or heir using names, addresses, instruments and public records, and rank them by dollars and by each state's escheat date.

**ML task:** Entity resolution (candidate generation by approximate nearest neighbours on name and address embeddings, then a pairwise match classifier) plus priority ranking
**Input data:** Suspense records with owner names, last addresses and decimals; recorded instruments; obituaries and probate indexes; returned-mail logs; state unclaimed-property lists; the operator's owner master file.
**Target:** Match probability between a suspended interest and a candidate person or estate; resolution type (address update, heirship, assignment); priority by dollars and days to dormancy.
**Evaluation metric:** Precision at the top of the review queue, since each false match risks paying the wrong person, and the share of suspended dollars resolved before escheat. Report results by state because dormancy periods differ.
**Scope:** 1 data scientist and an owner-relations lead, 3–4 months. Most of the effort is assembling public-record sources legally and building the review workflow.
**Data availability:** Operators hold suspense and owner data; public probate, obituary and unclaimed-property records are searchable but fragmented. Labels come from past resolutions in the operator's own files.

---

## 5. Leak Detection in Optical Gas Imaging Video
#cnns #object-detection #semantic-segmentation #change-point-detection #compliance #worker-facing

**Problem statement:** LDAR technicians film every component with OGI cameras and judge by eye whether a plume is a leak. Flag likely leaks in each clip, localise them to a component, and prioritise sites from continuous-monitor and SCADA signals so surveys go where emissions are likeliest.

**ML task:** Spatio-temporal segmentation and detection of gas plumes in infrared video, plus change-point detection on continuous methane-sensor and tank-pressure series
**Input data:** OGI clips with technician-confirmed leak labels, camera settings and weather; site equipment lists; continuous-monitor concentration series; tank pressure and flare pilot status from SCADA.
**Target:** Per-clip leak probability and plume mask; component attribution; site-level probability of an emission event in the coming survey interval.
**Evaluation metric:** Recall on confirmed leaks at a fixed false-alarm rate per survey hour; a missed leak is a compliance and emissions failure, while a false alarm costs a technician a second look. Report performance by background temperature and wind, where human detection also degrades.
**Scope:** 2 ML engineers and an LDAR programme lead, 6 months to a reviewer tool; it assists and never certifies a survey alone. Plume labels are subjective at low rates, so labels need multiple raters.
**Data availability:** Operators and LDAR contractors hold years of OGI video, mostly unlabelled beyond leak logs. A public OGI leak video set from Stanford researchers exists for pretraining (recalled), and controlled-release test sites provide ground truth.
