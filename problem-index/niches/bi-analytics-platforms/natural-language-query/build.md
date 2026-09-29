# Knowing When Not to Answer

**Niche:** [[niches/bi-analytics-platforms/natural-language-query/profile|Natural Language Query]]
**Industry:** [[industries/bi-analytics-platforms|BI & Analytics Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Conversational analytics fails by producing a confident, well-formatted, wrong number, and the capability that would prevent it — knowing when the question cannot be answered from the model — is nobody's feature.
**Tags:** #large-language-models #bayesian-inference #confidence-intervals #evaluation-metrics #hypothesis-testing #cross-validation #graph-theory #tacit-knowledge-ml
**Contested on:** Every serious competitor in conversational analytics is fighting to return an answer that is correct against a governed model and to refuse when the model cannot support the question — and whoever refuses well takes the account, because one confidently wrong answer ends the deployment.

## The Problem
An executive asks how many customers churned in the Northeast last quarter. The system produces a number. It is wrong, because the region field has three values for the Northeast introduced by three different systems, because churn requires a ninety-day window the model does not encode, and because the customer table includes test accounts. None of this is visible in the answer, which is a clean number in a clean chart. The decision is made. Three weeks later somebody notices, and the feature is switched off across the organisation — correctly, because a tool that is right most of the time and cannot tell you which time is worse than no tool.

## Why Nobody Has Built This
Refusal is commercially unattractive: a demonstration where the system declines is a bad demonstration, and the category is being sold on fluency. The research incentives point the same way, since benchmarks reward answering. Knowing whether a question is answerable requires modelling what the semantic layer does and does not cover, which nobody has represented explicitly — coverage is implicit in whatever was modelled. And organisations have not yet demanded it, because the failure takes a few weeks to surface and is attributed to the technology in general rather than to the absence of a specific capability.

## What to Build
Answerability as the primary product surface. An explicit coverage model: which business concepts the semantic layer supports, at what grain, over what time range, with what known caveats — maintained as content, since it is the thing being reasoned about. A classification of every incoming question against that coverage, producing one of three outcomes: answerable, answerable with a stated caveat, or not answerable with a specific reason — and the third is the valuable one, because "the model does not encode region for orders before 2023" is genuinely useful and a wrong number is not. Calibrated confidence on the answers that are given, validated against held-out questions from the customer's own history rather than against a public benchmark. A verification path that does not require reading SQL: show the row count, the filters applied in business language, and a sample of the underlying records, so a business user can sanity-check the answer themselves. And a feedback loop where analysts confirm or correct answers, which builds the organisation-specific evaluation set that is the only meaningful measure of whether the thing works.

## Target Customer
Data leadership deploying conversational analytics, the platform vendors shipping these features, and the conversational analytics entrants for whom trust is the entire adoption barrier.

## Impact If Built
The failure mode is confident wrongness, which destroys trust faster than any amount of correct answers rebuild it. Refusal and calibration are unglamorous, contrary to the way the category is currently marketed, and are the only path to a deployment that survives a year.
