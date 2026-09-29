# Fix: The Reviewer Saw It First and Told Nobody Who Could Act

**Niche:** Novel Harm Response
**Industry:** [[industries/trust-safety-tooling-vendors|Trust & Safety Tooling Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** A moderator sees something that matches no category, escalates it, and the escalation joins a policy queue rather than triggering anything.
**Tags:** #evaluation-metrics #change-point-detection #confidence-intervals #worker-facing #workflow-orchestration #automation
**Contested on:** Whether a new abuse pattern can be detected in the weeks when it does most of its damage.

## The Problem

A reviewer working a queue encounters something unfamiliar. A framing they have not seen, a coordinated pattern, a scam format that does not match any existing category. They escalate it as uncategorisable.

The escalation goes to a policy queue. Policy teams work through escalations to decide whether a new category is needed, which is a considered process operating on a weekly or monthly cadence.

Meanwhile three other reviewers on different shifts have escalated similar items. Nobody has connected them. The rate of uncategorisable escalations has risen sharply and nothing is watching the rate. And the pattern that four experienced humans independently flagged as new is working through a queue designed for policy deliberation rather than for detection.

By the time policy defines it, labelled data is produced and a model is retrained, the campaign is over.

The reviewers were the earliest and most reliable signal available. They noticed within hours. Their observation was routed to the slowest possible destination.

## Why It's Still Broken

**Escalation was designed for policy, not detection.** The path exists so that policy can decide whether the taxonomy needs extending, which is a legitimate and slow purpose.

**Nobody watches the rate.** Individual escalations are cases. The rate of uncategorisable escalations is a signal and is not monitored anywhere.

**Similar escalations are not clustered.** Four reviewers describing the same novel pattern in different words produce four unconnected cases.

**Reviewers are not treated as sensors.** Their observation is an input to a decision rather than a detection signal, which is a framing choice with large consequences.

**The escalation costs the reviewer.** Escalating takes longer than deciding, and in a queue with a throughput target the incentive is to make a call and move on.

**Nobody measures the delay.** From first reviewer escalation to deployed detection is not tracked, so the cost of routing the earliest signal to the slowest process is invisible.

## What a Fix Looks Like

**Monitor the uncategorisable escalation rate.** A rising rate is a direct signal that something new is happening, computable from data already collected, and watched by nobody.

**Cluster escalations semantically.** Four reviewers describing the same thing differently should appear as one emerging pattern rather than four cases. This is embedding-based clustering over the escalation text.

**Give escalations a fast path as well as a policy path.** A rapid-response route that can deploy a provisional detection — a few-shot classifier, a similarity match, a temporary rule — within hours, in parallel with the policy process that will eventually define the category properly.

**Make escalating cheap and rewarded.** A one-click "I have not seen this before" with no throughput penalty, and feedback to the reviewer when their escalation led to a response. Reviewers are the sensor and the sensor is currently discouraged.

**Feed report free text into the same signal.** Users describing an unfamiliar harm in a report's free text are a second independent channel, collected and unanalysed.

**Measure the interval.** First escalation to provisional response, tracked per incident. This produces the number that makes the case for the fast path.

**Close the loop with reviewers.** Telling the reviewers who escalated that a pattern was confirmed and acted on is what sustains the behaviour, and it is the same reinforcement problem that appears wherever a reporting behaviour matters.

## Who Feels the Pain

Users encountering a novel harm during the weeks between a reviewer noticing it and the system responding.

The reviewer, who saw it first, escalated it, and watched nothing happen — which teaches them not to escalate next time.

The policy team, receiving escalations as individual cases with no view of the rate or the clustering that would tell them something is emerging.

And the platform, whose earliest and most reliable detection signal is routed to a process designed for deliberation.

## Impact If Fixed

Monitoring the uncategorisable escalation rate is computable from existing data and is the earliest signal available, currently watched by nobody.

A fast path that can deploy a provisional detection in hours, alongside the policy process rather than after it, is what compresses the response interval from weeks to days.

And closing the loop with the reviewers who escalated is what sustains the signal — because a sensor that receives no feedback stops reporting, which is how the earliest detection channel quietly degrades.
