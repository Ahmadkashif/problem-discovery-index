# Machine Learning Opportunities — Specialty Design Studios

**Industry:** [[specialty-design-studios|Specialty Design Studios]]
**Derived from:** [[problems/specialty-design-studios/high-impact|High Impact]], [[problems/specialty-design-studios/low-impact-1|Low Impact 1]], [[problems/specialty-design-studios/low-impact-2|Low Impact 2]], [[problems/specialty-design-studios/worker-life-1|Worker Life 1]], [[problems/specialty-design-studios/worker-life-2|Worker Life 2]]

---

## 1. Learning the Technical Designer's Fit Correction
#tacit-knowledge-ml #cnns #semantic-segmentation #transfer-learning #gradient-boosting #evaluation-metrics #worker-facing #revenue-impact

**Problem statement:** A senior technical designer looks at a sample on a fit model and prescribes the pattern correction that converges in one round; a junior describes the wrinkle and the factory fixes the wrong piece. The ML problem is to learn the mapping from what the sample shows (images and measured deviations) to the correction that worked, using the next round's outcome as the label.

**ML task:** (a) Semantic segmentation of fit faults — drag lines, folds, strain, gaping, twisting — by garment region in multi-view sample photographs; (b) ranked prediction of pattern corrections (point-of-measure deltas and named operations such as "lower armhole" or "add to back rise") from the segmented faults, measured deviations, fabric, block and category, with a calibrated probability that each converges next round.
**Input data:** Front, side and back photographs of each fit sample on a known fit model or form; measured points of measure against spec and tolerance; that round's fit comments; fabric composition, weight and stretch; base block and grade; factory; and the next round's measurements and fit decision.
**Target:** Region-level fault masks; the correction set issued by the technical designer; and the outcome label — whether the next sample measured in tolerance and passed fit review on the corrected points.
**Evaluation metric:** For the correction ranker, top-3 hit rate against corrections that converged, scored separately from corrections the expert issued that did not converge — matching the expert's failures is not success. Report agreement with held-out senior technical designers against those seniors' own test-retest agreement on re-shown sessions as the ceiling. The asymmetric cost: a confidently wrong correction sent to a factory costs a full round and a month of calendar, so precision at the auto-suggest threshold matters more than coverage; low-confidence cases must fall back to the expert.
**Scope:** The data collection challenge comes first: the expert's read must be captured as it happens, which needs a fit-room capture app with fixed-view photo guides, voice dictation of comments, and automatic linking of each round to the next — without it there is no corpus, because studios' existing photographs are inconsistent and separated from outcomes. The labelling challenge is that experts disagree with themselves and with each other, and several different corrections can each work; labels must be outcome-graded, and a sample of sessions must be re-shown to the same and other experts to measure reliability. The deployment challenge is speed: suggestions must appear on a phone in the fit room within seconds, in the technical designer's vocabulary and the factory's units, or they will be ignored. Segmentation can start from pretrained garment-parsing networks; the correction model should be a gradient-boosted ranker over structured features before anything deeper. 2 ML engineers, 1 product engineer and a senior technical designer as domain lead, 9–12 months to a useful ranker for one category (knit tops or denim), with retrieval of similar past sessions useful within the first three months.
**Data availability:** Effectively none in usable form. Brands own most fit records under work-for-hire terms and studios keep inconsistent photo folders, so a studio, brand or 3D/PLM vendor must collect prospectively, with retention rights in the contract. Outcome labels are cheap once rounds are linked.

---

## 2. Predicting the Colourist's Lab-Dip Approval
#tacit-knowledge-ml #logistic-regression #gaussian-processes #feature-engineering #evaluation-metrics #automation

**Problem statement:** Lab dips are approved or rejected by a colourist viewing them in a light booth under several illuminants, and instrumental colour difference thresholds disagree with those visual decisions often enough that brands still look at every dip. Predict the colourist's decision from spectrophotometer data and context, so clear passes and clear fails are decided instantly and only borderline dips reach the light booth.

**ML task:** Binary classification (approve / reject) with a calibrated probability and a reason code (hue, chroma, lightness or metamerism under a named illuminant)
**Input data:** Reflectance spectra of the standard and each submitted dip; computed colour differences under D65, TL84, incandescent A and other specified illuminants; substrate, fibre and dye class; colour family; the mill; the submission round; and the colourist's recorded decision and comment.
**Target:** The colourist's approve/reject decision and the stated reason.
**Evaluation metric:** Precision on auto-approvals is binding — an auto-approved dip that the colourist would have rejected ships the wrong colour into bulk — so report precision at the threshold where dips are approved without viewing, plus the share of dips that threshold removes from the light booth. Agreement with the colourist's own repeat decisions on re-submitted identical dips sets the ceiling.
**Scope:** Instrument data is already digital and decisions are recorded per dip, so the corpus may exist; the work is joining spectra to decisions and modelling colour-family tolerances — a Gaussian process over colour space captures that a navy and a pale pink tolerate different numeric differences. 1 colour scientist and 1 ML engineer, 4–6 months for one palette.
**Data availability:** Held by colour standards and approval services, large brands' colour departments and dye houses; each brand's standards are its own, which limits pooling across brands.

---

## 3. Tech Pack Ambiguity Before It Becomes a Factory Question
#large-language-models #bert #logistic-regression #feature-engineering #evaluation-metrics #quick-win

**Problem statement:** Incomplete or ambiguous tech packs — a point of measure without a tolerance, an unspecified trim, a construction callout open to two readings, a prior-round comment not carried forward — generate factory questions and wrong samples. Score each line of a tech pack for the risk that it will produce a factory query or a sample error, before it ships.

**ML task:** Line-level text classification of tech pack callouts, measurement rows and BOM entries for ambiguity and incompleteness, plus a pack-level probability of a factory query or round-one sample error
**Input data:** Historical tech packs (PDF, Excel or PLM exports) with their factory question threads, sample error reports and round counts; the studio's or brand's construction vocabulary; BOM and trim libraries.
**Target:** For each line, whether it generated a factory question or a sample deviation; for each pack, query count and round-one pass/fail.
**Evaluation metric:** Recall on lines that later caused a sample error, at a flag rate the technical designer will tolerate (for example, no more than a handful of flags per pack); report reduction in factory queries per style before and after.
**Scope:** A language model extracts and normalises callouts; a fine-tuned BERT-class classifier or logistic regression scores risk; rules catch mechanical gaps such as a missing tolerance. 1 ML engineer, 3–4 months, given a few thousand historical packs with their question threads.
**Data availability:** PLM vendors and large studios hold packs and question threads; the join between a pack line and the question it caused must be reconstructed from chat and email, which is most of the labelling effort.

---

## 4. Fabric Drape Parameters From a Swatch, Not a Lab
#cnns #gaussian-processes #bayesian-optimization #transfer-learning #evaluation-metrics #automation

**Problem statement:** 3D garment simulation only replaces a physical sampling round if the fabric behaves in the simulator as it does on the body, which requires measured bending, stretch, shear and friction parameters most mills and studios do not have. Predict simulation parameters from a fabric's specification sheet, a photograph and a cheap drape test, and refine them against a single physical sample.

**ML task:** Multi-output regression from fabric features and images to simulator physics parameters, with Bayesian optimisation to calibrate against an observed drape or sample photograph
**Input data:** Fibre composition, weight, construction and finish; macro photographs of the swatch; a drape-test image where available; measured parameters for fabrics already digitised; physical sample photographs paired with their 3D simulations.
**Target:** Simulator parameter set per fabric; drape silhouette agreement between simulation and the physical sample.
**Evaluation metric:** Silhouette and fold agreement between simulated and physical drape (mask intersection-over-union in the same pose), and whether fit decisions made on the simulation match those made on the physical sample. Errors that hide drag lines cost more than errors that exaggerate stiffness, because they approve a sample that needed correcting.
**Scope:** The pairs of measured parameters and swatch data exist at 3D vendors and digitisation services; a Gaussian process surrogate over the simulator keeps calibration tractable. 2 ML engineers with simulation experience, 6–9 months.
**Data availability:** Concentrated at 3D software vendors and fabric digitisation services; studios hold physical samples and photographs but rarely the measured parameters.

---

## 5. Install Labour and Drayage Estimation From Exhibit Drawings
#gradient-boosting #random-forests #feature-engineering #confidence-intervals #evaluation-metrics #revenue-impact

**Problem statement:** Exhibit houses quote installation and dismantle labour and drayage from experience, and the floor bills actual hours at union rates. Predict labour hours and crated weight for a booth design from its drawings and component list, with an interval, using the house's own past installs.

**ML task:** Regression of install hours, dismantle hours and drayage weight with quantile intervals
**Input data:** Component counts and connection types from the 3D model; footprint and height; hanging signs, flooring and electrical; venue and labour jurisdiction; crew size; hours and weights invoiced on past shows.
**Target:** Actual labour hours by phase and actual billed weight.
**Evaluation metric:** Mean absolute percentage error on hours against the house's current estimators, and coverage of the 80% interval. Under-estimates cost more than over-estimates, because they surface as client budget overruns on the floor.
**Scope:** A modest, valuable model for a house with a few hundred past installs. 1 data scientist, 3 months, once component lists are extracted from models consistently.
**Data availability:** Exhibit houses hold drawings and invoiced labour; general service contractors hold labour and drayage billing across exhibitors but under the show organiser's and exhibitor's terms.
