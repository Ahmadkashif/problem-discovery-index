# Technique Modification Blind Spot for Osteoporotic Patients

**Niche:** [[niches/chiropractic-practices/geriatric-senior/profile|Geriatric & Senior Care]]
**Industry:** [[industries/chiropractic-practices|Chiropractic Practices]]
**Type:** Fix (Pain Point)
**One-liner:** DCs apply standard spinal manipulation techniques to elderly patients without systematically screening for osteoporosis or adjusting force parameters — creating an avoidable fracture risk that is chiropractic's most significant patient safety liability.
**Tags:** #gradient-boosting #binary-classification #tabular-ml #compliance #worker-facing

## The Problem
An estimated 10 million Americans over 50 have osteoporosis, and another 44 million have low bone density. A significant percentage of these patients receive chiropractic care without their DC knowing their bone density status. Standard HVLA (high-velocity, low-amplitude) manipulation at full force applied to an osteoporotic spine can cause vertebral compression fractures — a rare but devastating adverse event. Most DCs don't routinely screen for osteoporosis risk factors (age, gender, corticosteroid use, family history, low BMI) or modify their technique based on fracture risk. The clinical decision to modify technique is left to individual judgment without standardized risk assessment.

## Why It's Still Broken
DEXA bone density scans are performed by medical providers, not chiropractors. DCs typically don't have access to their patients' bone density results and don't routinely inquire about osteoporosis diagnosis or risk factors. The chiropractic curriculum covers osteoporosis as a contraindication but doesn't provide a practical screening protocol or force-modification guidelines based on risk stratification. No clinical decision support tool prompts the DC to assess fracture risk before selecting a technique.

## What a Fix Looks Like
A fracture risk screening protocol integrated into the chiropractic intake process: patient completes an osteoporosis risk questionnaire (FRAX-based), the system stratifies fracture risk (low, moderate, high), and recommends technique modifications for moderate-high risk patients (instrument-assisted adjustment, flexion-distraction, drop table technique instead of manual HVLA). For patients with known osteoporosis or high FRAX scores, the system flags contraindicated techniques and documents the risk assessment and technique selection rationale — providing both patient safety and malpractice protection.

## Who Feels the Pain
Elderly patients who receive inappropriate manipulation techniques without bone density screening. DCs who face malpractice liability when an iatrogenic fracture occurs in an unscreened patient — average malpractice settlement for chiropractic fractures: $250K-$500K.

## Impact If Fixed
Prevents iatrogenic fractures in osteoporotic patients — the single most preventable adverse event in chiropractic. Reduces malpractice risk and premiums for practices implementing standardized screening. Enables DCs to safely treat geriatric patients who would otherwise be refused chiropractic care due to undifferentiated fracture risk concerns.
