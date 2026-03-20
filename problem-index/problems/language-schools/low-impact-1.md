# Adaptive Curriculum Pacing for Mixed-Level Classes

**Industry:** [[language-schools|Language Schools]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic LMS platforms treat language learning like any other course — they cannot adapt pacing to CEFR-level spread within a single classroom or adjust for language-specific skill progressions.
**Tags:** #bayesian-inference #conditional-probability-and-bayes-theorem #linear-regression #probability-distributions #feature-engineering #evaluation-metrics #workflow-orchestration

## The Problem
Most language schools cannot afford to run dedicated sections for every half-level on the CEFR scale. A typical "B1" class contains students ranging from strong A2 to weak B2, and the instructor must somehow advance all of them. The LMS (Canvas, Moodle, Google Classroom) delivers content linearly — Module 1, Module 2, Module 3 — with no awareness that language acquisition follows non-linear, skill-specific progressions: a student might be B2 in reading comprehension but A2 in productive writing, or fluent in informal spoken register but unable to produce academic prose. The pacing problem is not just speed; it is multi-dimensional skill routing that generic platforms were never designed to handle.

## What Already Exists
Adaptive learning platforms like Knewton (now Wiley), Smart Sparrow, and even Duolingo's internal engine implement item-response-theory-based pacing. But these are designed for self-study or single-skill tracks (math, vocabulary). They do not model the four-skill framework (listening, speaking, reading, writing) that structures all institutional language instruction, do not map to CEFR can-do descriptors that accreditors require, and do not produce the class-level pacing reports that program directors use to coordinate across sections.

## The Customisation Gap
A language-school-specific pacing engine needs to: (1) model individual students across four skills on a continuous CEFR scale, not a single mastery score; (2) use Bayesian knowledge tracing to update skill estimates after each assignment, accounting for the fact that receptive skills (reading, listening) develop faster than productive skills (writing, speaking); (3) recommend differentiated homework paths so students in the same physical class receive materials matched to their weakest skill; (4) produce weekly pacing reports aligned to the school's curriculum map and CEFR can-do statements for the program director to review. The domain-specific logic — CEFR alignment, four-skill modeling, L1-transfer-aware difficulty estimation — does not exist in any off-the-shelf adaptive platform.

## Impact If Solved
Instructors spend 30-40% less time differentiating materials manually. Students in mixed-level classes progress 20-30% faster because they receive skill-targeted practice rather than one-size-fits-all assignments. Program directors gain visibility into which sections are on-pace and which are falling behind the curriculum map.
