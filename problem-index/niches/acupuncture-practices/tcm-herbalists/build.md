# TCM Herbal Formula Management System

**Niche:** [[niches/acupuncture-practices/tcm-herbalists/profile|Traditional Chinese Medicine Herbalists]]
**Industry:** [[industries/acupuncture-practices|Acupuncture Practices]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No English-language digital system exists for building, modifying, tracking, and costing custom TCM herbal formulas based on traditional diagnostic patterns.
**Tags:** #recommendation #bayesian-network #tabular-ml #tacit-knowledge-ml #data-integration

## The Problem
A TCM herbalist diagnosing a patient with "Liver Qi stagnation with underlying Spleen Qi deficiency" needs to select a base formula (e.g., Xiao Yao San), modify it based on the patient's specific presentation (add Xiang Fu for hypochondriac pain, remove Bai Zhu if dampness is absent), calculate gram weights, check against contraindications, cost the formula, and print mixing instructions for the patient or dispensary. This entire workflow happens on paper or from memory, drawing on decades of clinical pattern recognition that no software captures.

## Why Nobody Has Built This
TCM herbal formulation requires encoding a knowledge system that is 2,000+ years old, not standardized across all lineages, and relies on pattern-based reasoning that doesn't map neatly to Western diagnostic categories. The market (~15,000-20,000 US practitioners who prescribe herbs) is small for SaaS, and the product requires deep domain expertise that most software teams lack. Chinese-language products exist but are built for the Chinese healthcare system and poorly translated.

## What to Build
A formula workbench that: (1) starts from a classical base formula selected by the practitioner, (2) suggests modifications based on the diagnosed TCM pattern, (3) calculates gram weights and checks herb-herb interactions, (4) tracks the patient's formula history and response over time, (5) integrates with herb inventory for real-time costing and stock alerts, and (6) prints patient-ready formula instructions. The system should learn from the practitioner's modification patterns over time to offer increasingly personalized suggestions.

## Target Customer
TCM herbalists operating their own dispensary (bulk herbs or granules) who compound 10-30 custom formulas daily.

## Impact If Built
Saves 3-5 minutes per formula (30-60 minutes/day), reduces compounding errors, enables formula efficacy tracking that is currently impossible, and preserves practitioner knowledge that is otherwise lost when they retire.
