# The Rubric Rewritten From Scratch Every Time

**Niche:** [[niches/ai-model-evaluation-firms/domain-grading-criteria/profile|Domain Grading Criteria]]
**Industry:** [[industries/ai-model-evaluation-firms|AI Model Evaluation Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Evaluation harnesses are mature and free, and the grading criteria that decide whether an answer is actually correct in radiology or tax or contract review must be authored by a domain expert every single time.
**Tags:** #tacit-knowledge-ml #large-language-models #evaluation-metrics #hypothesis-testing #confidence-intervals #compliance #worker-facing #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to capture what a specialist means by correct in their own field, once, in a form that can grade at scale — and whoever does that takes the account, because the harness is free and the criteria are the product.

## The Problem
A firm wins an engagement evaluating a model for oncology decision support. A radiation oncologist spends three weeks with an evaluation engineer working out what counts as a correct answer: when a hedge is appropriate, when omitting a differential is an error and when it is good judgement, how to weigh a recommendation that is defensible but not standard of care, what to do when the vignette itself is unrealistic. The rubric ships, the engagement ends, and six months later a different team at the same firm starts the same process for a different oncology customer, with a different oncologist, arriving at criteria that are broadly similar and not comparable.

## Why Nobody Has Built This
The knowledge is tacit — a specialist knows a wrong answer immediately and articulating why is a different and harder task. Rubrics are treated as engagement deliverables owned by the customer rather than as firm assets, which is a contracting decision nobody has revisited. Every customer believes their context is unique, and they are partly right, which makes reuse a negotiation rather than a default. And the firms bill for expert time, so the incentive to reduce it is weak.

## What to Build
Make the criteria an asset that compounds. Build a structured rubric representation — criteria, weights, severity levels, exception conditions, worked examples — so that a rubric is data rather than a document, which is the precondition for reuse, versioning and coverage measurement and is a modelling exercise rather than a research one. Separate the domain-general layer from the customer-specific one, since a large share of what any oncology rubric contains is oncology rather than this customer, and splitting them makes the fourth engagement start at seventy percent rather than zero. Elicit from disagreements rather than from interviews: show the expert cases where graders disagreed and capture their reasoning, which surfaces tacit criteria far faster than asking them to enumerate rules, and is the technique the knowledge engineering literature settled on. Measure rubric coverage against real cases and report the fraction falling outside it, which tells the customer what the score does not cover and is currently unknown to everybody. Represent partial correctness and severity rather than binary pass and fail, because specialists do not think in binary and forcing them to discards most of the signal. Include a malformed-question verdict as a first-class outcome, since experts report this constantly and every rubric forces them to grade an answer to a bad question anyway. And version rubrics with the scores they produced, which the fix note develops.

## Target Customer
Evaluation firms, regulated industry buyers deploying models into specialist work, and the domain experts currently repeating this exercise.

## Impact If Built
The harness is free and the criteria are the product, and the product is rebuilt from scratch every engagement. Eliciting from grader disagreements surfaces tacit criteria faster than interviews, and splitting domain-general from customer-specific is what makes the asset compound.
