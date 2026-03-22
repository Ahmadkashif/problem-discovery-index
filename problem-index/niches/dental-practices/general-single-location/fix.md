# Intelligent Hygiene Recall Reactivation

**Niche:** [[niches/dental-practices/general-single-location/profile|General Dentistry Single-Location Practices]]
**Industry:** [[industries/dental-practices|Dental Practices]]
**Type:** Fix (Pain Point)
**One-liner:** Hygiene recall is the revenue lifeline of every general practice — when patients skip their 6-month cleaning, production drops and restorative needs go undetected — but current recall systems send the same generic postcard to every overdue patient regardless of their likelihood to respond.
**Tags:** #gradient-boosting #logistic-regression #feature-engineering #cross-validation #evaluation-metrics #revenue-impact #automation #tacit-knowledge-ml

## The Problem
Hygiene recall drives 25-35% of a general practice's production directly (prophylaxis, perio maintenance, fluoride) and generates 40-50% of restorative treatment indirectly (the cleaning visit is when cavities and crowns are diagnosed). When a patient doesn't return for their 6-month recall, the practice loses $200-400 in immediate hygiene revenue and $500-2,000 in downstream restorative production. Current recall systems — postcards, generic email blasts, robocalls — treat every overdue patient identically. A patient who missed by 2 weeks gets the same message as one who hasn't been seen in 3 years. A patient who always reschedules after a text gets the same postcard as one who only responds to phone calls. Reactivation rates for standard recall campaigns sit at 40-50%, meaning half of overdue patients are functionally lost.

## Why It's Still Broken
Experienced office managers develop tacit knowledge about which patients respond to which outreach: "Mrs. Johnson always cancels but rebooks if you call her directly," "The Martinez family only comes in during school breaks," "Patients on Delta Dental PPO are more likely to return because their cleanings are 100% covered." This pattern recognition exists in the office manager's head and disappears when they leave. The PMS stores the raw data — appointment history, insurance type, cancellation patterns, treatment history — but no recall system uses it to segment and personalize outreach. A logistic regression or gradient-boosted model trained on a practice's own recall history (features: months overdue, insurance type, cancellation history, treatment complexity, preferred contact channel, time of year) could predict reactivation probability and recommend the optimal channel, timing, and message urgency per patient.

## What a Fix Looks Like
An intelligent recall layer that sits on top of the existing PMS and segments overdue patients into tiers: high-probability reactivation (auto-send personalized text with one-tap rebooking link), medium-probability (phone call from front desk with specific talking points), and low-probability (re-engagement campaign with educational content about what happens when cleanings are skipped). The system learns from each practice's own data — which outreach actions led to rebooked appointments — and continuously improves its segmentation. For the office manager, it replaces the weekly "pull the overdue list and start calling" ritual with a prioritized action queue.

## Who Feels the Pain
The office manager or front desk staff who spends 3-5 hours per week manually calling overdue patients from an undifferentiated list, and the practice owner who watches production dip when recall rates drop below 80%.

## Impact If Fixed
Increasing recall reactivation from 45% to 65% for a typical single-location practice with 1,500 active patients recovers $80K-150K in annual production (hygiene + downstream restorative). The office manager reclaims 3-5 hours per week of manual calling time, redirected to higher-value patient interactions.
