# Machine Learning Opportunities — Optometry Practices

**Industry:** [[optometry-practices|Optometry Practices]]
**Derived from:** [[problems/optometry-practices/high-impact|High Impact]], [[problems/optometry-practices/low-impact-1|Low Impact 1]], [[problems/optometry-practices/low-impact-2|Low Impact 2]], [[problems/optometry-practices/worker-life-1|Worker Life 1]], [[problems/optometry-practices/worker-life-2|Worker Life 2]]

---

## 1. Glaucoma Suspect Progression and Referral Model
#tacit-knowledge-ml #cnns #transfer-learning #survival-analysis #gradient-boosting #evaluation-metrics

**Problem statement:** Reproduce the experienced optometrist's read of a glaucoma suspect. From OCT, visual field, photographs and pressure history, predict each eye's risk of progression over the next two to three years. Flag the scans whose red normative flags are artefacts or myopic false positives, so the OD can watch, treat or refer with evidence.

**ML task:** Multimodal survival analysis (time to structural or functional progression) plus binary classification of artefact or myopic false positive per scan
**Input data:** OCT RNFL and ganglion-cell thickness maps and B-scans (Zeiss Cirrus, Topcon Maestro and Triton, Heidelberg Spectralis), threshold visual field series with reliability indices, disc and fundus photographs or Optomap images, IOP series, central corneal thickness, refraction and axial length, age, race, family history, and treatment start dates
**Target:** Time to progression by guided progression analysis or OCT trend, conversion to treatment, and the ophthalmologist's finding on referral where it can be retrieved; per-scan labels for segmentation error and myopic pattern
**Evaluation metric:** Time-dependent concordance and calibration of two-year progression risk. For referral triage, sensitivity at a fixed specificity, because missing a progressing eye costs permanent field loss while a false referral costs a visit and a patient. Report results separately for high myopes, where normative databases fail most.
**Scope:** A team of three to four (an imaging ML engineer, a data engineer and a part-time glaucoma-trained optometrist) over nine to twelve months for a single-device model inside one platform. Pretrain the image encoder on public fundus and OCT sets, then fine-tune on the platform's longitudinal records. The tacit-knowledge challenges are the hard part. On collection, the expert's call must be captured as a structured suspect record at the moment of the exam, not inferred from billing codes. On labelling, progression criteria disagree and doctors disagree with themselves on cup-to-disc ratio, so the labels need adjudication, and treatment censors the outcome. On deployment, the risk must appear inside the exam, from whatever device the practice owns, faster than the OD's own glance.
**Data availability:** Rollups (MyEyeDr., EyeCare Partners before its sale, AEG Vision) and multi-OD groups hold years of device exports, but under HIPAA and in vendor formats. Public sets give pretraining data, not outcomes: the University of Washington Humphrey field dataset, REFUGE and ORIGA glaucoma photographs, and OCT sets (recalled). The AAO IRIS Registry holds ophthalmology-side outcomes. Labelling needs optometrist and glaucoma-specialist adjudication on a few thousand eyes.

---

## 2. Routine-versus-Medical Visit Router
#gradient-boosting #large-language-models #bert #decision-trees #evaluation-metrics #revenue-impact

**Problem statement:** For each completed visit, recommend which payer gets which services (vision plan, medical plan, patient), with codes, modifiers and the refraction charge, and predict whether that split will be paid in full.

**ML task:** Multi-class classification of the payer split, plus binary classification of first-pass payment, with LLM extraction of chief complaint and findings from the note
**Input data:** Exam notes and structured findings, diagnosis and procedure codes, the patient's active coverages and coordination-of-benefits order, plan rules digested from provider manuals, and historical claims with remittance and adjustment codes, audit recoupments and appeals
**Target:** The split that was ultimately paid, and paid in full or not
**Evaluation metric:** Precision on medical-routing recommendations, because a wrong medical claim invites audit, plus dollars recovered per hundred visits against the practice's current routing. Measure calibration by plan.
**Scope:** A two-person team over three to four months for a single EHR's export. The work is mostly the plan-rules library and remittance parsing; the model itself is a gradient-boosted classifier with a small LLM front end. It must explain its split in one sentence a biller trusts.
**Data availability:** Each practice holds its own claims and remittances (HIPAA). EHR vendors and billing services see many practices. Vision-plan manuals sit behind network portals, so practices can read them but cannot republish them.

---

## 3. Visual Field and OCT Usability Check
#cnns #semantic-segmentation #logistic-regression #evaluation-metrics #worker-facing #automation

**Problem statement:** While the patient is still in the chair, tell the technician whether a visual field or OCT scan will be usable to the doctor, or should be repeated now.

**ML task:** Binary classification of usability per test, plus segmentation-error detection on OCT B-scans, plus regression of expected workup minutes for scheduling
**Input data:** Field reliability indices (false positives, false negatives, fixation losses), point-wise sensitivities and test duration; OCT signal strength, B-scans and segmentation lines; patient age and history; the doctor's later accept-or-repeat decision
**Target:** Whether the doctor accepted the result or ordered a repeat; manually marked segmentation errors
**Evaluation metric:** Recall on unusable results, since a missed bad field costs a return visit, at a repeat-now rate the schedule can absorb. Track minutes saved per technician-day.
**Scope:** A small team over three to five months. Field reliability is tabular and quick. OCT segmentation-error detection needs a few thousand marked scans and a CNN per device family. Device APIs and exports are the integration risk.
**Data availability:** Devices store the raw tests, and practices hold the accept-or-repeat history implicitly in their charts. Labels need a technician supervisor or OD to mark several thousand tests.

---

## 4. Myopia Progression Forecaster for Children
#gaussian-processes #bayesian-inference #time-series-forecasting #regularization #evaluation-metrics #worker-facing

**Problem statement:** Forecast each child's axial length and refraction over the next one to three years, with and without treatment, so the OD can set expectations, judge whether a treatment is working and change course early.

**ML task:** Probabilistic time-series forecasting of axial length and spherical equivalent with a treatment covariate (hierarchical Gaussian process or Bayesian mixed-effects growth model)
**Input data:** Serial axial length (optical biometers such as the Topcon Myah or Zeiss IOLMaster), cycloplegic refraction, age, sex, ethnicity, parental myopia, time outdoors and near work where recorded, treatment type and start date (MiSight, Stellest, orthokeratology, atropine), and adherence
**Target:** Axial length and refraction at future visits, with prediction intervals
**Evaluation metric:** Mean absolute error of one-year axial growth, with interval coverage. The clinically useful threshold is detecting a child growing faster than expected for their treatment within one visit.
**Scope:** One to two people over three months for a working forecaster, with a growth-chart user interface. The model is small. The limit is data: few practices measure axial length routinely, and treatment effect estimates differ by product and population.
**Data availability:** Published growth curves and trial arms give priors. Myopia clinics and lens makers' programmes hold serial measurements, but under HIPAA and programme agreements. A practice can start from its own records.

---

## 5. Contact Lens Verification and Release Triage
#large-language-models #transformers #bert #naive-bayes #compliance #automation

**Problem statement:** Read every incoming seller verification request (fax, email or recorded robocall) and every prescription release event. Match each to the patient's current contact lens prescription and draft the correct response before the FTC Contact Lens Rule's eight-business-hour window closes.

**ML task:** Document and speech-to-text extraction, entity matching to the patient and prescription, and classification of the response (valid, invalid with reason, expired, wrong brand or parameters)
**Input data:** Faxed and emailed verification requests, robocall recordings, the EHR's contact lens prescriptions and fitting notes, release confirmations, and seller identities
**Target:** The correct response and reason, plus a flag for any request that would lapse into passive verification
**Evaluation metric:** Share of requests answered correctly inside eight business hours, with zero wrong-patient matches. A wrong verification is worse than a late one, because it puts the wrong lens on an eye.
**Scope:** A two-person team over two to three months for one EHR. Speech-to-text on robocalls and patient matching on partial details are the hard parts. Drafting the response itself is easy.
**Data availability:** Every practice receives these requests daily (volumes are an estimate). The prescriptions sit in the EHR. Labelled examples can be built from the practice's own past responses.
