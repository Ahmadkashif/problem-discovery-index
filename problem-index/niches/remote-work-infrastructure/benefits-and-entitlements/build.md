# Build: Statutory Entitlement as a Computed Floor

**Niche:** [[niches/remote-work-infrastructure/benefits-and-entitlements/profile|Benefits, Leave & Local Entitlements]]
**Industry:** [[industries/remote-work-infrastructure|Remote Work Infrastructure]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Compute each worker's statutory minimum entitlement from their own jurisdiction's rules, compare it to what the policy provides, and enforce the larger.
**Tags:** #compliance #data-integration #evaluation-metrics #confidence-intervals #descriptive-statistics #workflow-orchestration #worker-facing #automation
**Contested on:** Whether the statutory floor can be computed per worker across dozens of intricate accrual regimes.

## The Problem

Entitlement is the part of employment law that is most detailed and most often simplified into something wrong. Annual leave accrual with proration, carryover limits and expiry dates. Sick pay with waiting days, employer and state portions and duration caps. Parental leave with eligibility conditions and pay steps. Public holidays that fall on weekends and are or are not moved. Notice periods that scale with tenure. Thirteenth-month payments with their own timing and calculation base.

Platforms encode a simplified version and it is right in the ordinary case and wrong at the edges — a worker who takes leave across a year boundary, who is sick during booked leave, who joins mid-year, who has a public holiday during a leave period. The edges are where the entitlement is actually determined and where the worker is quietly short-changed.

The client's policy then sits on top, sometimes more generous, sometimes less, and the resolution is ad hoc.

## Why Nobody Has Built This

Entitlement rules are the most fiddly part of employment law and encoding them properly across sixty jurisdictions is a large unglamorous project. The simplified version works for most workers most of the time, and the errors are small, individual and quiet.

They are also invisible. A worker who accrued eighteen days when the law entitled them to twenty will not know, because they do not know their own country's rule and the platform's number appears authoritative.

And the client, who is the customer, wants policy consistency across markets and experiences statutory variation as an annoyance rather than as a floor.

## What to Build

Entitlement as a computation with the statutory floor enforced.

**Encode the accrual rules properly, including the edges.** Per jurisdiction: accrual method and rate, proration on joining and leaving, carryover limits and expiry, the interaction of public holidays with leave, sickness during leave, and the treatment of part-time and irregular hours. These are the rules that determine the outcome and they are where simplification produces error.

**Compute the statutory minimum per worker, continuously.** Not a policy figure but a calculated entitlement from their own jurisdiction's rules given their tenure, hours and circumstances, updating as the year progresses.

**Compare to policy and enforce the greater.** Where the client's policy is more generous, the policy applies. Where it is not, the statutory floor applies and the client is told. This resolution should be automatic rather than a case-by-case escalation, and stating it as the platform's standing position is what makes it work.

**Version by effective date.** Entitlement rules change and a worker's accrual in a year spanning a change follows both. Getting this right requires the rule base versioning from the determination niche.

**Show the worker their own entitlement and its basis.** Statutory minimum, policy provision, what applies, accrued to date, taken, remaining, and expiring when — with the rule cited. This is the single most valuable worker-facing feature in the industry and it is a rendering of a computation.

**Alert on the expiring and the unused.** Leave that will expire, entitlements not taken, parental leave eligibility approaching. Workers lose entitlements to not knowing, and a notification costs nothing.

**Check the population.** Workers whose recorded entitlement is below the statutory minimum for their jurisdiction, as a standing query. It should be empty and in practice will not be.

## Target Customer

Platform compliance and benefits operations, for whom a worker receiving less than their statutory minimum is a liability in every jurisdiction. Also clients' own risk functions, and worker representative bodies in the markets where these arrangements are common.

## Impact If Built

Entitlement becomes a computation from the worker's own law rather than a simplification of it, correct at the edges where it is actually determined. The statutory floor gets enforced automatically rather than negotiated per case. And the worker can see what they are entitled to and why — which is what stops entitlements being quietly lost.
