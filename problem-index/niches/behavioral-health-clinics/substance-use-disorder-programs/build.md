# ASAM Criteria Digital Assessment & Level-of-Care Decision Support

**Niche:** [[niches/behavioral-health-clinics/substance-use-disorder-programs/profile|Substance Use Disorder Treatment Programs]]
**Industry:** [[industries/behavioral-health-clinics|Behavioral Health Clinics]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Clinicians get a guided digital ASAM assessment that scores all six dimensions and produces a defensible level-of-care recommendation — replacing paper forms, manual scoring, and utilization review arguments.
**Tags:** #gradient-boosting #decision-trees #feature-engineering #large-language-models #attention-mechanisms #transformers #automation #compliance #cross-validation #evaluation-metrics

## The Problem
The ASAM Criteria is the gold standard for SUD treatment placement — determining whether a patient needs outpatient, IOP, PHP, residential, or medically managed inpatient care across six clinical dimensions (acute intoxication, biomedical conditions, emotional/behavioral conditions, readiness to change, relapse/continued use potential, and recovery environment). Clinicians currently complete this assessment on paper or fillable PDFs, manually score each dimension, and write a narrative justification for the recommended level of care. The process takes 45-90 minutes per patient, produces inconsistent scoring across clinicians, and generates documentation that frequently fails utilization review because the narrative doesn't explicitly map dimension scores to the ASAM placement grid.

## Why Nobody Has Built This
The ASAM Criteria is published by the American Society of Addiction Medicine and licensed — building a digital assessment requires navigating intellectual property agreements. The six-dimension scoring involves both structured data (withdrawal symptoms, vital signs, medication history) and unstructured clinical judgment (readiness to change, recovery environment risk). A useful tool must go beyond simple form digitization: it needs to suggest dimension scores based on clinical inputs, generate narrative justifications that satisfy payer utilization review criteria, and support clinical override with documentation. Most EHR vendors treat ASAM as a checkbox compliance feature rather than a clinical decision support opportunity.

## What to Build
A guided digital assessment workflow that walks clinicians through each ASAM dimension with structured questions, auto-suggests dimension severity scores based on responses, and generates a level-of-care recommendation with a payer-ready narrative justification. The system should accept clinical override at any dimension (with documentation of reasoning), pre-populate from existing intake data where available, and produce output in formats compatible with common utilization review submissions. A secondary ML layer trained on historical assessment-to-placement outcomes can flag cases where the recommended level of care diverges from typical patterns, prompting the clinician to strengthen their documentation before submission.

## Target Customer
Clinical directors and intake clinicians at IOP/PHP/residential SUD treatment programs who complete 5-20 ASAM assessments per week and spend significant time defending placement decisions to insurance utilization reviewers.

## Impact If Built
Reduces ASAM assessment time from 45-90 minutes to 20-30 minutes per patient. Improves utilization review approval rates by generating documentation that explicitly maps clinical findings to ASAM placement criteria. Standardizes scoring across clinicians within a program, reducing inter-rater variability that undermines clinical credibility with payers.
