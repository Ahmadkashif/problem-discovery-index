# Machine Learning Opportunities — Dental Practices

**Industry:** [[dental-practices|Dental Practices]]
**Derived from:** [[problems/dental-practices/high-impact|High Impact]], [[problems/dental-practices/low-impact-1|Low Impact 1]], [[problems/dental-practices/low-impact-2|Low Impact 2]], [[problems/dental-practices/worker-life-1|Worker Life 1]], [[problems/dental-practices/worker-life-2|Worker Life 2]]

---

## 1. Dental Benefit Extraction from Payer Portals
#ml-nlp #revenue-impact #quick-win

**Problem statement:** Given raw benefit summary pages from dental payer portals (HTML, PDF, or screen-scraped text), extract structured benefit details — annual maximum, remaining balance, deductible status, coverage percentages by category, frequency limitations, and waiting periods — into a standardized schema.

**ML task:** Document information extraction (NER + relation extraction)
**Input data:** Benefit summary pages from dental payer portals (semi-structured text/HTML)
**Target:** Structured benefit object: {annual_max, remaining_max, deductible, deductible_met, coverage_preventive_pct, coverage_basic_pct, coverage_major_pct, frequency_limits[], waiting_periods[], missing_tooth_clause}
**Evaluation metric:** Field-level extraction accuracy (must exceed 95% for financial fields); end-to-end extraction completeness rate
**Scope:** Quick win. Payer portal formats are semi-structured and repetitive — a fine-tuned extraction model or even regex + LLM hybrid works well. Start with the top 10 dental payers (covers 80% of patients). 4-6 week project per payer, parallelizable.
**Data availability:** Any dental office can provide screenshots/exports from the payer portals they use daily. 50-100 examples per payer is enough to build reliable extraction rules.

---

## 2. Treatment Acceptance Prediction
#ml-classification #revenue-impact

**Problem statement:** Given a treatment plan presentation (procedures, estimated cost, patient demographics, insurance coverage level, payment plan availability), predict whether the patient will accept the treatment — allowing the practice to prioritize follow-up and tailor the financial presentation.

**ML task:** Binary classification
**Input data:** Treatment plan details (procedures, total cost, patient responsibility), patient demographics (age, zip code, insurance type), historical acceptance decisions
**Target:** Binary: treatment_accepted (yes/no); secondary: predicted acceptance probability for case prioritization
**Evaluation metric:** AUROC; calibration (probability estimates must be reliable for prioritization)
**Scope:** Practices track treatment plan presentations and outcomes in their PMS. A logistic regression on cost, insurance coverage level, and procedure type is a strong baseline. 3-4 week project with 1,000+ treatment plan records.
**Data availability:** Dental PMS systems log presented treatment plans and whether they were scheduled. Most practices have 2-3 years of this data.

---

## 3. Dental Radiograph Pathology Detection Assistance
#ml-computer-vision #quick-win

**Problem statement:** Given a dental radiograph (bitewing, periapical, or panoramic), detect and highlight regions of interest — caries (cavities), periapical lesions, bone loss, and calculus — to assist the dentist's visual review.

**ML task:** Object detection / semantic segmentation on dental X-rays
**Input data:** Digital dental radiographs (DICOM or JPEG)
**Target:** Bounding boxes or segmentation masks for: caries, periapical_lesion, bone_loss, calculus, with confidence scores
**Evaluation metric:** mAP (mean average precision) at IoU 0.5; sensitivity (must catch real pathology) > 90%; specificity (don't flag too many false positives) > 85%
**Scope:** This is an active area of dental AI with published models (Overjet, Pearl, VideaHealth). For a smaller-scoped project, train a detection model on a public dental radiograph dataset (UFBA-UESC, Tufts Dental) as a proof-of-concept. 6-8 week project for a focused model on bitewing caries detection.
**Data availability:** Public datasets exist. For production, a practice's archive of labeled radiographs (where the dentist has documented findings in the chart) provides implicit labels.

---

## 4. Procedure-to-CDT Code Mapping from Voice
#ml-nlp #worker-facing #automation

**Problem statement:** Given the dentist's verbal callouts during a procedure ("prepping tooth 19 for an MO composite"), map the spoken description to the correct CDT procedure codes and charting entries.

**ML task:** Speech-to-structured-data (ASR + NER + code mapping)
**Input data:** Dentist's verbal procedure narration (audio → transcribed text)
**Target:** Structured output: {tooth_number, surfaces, procedure_type, CDT_code, materials_used}
**Evaluation metric:** Exact-match accuracy for CDT code; tooth number accuracy; surface accuracy
**Scope:** The dental terminology is specialized but finite — there are ~600 commonly used CDT codes and a fixed tooth numbering system. An ASR model (Whisper) + a fine-tuned NER model for dental entities + a lookup table for CDT mapping is a viable v1. 8-10 week project.
**Data availability:** Training data would need to be collected by recording (with consent) procedure narrations and pairing them with the charted procedures. 200-500 annotated narrations is sufficient for v1.

---

## 5. Insurance Calendar-Year Optimization
#ml-optimization #revenue-impact #quick-win

**Problem statement:** Given a patient's treatment plan, remaining insurance benefits, and benefit reset date, generate a treatment sequencing recommendation that maximizes insurance utilization across calendar years — e.g., "do the crown in December (uses this year's remaining $800), then the implant in January (next year's full $1,500 maximum)."

**ML task:** Constrained optimization (not strictly ML, but benefits from learned patient no-show/delay patterns)
**Input data:** Treatment plan with procedures and costs, patient's remaining benefits + maximum reset date, historical patient scheduling patterns (do they actually come back in January?)
**Target:** Optimized treatment sequence with estimated patient savings and scheduling recommendations
**Evaluation metric:** Patient out-of-pocket savings vs. unoptimized sequencing; patient adherence to recommended schedule
**Scope:** Genuine quick win. The optimization is deterministic once benefits are known — the ML layer adds patient behavior prediction (will they actually follow the recommended schedule?). 3-4 week project for the optimizer; additional 2-3 weeks for the behavior prediction layer.
**Data availability:** Treatment plans, benefit information, and scheduling history are all in the PMS.
