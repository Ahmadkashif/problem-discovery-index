# Machine Learning Opportunities — Home Inspection

**Industry:** [[home-inspection|Home Inspection]]
**Derived from:** [[problems/home-inspection/high-impact|High Impact]], [[problems/home-inspection/low-impact-1|Low Impact 1]], [[problems/home-inspection/low-impact-2|Low Impact 2]], [[problems/home-inspection/worker-life-1|Worker Life 1]], [[problems/home-inspection/worker-life-2|Worker Life 2]]

---

## 1. Multi-System Defect Detection from Inspection Photos
#cnns #object-detection #transfer-learning #loss-functions #backpropagation #evaluation-metrics #gradient-descent #matrix-algebra #feature-engineering #tacit-knowledge-ml

**Problem statement:** Experienced home inspectors read subtle visual defect evidence across 15 building systems — a multi-domain visual pattern recognition skill built from hundreds of inspections. A computer vision model trained on labeled inspection photos can provide a second-pass review of the inspector's photo record, flagging potential defects that the inspector photographed but didn't consciously register during the inspection.

**ML task:** Multi-system object detection and classification — defect type per photo from electrical, structural, roofing, plumbing, and exterior inspection categories. Per-photo output: defect present (yes/no), defect type, confidence score, bounding box of defect location in photo
**Input data:** Spectora inspection photos paired with the corresponding report narrative (defect descriptions written by the inspector for that photo). Natural language processing of the report narrative provides defect type labels for each photo. Initial focus: electrical panel photos, roofing photos, foundation photos (three systems with strongest visual signal).
**Target:** Defect flag per photo with defect type and confidence; sorted list of flagged photos for inspector review before report finalization
**Evaluation metric:** Recall on defects noted in report for the corresponding photo; precision on novel flags (model identifies defect not in inspector's original report — how often are these confirmed by follow-up?); E&O claim rate for inspections reviewed vs. not reviewed by the model
**Scope:** Spectora partnership provides access to millions of labeled inspection photos (report narrative = natural language label). This is one of the better-labeled datasets available in trades — the report writing workflow incidentally generates supervision. Fine-tuning a detection model on 100,000–500,000 labeled photo-defect pairs: 12-18 months for initial multi-system model.
**Data availability:** Spectora alone has enough photos from their inspector base to assemble a massive labeled dataset. Inspector consent and privacy framework (photos contain private property interiors) are the primary non-technical challenges.

---

## 2. Property-Specific Deficiency Frequency Prediction
#gradient-boosting #decision-trees #feature-engineering #cross-validation #evaluation-metrics #probability-distributions #bias-variance-tradeoff #quick-win

**Problem statement:** Predict which building systems have the highest deficiency probability for a specific property before the inspection, based on the property's characteristics, to focus the inspector's attention on highest-risk areas.

**ML task:** Ranking/scoring — deficiency probability per building system from property features
**Input data:** Inspection report deficiency records matched to property characteristics (age, construction type, foundation type, HVAC type, roofing material, geographic location/climate zone). Supervision: which systems had deficiencies per inspection.
**Target:** Pre-inspection priority report — top-5 systems most likely to have deficiencies for this property; specific defect types most common in this property class (e.g., "1930s balloon frame: fire stopping, knob-and-wire, galvanized supply")
**Evaluation metric:** Agreement rate between predicted high-priority systems and actual deficiency locations in the completed report; inspector-reported usefulness of pre-inspection focus list; recall on significant deficiencies in pre-flagged systems
**Scope:** Quick win — Spectora has the inspection report data. Property characteristics from county assessor records and MLS data. Gradient boosting on property features → deficiency frequency by system: 4-6 week project. The pre-inspection prep report adds immediate value to inspectors without requiring real-time photo analysis.
**Data availability:** Spectora report data + county assessor + MLS data via address matching. County assessor data is public; MLS data requires a data partnership or API access via a real estate tech partner.

---

## 3. Inspection Report Narrative Generation
#large-language-models #transformers #attention-mechanisms #transfer-learning #loss-functions #evaluation-metrics #quick-win

**Problem statement:** Generate professional, InterNACHI/ASHI-compliant report narratives from inspector voice notes and photo metadata, reducing post-inspection report writing time from 45-90 minutes to 15-20 minutes.

**ML task:** Conditional text generation — deficiency narrative from defect type, location, severity classification, and optional voice note input
**Input data:** High-quality inspection reports from certified inspectors with defect type labels per narrative section. Fine-tuning corpus: 50,000–100,000 well-written deficiency narratives from Spectora's report library (with inspector consent).
**Target:** Draft deficiency narrative per flagged item; appropriate severity language (monitor/repair/safety concern) based on defect type; consistent tone (professional, clear, non-alarmist)
**Evaluation metric:** Inspector acceptance rate (accepts draft without significant modification); readability score vs. inspector-written narratives; agent/buyer survey ratings on report clarity for AI-assisted vs. manual reports
**Scope:** Quick win relative to vision tasks — LLM fine-tuning on inspection report corpus requires less data than computer vision model training. A fine-tuned Llama or GPT-4 model on high-quality report narratives: 6-8 week project. Spectora integration is the distribution path.
**Data availability:** Spectora's platform contains hundreds of thousands of completed inspection reports. The report narratives, segmented by defect category and severity, are a high-quality fine-tuning corpus. Inspector privacy concerns (reports contain private property information) require consent framework.

---

## 4. Foundation Crack Severity Classification
#cnns #transfer-learning #loss-functions #backpropagation #evaluation-metrics #gradient-descent #feature-engineering #tacit-knowledge-ml

**Problem statement:** Foundation crack interpretation is one of the highest-liability areas in home inspection — inspectors who incorrectly dismiss active structural movement as normal settling face E&O claims. A classification model for foundation crack type (horizontal, stair-step, vertical, diagonal, offset) and severity can augment inspector judgment on this high-stakes deficiency category.

**ML task:** Multiclass classification — crack type from photo (crack orientation, pattern, width); binary classification (active vs. dormant movement indicator); severity classification (monitor/repair/evaluate by structural engineer)
**Input data:** Foundation crack photos labeled by structural engineers and experienced inspectors with movement status (active/dormant) and severity. Supervision from follow-up structural engineer reports that confirmed or revised the original inspector assessment.
**Target:** Crack type classification with confidence; active movement probability; recommended action tier (monitor/repair/structural engineer evaluation)
**Evaluation metric:** Agreement rate with structural engineer assessment on labeled foundation photos; recall on active movement cases (minimize false negatives in highest-liability category); false positive rate on dormant settling cracks
**Scope:** Structural engineering firms that review foundation reports have labeled evaluation data. A data partnership with a structural engineering firm provides both training labels and credibility for the model's recommendations. Fine-tuning a CNN specifically for foundation crack photos: 8-12 week project once dataset is assembled (5,000-15,000 labeled foundation photos covers the primary crack categories).
**Data availability:** Foundation crack photos exist in every home inspection company's photo library. Structural engineer evaluation reports provide the expert supervision labels. The challenge is joining crack photos to follow-up engineer assessments, which are not systematically linked in any platform.

---

## 5. Repair Cost Range Estimation from Deficiency Type and Location
#gradient-boosting #decision-trees #linear-regression #feature-engineering #cross-validation #evaluation-metrics #descriptive-statistics

**Problem statement:** Provide repair cost range estimates for identified deficiencies based on defect type and geographic location, enabling inspectors to include cost context in reports without manual research.

**ML task:** Regression — repair cost range (low/median/high) from deficiency type, severity, and ZIP code
**Input data:** HomeAdvisor/Angi cost data by project type and ZIP code; contractor bid data from platform marketplaces; historical repair cost records from home warranty companies
**Target:** Cost range estimate per deficiency type at the ZIP code level; confidence interval (narrow for common repairs, wide for scope-dependent items)
**Evaluation metric:** Coverage of the major deficiency categories in inspection reports (can the model estimate cost for 80%+ of common deficiency types?); agreement with actual contractor bids on a sample of jobs
**Scope:** Home repair cost data is commercially available (HomeAdvisor, Angi, RSMeans). Building the mapping from inspection deficiency terminology to cost database project types is the primary domain work. 4-6 week project once data sources are integrated.
**Data availability:** HomeAdvisor and Angi publish cost data by project type and geography. RSMeans and Craftsman cost databases provide construction cost data. A licensing agreement with one of these providers is the data foundation.
