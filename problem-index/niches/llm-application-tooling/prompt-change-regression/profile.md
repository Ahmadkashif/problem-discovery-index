# Prompt Change Regression

**Parent Industry:** [[industries/llm-application-tooling|LLM Application Tooling]]
**Category:** High Market Share
**Contested on:** Every serious competitor in this niche is fighting to tell a team whether a prompt change made their application better or worse across the whole input distribution — and whoever does that takes the account, because every team shipping one of these applications is currently guessing.

## Profile
**Market Size:** ~$420M US attributable to the regression problem
**Share of Parent Industry:** ~23% of category revenue
**Digital Adoption:** None — teams ship on hope
**Target Buyer:** Every team shipping an LLM application
**Automation Potential:** Very High — the comparison is mechanical given a set

## What Makes This a Distinct Niche
A prompt is the most-edited artefact in one of these applications and the only one with no regression test. Editing it to fix a reported failure changes behaviour on every other input, in both directions, and nothing checks. The team ships, the reported case is fixed, and two unrelated behaviours degrade quietly until somebody complains. Every element required to fix this exists — production inputs, historical outputs, a model that can grade, a versioning system — and the category has assembled them into tracing dashboards rather than into a before-and-after comparison. This is the gap that separates a team that can improve their application deliberately from one that oscillates.

## Current Tools & Gaps
Prompt versioning and registries, staged rollout, tracing, and evaluation harnesses that teams populate themselves. The gaps: no default regression set drawn from production; no paired comparison between two prompt versions on the same inputs; results reported without uncertainty on sets far too small; no detection of behaviours that changed but were not being checked; and no gate in the deployment path, so a prompt ships with less scrutiny than a code change.

## Problems
- [[niches/llm-application-tooling/prompt-change-regression/build|🔨 Build: A Deployment With No Regression Test]]
- [[niches/llm-application-tooling/prompt-change-regression/buy|🛒 Buy: Regression Testing and Progressive Delivery]]
- [[niches/llm-application-tooling/prompt-change-regression/fix|🔧 Fix: Shipped With Less Scrutiny Than a Typo Fix]]
