# Adaptive Practice Engine with Item-Type Diagnostics

**Niche:** [[niches/language-schools/test-prep-schools/profile|Test Preparation Schools (TOEFL/IELTS)]]
**Industry:** [[industries/language-schools|Language Schools]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Magoosh and Kaplan provide adaptive practice tests, but they adapt on difficulty only — they don't diagnose which specific item types (inference questions, vocabulary-in-context, lecture detail questions) the student consistently struggles with and prescribe targeted drills.
**Tags:** #bayesian-network #recommendation #tabular-ml #quick-win

## The Problem
TOEFL Reading has ~10 distinct item types (factual detail, vocabulary, inference, insert text, prose summary, etc.); IELTS Listening has multiple question formats (form completion, multiple choice, matching, map labeling). A student scoring 22/30 on TOEFL Reading may be perfect on factual detail questions but consistently miss inference and prose summary questions. Current adaptive platforms adjust overall difficulty but do not surface this item-type diagnostic or prescribe item-type-specific practice sets.

## What Already Exists
Magoosh provides adaptive TOEFL/IELTS practice with difficulty-adjusted questions. Kaplan and Manhattan Prep offer structured prep courses with practice tests. ETS Official TOEFL Practice provides authentic test experiences. All generate overall section scores and sometimes subsection breakdowns, but none provide the item-type diagnostic precision that would enable targeted remediation.

## The Customization Gap
An item-type diagnostic layer that: (1) tags every practice question with its item type (mapped to the test blueprint); (2) tracks per-student accuracy by item type over time; (3) identifies the 2-3 item types with the highest improvement potential (lowest current accuracy with sufficient practice volume for statistical confidence); (4) generates targeted practice sets focusing on those specific item types; and (5) shows the instructor a per-student item-type mastery matrix to inform classroom instruction priorities.

## Target Customer
Test prep instructors and school directors who want to move from "practice more" to "practice these specific item types" — enabling precision preparation that maximizes score improvement per hour invested.

## Impact If Solved
Students improve target scores 20-30% faster by focusing practice on high-leverage item types rather than undifferentiated repetition. Schools can demonstrate superior score improvement statistics compared to competitors offering generic practice, strengthening their market position.
