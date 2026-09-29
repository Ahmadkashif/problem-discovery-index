# Buy: Adaptive Assessment Adapted to a Tutor's First Session

**Niche:** [[niches/online-tutoring-platforms/diagnostic-and-preparation/profile|Diagnostic & Session Preparation]]
**Industry:** [[industries/online-tutoring-platforms|Online Tutoring Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Adaptive assessment engines place a student on a scale efficiently; a tutor needs to know which specific misconception is blocking them, which is a different question.
**Tags:** #bayesian-inference #maximum-likelihood-estimation #evaluation-metrics #confidence-intervals #graph-theory #large-language-models #data-integration #worker-facing
**Contested on:** Whether placement-oriented assessment can be repurposed to identify a specific misconception rather than a level.

## The Problem

Adaptive assessment is a mature technology. Item response theory, computerised adaptive testing, large calibrated item banks and diagnostic assessment products serve schools well and can place a student on a proficiency scale in twenty items with good precision.

A tutor does not need a scale position. They need to know that this student is subtracting fractions by subtracting numerators and denominators separately, or that they cannot hold a multi-step problem in working memory, or that they read the question wrong. The distinction is between a measurement and a diagnosis, and the assessment industry is built for the first.

## What Already Exists

Adaptive testing engines and IRT libraries. Calibrated item banks from assessment publishers. Diagnostic assessment products aimed at schools, some with misconception tagging. Curriculum standards with topic hierarchies. Knowledge-tracing models from the learning analytics literature. Intelligent tutoring system research with decades of misconception modelling in mathematics specifically.

## The Customization Gap

**Items need misconception tags, not just difficulty parameters.** IRT items are calibrated for discrimination and difficulty. A diagnostic item needs distractors each of which corresponds to a specific wrong reasoning path, so the chosen answer names the misconception. Item banks with this structure exist in research and are rare commercially, and building them is the substantive work.

**The prerequisite graph has to be explicit.** Adaptive tests move along a difficulty dimension. Diagnosis moves down a dependency chain — a student failing at algebra gets tested on the fractions and arithmetic beneath it. That requires a structured prerequisite model as the search space, which standards documents approximate and no assessment engine contains.

**The time budget is a few minutes, not twenty items.** A family will not sit a child down for a half-hour test before their first tutoring session. The diagnostic has to be short, or better, inferred from work the student has already done, with a formal assessment only as a fallback. That inverts the assessment product's assumption entirely.

**Existing evidence should be used before any new assessment.** Homework, prior session transcripts, uploaded assignments and the parent's description all carry diagnostic signal. No assessment product ingests unstructured prior evidence, and here it is both cheaper and better than testing the student again.

**The output is a brief for a professional, not a score report.** A tutor needs a ranked hypothesis with the distinguishing question attached and their own judgement retained. Assessment products produce reports for teachers and administrators with a different shape and a different confidence posture.

## Target Customer

Assessment vendors, for whom tutoring marketplaces are a new channel and misconception-level diagnosis is an existing research capability they have not commercialised. Also tutoring platforms evaluating a diagnostic product and finding it returns a grade level when their tutors need a gap.

## Impact If Solved

The psychometric engine, item calibration and adaptive machinery get reused, and the misconception-tagged items, the prerequisite graph, the short-or-inferred budget, the prior-evidence ingestion and the professional-brief output get built. The concrete result is a tutor starting the first session with a hypothesis instead of a blank page.
