# SRE During a Capacity Event

**Industry:** [[ai-inference-providers|AI Inference Providers]]
**Type:** Worker Life Changing
**One-liner:** Site reliability engineers manage capacity crises by hand — deciding in real time which customer gets degraded so that another does not — because the system has no way to anticipate a spike or to arbitrate between guarantees.
**Tags:** #time-series-forecasting #change-point-detection #gradient-boosting #confidence-intervals #optimization-fundamentals #evaluation-metrics #workflow-orchestration #worker-facing

## The Problem
Demand exceeds capacity. Latency rises across a fleet, queues build, and the on-call engineer has minutes to act.

The available moves are all bad. Add capacity, which takes long enough that the spike may pass first. Shed load, which means choosing whose requests to reject. Migrate a tenant, which requires loading model weights elsewhere and takes minutes. Reduce batch sizes, trading throughput for latency. Ask a large customer to slow down, which is a phone call.

Choosing requires knowing which customers have the strictest guarantees, which are on committed contracts, which are in a trial, which are about to renew, and which will simply leave. That information is spread across the contract system, the account team's knowledge and the engineer's memory.

The events are unannounced. A customer's launch, a batch job, a viral moment — the engineer learns about it from the alert. They spend the first ten minutes establishing what is happening, which is the most valuable ten minutes.

## Why It Matters to the Worker
This is high-stakes real-time decision making with commercial consequences and no decision support. An engineer is choosing which customer to disappoint, at three in the morning, with incomplete information about what those customers are worth.

The unpredictability is the corrosive part. The events cannot be planned for, they arrive without warning, and the on-call rotation is therefore permanently tense in a way that a predictable operational load is not.

The blame dynamics are unpleasant. A capacity event is a business failure with a technical trigger, and the post-incident discussion involves the account team, the capacity planners and the engineer who made the call. The engineer made a defensible decision with the information available and it will be second-guessed with information they did not have.

Attrition on these teams is high and the reason given is consistently the on-call load rather than the technical difficulty.

## What a Solution Looks Like
Early warning from leading indicators. Many spikes ramp before they peak — a customer's traffic rising gradually over an hour, queue depth trending, a batch job's first requests arriving. Detecting the ramp and predicting the peak gives the minutes that make proactive capacity possible.

Predictive warm-up. If a spike is anticipated, weights can be staged on standby capacity before it arrives, which is the only way to defeat cold start.

Codified priorities. Which tenants are protected under which conditions should be a policy the system executes, not a judgement an engineer makes at three in the morning under pressure. The commercial input belongs in a contract system rather than in someone's memory.

Automated graceful degradation. Reducing batch sizes, shedding the lowest-priority traffic and throttling by policy are mechanical responses that should execute automatically within bounds, with the engineer supervising rather than typing.

Customer signalling, incentivised. A pricing structure that rewards announcing a launch would remove a large share of these events entirely, and it is a commercial decision rather than a technical one.

## Impact If Solved
Capacity events are the defining stressor of reliability work in this category and are handled by manual arbitration under time pressure. Early warning plus codified priority converts a crisis into a policy execution, and predictive warm-up addresses the cold start that makes reactive scaling too slow to help.
