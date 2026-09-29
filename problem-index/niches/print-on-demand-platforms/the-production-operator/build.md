# Running a Job You Can See Will Fail

**Niche:** [[niches/print-on-demand-platforms/the-production-operator/profile|The Production Operator]]
**Industry:** [[industries/print-on-demand-platforms|Print on Demand Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Production operators run jobs they can often tell will fail, spend their shift on reprints of work that should never have been accepted, and have no route to say so.
**Tags:** #worker-facing #tacit-knowledge-ml #evaluation-metrics #automation #confidence-intervals #descriptive-statistics #revenue-impact #gradient-boosting
**Contested on:** Every serious competitor in this niche is fighting to let the person at the press stop a job that will fail — and whoever does that saves the margin, because the operator can usually see it coming and the workflow gives them nowhere to say so.

## The Problem
An operator loads a job and sees a fine-line design on a heavily textured fabric in a colour they know does not hold. They have printed this combination and watched it fail. There is no stop button, no flag, no comment field — the queue moves forward and their target is items per hour. They print it. It fails inspection. Tomorrow the reprint arrives in their queue, they print it again on the same combination, and it fails again. Over a year they do this hundreds of times, and every instance was preventable by a judgement they made for free and had nowhere to record.

## Why Nobody Has Built This
The production workflow was designed as a throughput pipeline with the operator as an executor rather than as a decision maker. A stop mechanism is assumed to be abused or to harm throughput, which is an assumption from a different kind of manufacturing and has not been tested here. Their observations were never solicited, so the absence of a channel is not experienced as a gap by anybody upstream. And the reprint cost is booked centrally while the throughput target is theirs.

## What to Build
Give them the button and use what it produces. Add a flag-before-printing action with a short reason, taking seconds, which costs nothing, does not require anybody to act on it immediately, and immediately creates the most accurate prediction dataset in the business — this is the fix and it can ship in a sprint. Route flagged jobs for a quick decision: reprint-risk accepted, artwork returned to the merchant, or rerouted to a facility that handles it, so the flag leads somewhere rather than into a log. Measure the flags against outcomes, which validates the operators' judgement and is the evidence that turns a complaint into a control. Feed confirmed flags into the outcome prediction model as the highest-quality labels available, since an experienced operator's call is better than anything the model would infer unaided. Aggregate the reasons, since a recurring flagged combination is an artwork policy or a routing problem rather than a per-job one. Tell the operator what happened to their flag, because a channel that swallows input is used once. Adjust the throughput target so flagging does not cost them, which is what determines whether the mechanism is used at all. Ask them directly which combinations they dread, since a single conversation with a shift produces a list nobody has. And recognise the expertise, since it is the most accurate and least valued prediction capability the business has.

## Target Customer
Production leadership at platforms and partner facilities, the operators, and the platform's prediction and routing work which their judgement would immediately improve.

## Impact If Built
The operator's judgement is the most accurate prediction available, free, at the exact moment it would prevent the loss, and there is no field to record it. A flag with a reason ships in a sprint and produces the highest-quality labels the prediction model could have.
