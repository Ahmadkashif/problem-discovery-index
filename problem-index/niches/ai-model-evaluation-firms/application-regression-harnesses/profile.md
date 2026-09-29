# Application Regression Harnesses

**Parent Industry:** [[industries/ai-model-evaluation-firms|AI Model Evaluation Firms]]
**Category:** Contested Sub-Niche
**Contested on:** Every serious competitor in this sub-niche is fighting to tell a product team whether their change made their own application better, per commit, at a cost that fits a tooling budget — and whoever does that takes the account, because that is the only question an application team is asking.

## Profile
**Market Size:** ~$130M US and the fastest-growing line in the category
**Share of Parent Industry:** ~16% of category revenue
**Digital Adoption:** Moderate — adopted widely, trusted narrowly
**Target Buyer:** Engineering teams shipping products built on models
**Automation Potential:** Very High — this is a continuous integration problem

## What Makes This a Distinct Niche
Thousands of teams ship applications built on models they do not train. Their question is narrow and constant: did the change I just made — a prompt edit, a retrieval tweak, a model version bump forced by a deprecation — make my application better or worse on my task. They compare against a spreadsheet of test prompts and somebody reading the outputs, which is the alternative these products must beat. The contest is a regression signal that is trustworthy enough to gate a deploy, cheap enough to run per commit, and specific enough to their domain to catch what matters, on a test set they built themselves and do not have time to maintain.

## Current Tools & Gaps
Harness libraries, tracing, judge-model graders, dataset management and regression dashboards. The gaps: test sets are assembled once and never maintained, so they drift away from what production actually sees; the judge grading them is unvalidated against the team's own standard; results are reported without uncertainty on suites far too small to support the comparison; costs scale with suite size in a way that pushes teams toward suites too small to be informative; and nothing connects the evaluation set to production traffic, which is where the real failures are.

## Problems
- [[niches/ai-model-evaluation-firms/application-regression-harnesses/build|🔨 Build: A Test Set Written Once and Never Maintained]]
- [[niches/ai-model-evaluation-firms/application-regression-harnesses/buy|🛒 Buy: Continuous Integration and Canary Practice]]
- [[niches/ai-model-evaluation-firms/application-regression-harnesses/fix|🔧 Fix: Twenty Prompts in a Spreadsheet]]
