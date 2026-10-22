# Machine Learning Opportunities — Outdoor Advertising Companies

**Industry:** [[outdoor-advertising-companies|Outdoor Advertising Companies]]
**Derived from:** [[problems/outdoor-advertising-companies/high-impact|High Impact]], [[problems/outdoor-advertising-companies/low-impact-1|Low Impact 1]], [[problems/outdoor-advertising-companies/low-impact-2|Low Impact 2]], [[problems/outdoor-advertising-companies/worker-life-1|Worker Life 1]], [[problems/outdoor-advertising-companies/worker-life-2|Worker Life 2]]

---

## 1. Learning the Real Estate Manager's Read of a Location
#tacit-knowledge-ml #gradient-boosting #cnns #transfer-learning #feature-engineering #evaluation-metrics #revenue-impact

**Problem statement:** Senior real estate managers judge, from a drive-by, what a location will earn and whether a static face is worth converting to digital, a judgement they cannot specify and that leaves when they do. The ML problem is to learn location yield from the operator's own billing history and site attributes, capture the expert's decision-time read alongside it, and give every manager a desk-side estimate with reasons.

**ML task:** Regression of relative face yield (occupancy-weighted net rate against the market's own faces) plus a separate uplift model for static-to-digital conversion; image models for read time and obstruction from street-level and dashcam imagery feed both
**Input data:** Per-face contract, occupancy, rate and digital loop sell-through history (years per face, tens of thousands of faces at a large operator); site geometry (setback, height, angle to the roadway, read side); traffic counts, posted speed, signal locations; Geopath impressions; nearby competitive faces; advertiser categories in the trade area from business listings; street-level imagery and crew dashcam video of the approach; permit and spacing constraints; the manager's structured site score and notes at decision time, captured going forward.
**Target:** Relative yield over the next 12–36 months; post-conversion revenue multiple for digital candidates; agreement between the model's ranking and the manager's.
**Evaluation metric:** Rank correlation between predicted and realised relative yield on faces held out by market and by time, since a model validated on random faces within a market is copying neighbours. For conversions, the realised uplift of the model's top-decile picks against the manager's picks over the same period. Report the manager's own test-retest consistency on a re-scored sample as the ceiling. Under-predicting a great site costs an opportunity; over-predicting a conversion costs ~$200,000, so precision at the top of the ranking matters more than overall fit.
**Scope:** Data collection comes first and is the hardest part. The billing history exists but has to be joined face by face to site attributes and imagery. The expert's read has to be captured when the decision is made, through a one-minute structured score and voice note in the approval workflow, because reconstructing it later produces hindsight. Labelling is difficult because revenue is confounded by the account executive, the market cycle and pricing policy, so labels must be relative within market and period, and managers' repeated scores on a sample are needed to measure their consistency. Deployment only works if the tool is faster than a drive: it ranks hundreds of candidate parcels or conversion candidates at a desk, shows the comparable faces behind each estimate, and leaves the final drive to the expert. 2 ML engineers, 1 data engineer and a senior real estate manager as domain lead, 6–9 months to a usable ranking in two or three markets; the graded expert record takes two to three years to mature.
**Data availability:** Large operators hold the decisive asset, their own per-face revenue history, and rarely join it to site data. Imagery is licensable; traffic counts are public from state DOTs; Geopath data comes with membership. Independents have too few faces to train alone, which argues for a pooled model sold to them.

---

## 2. Structure and Posting Inspection From Crew Photos
#cnns #object-detection #semantic-segmentation #transfer-learning #evaluation-metrics #worker-facing #automation

**Problem statement:** Every posting produces a proof photo that is checked by eye, if at all. The same photo could confirm the right creative is on the right face and reveal structural defects (corrosion, missing guardrail, damaged catwalk, lamps out, torn vinyl, encroaching vegetation) that are now reported only when a crew remembers to.

**ML task:** Creative verification by image matching against the contracted artwork; multi-label defect detection and segmentation on structure photos
**Input data:** Proof-of-posting photos with face ID, GPS and timestamp; contracted creative files; maintenance work orders and structural inspection reports as weak labels; a labelled sample of defect photos from structural engineers.
**Target:** Match / mismatch / wrong face for each posting; defect classes with bounding boxes or masks and a severity grade.
**Evaluation metric:** For creative verification, false-accept rate on wrong postings (each one becomes a makegood) at a false-reject rate crews will tolerate. For defects, recall on safety-critical classes (guardrail, catwalk, ladder) is binding; a missed failing catwalk is an injury risk, while a false flag costs an inspection visit.
**Scope:** Verification is a quick win with off-the-shelf image matching. Defect detection needs a few thousand labelled images; proof photos are framed for the advertiser, not the structure, so the capture protocol needs one extra structure shot per visit. 1 ML engineer and 1 mobile engineer, 4 months for verification, a further 4–6 for defects.
**Data availability:** Operators hold millions of proof photos; defect labels must be created, and work orders give noisy ones.

---

## 3. Ground Lease Renewal and Loss Risk
#survival-analysis #gradient-boosting #feature-engineering #large-language-models #data-integration #revenue-impact

**Problem statement:** Predict which ground leases are at risk of non-renewal, a large rent demand or assignment to a lease aggregator, early enough for the real estate team to renegotiate, buy the land or secure an easement first.

**ML task:** Time-to-event modelling of lease loss and rent reset, with lease terms extracted from documents by a language model
**Input data:** Lease documents and amendments (term, options, escalators, percentage-rent clauses, notice and sale provisions); payment history; landlord type and changes of ownership from county records; face revenue against rent; buyout solicitations landlords forward; local development and rezoning activity.
**Target:** Time to non-renewal, assignment or rent increase above a threshold; size of the rent increase.
**Evaluation metric:** Concordance index and time-dependent AUC at 12 and 24 months, measured on later years. Recall on high-revenue sites matters most: losing a top-decile site is expensive and usually permanent, and an unnecessary early renegotiation costs little.
**Scope:** Extraction is the bulk of the work, across tens of thousands of scanned leases with decades of amendments. 1 ML engineer and 1 data engineer with a real estate administrator, 5–6 months.
**Data availability:** Lease files and payment history are internal; ownership changes are public; aggregator approaches are seen only when landlords report them.

---

## 4. Digital Loop Demand Forecasting and Pricing
#time-series-forecasting #temporal-fusion-transformers #bayesian-inference #gradient-boosting #revenue-impact #automation

**Problem statement:** Forecast sold share of each digital face's loop by week and daypart across direct and programmatic demand, and set rate cards and programmatic floors that fill the loop without undercutting direct sales.

**ML task:** Hierarchical multi-horizon forecasting of sell-through and clearing price, with price-response estimation
**Input data:** Loop occupancy and rates by face, week and daypart; booking pace curves; programmatic bid and clearing data from the supply platform; seasonality, local events and category demand; Geopath impressions by daypart.
**Target:** Sold share and average rate 1–26 weeks ahead; expected revenue at candidate prices.
**Evaluation metric:** Weighted absolute percentage error on revenue at the market level, and realised yield against the prior pricing policy in a holdout of markets, because forecast accuracy alone doesn't show that the pricing improved.
**Scope:** Booking-pace data needs cleaning from contract systems; price experiments need sales leadership's consent. 2 data scientists, 5 months.
**Data availability:** Internal, and good at the large operators; thin at independents.

---

## 5. Creative Compliance Classification for Digital Faces
#large-language-models #transformers #cnns #k-nearest-neighbors #compliance #workflow-orchestration #automation

**Problem statement:** Classify each creative entering a digital loop by category, claims and disclosures, and check it against the face's rule set: proximity restrictions, state display rules, lease restrictions, political disclosure requirements and sold exclusivities.

**ML task:** Multimodal classification of category and attributes, text extraction from the creative, and rule evaluation against a per-face registry
**Input data:** Creative image files; advertiser metadata; historical approval and rejection decisions with reasons; per-face rules built from codes, GIS buffers and lease clauses.
**Target:** Category labels, detected disclosures, legibility score at read distance, approve / flag with the specific rule cited.
**Evaluation metric:** Recall on creatives that a human reviewer would reject is binding: a cannabis ad near a school or a missing political disclaimer has legal consequences, while a false flag costs a reviewer a few seconds. Track reviewer time per creative before and after.
**Scope:** The models are available off the shelf; the rule registry is the real work and has to be maintained as codes change. 1 ML engineer, 1 engineer and a compliance lead, 4 months.
**Data availability:** Approval logs exist at large operators but rarely record reasons; capture them going forward.
