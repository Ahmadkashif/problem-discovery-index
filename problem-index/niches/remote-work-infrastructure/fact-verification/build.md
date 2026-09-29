# Build: Continuous Fact Verification From Both Sides

**Niche:** [[niches/remote-work-infrastructure/fact-verification/profile|Fact Verification]]
**Industry:** [[industries/remote-work-infrastructure|Remote Work Infrastructure]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Establish the engagement's actual characteristics from the worker, from the platform's own data and over time, rather than from the client's description at setup.
**Tags:** #compliance #gradient-boosting #change-point-detection #confidence-intervals #evaluation-metrics #hypothesis-testing #descriptive-statistics #worker-facing
**Contested on:** Whether a platform will verify facts against the account that is paying it.

## The Problem

A platform can process a contractor payment correctly and cannot make the underlying relationship compliant. The compliance of the relationship depends on facts the platform does not check.

Misclassification is rarely a deception at setup. It is drift: an engagement begins as genuine project contracting and becomes, over three years, a full-time role with a manager, set hours, exclusive working and the client's equipment. Nothing re-evaluates, so the determination made in year one persists into year four, when the authority looks.

The signals are available. Engagement duration, payment regularity, whether the worker has other engagements on the platform, invoice patterns, whether the contract has been renewed repeatedly without scope change, whether the client provides tooling accounts — all of it sits in the platform's own records. And the worker knows the rest and is never asked.

## Why Nobody Has Built This

The client is the customer. Verification means being prepared to conclude that a paying account's engagement is not what they said, which risks the account and produces a written record of a non-compliant arrangement.

Asking the worker is more awkward still. A worker who reports that they have a manager, set hours and no other clients has just supplied evidence against their own engagement's structure — and possibly against their own income, since the likely consequence is that the client terminates rather than converts.

And the service is sold as removing the burden of thinking about this. A platform that starts checking facts is asking the customer to defend their arrangement, which is the opposite of the proposition.

## What to Build

Verification from the platform's own data, from the worker, and continuously.

**Score drift from the records.** Engagement duration, renewal count without scope change, payment regularity and amount consistency, the number of other clients the worker has on the platform, and the gap between invoiced and contracted scope. A model over the platform's own contractor population, trained on the engagements that were later challenged, identifies the ones drifting toward employment. This requires no one's cooperation.

**Ask the worker, carefully.** A short periodic check covering the factors the tests turn on: do you have set hours, who directs your work, do you work for others, whose equipment do you use, could you send a substitute. Framed as protecting their own position, which it genuinely is, and handled so that a concerning answer triggers a review rather than an immediate consequence for the worker.

**Re-evaluate on a cadence and on signals.** Annually at minimum, and whenever a drift signal crosses a threshold. A determination made once at setup is the structural error; the engagement changes and the determination does not.

**Design the intervention before you build the detection.** What happens when an engagement is found to have drifted: a conversation with the client, a recommended conversion to employment, a scope correction, a wind-down, or withdrawal of service. Without a defined ladder, detection produces findings nobody can act on and everybody regrets having.

**Protect the worker in the process.** The worker who answered honestly must not lose their income for it. A finding should route to the client as a compliance requirement rather than as a report of what the worker said, and the platform should treat retaliation as a termination-grade breach.

**Report it as an aggregate first.** The share of contractor engagements showing drift indicators, by jurisdiction and client segment, without naming individuals. That number is both the business case and a far easier thing to put in front of leadership than a list of accounts.

## Target Customer

Clients' own risk functions at larger enterprises, who carry the exposure and increasingly want the check rather than the assurance. Also platforms positioning on genuine compliance rather than on convenience — a smaller set, and the one for whom this is a strategy — and tax and labour authorities, whose interest in this question is rising.

## Impact If Built

The facts that classification actually turns on get checked rather than assumed, from the platform's own records and from the person doing the work. Drift — which is how misclassification actually happens — gets detected while it is correctable rather than years later from an authority. And the industry's sharpest exposure moves from unexamined to measured.
