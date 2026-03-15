# Machine Learning Opportunities — Plumbing Contractors

**Industry:** [[plumbing-contractors|Plumbing Contractors]]
**Derived from:** [[problems/plumbing-contractors/high-impact|High Impact]], [[problems/plumbing-contractors/low-impact-1|Low Impact 1]], [[problems/plumbing-contractors/low-impact-2|Low Impact 2]], [[problems/plumbing-contractors/worker-life-1|Worker Life 1]], [[problems/plumbing-contractors/worker-life-2|Worker Life 2]]

---

## 1. Sewer Pipe Defect Detection from Inspection Camera Video
#cnn #object-detection #semantic-segmentation #computer-vision #tacit-knowledge-ml

**Problem statement:** Experienced drain technicians identify pipe defects (root intrusion, cracking, offset, belly, grease accumulation, pipe material degradation) by watching sewer camera video footage — a visual pattern recognition skill built from thousands of camera runs. A convolutional model trained on labeled inspection footage can replicate this per-frame defect detection for residential and commercial plumbing pipe diameters (3"-6"), enabling junior technicians to produce expert-quality condition assessments.

**ML task:** Multi-label object detection per video frame: root intrusion (light/moderate/heavy), circumferential crack, longitudinal crack, pipe offset (degrees), belly/sag, grease accumulation, debris blockage, pipe material identification; temporal aggregation across frames to produce a condition report by footage position
**Input data:** Sewer inspection camera footage (MP4/AVI) with frame-level defect annotations by certified drain technicians. PACP coding standard serves as the defect taxonomy. Labeled dataset needs to cover multiple pipe materials (PVC, cast iron, clay tile, orangeburg, ABS) and pipe diameters (3" to 6" residential, up to 12" light commercial).
**Target:** Per-frame defect classification with confidence scores; aggregated inspection report with defect list, footage timestamp/position, severity rating per defect, recommended action tier (monitor / schedule repair / urgent)
**Evaluation metric:** Recall > 0.85 on structural defects (cracks, offsets that require repair); precision > 0.80 to maintain technician trust; PACP agreement rate between model and certified human reviewer; false positive rate on clean footage
**Scope:** Municipal sewer AI (Envirosight, WinCan AI) has demonstrated this is solvable for large infrastructure pipes. Residential plumbing requires a new labeled dataset focused on smaller diameters and residential defect distributions. Dataset assembly (10,000-30,000 labeled frames across diverse conditions) is the primary project scope. Training a fine-tuned YOLOv8 or Detectron2 model on this dataset: 12-18 months end-to-end. A data partnership with a major sewer inspection camera manufacturer (RIDGID, Spartan) would provide both dataset access and distribution.
**Data availability:** Sewer inspection footage exists at every plumbing company using camera inspection. Creating labeled training data requires PACP-certified technician annotation. A consortium of 10-20 plumbing contractors annotating their historical footage could assemble a sufficient training dataset.

---

## 2. Plumbing Fault Acoustic Signature Classification
#cnn #multiclass-classification #signal-processing #tacit-knowledge-ml #quick-win

**Problem statement:** Experienced plumbers diagnose plumbing system faults partially through acoustic cues — water hammer (banging pipes on valve closure), cavitation (hissing/vibration from undersized lines or pump issues), pipe vibration indicating loose hangers, the specific sound of a running toilet flapper leak, or the pressure surge pattern of a failing pressure reducing valve. Capture and classify these acoustic signatures to support remote diagnosis and apprentice training.

**ML task:** Multiclass audio classification (fault type from acoustic recording) — diagnosis from 10-20 common plumbing fault acoustic signatures
**Input data:** Acoustic recordings of plumbing system sounds at pipes, fixtures, and mechanical equipment, labeled by fault type by master plumbers. Recording device: smartphone placed against the pipe or near the fixture. Fault types: water hammer, cavitation, loose hanger vibration, toilet flapper running, PRV failure, drain partial blockage (gurgling), copper expansion (ticking), and normal operation baseline.
**Target:** Fault type classification with confidence score; ranked differential diagnosis for ambiguous recordings; recommended next diagnostic step
**Evaluation metric:** Top-1 accuracy on held-out labeled recordings; master plumber agreement rate; reduction in diagnostic time for technicians using acoustic classification vs. unaided
**Scope:** Acoustic data collection is low-cost — technicians record sounds with their phone during service calls, master plumbers annotate. 500-1,000 labeled recordings per fault type is sufficient for a CNN audio classifier (spectrogram input). Training on mel-spectrograms with a pre-trained audio classification backbone (VGGish, YAMNet fine-tuned) is achievable in 6-8 weeks with sufficient labeled data. Data collection is the primary timeline driver.
**Data availability:** No existing labeled plumbing acoustic dataset. Requires prospective collection by a consortium of plumbing firms. A well-structured 6-month data collection campaign across 5-10 active plumbing firms can generate sufficient training data. The fault types are common — most firms encounter each category weekly.

---

## 3. Service Call Outcome and Upsell Prediction
#gradient-boosting #binary-classification #tabular-ml #revenue-impact

**Problem statement:** Predict which service calls are likely to result in a repair authorization (vs. customer declining), and which calls present the highest-probability upsell opportunity (customer approves additional recommended work) — enabling smarter dispatching and technician preparation.

**ML task:** Binary classification (repair authorized: yes/no); separate binary classification (upsell approved: yes/no) from service call intake data
**Input data:** Service call history: service type (drain clearing, leak repair, water heater repair, etc.), customer type (owner vs. renter, residential vs. commercial), property age, time since last service call, technician assigned, how the call was initiated (repeat vs. new customer), season, call urgency (emergency vs. scheduled)
**Target:** Authorization probability per incoming service call; upsell opportunity score for specific add-on services (water heater replacement, whole-home repiping evaluation, water softener recommendation)
**Evaluation metric:** AUC-ROC for authorization prediction; precision at top-20% upsell flag (technician preparation overhead); revenue per service call correlation with upsell score
**Scope:** Any plumbing firm with 2,000+ service call records with outcomes has training data. ServiceTitan logs all of this data. Gradient boosting on structured call features: 3-4 week project. Technician coaching integration (briefing the tech on likely upsell opportunities before the call) is the implementation step with the highest business impact.
**Data availability:** ServiceTitan and similar platforms log service call type, customer, outcome, and revenue. Authorization rates are computable from invoice status. Upsell labels require that add-on work is logged separately from the primary call — available in firms with disciplined service code usage.

---

## 4. Water Leak Origin Localization from Stain Pattern Analysis
#cnn #regression #computer-vision #tacit-knowledge-ml

**Problem statement:** Experienced plumbers can look at a water stain on a ceiling or wall and estimate the likely pipe run responsible — using the stain shape, color progression, and location relative to known plumbing fixtures to triangulate the leak source before cutting drywall. A computer vision model can replicate this spatial reasoning from photos to reduce unnecessary destructive investigation.

**ML task:** Regression/localization — given a photo of a water stain on a ceiling or wall and the building's rough plumbing layout (floor plan with fixture locations), predict the most likely pipe segment responsible and the probability distribution across possible sources
**Input data:** Photos of water stain damage labeled with confirmed leak source by master plumbers who investigated the stain. Building context (fixture layout, floor where stain appears, floor above fixture locations).
**Target:** Ranked probability list of likely leak sources (specific pipe segment or fixture) with confidence; recommended investigation sequence (where to look first)
**Evaluation metric:** Top-1 accuracy on confirmed leak source vs. model prediction; recall on "urgent" cases (structural water damage sources); reduction in drywall opening required to locate leak vs. unaided investigation
**Scope:** Stain pattern data requires prospective collection with labeled outcomes — master plumber labels the stain photo with the confirmed source after investigation. 1,000-2,000 labeled case sets provides training signal. The model must be multimodal (image + structural context). 10-14 week project once sufficient data is assembled. A longer-term data collection program is needed first.
**Data availability:** Plumbing firms investigate water intrusion regularly. Systematic documentation (photo before investigation + confirmed source after) requires a process change but low technology investment. A firm doing 5 water intrusion investigations per week can assemble 250+ labeled cases per year.

---

## 5. Predictive Maintenance Scheduling for Residential Water Heaters and Drains
#gradient-boosting #survival-analysis #tabular-ml #revenue-impact

**Problem statement:** Predict which water heaters in a plumbing firm's customer base are approaching failure (based on age, model, installation environment, and service history) — enabling proactive replacement outreach before the customer calls at 9pm with no hot water, and scheduling drain maintenance before a backup occurs.

**ML task:** Survival analysis (time-to-failure) for water heaters; binary classification (drain backup within 90 days: yes/no) for customers with prior drain service history
**Input data:** Customer service history: water heater installation date and model (age + manufacturer failure rates), prior drain service frequency and severity, property age, known hard water conditions (affects water heater anode rod lifespan), any prior water heater service calls
**Target:** Water heater replacement probability score per customer over next 12 months; drain maintenance recommendation flag for high-frequency customers approaching next likely backup
**Evaluation metric:** Recall on customers who called for emergency water heater replacement (did we flag them as high-risk in the prior 6 months?); proactive outreach conversion rate (of flagged customers contacted, what % agreed to proactive service?); revenue from proactive vs. reactive service calls
**Scope:** A plumbing firm with 3+ years of service history and 1,000+ customer records has sufficient data. Gradient boosting survival model on structured customer history: 4-6 week project. The business model innovation (proactive outreach vs. waiting for emergency calls) is as important as the model — proactive replacements are scheduled and profitable; emergency calls are disruptive and competitively margin-pressured.
**Data availability:** ServiceTitan logs all service history with equipment type and date. Water heater installation records are in the job completion notes. Model and age data may require parsing from service notes — a data extraction step. HVACR failure rate databases provide population-level failure priors by model.
