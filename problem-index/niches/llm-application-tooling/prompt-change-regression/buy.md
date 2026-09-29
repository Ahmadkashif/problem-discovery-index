# Regression Testing and Progressive Delivery

**Niche:** [[niches/llm-application-tooling/prompt-change-regression/profile|Prompt Change Regression]]
**Industry:** [[industries/llm-application-tooling|LLM Application Tooling]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Software engineering's answer to a change with unknown blast radius is a regression suite and a canary, and prompt changes get neither.
**Tags:** #automation #workflow-orchestration #hypothesis-testing #confidence-intervals #evaluation-metrics #change-point-detection #quick-win #cross-validation
**Contested on:** Every serious competitor in this niche is fighting to tell a team whether a prompt change made their application better or worse across the whole input distribution — and whoever does that takes the account, because every team shipping one of these applications is currently guessing.

## The Problem
A change whose effects cannot be fully reasoned about is exactly what regression suites and progressive delivery exist for. The suite catches what the author did not think to check; the canary limits exposure and analyses real traffic before full rollout; the rollback returns to a known state in seconds. All three are standard, mature and automated in any competent engineering organisation, and none of them is applied to the single most frequently changed artefact in an LLM application.

## What Already Exists
Regression test suites with continuous integration gating; snapshot and approval testing for outputs without exact expected values; canary deployment with automated analysis and rollback; feature flags with instant kill switches; and shadow traffic evaluation.

## The Customization Gap
The adaptation is to an artefact whose output is generated text. It requires: (1) approval testing on semantic rather than exact equivalence, since a snapshot test on generated output fails on every run and approval testing is the closest existing analogue that needs the least adaptation; (2) canary analysis on output quality rather than error rate, because a prompt change breaks nothing mechanically and degrades the thing nothing monitors; (3) statistical gating rather than binary pass-fail, since every case is stochastic and a single failing run is not a regression; (4) implicit user signals as the canary metric — retries, edits, escalations, abandonment — which are available and dense where explicit feedback is sparse; and (5) prompt versions treated as deployable artefacts with the same controls as code, which is a governance change more than a technical one and is the step most teams have deliberately avoided because instant prompt edits feel like a feature.

## Target Customer
Teams shipping LLM applications, platform and release engineering functions, and the progressive delivery vendors for whom output quality is an unserved canary signal.

## Impact If Solved
The standard answer to an unbounded-blast-radius change is a suite and a canary, and prompts get neither. Approval testing on semantic equivalence needs the least adaptation, and implicit behavioural signals are dense enough to gate a canary where explicit feedback is not.
