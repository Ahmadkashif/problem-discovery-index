# Fix: Approved Is Not Paid

**Niche:** Payments & Programme Operations
**Industry:** [[industries/bug-bounty-platforms|Bug Bounty Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A finding is accepted, then approved, then eventually paid, and the interval between those events is unpredictable, unreported and absorbed entirely by the researcher.
**Tags:** #evaluation-metrics #confidence-intervals #worker-facing #compliance #revenue-impact #workflow-orchestration
**Contested on:** Whether the administrative shell around a programme runs itself or consumes staff attention every cycle.

## The Problem

A submission is accepted. The researcher sees a state change and an amount. Then nothing happens for a while.

Between acceptance and money arriving sit several steps invisible to the researcher: the programme's internal approval, which may wait for a manager who is on leave; the platform's payout batch, which runs on a schedule nobody published; compliance screening; and the payment rail itself, which varies by country. The total can be days or can be many weeks, and the researcher has no way to know which.

For someone whose income is irregular and comes from several programmes in several currencies, this is a genuine cash-flow problem. It is also entirely invisible in the industry's metrics: platforms report time to triage and time to resolution, both of which end well before the money moves.

The information exists. Every platform knows its own median accepted-to-paid interval, by programme and by country. None publishes it, and the researcher choosing where to spend a week is choosing partly on an economic variable nobody will tell them.

## Why It's Still Broken

**It is not measured as a service level.** Contracts specify triage speed. Payment speed is not a term anyone negotiates, so it is not reported, so it is not managed.

**The delay is distributed across parties.** Programme approval, platform batch, compliance, rail. Each party sees only their own step and none owns the total, which is the classic condition for an unmanaged end-to-end interval.

**The cost falls on the party with no leverage.** Researchers absorb the delay, do not pay fees, and have no contractual standing to complain about it.

**Approval sits with busy people.** A programme manager approving payouts individually, alongside a full-time role, is a natural bottleneck — which is the case for the policy-driven approval described in this niche's build.

**Compliance genuinely varies.** Screening and jurisdiction requirements produce real, irreducible variation for some recipients, which makes a single promised interval impossible and is used to justify publishing nothing.

## What a Fix Looks Like

**Publish the distribution, not a promise.** Median and spread of accepted-to-paid, by programme and by recipient country, visible before a researcher chooses a target. Where compliance introduces variation, report it honestly as a distribution rather than avoiding the question. This costs nothing, uses data the platform already has, and is the whole fix.

**Show the researcher where their payment is.** Which step, what is outstanding, what the expected remaining time is. Unknown-and-waiting is far worse than a known interval, and most of the frustration here is uncertainty rather than duration.

**Set an internal service level on the total.** Accepted-to-paid as a managed metric with an owner, which is currently nobody's number because each party measures their own segment.

**Automate the approval step by policy.** Most payouts are routine and require no judgement. Rule-based auto-approval below thresholds removes the most common bottleneck and leaves human attention for the exceptions.

**Offer expedited payment where it matters.** Some researchers need faster settlement and would accept a small cost for it. Nobody offers the choice.

**Report payment speed per programme publicly.** The same accountability logic that applies to severity and acceptance rates: programmes that pay promptly benefit from the comparison, and those that do not face a cost they currently do not.

## Who Feels the Pain

The researcher, carrying the cash-flow consequence of an interval they cannot see, predict or influence, on income that is already irregular.

Researchers in countries with slower payment rails, who absorb the longest delays and are frequently the participants for whom the money matters most.

Programme managers, who become a bottleneck they did not intend and are blamed for a delay that is mostly not theirs.

And the platform, for whom this is a quiet and persistent source of researcher dissatisfaction that appears in no metric they track.

## Impact If Fixed

Publishing the distribution costs nothing and removes the uncertainty that is most of the harm here. Researchers can plan, and can factor payment speed into where they work.

Policy-driven auto-approval removes the most common single bottleneck and improves the programme manager's week at the same time.

And making accepted-to-paid a managed metric with an owner would bring the same discipline to the end of the process that the industry already applies to the beginning — where it currently stops measuring precisely at the point the researcher starts caring most.
