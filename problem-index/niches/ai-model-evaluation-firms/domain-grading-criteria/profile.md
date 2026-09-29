# Domain Grading Criteria

**Parent Industry:** [[industries/ai-model-evaluation-firms|AI Model Evaluation Firms]]
**Category:** Low Digitized
**Contested on:** Every serious competitor in this niche is fighting to capture what a specialist means by correct in their own field, once, in a form that can grade at scale — and whoever does that takes the account, because the harness is free and the criteria are the product.

## Profile
**Market Size:** ~$220M US
**Share of Parent Industry:** ~28% of category revenue
**Digital Adoption:** Very Low — authored by an expert every time
**Target Buyer:** Regulated and specialist industry buyers deploying models
**Automation Potential:** Medium — elicitation is the bottleneck, application is automatable

## What Makes This a Distinct Niche
Evaluation harnesses are mature, open and free. What is not free is knowing whether an answer is actually correct in radiology, in tax, in contract review, in structural engineering. That requires a specialist to articulate criteria that they have never had to write down, that vary by context, and that include cases where the reasonable answer is that the question is malformed. Every engagement starts this from scratch, with a domain expert and an evaluation engineer in a room, producing a rubric that covers the cases they thought of. The rubric is then applied at scale to cases neither of them imagined. This is the category's real cost centre and its most defensible asset, and nobody treats it as an asset.

## Current Tools & Gaps
Rubric authoring in documents and spreadsheets, expert interviews, and iterative refinement against disagreements. The gaps: no reuse across engagements within the same domain, so the fourth radiology rubric is written from scratch; no coverage measurement, so nobody knows what fraction of real cases the rubric addresses; no versioning, so a rubric change silently makes scores incomparable; and no way to express partial correctness, degrees of harm, or the case where the question itself is wrong — which specialists say is common.

## Problems
- [[niches/ai-model-evaluation-firms/domain-grading-criteria/build|🔨 Build: The Rubric Rewritten From Scratch Every Time]]
- [[niches/ai-model-evaluation-firms/domain-grading-criteria/buy|🛒 Buy: Knowledge Elicitation and Rubric Design]]
- [[niches/ai-model-evaluation-firms/domain-grading-criteria/fix|🔧 Fix: The Rubric That Changed and the Scores That Did Not Say So]]
