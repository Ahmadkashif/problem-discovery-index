# Domain Expert Rater

**Industry:** [[ai-model-evaluation-firms|AI Model Evaluation Firms]]
**Type:** Worker Life Changing
**One-liner:** A practising physician or attorney rating model outputs is doing genuinely hard cognitive work at piece rates, against rubrics that do not cover the cases they actually encounter, with no way to record that the question itself was wrong.
**Tags:** #bayesian-inference #hypothesis-testing #confidence-intervals #evaluation-metrics #large-language-models #expectation-maximization #worker-facing #tacit-knowledge-ml

## The Problem
Expert evaluation requires experts. A firm assessing medical reasoning hires physicians; one assessing legal outputs hires attorneys; one assessing code hires engineers. They rate outputs against a rubric, typically paid per item.

The work is harder than the pay structure assumes. Reading a model's clinical reasoning carefully enough to identify a subtle error takes real time and real attention, and the errors that matter are exactly the ones that require it — a plausible-sounding recommendation with a wrong dosage, an argument that cites a real case for a proposition it does not support. Skimming produces a rating; it does not produce a correct one.

The rubric routinely does not fit. A rater encounters an output that is correct but incomplete, or that answers a differently-framed question, or that is right for a reason the rubric does not anticipate. The interface offers the rubric's categories. So they choose the least wrong option, and that choice becomes data.

There is no channel for the most valuable thing they notice: that the item itself is flawed, that the reference answer is wrong, or that the two options are not comparable.

## Why It Matters to the Worker
These are professionals with alternative uses of their time, doing this because it pays reasonably per hour if they work quickly — which directly conflicts with the care the task requires. The piece-rate structure penalises exactly the diligence the work depends on.

The rubric constraint is professionally uncomfortable. An expert asked to record a judgement they do not hold, because the interface has no option for the judgement they do hold, experiences that as being asked to falsify their assessment in a small way, repeatedly.

Their expertise is systematically discarded. A physician who notices that a reference answer is outdated has identified a defect in the evaluation more valuable than any individual rating, and there is nowhere to put it.

And the feedback loop is absent. Raters are scored on agreement with other raters or with a reference, are rarely told how they scored, and are never told when their dissent turned out to be right.

## What a Solution Looks Like
Rubrics with an escape hatch, always. A "the item is flawed" option with free text, routed to the evaluation designers rather than discarded, converts the rater from an instrument into an observer — which is what they actually are and what they are being paid for.

Payment structures that reward care. Time-based or hybrid compensation on items known to be hard, and explicit recognition that a thorough rating of a subtle case is worth more than three fast ones, because it is.

Dissent treated as signal. When an expert with a strong record disagrees with the consensus, that is evidence about the item, not automatically evidence about the rater — and latent-truth estimation supports the distinction directly.

Feedback to raters: how their ratings compared, where they were the lone correct dissenter, what the item turned out to be. Experts are motivated by getting it right and are currently told nothing.

Calibration items with genuinely known answers, used to measure error-detection ability rather than style agreement, so that expertise is verified against the capability that matters.

## Impact If Solved
Expert raters are the anchor for the field's most consequential judgements about model capability, and they work under a structure that penalises care and discards their most valuable observations. Fixing the incentive and the escape hatch improves the data directly, because a rushed rating against an ill-fitting rubric is precisely the input that makes an evaluation meaningless.
