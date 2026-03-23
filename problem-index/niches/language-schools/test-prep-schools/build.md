# Automated TOEFL/IELTS Writing & Speaking Scorer

**Niche:** [[niches/language-schools/test-prep-schools/profile|Test Preparation Schools (TOEFL/IELTS)]]
**Industry:** [[industries/language-schools|Language Schools]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No product today scores TOEFL integrated writing tasks or IELTS speaking responses with the rubric fidelity and diagnostic detail that a trained human rater provides — students practice these sections blindly or wait days for teacher feedback.
**Tags:** #bert #lstm #nlp #speech-processing #tacit-knowledge-ml

## The Problem
TOEFL and IELTS each include subjectively scored components (writing and speaking tasks) that are the hardest to improve through self-study because students cannot accurately self-assess. A student writes a TOEFL integrated essay and has no way to know if it would score 3 or 4 out of 5 — let alone which specific rubric criteria are weak. Schools assign teachers to score practice responses, but a teacher scoring 20 practice essays at 15 minutes each consumes 5 hours of teacher time per class per week. Most schools limit practice essay scoring to 2 per week per student, creating a feedback bottleneck that slows improvement.

## Why Nobody Has Built This
ETS uses automated scoring (e-rater) as a secondary scorer for TOEFL writing, but does not make e-rater available as a standalone practice tool. The challenge for test prep schools is that automated scoring must match the specific rubric used by ETS or the British Council — not generic essay quality metrics. IELTS speaking scoring requires assessing pronunciation, lexical resource, grammatical range, and fluency/coherence from audio — a multimodal task that demands both ASR quality on accented L2 speech and rubric-aligned evaluation. Existing AES systems (Grammarly, WriteToLearn) assess general writing quality, not test-specific rubric adherence.

## What to Build
A scoring engine trained on the specific rubrics for TOEFL iBT Writing (independent + integrated tasks) and IELTS Writing (Task 1 + Task 2) and Speaking (Parts 1-3). For writing: the system scores each rubric dimension (task response, coherence, lexical resource, grammatical range), provides band/score-level feedback, and highlights specific passages that exemplify strengths and weaknesses. For speaking: ASR transcribes the response, acoustic features assess fluency and pronunciation, and NLP features assess lexical and grammatical range against the rubric. Output: per-criterion score, band descriptor alignment, and specific improvement recommendations.

## Target Customer
Test prep school directors and instructors who need to provide unlimited writing and speaking practice with immediate scored feedback, currently limited by teacher grading capacity.

## Impact If Built
Students practice writing and speaking 3-5x more frequently with immediate feedback (vs. 2x per week with delayed teacher feedback), accelerating score improvement by an estimated 2-4 weeks for a typical prep cycle. Schools can serve more students per teacher without compromising feedback quality.
