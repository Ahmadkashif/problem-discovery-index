# AI-Powered Patient-Clinician Matching System

**Niche:** [[niches/behavioral-health-clinics/intake-triage-matching/profile|Intake Triage & Patient-Clinician Matching]]
**Industry:** [[industries/behavioral-health-clinics|Behavioral Health Clinics]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A system that takes a patient's intake information and produces a ranked recommendation of the top 3 clinicians with match-quality explanations — replacing the institutional knowledge that currently lives in one coordinator's head.
**Tags:** #gradient-boosting #decision-trees #feature-engineering #tacit-knowledge-ml #bert #transfer-learning #evaluation-metrics #cross-validation #data-integration

## The Problem
Patient-clinician matching in behavioral health is a tacit knowledge problem: experienced intake coordinators develop intuition over hundreds of matches about which therapist-patient pairings "stick" and which lead to early dropout. This intuition incorporates hard constraints (insurance, availability, specialty) and soft signals (a patient's communication style in the intake call, whether they'll respond better to a structured CBT approach or an exploratory psychodynamic one, whether a particular therapist's personality will click). When the coordinator who holds this knowledge leaves, match quality drops immediately — new coordinators default to whoever has the next opening, leading to 30-40% higher dropout rates in the first three sessions.

## Why Nobody Has Built This
The outcome data needed to train a matching model (which pairings led to retention past session 3, therapeutic alliance scores, patient satisfaction) sits locked inside EHR systems that don't expose it in a usable format. Connecting intake characteristics to retention outcomes requires linking intake forms, session attendance records, and discharge data across systems — a data integration challenge that's not worth solving for a horizontal platform but is essential for a behavioral health-specific one. The soft matching factors (therapeutic modality fit, communication style compatibility) are hard to operationalize as features without deep domain expertise in clinical psychology.

## What to Build
A matching engine that ingests structured intake data (presenting concern, insurance, schedule, preferences) and unstructured intake notes (coordinator's freeform observations from the intake call), cross-references against clinician profiles (specialties, modalities, insurance panels, availability, current caseload), and applies a learned ranking model trained on historical match outcomes. The system uses BERT-based text classification to extract clinical signals from intake narratives (acuity level, likely diagnosis category, therapeutic modality fit) and a gradient-boosted ranking model to score clinician-patient pairs. It outputs a ranked top-3 recommendation with plain-language explanations ("Dr. Chen specializes in EMDR for trauma, accepts BlueCross, and has Tuesday evening availability matching the patient's preference").

## Target Customer
Multi-clinician behavioral health practices (8+ therapists) where intake coordination is a bottleneck — particularly practices experiencing intake coordinator turnover or rapid clinician hiring where the coordinator can't keep the full roster in their head.

## Impact If Built
Reduces patient dropout before session 3 by 20-35% (from industry average of 40% to 25% or below), recovers $100K-250K in annual revenue per practice from retained patients, and eliminates the single-point-of-failure risk of coordinator turnover destroying match quality.
