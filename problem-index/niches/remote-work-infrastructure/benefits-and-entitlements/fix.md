# Fix: The Worker Does Not Know What They Are Entitled To

**Niche:** [[niches/remote-work-infrastructure/benefits-and-entitlements/profile|Benefits, Leave & Local Entitlements]]
**Industry:** [[industries/remote-work-infrastructure|Remote Work Infrastructure]]
**Type:** Fix (Pain Point)
**One-liner:** The platform shows a leave balance and the worker has no idea whether their own country's law entitles them to more.
**Tags:** #compliance #descriptive-statistics #evaluation-metrics #workflow-orchestration #confidence-intervals #worker-facing #quick-win #data-integration
**Contested on:** Whether the worker will be told what their own country's law gives them.

## The Problem

A worker employed through an employer of record sees a leave balance in a portal. Eighteen days. They take leave against it.

They do not know whether their country's statutory minimum is fifteen days or twenty-five. They do not know whether the eighteen includes public holidays or is on top of them. They do not know what happens to unused days at year end. They do not know their sick pay entitlement, their notice period, or whether they qualify for parental leave.

The platform knows all of it — it must, because it is legally obliged to provide it — and shows a number. So a worker receiving less than their statutory entitlement has no way to notice, and a worker who would be entitled to something they never claim simply does not claim it.

## Why It's Still Broken

The portal was built to administer leave requests, and a balance is what administration needs. Explaining the entitlement's legal basis was not a requirement.

There is also a mild disincentive: a worker who knows their statutory entitlement precisely is a worker who can check, and may find a discrepancy. Not telling them is the state that produces no queries.

And the worker's country's rules are held by the compliance team in a form that was never intended to be shown to anyone.

## What a Fix Looks Like

Show the entitlement and its basis. It is a rendering of what the platform must already know.

Display two numbers, not one. Your statutory minimum under [country] law, and your entitlement under your employer's policy, with the applicable one marked. Where the policy is more generous, say so — it is a benefit the client is providing and they should get credit for it.

Cite the rule. One line naming the statutory basis, in plain language. This is what converts a number into something a worker can check and trust.

Cover the entitlements nobody mentions. Sick pay and its conditions, parental leave and eligibility, notice period by tenure, public holidays, pension or social contributions being made on their behalf, and any thirteenth-month or statutory bonus. A single page per worker, generated from their jurisdiction and tenure.

Write it in their language. A statutory entitlement explained in English to a worker who works in Portuguese is not explained.

Alert on expiry and eligibility. Leave expiring, an eligibility threshold approaching, a notice period changing at a tenure milestone. Workers lose entitlements to not knowing and a notification is free.

Give them a route to ask. A question about their own entitlement should reach the compliance function, not a generic support queue, because the answer is a legal one.

And run the check. Any worker whose recorded entitlement is below their jurisdiction's statutory minimum, as a standing query. It should return nothing.

## Who Feels the Pain

Workers, who cannot tell whether they are receiving what their own country requires and who lose entitlements they never knew they had — most acutely those in jurisdictions with generous statutory provision working for clients with less generous policies. Clients, exposed by shortfalls nobody noticed. And the platform, whose legal obligation is to provide entitlements that the worker cannot verify.

## Impact If Fixed

The worker can see what their own law gives them, alongside what the policy gives them, with the basis cited — which is the only mechanism by which a shortfall is ever noticed. Entitlements stop being lost to ignorance. And the standing check confirms that the statutory floor is actually being met, which nobody currently verifies.
