# Machine Learning Opportunities — Construction Tech Platforms

**Industry:** [[construction-tech-platforms|Construction Tech Platforms]]
**Derived from:** [[problems/construction-tech-platforms/high-impact|High Impact]], [[problems/construction-tech-platforms/low-impact-1|Low Impact 1]], [[problems/construction-tech-platforms/low-impact-2|Low Impact 2]], [[problems/construction-tech-platforms/worker-life-1|Worker Life 1]], [[problems/construction-tech-platforms/worker-life-2|Worker Life 2]]

---

## 1. Activity-Level Schedule Slip Forecasting
#gradient-boosting #survival-analysis #time-series-forecasting #feature-engineering #cross-validation #evaluation-metrics #confidence-intervals #causal-inference #revenue-impact

**Problem statement:** Construction schedules are updated retrospectively — they record slip that has already occurred. Every signal that would have predicted it (RFI latency on the affected activity, submittal rejections, crew counts below plan, change order activity in the same area, subcontractor history) is captured weeks earlier in the same platform and never joined to the schedule.

**ML task:** Time-to-event modelling of activity start and finish with time-varying covariates; equivalently, a daily-updated distributional forecast per activity
**Input data:** Baseline and current schedule activities with logic and float; open RFI and submittal state mapped to activities; daily reports (trade presence, crew counts, weather, delays noted); change orders with location and cause; subcontractor identity and their historical performance across the vendor's customer base; project attributes (type, value, delivery method, region, owner type).
**Target:** Actual activity start and finish dates against the original baseline, with re-baselining events recorded separately so the original commitment is recoverable.
**Evaluation metric:** Calibration of the predicted distribution (are 80% intervals right 80% of the time) and lead time on correctly identified slips, measured as days between the prediction crossing a threshold and the slip becoming visible in the schedule update. A point-estimate accuracy metric would hide the property that matters, which is honest uncertainty.
**Scope:** The hard prerequisite is mapping RFIs, submittals and daily report lines to schedule activities, which is not maintained on most projects and must itself be inferred from text, location and timing. That mapping is roughly half the project. Survival models with time-varying covariates handle the structure naturally. 3-4 ML engineers plus a construction scheduler, 8-12 months.
**Data availability:** Rich but fragmented. The schedule usually lives outside the platform in Primavera or MS Project and arrives as periodic imports of varying fidelity. Re-baselining destroys the original target unless historical versions were retained, which they often were not. Subcontractor identity is inconsistently normalised across projects and needs entity resolution before cross-project history is usable.

---

## 2. Submittal Register Extraction from Project Specifications
#large-language-models #bert #transformers #word-embeddings #transfer-learning #evaluation-metrics #workflow-orchestration

**Problem statement:** The submittal register is built by hand at the start of every project by a project engineer reading a specification of several hundred pages. Templates transfer badly because specs are assembled from master guides with project-specific edits, and the edits are where the risk concentrates.

**ML task:** Document structure parsing plus information extraction — identifying each required submittal with its specification section, type, quantity, form, and stated review period
**Input data:** Project specification documents as submitted (typically PDF, CSI MasterFormat structured, of highly variable production quality); historical registers built by engineers from those same specifications as labelled pairs; contract documents where they modify review periods.
**Target:** The confirmed register — one row per required submittal with section reference, description, type and review duration.
**Evaluation metric:** Recall on required submittals is the dominant metric, because a missed submittal becomes a field delay while a spurious one costs a moment of review. Report recall at fixed precision levels, and separately measure exact-match accuracy on the review period field, which is frequently mis-stated by templates.
**Scope:** Specification documents are long and structured, and section-aware chunking does most of the work. The variability is in production quality — scanned specs, inconsistent numbering, addenda that modify sections after the fact. Addenda handling is a distinct and commonly botched sub-problem. 2 ML engineers plus a project engineer, 4-5 months.
**Data availability:** Excellent. Vendors hold specifications and the registers eventually built from them for hundreds of thousands of projects, which is a large, naturally paired training set nobody has assembled.

---

## 3. Semantic Drawing Comparison by Trade
#cnns #object-detection #semantic-segmentation #feature-engineering #evaluation-metrics #transfer-learning #worker-facing

**Problem statement:** Sheet comparison operates on pixels and reports that everything changed when a title block was reissued. What a foreman needs is the three changes affecting their trade, and the feature is therefore widely shipped and widely ignored.

**ML task:** Object detection and segmentation on construction drawings, followed by object-level differencing between revisions and trade-relevance filtering
**Input data:** Drawing sheets across revisions (vector PDF where available, raster where scanned), with discipline and sheet type metadata; BIM models where present, as a source of weak supervision for object identity; historical revision clouds and delta markers as noisy labels for what the design team considered a change.
**Target:** A set of changed objects per revision pair — fixtures, doors, walls, dimensions, equipment tags, penetrations — each classified by the trades it affects.
**Evaluation metric:** Precision and recall on changed objects against a hand-labelled evaluation set of revision pairs, reported per trade. The operational metric is the false alarm rate per sheet, since trust collapses if the filtered view is still noisy.
**Scope:** The labelled drawing corpus is the whole problem — nobody has built one, and the platform vendors are the only parties with enough drawings to do so. Revision clouds provide weak labels to bootstrap. Vector PDFs are much easier than raster and cover a growing majority. 3 ML engineers plus a drafter for annotation supervision, 8-10 months.
**Data availability:** Enormous volume, essentially no labels. Drawings are also customer confidential and cross-customer training requires contractual permission that standard terms usually do not grant, which is the binding constraint rather than the technical one.

---

## 4. Daily Report Generation from Site Capture
#cnns #object-detection #large-language-models #transformers #word-embeddings #evaluation-metrics #automation #worker-facing

**Problem statement:** The daily report is contractually required, is the primary evidence in delay claims, and is written from memory at the end of a twelve-hour day. Nearly every fact in it was recorded elsewhere during the day — in photos, gate logs, delivery tickets, weather APIs and coordination messages.

**ML task:** Multimodal aggregation — trade and activity recognition from site photographs, crew count estimation, and generation of narrative report sections grounded in the retrieved artefacts
**Input data:** Timestamped and geotagged site photographs; sign-in or badge system records; delivery tickets; weather API by site location; project coordination messages and logged safety observations; the schedule's planned activities for the day; the superintendent's own prior reports as style examples.
**Target:** The superintendent's confirmed daily report, with their edits to the draft as the correction signal.
**Evaluation metric:** Proportion of report fields accepted unedited; accuracy of trade presence and crew counts against sign-in records held out from the model; and time from opening to signature against the pre-deployment baseline. Any generated statement not traceable to an artefact should be counted as a hard failure, because the report is evidence.
**Scope:** Grounding is the design constraint — nothing may be asserted that does not trace to a photo, ticket, log entry or API response, since a hallucinated fact in a contemporaneous record is worse than a thin one. Crew counting from photographs is the least reliable component and should present a range, not a number. 3 ML engineers plus a superintendent advisor, 6-8 months.
**Data availability:** Very strong. Photo volume per project runs to tens of thousands of images with timestamps and increasingly with location. Prior reports paired with the same day's artefacts form a natural training set. Photos are confidential and often depict identifiable workers, which constrains cross-customer use.
