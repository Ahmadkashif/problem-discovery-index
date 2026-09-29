# The Requester Who Cannot Tell Whether Their Data Is Any Good

**Industry:** [[crowdsourcing-platforms|Crowdsourcing Platforms]]
**Type:** Worker Life Changing
**One-liner:** A researcher or engineer receives ten thousand labels, an agreement statistic and no way to know whether the disagreements are noise, ambiguity or their own unclear instructions.
**Tags:** #bayesian-inference #expectation-maximization #confidence-intervals #hypothesis-testing #gradient-boosting #evaluation-metrics #worker-facing #bert

## The Problem
On the other side of the transaction is a researcher, graduate student or machine learning engineer who needs labelled data and has a budget. They design a task, post it, receive submissions, and must decide whether the result is usable.

The instruments are thin. An inter-annotator agreement statistic summarises disagreement into one number that cannot distinguish between a genuinely ambiguous construct, poorly written instructions and unreliable workers — three problems with completely different remedies. Gold-standard accuracy assumes the gold labels are right. Attention check pass rates measure attention.

So requesters respond to any quality concern with the same tools: tighten approval thresholds, add attention checks, restrict to higher-qualification workers, and reject more. That treats every problem as a workforce problem, raises cost, excludes workers, and leaves an ambiguous task ambiguous.

The consequences run downstream. Research conclusions rest on this data, and machine learning systems are trained on it — so an ambiguity resolved inconsistently by workers becomes a systematic inconsistency in a model, generally undetected.

And most requesters have no methodological training in annotation design. They are domain experts who need labels, working from documentation that explains the platform's mechanics rather than how to design a task that produces reliable data.

## Why It Matters to the Worker
The requester is a worker too, usually a junior researcher or engineer under time and budget pressure, making methodological decisions they were never trained for, whose consequences they cannot see.

The lack of diagnosis is the specific difficulty. Knowing that agreement is low tells them something is wrong and nothing about what, so the response is a guess. Repeating a batch because the first one was unusable is a direct budget loss and is common.

And the incentive gradient is uncomfortable. The available remedies — rejection, exclusion, tighter thresholds — all shift cost onto workers, and a requester who does not understand that their instructions caused the disagreement will use them in good faith. Most requesters are not trying to treat workers badly; they are trying to get usable data with tools that point them in that direction.

## What a Solution Looks Like
Decompose the disagreement. Probabilistic models that jointly estimate worker reliability and item difficulty separate unreliable workers from ambiguous items, which is exactly the distinction the requester needs and the single agreement statistic hides. The methods are decades old and are not in these platforms.

Point at the instruction. Clustering disagreements by the ambiguity that produced them, and mapping them back to the specific instruction that failed to resolve it, converts a quality complaint into an editable sentence.

Audit the gold standard. Items that competent workers consistently fail should be flagged for review rather than treated as ground truth, because a wrong gold item penalises correct work and corrupts the reliability estimates simultaneously.

Guide the design before the money is spent. A short pilot spanning the edge cases in the requester's own data, with divergence reported, costs a fraction of a batch and prevents the most expensive failures.

And report the labour consequences of their choices. Showing a requester the realised hourly rate their pay implies, and the rejection rate they are applying relative to comparable tasks, gives good-faith requesters the information to behave well — which most will.

## Impact If Solved
Requesters make consequential methodological decisions without training, using an agreement statistic that cannot diagnose anything, and the available remedies all push cost onto workers. Disagreement decomposition, instruction-level diagnosis and gold auditing give them the diagnosis they need, and surfacing the labour consequences of their pay and rejection choices is what turns a well-intentioned requester into a good one.
