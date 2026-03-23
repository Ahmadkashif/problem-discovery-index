# Hands-On Skill Assessment via Video Verification

**Niche:** [[niches/corporate-training/manufacturing-floor-training/profile|Manufacturing Floor Skills Training]]
**Industry:** [[industries/corporate-training|Corporate Training]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No platform today verifies manufacturing skills by analyzing video of the worker performing the actual task — assessments are either paper quizzes (testing knowledge, not skill) or supervisor observation (inconsistent, unscalable).
**Tags:** #cnn #object-detection #computer-vision #tacit-knowledge-ml #worker-facing

## The Problem
A CNC operator completes a training module on 5-axis machine setup. The quiz asks multiple-choice questions about setup sequence. The operator scores 90%. Two weeks later, they crash a $80,000 spindle because they skipped a critical alignment step that the quiz didn't test. The gap between "knows the procedure" and "can execute the procedure" is the central problem of manufacturing skills training — and no digital assessment tool bridges it. Supervisor sign-offs are the industry standard, but supervisors vary in rigor: one watches the entire setup, another glances over and signs the form.

## Why Nobody Has Built This
Verifying physical skill execution from video requires: (1) capturing video of the worker performing the task at the workstation (camera placement, lighting, angle standardization); (2) detecting specific procedural steps and their sequence from the video (tool selection, fixture placement, measurement verification, safety steps); (3) comparing the observed sequence against the defined SOP; and (4) flagging deviations or omissions. This is a complex computer vision problem that varies by task type, machine type, and facility layout. The ROI case is strong (preventing one spindle crash pays for years of software), but the technical barrier has been too high for manufacturing-focused software companies.

## What to Build
A video-based skill verification system where: (1) the worker records themselves performing a critical procedure using a workstation-mounted tablet or phone; (2) a CV model identifies key procedural steps (tool changes, measurement actions, safety lockout steps) and their sequence; (3) the system compares the observed procedure against the SOP and flags missing or out-of-sequence steps; (4) the supervisor receives a verification report highlighting any deviations for review. Phase 1 focuses on the 10-15 most critical procedures per plant, where errors have the highest safety or scrap cost.

## Target Customer
Plant Managers at discrete manufacturing facilities (aerospace, automotive, medical device) where a single procedural error can cause $10,000-$100,000 in scrap, equipment damage, or quality escapes.

## Impact If Built
Reduces procedural errors by an estimated 40-60% for verified tasks, prevents 2-5 major quality escapes per plant per year ($50,000-$500,000 in savings), and provides an objective skills assessment record that replaces subjective supervisor sign-offs.
