# Build: Implied Rate at the Moment of Pricing

**Niche:** [[niches/crowdsourcing-platforms/pay-setting-and-rate/profile|Pay Setting & the Realised Rate]]
**Industry:** [[industries/crowdsourcing-platforms|Crowdsourcing Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Predict how long the task will take from the platform's own history and show the requester the hourly rate their price implies, before they post it.
**Tags:** #gradient-boosting #survival-analysis #confidence-intervals #evaluation-metrics #descriptive-statistics #time-series-forecasting #revenue-impact #worker-facing
**Contested on:** Whether task duration can be predicted accurately enough to price against before anyone has done the task.

## The Problem

Pay is set per task by a requester with no visibility of how long the task takes. Their estimate comes from doing one themselves — quickly, knowing exactly what they meant by every instruction — or from a guess.

Systematic underestimation follows. The requester who designed the task is the fastest possible person at it, and the gap between their time and a first-time worker's is large and consistent. A per-task price set from the designer's own speed is roughly a third of what they intended to pay, and nothing ever corrects it.

The platform holds the completion time distribution for millions of tasks, tagged by type, interface, item count and instruction length. Predicting a new task's duration from that is a routine problem with abundant labels.

## Why Nobody Has Built This

Showing the implied rate makes it visible, and the visible number has a floor beneath which a requester would be uncomfortable posting. That reduces the supply of very cheap work, which reduces platform volume.

The academic segment has moved on this under pressure from ethics review boards, which is the proof that the constraint is norms and buyer expectations rather than technology. Elsewhere the number is simply not shown.

There is also a mild prediction problem for genuinely novel task types, which is real and does not prevent the display — a prediction with an interval, from comparable tasks, is enormously better than nothing.

## What to Build

A duration model and a pricing interface built around the implied rate.

**Predict duration before the first submission.** Features available at posting: task type, interface elements, item count, instruction length and reading level, media presence, required qualifications, and the requester's own history. A gradient-boosted model on the platform's completion history handles this well, and for a task type the platform has seen thousands of times the prediction is tight.

**Update from the first submissions.** After twenty completions the empirical distribution is better than any prior, and the implied rate should be recomputed and the requester notified if it has moved materially.

**Show the rate as the primary number in the pricing interface.** Not the per-task price with a rate in small print — the implied hourly rate, prominent, with an interval, updating as the requester changes the price. "At $0.50 per task and a median completion time of 14 minutes, this pays $2.14 per hour." Most requesters correct immediately on seeing that sentence, because most never intended it.

**Include the unpaid time.** Instruction reading, qualification tests and abandoned attempts are part of the worker's time cost, and an implied rate that ignores them overstates. Including them is both more honest and more useful, and the platform records all three.

**Benchmark against something.** A comparison to the platform median, to the relevant minimum wage in the worker population's main jurisdictions, and to the requester's own previous tasks. A number with no reference point does not move behaviour.

**Give the worker the estimate too.** Predicted completion time and implied rate on every task listing, before they accept. This is what worker-built extensions already approximate from community data, badly, and the platform could do it properly.

## Target Customer

Platforms serving academic requesters, where ethics boards already require pay justification and this makes it a one-click answer, and platforms wanting to differentiate on fairness in a market where researchers publish on exactly this. Also requesters directly, most of whom are not trying to underpay.

## Impact If Built

The requester finds out what they are paying at the moment they decide it, which is the only moment that matters and the one where almost all of them will correct. The worker sees an honest time estimate before accepting. And the market's central failure — an estimation gap nobody is told about — closes with arithmetic the platform already has.
