# Fix: Two Specialists, Same Facts, Different Answers

**Niche:** [[niches/remote-work-infrastructure/rule-application/profile|Rule Application]]
**Industry:** [[industries/remote-work-infrastructure|Remote Work Infrastructure]]
**Type:** Fix (Pain Point)
**One-liner:** Nobody has ever checked whether two compliance specialists given the same engagement reach the same determination.
**Tags:** #hypothesis-testing #confidence-intervals #descriptive-statistics #evaluation-metrics #cross-validation #compliance #quick-win #workflow-orchestration
**Contested on:** Whether the platform will measure the consistency of the judgement it sells.

## The Problem

Compliance determinations are made by individual specialists reading guidance and applying judgement. The volume is high, the jurisdictions are many, and the guidance is prose.

Under those conditions, inconsistency is certain. Two specialists reading the same page about the same country, given the same engagement facts, will not always reach the same determination — because the guidance admits interpretation, because their experience differs, and because the facts are rarely clean.

Nobody has measured it. There is no double-determination sample, no agreement statistic, no calibration exercise. The platform sells a determination and does not know whether its own determination function is reproducible, which is the most basic quality property a judgement service can have.

## Why It's Still Broken

Measuring it produces a number that is uncomfortable to hold. If two specialists agree on eighty percent of borderline engagements, the platform knows that a fifth of its determinations are essentially a draw — in writing, about a product sold as a settled status.

Determination volume is also high and specialist capacity is the constraint, so routing anything twice feels like a luxury.

And the compliance function's metrics are turnaround time and backlog, neither of which is a quality measure.

## What a Fix Looks Like

Measure agreement. It requires no methodology beyond routing some cases twice.

Sample and route blind. A standing sample of engagements determined independently by a second specialist who cannot see the first outcome, with both recorded. Start at a low rate — one in fifty — which is affordable and sufficient to establish the level.

Stratify toward the borderline. Straightforward determinations will agree; the informative sample is the engagements near a classification boundary, in jurisdictions with ambiguous tests, or of a type the platform handles rarely. Sampling there uses the capacity well.

Report agreement by jurisdiction and by determination type. Low agreement on one country's contractor test means that country's guidance is underspecified — a finding about the rule, which is fixable, rather than about the specialists, which is not.

Run calibration on the disagreements. A short session comparing reasoning on the cases that diverged is the cheapest and most effective improvement available, and it is standard practice in every other judgement function.

Feed the findings into the rule base. Every disagreement is a defect report on the guidance, and the pattern of disagreements is the prioritised list for structuring the rules.

And report the agreement rate internally as a quality metric alongside turnaround. A compliance function measured only on speed will produce fast determinations of unknown quality, which is the current state.

## Who Feels the Pain

Compliance specialists, making consequential judgements with no feedback on whether their colleagues would agree, and carrying the professional weight of it alone. Clients, receiving a determination whose reproducibility is unknown. Workers, whose employment status rests on it. And the platform, whose central product has never been quality-measured.

## Impact If Fixed

The reproducibility of the platform's core judgement becomes a known number, from routing one case in fifty twice. Low-agreement jurisdictions get identified as guidance defects rather than as specialist failures. And calibration on the disagreements — the cheapest improvement in any judgement function — becomes possible because the disagreements are now visible.
