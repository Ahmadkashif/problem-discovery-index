# Fix: The Threshold Is Set by Review Capacity

**Niche:** Operating Point & Threshold Setting
**Industry:** [[industries/trust-safety-tooling-vendors|Trust & Safety Tooling Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** The number is tuned until the review queue is a size the team can handle, and then described as a policy decision about harm.
**Tags:** #evaluation-metrics #confidence-intervals #probability-distributions #compliance #worker-facing #workflow-orchestration
**Contested on:** Whether the number that decides how much harm is missed and how much legitimate speech is removed is chosen with a framework.

## The Problem

The threshold is set. The queue is too large — the review team cannot work it within the service level. The threshold goes up. The queue becomes manageable.

That adjustment moved the operating point. More harmful content now passes unactioned, and the volume of it is not measured. The decision was made for an operational reason and is subsequently described, in policy documents and in regulatory submissions, as the platform's approach to balancing safety and expression.

This is not deception. The people involved are managing a real constraint with real service levels. But the effect is that the platform's most consequential moderation parameter is set by its staffing budget and is presented as a policy position.

It also means the parameter moves for reasons unrelated to harm. Review headcount changes, a hiring freeze, a seasonal volume spike, a vendor contract renegotiation — each can move the threshold, and each moves how much harmful content reaches users.

And because the capacity constraint is not stated, nobody can see that the platform's safety posture is a function of its operations budget.

## Why It's Still Broken

**The constraint is genuine.** Review capacity is finite and a queue that cannot be worked is worse than one that is filtered, so the adjustment is a reasonable operational response.

**Stating it is awkward.** A platform acknowledging that its threshold is set by staffing has said something uncomfortable about its safety commitments.

**The two decisions are made by the same person.** The person tuning the threshold is frequently the person responsible for the queue, so the operational and the policy considerations are not separated even in their own mind.

**The policy document was written separately.** Policy states an approach; configuration implements a constraint; nobody reconciles them.

**The missed-harm consequence is unmeasured.** Nobody measures how much harmful content passes unactioned at a given threshold, so the cost of raising it is invisible.

**Nobody asks how the number was set.** Regulators ask about policies and processes, not about the configuration value and its basis.

## What a Fix Looks Like

**Separate the two decisions explicitly.** The harm-based threshold — where the balance should sit — and the capacity-adjusted threshold actually in force, recorded as different numbers with the gap between them visible.

**Report the gap.** How much additional content would be reviewed at the harm-based threshold, and therefore what capacity would be required to operate at it. This converts an invisible compromise into a resourcing argument with a number.

**Measure what passes.** Sample content below the threshold and review it. The rate of harmful content passing unactioned is measurable, is not measured, and is the cost of the capacity constraint.

**Record the reason for every change.** A threshold moved for capacity reasons should be recorded as such, so the history shows what drove the platform's safety posture over time.

**Use tiering to absorb capacity pressure differently.** Rather than raising the single threshold, add an intermediate tier handled with lighter review. This preserves more coverage at lower cost than simply cutting off.

**Make the capacity constraint visible to leadership.** A platform whose safety posture is set by its review budget should have that stated to the people who set the budget, which is the argument that would change it.

**State it in regulatory submissions.** Where a platform describes its moderation approach, the capacity constraint is part of the truth, and describing the harm-based position without it is a partial account.

## Who Feels the Pain

Users encountering harmful content that a lower threshold would have caught, in a volume nobody has measured.

The trust and safety engineer, making an operational adjustment they know is a policy decision, with no framework and no way to raise it.

The review team, whose capacity is silently determining the platform's safety posture.

And the platform's own leadership, who believe their moderation approach reflects a policy judgement and are looking at a staffing constraint.

## Impact If Fixed

Recording the harm-based threshold separately from the capacity-adjusted one makes the compromise visible, and it costs two numbers instead of one.

Reporting the capacity gap converts an invisible operational compromise into a resourcing argument with a magnitude, which is the only form in which it gets addressed.

And measuring what passes below the threshold would give the missed-harm side of the trade a number, which is the half that currently has none and the half the capacity constraint silently increases.
