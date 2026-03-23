# Bilingual Academic-Language Integrated Assessment

**Niche:** [[niches/tutoring-centers/esl-immigrant-tutoring/profile|ESL & Immigrant Family Tutoring]]
**Industry:** [[industries/tutoring-centers|Tutoring Centers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An assessment system that measures a student's academic knowledge separately from their English proficiency — so a student who understands algebra but can't read English word problems receives an algebra intervention plan, not an English remediation plan.
**Tags:** #llm #multiclass-classification #nlp #multimodal #worker-facing

## The Problem
A 10th-grade immigrant student arrives at a tutoring center with strong math skills from their home country but limited English. The center's math diagnostic is in English. The student fails — not because they don't understand quadratic equations but because they can't read the word problems. The center assigns them to basic math remediation, wasting months on material they already know. The alternative is equally bad: if the center assesses them informally in their native language, the results are unstandardized and can't be compared to grade-level expectations. No assessment separates "what this student knows" from "what this student can demonstrate in English."

## Why Nobody Has Built This
Building bilingual assessments requires: (1) equivalent-difficulty test items in multiple languages (translation isn't sufficient — mathematical terminology and problem-framing conventions differ across languages and educational cultures); (2) a scoring model that separately estimates content knowledge and language proficiency; (3) support for the specific languages of the immigrant populations served (Spanish, Mandarin, Arabic, Haitian Creole, Portuguese, Vietnamese). The market fragmentation by language — and within language by educational tradition — makes this expensive to develop and maintain. Standardized test publishers avoid it because they serve the English-medium school system.

## What to Build
A multilingual adaptive assessment platform that presents academic content in the student's dominant language alongside English, scoring both language proficiency and content knowledge independently. For math: problems are presented visually and symbolically (reducing language dependence) with text support in the student's language. For reading/writing: parallel assessments in the student's language (measuring comprehension ability) and in English (measuring English reading level). Output: two separate scores — "content knowledge level: 9th grade math" and "English academic language level: 4th grade equivalent" — with a curriculum plan that addresses both dimensions appropriately.

## Target Customer
Directors of ESL tutoring centers and immigrant-serving community organizations with 30+ students from multilingual backgrounds who need accurate academic placement that doesn't confuse language barriers with knowledge gaps.

## Impact If Built
Eliminates academic misplacement of English learners — estimated at 40-60% of immigrant students placed in tutoring programs below their actual knowledge level. Saves 2-6 months of wasted remediation per misplaced student. Enables tutoring centers to target the actual gap (language, content, or both) from day one.
