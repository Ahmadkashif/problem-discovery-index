# Fix: Clinicians Idle in One State, Queues in Another

**Niche:** [[niches/telehealth-platforms/licensure-and-capacity/profile|Licensure, Credentialing & Capacity Matching]]
**Industry:** [[industries/telehealth-platforms|Telehealth Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Three clinicians are logged on with no patients and a queue is building two states away, and nobody sees both facts at once.
**Tags:** #descriptive-statistics #time-series-forecasting #evaluation-metrics #confidence-intervals #workflow-orchestration #quick-win #automation #worker-facing
**Contested on:** Whether the platform will look at idle capacity and queue depth on the same screen.

## The Problem

At any given moment a national telehealth platform has clinicians logged on with nothing to do and patients waiting. The two are in different states, and the licences do not overlap.

Nobody sees this. The operations view shows aggregate wait time and aggregate clinician utilisation, both of which look acceptable. The state-level picture — where the idle capacity is and where the queue is — is the only view that would reveal the mismatch, and it is not built.

The consequence is paid idle time on one side, breached service levels on the other, and clinicians who log on for a shift and earn little because the demand was elsewhere. That last effect drives clinicians off the platform, which tightens the constraint further.

## Why It's Still Broken

Aggregate metrics are what leadership dashboards were built on, and they conceal this perfectly: total utilisation and average wait can both look fine while a third of the states are mismatched.

The state-level view also feels like detail rather than signal, until someone looks at it. And the response — who to route to, which incentive to send, which licence to fund — requires the forecasting and optimisation that has not been built, so there has been no demand for the view that would drive it.

Clinicians experience the problem and cannot articulate it precisely, because they see only their own empty queue.

## What a Fix Looks Like

Build the state-level operational view and act on the obvious cases.

Show idle clinician-hours and queue depth by state, live, on one screen, with the mismatch highlighted. This is a pivot over data the platform already has and it makes the problem visible for the first time.

Track it historically by state and hour. Recurring patterns — this state is always short on Sunday evenings, that one always has idle capacity mid-afternoon — are stable and are the basis for every improvement. Most of them will turn out to be predictable and persistent.

Tell clinicians before their shift. A clinician choosing when to log on should see where demand is expected and whether their licences cover it. Many will shift their hours voluntarily, which costs nothing and is the cheapest available lever.

Target the incentive at the people who can act. A surge rate should go to clinicians licensed in the short state who work those hours, not to the whole pool. This is a filter on an existing mechanism.

Use the historical mismatch to direct the licence budget. The states that are persistently short and the clinicians who work the hours when they are short together identify the licences worth funding — which is a query over the same view rather than the full optimisation.

And measure the cost. Idle paid hours and breached service levels by state, monthly. Nobody produces this number and it is what makes the case for doing anything else.

## Who Feels the Pain

Clinicians who log on for a shift and earn a fraction of what they expected because demand was in a state they are not licensed in, and who leave for platforms where that happens less. Patients in states that are structurally short. And the platform, which pays for idle capacity and breaches service levels simultaneously while its aggregate dashboard looks healthy.

## Impact If Fixed

The mismatch becomes visible, which is the whole first step. Clinicians get told where the demand will be and many respond without any incentive. Surge incentives reach people who can actually serve the shortage. And the licence budget starts going to the pairs that relieve the constraint rather than to whoever asked.
