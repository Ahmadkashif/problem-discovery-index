# Surface EMG with Palpation Correlation Engine

**Niche:** [[niches/chiropractic-practices/palpation-digitization/profile|Palpation & Tactile Assessment Digitization]]
**Industry:** [[industries/chiropractic-practices|Chiropractic Practices]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Surface EMG devices measure paraspinal muscle activity objectively, but none correlate sEMG patterns with expert palpation findings to help junior DCs understand what the numbers mean in terms of what they should feel.
**Tags:** #gradient-boosting #multiclass-classification #signal-processing #tacit-knowledge-ml

## The Problem
Surface EMG (sEMG) devices (Insight Subluxation Station, MyoVision) measure bilateral paraspinal muscle activity at each spinal level, producing numerical asymmetry scores. These scores provide objective data, but DCs don't know how to connect them to their palpation findings. An sEMG asymmetry at T5 might correspond to a fixation the DC can feel — or it might be an artifact from electrode placement. The sEMG number alone doesn't tell the DC what adjustment to perform or what tissue state to expect when they palpate. The tool provides data without clinical context.

## What Already Exists
Insight Subluxation Station and MyoVision are established sEMG products used by thousands of chiropractors. They produce visual "scan" reports showing asymmetry at each spinal level. Chiropractors use these scans for patient education (showing "here's where your spine is out of balance") but rarely for clinical decision-making because the correlation between sEMG findings and palpation-based treatment decisions hasn't been mapped.

## The Customization Gap
The gap is a correlation layer that maps sEMG patterns to palpation findings and clinical decisions. An experienced DC uses the sEMG device and simultaneously records their palpation findings at each level (subluxation listing, tissue texture, mobility). Over hundreds of exams, the system learns the relationship between sEMG patterns and specific palpation findings — "this sEMG pattern at T5-T7 correlates with the palpation finding of posterior T6 fixation with bilateral paraspinal hypertonicity 85% of the time." Junior DCs can then use the sEMG scan as a guide for where to focus their palpation and what they should expect to feel.

## Target Customer
Chiropractic practices already using sEMG devices (estimated 15,000-20,000 practices in the US) who want to connect objective scan data to clinical palpation and treatment decisions.

## Impact If Solved
Transforms sEMG from a patient education tool into a clinical decision support tool. Reduces the palpation skill gap between experienced and junior DCs by providing objective guidance on where and what to feel. Improves inter-examiner reliability of palpation findings by anchoring subjective assessments to objective sEMG data.
