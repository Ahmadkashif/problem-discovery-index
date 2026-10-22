# Machine Learning Opportunities — Reinsurers

**Industry:** [[reinsurers|Reinsurers]]
**Derived from:** [[problems/reinsurers/high-impact|High Impact]], [[problems/reinsurers/low-impact-1|Low Impact 1]], [[problems/reinsurers/low-impact-2|Low Impact 2]], [[problems/reinsurers/worker-life-1|Worker Life 1]], [[problems/reinsurers/worker-life-2|Worker Life 2]]

---

## 1. Learning the Underwriter's Own-View-of-Risk Loads
#tacit-knowledge-ml #gradient-boosting #bayesian-inference #causal-inference #evaluation-metrics #feature-engineering #revenue-impact

**Problem statement:** Experienced property cat underwriters adjust vendor model output for insured-value adequacy, data quality, claims culture, litigation climate and non-modelled perils, a judgement built over many renewals that they cannot specify. The ML problem is to learn those adjustments from submission features and the underwriters' historical loads, then estimate which adjustments predicted the cedent's later experience relative to the model.

**ML task:** Regression of each adjustment component (load as a multiple of modelled loss cost) on submission features, plus a hierarchical Bayesian model of each cedent's experience-to-model ratio, used to grade the loads
**Input data:** Submission exposure summaries (value per unit by occupancy and region, construction mix, geocoding resolution, secondary-modifier completeness); cedent historical loss schedules; modelled loss costs per layer from each licensed model; the bound price and recorded loads; state-level litigation and claims-handling indicators; post-event cedent notifications and loss bordereaux; industry loss index estimates (PCS, PERILS) for each event.
**Target:** The underwriter's load per component (supervised imitation); and, for grading, each cedent's ratio of reported event losses to modelled event losses across all events, including those that never reached the reinsurance layers.
**Evaluation metric:** For imitation, mean absolute error of the predicted load against held-out underwriter decisions, reported against the underwriter's own test-retest variation on re-priced submissions as the ceiling. For grading, the out-of-time log-likelihood of cedents' experience-to-model ratios with and without the loads as predictors, with credible intervals. Underestimating a load is costlier than overestimating it, because an underpriced cat layer loses its whole limit once in a bad year, while an overpriced one loses only the line. Report the asymmetric loss explicitly.
**Scope:** The data collection challenge is the binding one. The adjustment must be captured as separate reasoned components at the moment of pricing, so the system needs a near-zero-effort capture surface in the pricing workbook, drafted from the referral memo and confirmed by the underwriter, plus a back-fill of past seasons from workbooks and memos. The labelling challenge is that catastrophe labels are rare and correlated: one storm grades dozens of cedents at once, so grading must use every event's ground-up experience, not only layer losses, and pool across cedents hierarchically. Underwriters also disagree with themselves after a bad season, which needs blind re-pricing on a sample to measure. The deployment challenge is the renewal clock: suggestions must appear in the existing workflow before the quote leaves and faster than the underwriter's own recall, with the evidence shown. 2 ML engineers, 1 cat modeller and a senior underwriter part-time, 9–12 months, with value arriving first as retrieval ("loads applied to cedents with this profile, and how they performed").
**Data availability:** Modelled loss costs and bound prices exist in every reinsurer's systems. The reasoned loads exist only in fragments in workbooks and memos, and reconstructing them is most of the work. Cedent loss experience arrives through notifications and bordereaux but is rarely joined to the pricing record.

---

## 2. Exposure Data Quality and Insured-Value Adequacy Scoring
#gradient-boosting #k-nearest-neighbors #large-language-models #feature-engineering #evaluation-metrics #data-integration #automation

**Problem statement:** Score each cedent submission for model readiness and plausibility: map free-text construction and occupancy to model codes, flag locations whose insured values are implausible against rebuild-cost benchmarks, and estimate how much the data defects would move the modelled loss.

**ML task:** Text-to-code classification (construction, occupancy) with an LLM plus retrieval of past mappings; regression of expected rebuild cost per location from building attributes and region; location-level outlier flags by nearest-neighbour comparison against similar buildings
**Input data:** Submission exposure files across cedents and years; past mappings confirmed by exposure analysts; external building attributes and rebuild-cost benchmarks where licensed; geocoding resolution; vendor model sensitivity runs.
**Target:** Model codes per location; expected insured value per location; a submission-level data-quality score and the modelled-loss impact of filling defects with expected values.
**Evaluation metric:** Mapping accuracy against analyst-confirmed codes, with recall on high-impact misclassifications (frame coded as masonry) weighted above all others. Value-adequacy precision at the top of the flagged list. The submission score is judged by whether it explains later experience-to-model ratios (entry 1).
**Scope:** 2 data scientists and an exposure analyst, ~5 months to a first version. The mapping work is a quick win. The value-adequacy model needs licensed building data to be credible.
**Data availability:** Every reinsurer holds years of submissions and its analysts' cleaned versions, a ready-made labelled set for mapping. Rebuild-cost benchmarks are licensed from estimating data providers.

---

## 3. Casualty Loss Trend and Development Across Cedents
#bayesian-inference #mcmc-sampling #change-point-detection #time-series-forecasting #survival-analysis #evaluation-metrics #revenue-impact

**Problem statement:** Casualty excess-of-loss layers are priced on trend and development assumptions fitted from cedents' ceded triangles and large-loss listings. Estimate trend and development jointly across many cedents, detecting when a line's severity trend shifts (social inflation), so that each cedent's selection borrows strength from the portfolio.

**ML task:** Hierarchical Bayesian loss development with cedent and line effects; change-point detection on severity trend by line, venue and accident year; time-to-settlement modelling of large claims
**Input data:** Ceded loss triangles and individual large-loss listings across cedents and years; claim attributes where provided (venue, injury type, attorney involvement); exposure bases; market benchmarks such as the RAA loss development study; published verdict and trend indicators.
**Target:** Ultimate loss by cedent, line and accident year with a predictive distribution; posterior probability and date of trend shifts.
**Evaluation metric:** Out-of-time calibration of predicted ultimates against later evaluations (the share of actual development falling inside the 80% interval) and the bias of point estimates. Under-reserving is the costly direction. Swiss Re estimated social inflation raised US liability claims by 57% in a decade, and late detection compounds across accident years.
**Scope:** 1 actuary-data scientist and 1 engineer, ~6 months. The statistics are established; the work is assembling consistent ceded data across cedents and setting priors the reserving committee accepts.
**Data availability:** Reinsurers hold ceded triangles for every casualty treaty they write, under the confidentiality of each placement. Using it to price and reserve the reinsurer's own book is the purpose for which it was supplied.

---

## 4. Treaty Wording Clause Extraction and Drift Detection
#transformers #bert #large-language-models #word-embeddings #evaluation-metrics #compliance #automation

**Problem statement:** Extract and classify every clause in a treaty wording, align it with the expiring contract and the market model clause, and flag deviations that change what counts as one loss occurrence or what is excluded.

**ML task:** Clause segmentation and multi-class classification; semantic alignment of clause pairs across versions; deviation scoring against model clauses
**Input data:** Historical wordings and slips across cedents and years; market model clause libraries; claims files where wording disputes arose.
**Target:** Clause type per segment; aligned clause pairs; a materiality flag per deviation (changes event definition, reinstatement basis, exclusion scope).
**Evaluation metric:** Recall on material deviations, judged by wording specialists, is the binding metric: a missed hours-clause change can cost a reinstatement, while a false flag costs a minute. Measure review time per wording before and after.
**Scope:** 1 ML engineer and a wording specialist, ~4 months. Clause classification transfers well from legal language models, and the materiality layer needs specialist labels on a few hundred deviations.
**Data availability:** Every reinsurer holds its signed wordings; labelled deviations must be created by specialists, seeded from past disputes.

---

## 5. Event Loss Nowcasting and Loss Creep
#gaussian-processes #bayesian-inference #monte-carlo-methods #time-series-forecasting #evaluation-metrics #workflow-orchestration

**Problem statement:** In the first weeks after an event, estimate the reinsurer's ultimate loss by contract from vendor footprints, early industry estimates and cedents' first notifications, and predict how much the industry and cedent figures will creep upward as claims develop.

**ML task:** Bayesian updating of per-contract loss distributions as signals arrive; Gaussian-process regression of final-to-preliminary industry loss ratios on event type, peril, region and litigation environment, chosen because it gives calibrated uncertainty from few events; Monte Carlo propagation through treaty terms
**Input data:** Vendor event footprints and their revisions; PCS and PERILS preliminary and resurvey estimates; cedent notifications over time; in-force exposure and treaty terms; historical events with their development paths.
**Target:** Ultimate loss per contract and in aggregate, with intervals; expected creep from the first industry estimate to the final.
**Evaluation metric:** Calibration of the day-7 and day-30 interval against the loss reported 12–24 months later, and the bias of the point estimate. Under-estimation costs more than over-estimation: it becomes a reserve increase, a rating agency conversation and, for collateralised capital, a delayed release.
**Scope:** 2 data scientists and a cat modeller, ~6 months. The history is small (tens of major events per peril region), so models must be simple and priors explicit.
**Data availability:** Industry estimate histories are licensed from index providers; own-contract development is in the reinsurer's claims system but rarely stored as dated snapshots, which must start now.
