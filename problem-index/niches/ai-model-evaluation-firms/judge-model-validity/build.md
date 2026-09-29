# The Measuring Instrument Nobody Calibrated

**Niche:** [[niches/ai-model-evaluation-firms/judge-model-validity/profile|Judge Model Validity]]
**Industry:** [[industries/ai-model-evaluation-firms|AI Model Evaluation Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Model-as-judge is the dominant automated grading method in the industry and its agreement with the human judgement it replaced is rarely measured and almost never reported.
**Tags:** #large-language-models #hypothesis-testing #confidence-intervals #evaluation-metrics #logistic-regression #descriptive-statistics #bayesian-inference #cross-validation
**Contested on:** Every serious competitor in this niche is fighting to state how much a model grader agrees with the humans it replaced, per task and continuously — and whoever does that takes the account, because the dominant grading method in the industry is also the least validated.

## The Problem
A team grades ten thousand responses with a judge model and reports 78 percent correct. The judge was never checked against human judgement on this task. It may agree with the team's experts ninety percent of the time, or sixty. The direction of its errors is unknown — it may systematically accept confidently-worded wrong answers, or penalise correct terse ones. The reported figure has an unknown relationship to the quantity it claims to measure, and it is used to compare models, gate releases and inform purchases. Everyone in the field knows this, and it is reported as a percentage with no caveat.

## Why Nobody Has Built This
Validation requires human labels on the specific task, which is the cost the judge was adopted to avoid — so the validation looks like it defeats the purpose, even though a few hundred labels is a tiny fraction of ten thousand items. Publishing an agreement figure invites the question of what the score means when agreement is seventy percent, which nobody wants to answer. Judges are treated as a component rather than as an instrument. And the field's norm of unqualified percentages makes an unvalidated judge look normal.

## What to Build
Calibrate the instrument and report the calibration. Measure agreement against human judgement on a stratified sample for every judge and task, and report it with the score as a standing property — a few hundred labels supports this, which is cheap against the cost of the evaluation itself and is the central build here. Characterise the disagreement rather than summarising it: where the judge is too lenient, where too strict, which response styles it over-rewards, which item types it handles poorly, since the pattern is far more actionable than the headline agreement number. Test explicitly for the documented biases — self-preference, length, position, confident phrasing — on a designed probe set, which is mechanical and reusable across judges. Correct for measurable bias where the pattern is stable, and report both raw and corrected. Measure the judge's self-agreement on repeated identical inputs, since that sets a ceiling on how good the measurement can be and is trivially computable. Re-validate on every judge model change, which the fix note develops. Use an ensemble of judges where the budget allows, reporting their disagreement as a per-item confidence, which identifies the items where the automated grade should not be trusted. And publish the judge prompt and the validation data, because a grader that cannot be inspected is an assertion.

## Target Customer
Evaluation firms, application teams grading with models, labs, and the buyers relying on judge-graded results.

## Impact If Built
A few hundred human labels calibrate a ten-thousand-item evaluation, which is cheap and almost nobody does it. Characterising where the judge is lenient or strict is more actionable than the agreement figure, and judge self-agreement sets a computable ceiling on the whole measurement.
