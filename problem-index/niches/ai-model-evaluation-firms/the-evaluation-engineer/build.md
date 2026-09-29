# Did the Model Change or Did the Grader?

**Niche:** [[niches/ai-model-evaluation-firms/the-evaluation-engineer/profile|The Evaluation Engineer]]
**Industry:** [[industries/ai-model-evaluation-firms|AI Model Evaluation Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Evaluation engineers spend their days establishing whether a score moved because the model changed or because the grader is non-deterministic, the parser broke, or the rubric was interpreted differently this run.
**Tags:** #hypothesis-testing #confidence-intervals #change-point-detection #evaluation-metrics #descriptive-statistics #automation #worker-facing #causal-inference
**Contested on:** Every serious competitor in this niche is fighting to answer "did the model change or did the measurement change?" without a person spending a day on it — and whoever does that takes the account, because that question consumes most of an evaluation engineer's week.

## The Problem
Monday's run scored 76. Tuesday's scored 71. Between them: the model provider deployed a silent update, a colleague edited three items, the judge model was on a different version, one grader's prompt was tweaked, and the output parser started failing on responses that now begin with a preamble. The engineer spends the day re-running subsets with variables held fixed, comparing outputs by hand, and eventually establishing that four of the five points were the parser. Every one of those five changes was recorded somewhere. Nothing put them next to the score.

## Why Nobody Has Built This
The moving parts belong to different systems — the model provider, the item repository, the grader configuration, the harness code — and no single component sees them all. Attribution requires holding things fixed, which means re-running, which costs model calls that nobody budgeted for debugging. Evaluation teams are small and their tooling is built by whoever is least busy. And the firms' engineering effort goes to the customer-facing product, because the internal tax is invisible in any metric anyone reports.

## What to Build
Decompose the movement automatically. Version all five components as a unit — model, item set, prompt, grader, rubric — and record the full tuple with every score, since attribution is impossible without it and most harnesses version one or two. Diff the tuple between any two runs and report what changed before the engineer asks, which turns a day of investigation into a paragraph and is most of the value here. Estimate each component's contribution by re-running a small stratified subset with components held fixed, which is a designed experiment rather than a manual bisect and costs a fraction of a full run. Maintain a fixed anchor set re-run on every configuration, so the measurement apparatus's own drift is continuously visible and separable from model movement — this is cheap, standing infrastructure and it converts an investigation into a lookup. Detect silent model provider updates by monitoring fingerprint behaviour on a canary set, since these are frequently undisclosed and are a recurring cause of unexplained movement. Regression-test the graders themselves against fixed input-output pairs, because a grader is code and is the only code in the pipeline nobody tests. Alert on parser failure rates, which the fix note develops. And measure the team's time spent on attribution, so the cost of not building this is visible to whoever funds it.

## Target Customer
Evaluation engineering teams inside firms and labs, application teams running their own evaluations, and the platform vendors whose customers hit this daily.

## Impact If Built
Every cause of the ambiguity is already recorded and nothing puts them next to the score. A fixed anchor set re-run on every configuration makes the measurement apparatus's own drift continuously visible, which converts a day of investigation into a lookup.
