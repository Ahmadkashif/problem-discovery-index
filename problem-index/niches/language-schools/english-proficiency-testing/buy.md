# Automated Scoring That Has to Survive an Appeal

**Niche:** [[niches/language-schools/english-proficiency-testing/profile|English Proficiency Testing Organizations]]
**Industry:** [[industries/language-schools|Language Schools]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Scoring speech and writing at scale is a solved machine learning problem and an unsolved accountability problem.
**Tags:** #large-language-models #evaluation-metrics #anomaly-detection #hypothesis-testing #compliance

## The Problem
Speaking and writing are scored by trained human raters against detailed rubrics, at enormous volume, on a turnaround candidates and institutions expect in days. Rater capacity is the cost centre and the scheduling constraint, and rater agreement is a permanent quality concern.

Automated scoring exists and is used, typically alongside human rating. Extending it is the obvious efficiency, and the obstacle is not accuracy in the ordinary sense. A score of this kind changes a person's immigration status. It is appealed, it is litigated, and it is subject to regulatory scrutiny in several jurisdictions. A model that agrees with human raters 95% of the time and cannot explain any individual score is not deployable at that stake.

## What Already Exists
Automated essay and speech scoring have decades of research and mature commercial implementations. Modern language and speech models score fluently and cheaply. Evaluation tooling for model agreement and drift is standard.

## The Customization Gap
Everything specific here is about defensibility rather than accuracy.

**Construct validity, not correlation.** A model that predicts human scores from surface features — length, vocabulary sophistication, fluency rate — will correlate well and be measuring the wrong thing, and will be shown to be doing so the first time someone games it. The system must be demonstrably scoring the rubric constructs, which is a far stronger requirement than agreement.

**Fairness across first languages, tested explicitly.** Candidates come from every language background, and a model can perform systematically differently by accent or transfer pattern. Detecting and constraining that is a design requirement, not a post-hoc audit, and the organization has the data to do it properly.

**Every score must be explainable and reproducible.** An appeal requires showing why a performance received the score it did, and reproducing it exactly on a version of the model that may be two generations old. Model versioning with per-candidate score provenance is a regulatory requirement here and an afterthought in most deployments.

**Adversarial robustness.** Test preparation industries reverse-engineer scoring, and memorized templates and gaming strategies circulate quickly. Detecting them is continuous adversarial work no generic scoring product addresses.

**Human rating remains the anchor.** The design question is not full automation but how to route human capacity — to borderline cases, to appeals, to candidates near a decision boundary. That is a triage problem where calibrated uncertainty matters more than accuracy.

## Target Customer
Chief Psychometrician or VP of Assessment Technology, where rating capacity governs cost and turnaround and where scoring defensibility is an existential requirement.

## Impact If Solved
Human rating is the largest operating cost and the turnaround constraint on a test taken by millions. Extending automation with construct validity, tested fairness, and per-score provenance moves capacity to the cases that need judgment — and does it in a form that survives the appeal, the regulator, and the litigation that a lower-stakes assessment never faces.
