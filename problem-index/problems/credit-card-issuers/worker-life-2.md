# The Credit Strategy Analyst and Four Hundred Rules

**Industry:** [[credit-card-issuers|Credit Card Issuers]]
**Type:** Worker Life Changing
**One-liner:** A credit strategy analyst owns hundreds of decision-engine rules for line increases, decreases and over-limit authorisations, and spends more time documenting, regression-testing and explaining each change than deciding it.
**Tags:** #decision-trees #gradient-boosting #causal-inference #large-language-models #worker-facing #compliance #workflow-orchestration

## The Problem
Line management at a card issuer runs on strategy trees in a decision engine — FICO Platform, Experian PowerCurve, Provenir or an in-house equivalent. A mature portfolio accumulates hundreds of rules: proactive line-increase eligibility by score band and utilisation, line-decrease triggers when a bureau attribute deteriorates, over-limit authorisation tolerances, exclusions for recent hardship, overrides added after a loss spike three years ago that nobody has revisited. Each strategy has champion and challenger cells running at once.

A change of one cut-off is a project. The analyst writes the business case, back-tests it on historical cells, runs it past model risk if a score is involved, maps every new decline or decrease reason to an adverse action reason code so Reg B notices stay accurate, has it reviewed by fair lending, opens a change ticket, waits for the release window, and then watches the test cell for months. When losses tick up at quarter-end, the analyst is the one asked, within a day, which strategy did it.

## Why It Matters to the Worker
The analysts who do this work are hired for their judgement on credit risk, and they spend most of the week on its paperwork. Rule interactions are hard to see — a change to one branch silently reroutes accounts in another — so every edit carries the risk of a mistake that shows up as a loss or a complaint months later, with the analyst's name on the change log. Knowledge of why a rule exists lives with the person who wrote it; when they leave, the next analyst inherits a tree they are afraid to prune.

## What a Solution Looks Like
A strategy workbench that reads the live decision tree and shows, for any proposed change, which accounts would move, the expected incremental balance and loss on comparable historical test cells, the adverse action reasons triggered and whether they still match the drivers, and any rule it shadows or contradicts. It drafts the change documentation and the model-risk summary from the analysis for the analyst to edit, keeps the rationale attached to each rule, and flags rules whose original reason no longer holds.

## Impact If Solved
Turning a three-week change process into a few days lets an analyst run more and better tests a year, makes the tree understandable to the next person who owns it, and removes the documentation work that crowds out the credit judgement the job exists for.
