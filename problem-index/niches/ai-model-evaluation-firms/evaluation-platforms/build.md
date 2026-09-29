# One Mechanism, Two Unrelated Businesses

**Niche:** [[niches/ai-model-evaluation-firms/evaluation-platforms/profile|Evaluation Platforms]]
**Industry:** [[industries/ai-model-evaluation-firms|AI Model Evaluation Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The same harness is sold to a handful of frontier labs buying research findings and to thousands of product teams buying a regression check, and the two purchases share only the runner.
**Tags:** #evaluation-metrics #workflow-orchestration #automation #large-language-models #data-integration #confidence-intervals #compliance #hypothesis-testing
**Contested on:** Not terminal — the contest differs by who is being evaluated and why, and the decomposition is recorded in the profile.

## The Problem
A vendor demonstrates a harness to a frontier lab's evaluation team and to a fintech shipping a support assistant. The lab asks what novel capability elicitation the firm brings, how findings are handled under embargo, and whether the team can design an evaluation for a capability that has no benchmark. The fintech asks what it costs per build, whether it runs in their pipeline without sending customer data anywhere, and whether it will catch a regression in their own domain. The product answers the mechanics for both and the actual question for neither, because the mechanics are the commodity part.

## Why Nobody Has Built This
The harness genuinely is common, which makes the single-product framing look efficient right up to the sales conversation. The lab business has enormous revenue per account and the application business has volume, which makes both attractive and neither easy to abandon. The skills differ completely — research judgement against pipeline engineering — and a firm strong in one staffs poorly for the other. And the category is young enough that the positioning question has not yet been forced.

## What to Build
Build the commodity layer properly and let the two businesses diverge above it. The genuinely shared substrate — deterministic execution, result storage, versioning of prompts, datasets and graders, uncertainty reporting, cost accounting — is weak in nearly every product and is the real opportunity at this level, because both sides need it and neither gets it. Version every component of an evaluation as a unit: the item set, the grader, the rubric, the model version and the prompt, since a score is only interpretable against all five and most platforms version one or two. Make results reproducible, which is harder here than elsewhere because both the model under test and the grader are non-deterministic, and being precise about what reproducibility means under that is more useful than claiming it. Report uncertainty on every number, which the fix note develops. Account for evaluation cost explicitly, since running a large suite against a frontier model is a material spend that nobody budgets or optimises. Keep the data boundary configurable, because one side operates under lab confidentiality and the other under customer data restrictions, and both are absolute. And be explicit about which business the product serves, since the alternative is selling research capability to a pipeline buyer and losing both.

## Target Customer
Evaluation firms deciding which business they are in, frontier labs, and application engineering teams.

## Impact If Built
The shared substrate — versioning of the whole evaluation unit, reproducibility under double non-determinism, uncertainty, cost — is weak everywhere and is what both businesses actually need from the common layer.
