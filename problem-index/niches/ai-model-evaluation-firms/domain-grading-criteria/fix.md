# The Rubric That Changed and the Scores That Did Not Say So

**Niche:** [[niches/ai-model-evaluation-firms/domain-grading-criteria/profile|Domain Grading Criteria]]
**Industry:** [[industries/ai-model-evaluation-firms|AI Model Evaluation Firms]]
**Type:** Fix (Pain Point)
**One-liner:** A rubric is refined throughout an engagement, and scores from before and after the refinement are reported on the same chart as though they measured the same thing.
**Tags:** #evaluation-metrics #compliance #descriptive-statistics #confidence-intervals #hypothesis-testing #data-integration #quick-win #automation
**Contested on:** Every serious competitor in this niche is fighting to capture what a specialist means by correct in their own field, once, in a form that can grade at scale — and whoever does that takes the account, because the harness is free and the criteria are the product.

## The Problem
Week two: the rubric penalises any hedged answer. Week five: the expert decides hedging is appropriate in ambiguous cases and the criterion is softened. Week nine: a severity level is added. The final report shows a score trend rising across the engagement, presented as the model improving under iteration. Some of that rise is the rubric loosening. Nobody recorded which portion, the chart has one line, and the customer draws a conclusion the data does not support. This happens in most engagements and is rarely deliberate.

## Why It's Still Broken
Rubric refinement is correct and necessary — the first version is always wrong — so the fix cannot be to freeze it. Rubrics live in documents without version control, so there is frequently no record of what changed when. Re-grading historical items under the new rubric costs expert or judge time that the engagement did not budget. And a rising line is the result everyone hoped for, which suppresses the question.

## What a Fix Looks Like
Version the rubric and re-anchor the scores. Put the rubric under version control with every score tagged to the version that produced it, which is basic bookkeeping and makes the problem visible rather than solving it invisibly. Re-grade a fixed anchor set on every rubric change — the same thirty items throughout the engagement — so the rubric's own drift is measured directly and can be subtracted from the trend, which is cheap and is the substance of the fix. Report score movement decomposed into model change and rubric change, since that is the question the customer is implicitly asking and neither party can currently answer it. Never plot scores from different rubric versions as a continuous series without marking the change points. Record the reason for each rubric change, because a loosening made to accommodate a model's behaviour is a different act from one made on reflection about the domain, and only the record distinguishes them. Require the expert to sign off on changes, which slows nobody down and creates accountability for a decision currently made informally. And report the final rubric alongside the final score, since a score without its criteria is uninterpretable and is nonetheless how most of these results circulate.

## Who Feels the Pain
Customers reading improvement into a chart that partly reflects a moving standard; the experts whose considered refinements are silently converted into apparent model gains; and the firms whose genuinely good results are indistinguishable from rubric drift.

## Impact If Fixed
Re-grading a fixed anchor set on every rubric change measures the rubric's own drift directly and costs very little. Decomposing score movement into model change and rubric change answers the question the customer is actually asking.
