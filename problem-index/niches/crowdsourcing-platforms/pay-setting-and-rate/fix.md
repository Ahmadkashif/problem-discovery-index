# Fix: Nobody Tells the Requester What It Turned Out To Be

**Niche:** [[niches/crowdsourcing-platforms/pay-setting-and-rate/profile|Pay Setting & the Realised Rate]]
**Industry:** [[industries/crowdsourcing-platforms|Crowdsourcing Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The batch completes, the platform knows exactly what hourly rate was paid, and the requester's summary reports the total cost.
**Tags:** #descriptive-statistics #evaluation-metrics #confidence-intervals #compliance #workflow-orchestration #quick-win #worker-facing #data-integration
**Contested on:** Whether the realised rate will be reported after the fact, when it is a completed measurement rather than a prediction.

## The Problem

A batch finishes. The requester receives a completion summary: items collected, total cost, agreement statistics, time to completion.

The platform also knows the median, quartiles and distribution of actual completion times, and therefore knows precisely what hourly rate the work paid. It does not appear anywhere.

So a requester who intended $8 an hour and paid $2.40 completes the study, publishes the paper or ships the model, and posts the next batch at the same rate. The error is never corrected because it is never surfaced, and the same requester repeats it for years.

This is the version of the problem with no prediction uncertainty at all — the work is done and the number is a measurement.

## Why It's Still Broken

Nobody built the line in the report. That is essentially the whole explanation: the completion summary was designed around cost and data quality because those are what a requester asked about, and the realised rate was never on anyone's list.

Where it has been considered, the objection is that it reflects badly on requesters and might make them uncomfortable. That is true and it is the mechanism by which it works — a requester who feels uncomfortable about $2.40 an hour raises their next price.

And there is no external requirement outside the academic segment, where ethics boards have begun asking and where the platforms serving that segment have moved furthest.

## What a Fix Looks Like

Put the realised rate in the completion report. One line, from data already computed.

Report median realised hourly rate, with quartiles, based on actual completion times including instruction reading. The distribution matters: a median of $6 with a bottom quartile at $2 tells a requester that their slower and more careful workers were badly paid, which is usually the group whose data they most want.

Compare it to something. The platform median, the requester's own previous batches, and the relevant minimum wage in the jurisdictions where the work was done. A bare number is less useful than a comparison.

Offer the bonus in the same screen. A requester who sees that their batch paid $2.40 and can top it up to $8 with one action will frequently do it — the money is small relative to a research budget and the intent was never to underpay. Making the correction one click is what converts the disclosure into a payment.

Report it for the academic segment as a compliance artefact. Ethics boards increasingly ask for pay justification, and a platform-generated realised-rate report is exactly the document required — turning an uncomfortable number into a valued feature for that buyer.

Show workers the same statistic per requester. Realised rate paid by this requester's previous batches, on the task listing. This is what worker forums and extensions already approximate and it is the strongest incentive for a requester to price properly.

And track it across the platform. Median realised rate over time, by task type and worker geography, published. A platform that reports this is inviting scrutiny it will eventually receive anyway, on terms it sets.

## Who Feels the Pain

Workers, paid a fraction of what the requester intended, repeatedly, by requesters who would fix it if they knew. Requesters, whose ethics approvals and institutional commitments are quietly breached by an arithmetic error nobody shows them. Researchers studying this market, reconstructing the number from outside. And the platform, whose reputation is shaped by a statistic it could publish and improve.

## Impact If Fixed

The requester learns what they actually paid, at the point where correcting it costs them one click and a small amount of money. Academic requesters get the compliance artefact their ethics board is asking for. And the estimation gap that drives this market's most-studied failure gets closed by a line in a report.
