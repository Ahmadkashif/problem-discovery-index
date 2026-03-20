# Triage Prioritization Support for Medical Assistants

**Industry:** [[urgent-care|Urgent Care Centers]]
**Type:** Worker Life Changing
**One-liner:** Medical assistants performing intake triage at urgent care centers get a real-time acuity score that validates their clinical instinct and flags the patients who look stable but may not be — reducing the weight of making that call alone.
**Tags:** #gradient-boosting #decision-trees #feature-engineering #cross-validation #evaluation-metrics #probability-distributions #worker-facing

## The Problem
Urgent care medical assistants perform triage — gathering chief complaint, vital signs, and brief history — often within their first few years of clinical experience and without physician oversight at intake. The task is clinically consequential: misclassifying a patient with early sepsis, a cardiac event masquerading as indigestion, or a pediatric respiratory deterioration as "routine" can have serious consequences. Experienced MAs and nurses develop triage intuition over years, but newer staff lack that pattern recognition and are making acuity judgments under time pressure with a waiting room full of patients watching them.

## Why It Matters to the Worker
The anxiety of triage responsibility — particularly for newer clinical staff — is a significant source of occupational stress in urgent care. Medical assistants know they don't have the clinical depth of a nurse or PA but are performing triage functions at many centers for cost reasons. When something goes wrong with a patient who waited too long, the MA who did the intake carries real psychological weight for that outcome. Having a data-driven acuity flag that surfaces "this patient's profile (age + chief complaint + vital signs + time of day + arrival context) statistically resembles presentations that required escalation" provides a safety net that validates the MA's instinct or gives them grounds to call a clinician over for a second look.

## What a Solution Looks Like
A simple scoring model integrated into the intake workflow: as the MA enters vital signs and chief complaint, the system computes an acuity probability score (low/medium/high/immediate) with a brief explanation of the primary contributing factors ("SpO2 94% + chief complaint of SOB in 68yo = high acuity flag"). The MA still makes the call, but they have a second opinion. The model is trained on the center's own historical data — visit acuity vs. actual clinical outcome — so the flags are calibrated to real patterns at that specific center.

## Impact If Solved
Reduces the psychological burden on new clinical staff performing triage alone, likely reduces adverse wait-time events, and serves as an accelerated training tool — newer MAs learn faster when they can see which intake patterns correlate with high-acuity outcomes. Estimated reduction in inappropriate-wait adverse events of 30-50% in the first year of deployment.
