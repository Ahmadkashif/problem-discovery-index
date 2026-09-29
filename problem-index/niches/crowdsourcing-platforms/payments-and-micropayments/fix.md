# Fix: The Money Is Held for Four Weeks by Default

**Niche:** [[niches/crowdsourcing-platforms/payments-and-micropayments/profile|Payment, Micropayments & Cross-Border]]
**Industry:** [[industries/crowdsourcing-platforms|Crowdsourcing Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Work submitted today is auto-approved in several weeks because that is where the default was set, and nobody chose it deliberately.
**Tags:** #descriptive-statistics #evaluation-metrics #confidence-intervals #workflow-orchestration #compliance #worker-facing #quick-win #revenue-impact
**Contested on:** Whether the auto-approval window will be set to something a requester actually needs.

## The Problem

A requester posts a batch with an auto-approval period. The default on several platforms is measured in weeks, sometimes as long as a month, and most requesters accept the default without considering it — they are thinking about their study or their dataset, not about when a worker gets paid.

So the worker's earnings sit unavailable for weeks. For someone whose crowdwork is a meaningful part of their income, this is a rolling month of held wages, and it compounds across every batch they work.

The requester almost never needs it. Most review their results within days, or never review them at all and let auto-approval run. The long window is protecting against a review that is not going to happen.

## Why It's Still Broken

Defaults are sticky and nobody owns this one. It was set conservatively at some point, it protects the requester, and no requester has ever complained that it is too long.

The platform has no incentive to shorten it: a shorter window increases the rate of rejections-after-payment disputes slightly and provides no revenue benefit.

And the workers affected have no channel through which to raise it, so the default persists by inertia rather than by decision.

## What a Fix Looks Like

Change the default and make the long window deliberate.

Set the default to a few days. A requester who genuinely needs longer can extend it at posting, with a prompt asking why. Most will not, because most do not need it, and this single change moves the majority of payments weeks earlier.

Show the requester the consequence at posting. "Your approval window means workers are paid on the 28th." Requesters overwhelmingly have not thought about this and many will shorten it once they see the date.

Auto-approve on inaction faster. Where a requester has not opened the results at all after a few days, approve. The window exists to permit review; no review has occurred and none is coming.

Pay progressively. Approve and pay in tranches as a batch is reviewed, rather than holding everything until the window closes. A requester who reviews the first two hundred submissions on Tuesday should have paid for them on Tuesday.

Publish approval speed per requester, which is the discipline mechanism — a requester whose median approval time is twenty-six days will get fewer workers once that is on their listing.

And let the worker see the date. Pending earnings with an expected availability date, per batch. Currently a worker sees a pending balance with no indication of when it becomes real.

## Who Feels the Pain

Workers, whose earnings are unavailable for weeks by default, most acutely those for whom the income is immediate and necessary. New workers, who have no float to absorb the lag. And the platform, which is imposing a rolling month of held wages on its entire supply side through a setting nobody chose.

## Impact If Fixed

Most payments arrive weeks earlier, from a default change and a prompt. Requesters who need a long window still have one, deliberately. Approval speed becomes visible and therefore competitive. And a worker can see when their money becomes real.
