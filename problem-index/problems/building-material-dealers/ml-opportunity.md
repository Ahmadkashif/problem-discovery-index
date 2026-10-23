# Machine Learning Opportunities — Building Material Dealers

**Industry:** [[building-material-dealers|Building Material Dealers]]
**Derived from:** [[problems/building-material-dealers/high-impact|High Impact]], [[problems/building-material-dealers/low-impact-1|Low Impact 1]], [[problems/building-material-dealers/low-impact-2|Low Impact 2]], [[problems/building-material-dealers/worker-life-1|Worker Life 1]], [[problems/building-material-dealers/worker-life-2|Worker Life 2]]

---

## 1. Learning the Estimator's Lumber Package From Plan Sets and Job Outcomes
#tacit-knowledge-ml #object-detection #cnns #large-language-models #gradient-boosting #evaluation-metrics #revenue-impact #workflow-orchestration

**Problem statement:** Veteran estimators read a residential plan set that carries no framing plan and "just know" the girders, blocking, plate lengths, beams and waste this builder and framer will need. The ML problem is to draft a complete, priced framing package from the plan set and learn the estimator's adjustments to it from their own edits and from the job's delivered net quantities.

**ML task:** Two stages. First, sheet understanding: object detection and segmentation of walls, openings, dimensions, room labels, roof outlines and schedules on plan PDFs, feeding a deterministic framing generator that produces a drawn-quantity list. Second, adjustment learning: per-category regression of the quantity the job will actually consume, given the drawn quantity and builder, framer, designer, region and season features, plus multi-label prediction of items the estimator adds that the drawings imply but don't show.
**Input data:** Plan set PDFs (floor plans, elevations, window and door schedules, sections where present), the estimator's final takeoff and edit trail, the dealer's item master and price file, and per job from the ERP: original package, add-on orders, returns, back-charges, delivery tickets and plan revision dates. Public permit-portal plan sets and synthetic price files serve for a prototype.
**Target:** Per line item: required quantity (board feet, pieces, sheets) after adjustment; per job: probability that each commonly added item (girder, beam, blocking package, treated ledger, longer plates) is needed; the priced package total.
**Evaluation metric:** Absolute percentage error of package total and of each category against net job consumption (delivered minus returns plus add-ons), on jobs split by time and by builder, reported only on jobs with no recorded plan revision. Recall on items the senior estimator added, at a precision the estimator tolerates: a missed beam costs an add-on truck and a builder's goodwill, a false suggestion costs seconds. Report model error beside the estimators' own disagreement on a re-takeoff sample as the ceiling.
**Scope:** The data collection challenge comes first: the estimator's assumptions have to be captured as they work, so the takeoff screen must log every edit to the drafted list with a one-click reason, because historical takeoffs hold only the output. The labelling challenge is that net consumption mixes takeoff error with framer waste, theft and plan changes, and experts disagree with themselves (waste factors shift with the season and the bid), so revisions must be tracked and a sample of plans taken off twice by two estimators to measure agreement. The deployment challenge is speed: the draft must arrive in minutes with the sheet and assumption behind each line, faster than the estimator can start, or it is ignored. 2 ML engineers, a CAD or geometry engineer and a senior estimator as domain lead, 6–9 months; a priced draft from a plan set is demo-able in two weeks.
**Data availability:** Plan sets arrive with every bid request; add-ons and returns sit in every LBM ERP under the job account, untouched by analysis. Edit reasons don't exist until a workflow captures them. Plan revision dates are in email and need joining.

---

## 2. Commodity Margin at Risk Across Open Quotes
#time-series-forecasting #temporal-fusion-transformers #gradient-boosting #exponential-smoothing #feature-engineering #revenue-impact

**Problem statement:** For every open lumber and panel quote, estimate the distribution of replacement cost on the likely ship date, so the dealer can set hold periods, reprice before margin disappears and see total margin at risk across the book.

**ML task:** Probabilistic (quantile) forecasting of species-grade-size replacement costs over a 1–12 week horizon, plus a ship-date model for each quote (conversion probability and time to release), combined into a margin-at-risk distribution per quote and for the book.
**Input data:** Weekly price assessments where licensed (Random Lengths composites and item prices), CME lumber futures curves, mill and wholesaler quotes received by the buyer, the dealer's own purchase costs and inventory, duty and tariff schedules for Canadian softwood, housing starts and permits, quote headers and lines with dates, customer and hold terms, and later releases matched to quotes.
**Target:** Replacement cost quantiles by item and horizon; quote conversion and release date; margin at ship versus margin quoted.
**Evaluation metric:** Pinball loss and interval coverage of cost forecasts on rolling out-of-time windows, with particular attention to coverage in sharp moves; for the decision, realised margin on shipped packages against a baseline of fixed hold periods. Under-coverage in a rising market is the costly error, because it ships packages below replacement cost.
**Scope:** A pricing data scientist and an engineer, 3–4 months to a useful dashboard. The honest difficulty is that lumber prices are hard to forecast beyond a few weeks; the value is less in the point forecast than in sizing exposure and flagging which quotes to reprice, which a calibrated interval does well enough.
**Data availability:** Assessments are licensed; futures are public; the dealer's quotes, costs and releases are its own, though quote-to-release matching needs cleaning.

---

## 3. Contractor Credit Risk and Lien-Deadline Triage
#survival-analysis #gradient-boosting #logistic-regression #compliance #revenue-impact #automation

**Problem statement:** Predict which contractor job accounts will go past terms or default, early enough for the credit manager to act, and rank which jobs need a preliminary notice or lien filing before the statutory window closes.

**ML task:** Time-to-event modelling of days-to-pay and default per account and per job, plus a ranking of jobs by expected loss given the notice deadlines that apply to them.
**Input data:** Credit applications and limits, invoice and payment histories by job account, first-delivery dates from delivery tickets, project and owner records, state notice rules (for example California's 20-day preliminary notice), lien waivers received, joint-check arrangements, commercial bureau data where licensed, and public signals such as permits and new liens filed against the contractor.
**Target:** Hazard of reaching 60/90 days past due or charge-off; expected loss per job if the notice window lapses.
**Evaluation metric:** Concordance index and time-dependent AUC for the survival model; recall of eventual write-offs in the top decile of alerts, since a missed default costs the whole job's materials while a false alert costs a phone call. Notice compliance measured as the share of eligible jobs noticed before the deadline.
**Scope:** One data scientist and an engineer, 3–5 months. The notice-deadline engine is rule work and should ship first; the risk model needs a few years of payment history and a clean link from deliveries to jobs.
**Data availability:** All in the dealer's ERP and credit files; first-delivery dates are reliable only where delivery tickets are captured electronically. Contractor payment data is the dealer's own record of its customers.

---

## 4. Failed-Delivery Prediction and Load Sequencing
#gradient-boosting #optimization-fundamentals #dynamic-programming #cnns #worker-facing #workflow-orchestration

**Problem statement:** Predict which job-site deliveries will fail or need a second truck, and build each day's routes and load order so trucks leave full, in the right sequence, to sites that are ready.

**ML task:** Binary classification of delivery failure (site not ready, inaccessible, refused, missing items) per stop, feeding a vehicle routing problem with time windows, truck capabilities (boom, flatbed, moffett) and load-sequence constraints; optional photo verification of loaded items against the ticket.
**Input data:** Delivery tickets and outcomes, site coordinates and photos from past drops, builder and superintendent histories, weather and soil-moisture proxies, order lines with dimensions and weights, truck and driver rosters, yard pick times.
**Target:** Failure probability per stop; routes and load plans minimising cost and failed drops.
**Evaluation metric:** AUC and calibration of failure prediction; for the plan, failed or returned deliveries per hundred drops and truck utilisation against the dispatcher's own plans over matched weeks.
**Scope:** An operations research engineer and a data scientist, 4–6 months. Routing is a solved class of problem; the dealer-specific difficulty is that failure causes are rarely coded today, so the first months are capture.
**Data availability:** Tickets and GPS exist at dealers with dispatch software; failure causes and site photos must be captured by drivers.

---

## 5. Plan Revision Change Detection for Components and Special Orders
#object-detection #transformers #graph-neural-networks #large-language-models #worker-facing #automation

**Problem statement:** Given two versions of a plan set, find every change that affects trusses, wall panels, headers or the window and door schedule, map each change to the affected components or special-order units, and flag configured windows that no longer fit their openings.

**ML task:** Multimodal sheet alignment and change detection between drawing versions, followed by structured mapping of changes onto a building graph (walls, bearings, openings, roof planes) that links to truss profiles, panel layouts and special-order lines.
**Input data:** Successive plan set PDFs, component designs exported from MiTek or Alpine software, window and door schedules and configured quote lines, and designers' past revision decisions.
**Target:** A list of structural and opening changes with locations; affected component and special-order lines; a draft revision for the designer or window specialist to accept.
**Evaluation metric:** Recall of changes that the designer eventually acted on (a missed bearing change becomes a field fix), at a precision that keeps review under a few minutes per revision; time per revision against current practice.
**Scope:** An ML engineer with document-vision experience, a geometry engineer and a senior designer, 6–8 months. Drawing alignment is tractable; the hard part is building the link from drawing changes to the component model, which the plate suppliers' software owns.
**Data availability:** Revisions sit in email and design files at every component plant; integration depends on export access to MiTek or Alpine projects.
