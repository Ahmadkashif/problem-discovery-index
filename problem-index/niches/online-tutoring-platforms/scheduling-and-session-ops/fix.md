# Fix: The Policy Was Written for the Conversion Rate

**Niche:** [[niches/online-tutoring-platforms/scheduling-and-session-ops/profile|Scheduling, Cancellation & Session Ops]]
**Industry:** [[industries/online-tutoring-platforms|Online Tutoring Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Every cancellation rule in this industry resolves in favour of whoever might not book, and the tutor holding the empty slot pays for it.
**Tags:** #descriptive-statistics #evaluation-metrics #confidence-intervals #hypothesis-testing #workflow-orchestration #worker-facing #quick-win #compliance
**Contested on:** Whether the cost of a cancellation will be allocated to the party who caused it.

## The Problem

Cancellation policies in this industry are set by whoever owns booking conversion. A short notice window converts better. A generous refund converts better. Not penalising a no-show converts better. Every decision in the policy, made in isolation, points the same way, and the cumulative result is a rule set under which a family can cancel two hours before a session at no cost, repeatedly, indefinitely.

The tutor has held the hour, prepared for it, turned down alternatives, and receives nothing. If it happens on a Tuesday evening they have lost the most valuable slot in their week.

The same family often does it again. No mechanism tracks the pattern, and the tutor's only option is to decline their future bookings — which may itself count against their acceptance metrics.

## Why It's Still Broken

Because the cost is entirely off the platform's books. A cancellation is a refund, a rescheduling and a slightly unhappy tutor. It does not appear in any metric the policy owner is measured on, while the conversion effect of tightening the policy appears immediately and negatively.

Nobody has computed the aggregate either. The total hours lost to short-notice cancellations, and their distribution across tutors and families, is a simple query that no platform runs, so the policy has never been argued against with a number.

And the party bearing the cost has no voice in the policy. Tutors are contractors, dispersed, and consulted about rules that govern their income roughly never.

## What a Fix Looks Like

Allocate the cost to whoever caused it, and measure the total first.

Compute the number. Hours lost to cancellations inside the window, by notice period, by family, by tutor, with the compensation paid. Distribution rather than mean — a small share of families almost certainly accounts for a large share of late cancellations, which changes what the right policy is entirely.

Pay the tutor for short-notice cancellations, at a meaningful fraction, automatically. This is what the policy is for and most platforms implement it partially, conditionally, or with a claim step that suppresses it. The cost falls on whoever cancelled, which is the correct allocation and also the only thing that changes behaviour.

Handle repeat cancellers specifically rather than through a uniform rule. A family who cancels late once is ordinary life; a family who does it five times is imposing a recurring cost, and the response is a graduated one — a note, then a deposit requirement, then a shorter-notice restriction. A uniform policy tuned for the first case will never address the second.

Let tutors decline bookings from repeat late-cancellers without it counting against them. Currently this is the only defence available and it is penalised.

Separate genuine emergencies. A child who is ill is not the same as a family who forgot, and a policy that cannot tell them apart will be either unfair or ineffective. A stated reason, with a small number of no-fault cancellations per term, handles nearly all of it.

And consult the tutors. A policy governing their income, set without asking them, is both worse and more resented than one arrived at with input, and the input is cheap to gather.

## Who Feels the Pain

Tutors, who lose held hours with no compensation and no recourse, most acutely at the peak evening slots that are their highest-value inventory. Tutors with fewer students, for whom one cancellation is a larger share of the week. Families who behave reasonably and are governed by a policy written around those who do not. And the platform, which is losing supply at peak times to a cost it has never counted.

## Impact If Fixed

The cost of a cancellation lands on the party who caused it, which is both fair and the only thing that reduces the rate. Repeat cancellers get handled specifically instead of through a rule that cannot see them. And the platform learns how many peak-hour supply hours it is losing to a policy tuned for conversion — a number that will surprise whoever owns it.
