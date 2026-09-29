# The Retroactive Recalculation Nobody Performs

**Niche:** [[niches/payroll-platforms/wage-calculation-time-integration/profile|Wage Calculation & Time Integration]]
**Industry:** [[industries/payroll-platforms|Payroll Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A non-discretionary bonus paid quarterly retroactively increases the regular rate for every overtime hour in the quarter, the recalculation is required and mechanical, and a great many employers simply do not do it.
**Tags:** #descriptive-statistics #evaluation-metrics #confidence-intervals #compliance #automation #hypothesis-testing #quick-win #revenue-impact
**Contested on:** *Not terminal as stated* — see the sub-niches for the two distinct forms this contest takes.

## The Problem
An employer pays a quarterly production bonus tied to measurable output. Because it is non-discretionary, it must be allocated back across the period it was earned and the overtime premium on every overtime hour in that period must be recomputed at the higher regular rate. The additional amount per employee is small — frequently tens of dollars — and the calculation is entirely mechanical. A substantial number of employers do not perform it, some because they believe the bonus is discretionary and some because nobody told them, and the shortfall accumulates quietly across every bonus period for every employee who worked overtime. It is one of the most common wage and hour findings and one of the least intentional.

## Why It's Still Broken
The rule is genuinely non-obvious to a non-specialist, and the classification of a bonus as discretionary or not is a judgement an employer makes when designing the plan, frequently without advice. Payroll engines support retroactive recalculation and do not initiate it, because the trigger is a legal characterisation rather than a system event. And the amounts are individually so small that no employee notices, which means the only feedback mechanism is an audit or a claim years later covering everyone.

## What a Fix Looks Like
Classify the earning and trigger the recalculation automatically. Every supplemental earning type is characterised at configuration time with the question asked plainly — is this promised, announced in advance, or tied to a measurable standard, in which case it is not discretionary — with guidance rather than a blank field, since the characterisation is where employers go wrong. Anything non-discretionary automatically triggers the retroactive allocation and overtime recomputation for the period it covers, with the resulting adjustments itemised on the pay statement so the employee can see what it is. Flag existing configurations where a recurring earning is marked discretionary and looks structurally otherwise — a bonus paid every quarter to everyone who hit a target is not discretionary regardless of how it is labelled — which is a check that would surface most of the exposure on day one. And compute the historical shortfall where the pattern is found, because the remedy is back pay to identifiable people and an employer that discovers it should be able to see the size of what it owes.

## Who Feels the Pain
Employees underpaid a small amount on every overtime hour for years; employers facing a collective claim for something they did not know they were doing; and payroll practitioners who suspect the configuration is wrong and have no way to check it.

## Impact If Fixed
The configuration audit is a query and reliably finds mischaracterised earnings at most employers with variable pay. Automating the recalculation removes a recurring, unintentional and well-litigated underpayment, and the amounts — small per employee, substantial in aggregate — go to the people who earned them.
