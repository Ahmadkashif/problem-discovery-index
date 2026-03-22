# AI-Guided OASIS Assessment with Auto-Population

**Niche:** [[niches/home-health-agencies/oasis-documentation/profile|OASIS Assessment & Clinical Documentation]]
**Industry:** [[industries/home-health-agencies|Home Health Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Pre-fill OASIS responses from prior assessments and recent visit documentation, guide clinicians through skip patterns with visual decision trees, validate clinical consistency in real-time, and predict PDGM payment impact as responses are entered.
**Tags:** #decision-trees #gradient-boosting #large-language-models #transfer-learning #feature-engineering #evaluation-metrics #tacit-knowledge-ml #automation #compliance #worker-facing

## The Problem
Experienced OASIS clinicians develop tacit expertise in navigating the assessment efficiently — they know which questions to expect based on the patient's diagnosis, they anticipate skip patterns, they recognize when a response is clinically inconsistent with other answers, and they understand how response combinations affect PDGM payment classification. This expertise takes 2-3 years to develop. New clinicians — and there are many, given 60%+ turnover — struggle with the assessment's complexity, making errors that cause claim denials and quality score degradation. Even experienced clinicians spend 45-60 minutes on an assessment that could be completed in 25-30 minutes if stable responses were pre-filled and navigation was intelligent.

## Why Nobody Has Built This
OASIS is CMS-defined and updated periodically (OASIS-E was a major revision), making any automation tool dependent on ongoing CMS spec tracking. The clinical consistency rules are nuanced — a machine must understand that a wound that was "healing" last assessment but shows increased measurements this assessment has a clinical contradiction that needs clinician review, not auto-correction. Pre-filling responses from prior assessments risks carrying forward outdated clinical information if the clinician doesn't carefully review each pre-filled response. EMR vendors have been reluctant to add this complexity to their platforms, and OASIS scrubber vendors (SHP, OASIS Answers) have built their business model on post-completion review rather than in-assessment guidance.

## What to Build
An OASIS assessment workflow engine that: (1) pre-fills responses from the patient's most recent prior OASIS with change-detection highlighting (responses that may have changed based on recent visit notes are flagged for review while stable responses are pre-populated), (2) dynamically enforces skip patterns so clinicians never see irrelevant questions, (3) validates clinical consistency in real-time (wound measurements vs. healing status, functional scores vs. reported assistance levels, cognitive status vs. medication management capability), (4) predicts the PDGM payment group from current responses and alerts the clinician when a response change would shift the payment classification, and (5) generates an assessment completion quality score predicting the likelihood of scrubber rejection.

## Target Customer
Medicare-certified home health agencies completing 100+ OASIS assessments per month, particularly those with high clinician turnover where newer nurses are responsible for OASIS completion without years of experience.

## Impact If Built
Reducing average OASIS completion time from 55 minutes to 28 minutes would reclaim 45 clinician-hours per month per 100 assessments. Reducing OASIS-related claim denials by 50-60% would protect $300K-$600K annually for a mid-size agency. Accurate PDGM payment classification from consistent OASIS coding would increase revenue by 3-5% through correct episode payment without any change in care delivery.
