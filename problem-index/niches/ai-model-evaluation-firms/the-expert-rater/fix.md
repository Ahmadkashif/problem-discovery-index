# No Way to Say the Question Was Wrong

**Niche:** [[niches/ai-model-evaluation-firms/the-expert-rater/profile|The Expert Rater]]
**Industry:** [[industries/ai-model-evaluation-firms|AI Model Evaluation Firms]]
**Type:** Fix (Pain Point)
**One-liner:** Experts routinely encounter evaluation items that are malformed, clinically implausible or have no correct answer, and the interface makes them grade a response to it anyway.
**Tags:** #worker-facing #evaluation-metrics #descriptive-statistics #hypothesis-testing #confidence-intervals #quick-win #automation #compliance
**Contested on:** Every serious competitor in this niche is fighting to keep scarce practising specialists willing to do this work — and whoever does that takes the supply, because the entire domain evaluation business depends on a pool that is currently being spent down.

## The Problem
A physician rating clinical vignettes reaches one describing a presentation that could not occur, with lab values inconsistent with the history and a question that has no defensible answer. The correct professional response is that the item is invalid. The interface offers a rating scale. They pick something, because leaving it blank is unpaid and flagging goes nowhere, and that rating enters the dataset as a judgement about the model. The item stays in the bank and is served to the next fifty raters, who do the same. Experts report this as one of the most demoralising parts of the work, and it is invisible in every metric the firm tracks.

## Why It's Still Broken
An item-invalid option complicates aggregation, since a rating with a fourth outcome does not fit the analysis pipeline. It also produces an uncomfortable number — the share of the item bank that experts consider invalid — which somebody would have to own. Raters who flag heavily may score as low quality under agreement-based metrics, which actively punishes the behaviour the firm needs. And the people who built the item bank are not the people hearing the complaint.

## What a Fix Looks Like
Make invalid a first-class verdict. Add an item-invalid outcome with a reason taxonomy — implausible, internally inconsistent, ambiguous, out of scope, no correct answer — and pay for it at the full item rate, since an unpaid flag is a flag nobody uses and the payment is what makes the signal real. Route flagged items to review and remove or repair confirmed ones, closing the loop that currently ends in a text field. Report the invalid rate per item source as a standing quality metric, which is the number that would improve item construction and which no firm publishes. Exclude flagged items from model scores rather than counting a coerced rating, because a rating of a malformed question is measurement error entering as signal. Never penalise flagging in rater quality scores, and audit whether flagging correlates with expertise — it usually does, since the specialists who notice a flawed vignette are the better ones. Tell the rater what happened to their flag, which is the feedback that sustains the behaviour. And track the invalid rate over time as evidence that item construction is improving, which is the only way this gets better rather than being absorbed.

## Who Feels the Pain
Experts coerced into grading nonsense and leaving over it; customers whose scores include ratings of unanswerable questions; and the item authors who never learn which of their vignettes do not survive contact with a specialist.

## Impact If Fixed
Paying full rate for an item-invalid verdict is what makes the signal real rather than decorative. The invalid rate per item source is the metric that would actually improve item construction and no firm currently reports it.
