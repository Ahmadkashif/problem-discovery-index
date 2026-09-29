# The Agent Reviewing a Deactivation Appeal

**Industry:** [[gig-delivery-platforms|Gig Delivery Platforms]]
**Type:** Worker Life Changing
**One-liner:** Someone lost their income because an automated system flagged their account, and an agent with a policy and a queue decides within minutes whether they get it back.
**Tags:** #gradient-boosting #graph-neural-networks #confidence-intervals #bert #evaluation-metrics #compliance #worker-facing #hypothesis-testing

## The Problem
Deactivation ends a courier's access to the platform and, for the many people doing this full time, their income. The triggers are customer complaints, low ratings, completion or acceptance metrics, alleged fraud, background check results and policy violations, and much of the detection is automated.

The notice is frequently generic — a policy reference and a statement that the account has been deactivated — and the appeal is a form. An agent reviews it with the flag, whatever evidence the system captured, and the courier's written explanation, under queue pressure.

The evidence is often thin and one-sided. A customer complaint that food was not delivered may be true, may be a customer seeking a refund, may be a theft from a doorstep, and the available record rarely distinguishes them. A fraud flag may reflect genuine abuse or a location signal anomaly from a phone in a lift.

Because the classification is contractor, none of the process protections that would attach to dismissal from employment apply — no notice period, no hearing, no requirement to state a case. Several jurisdictions have begun imposing deactivation protections precisely because of this gap, and the classification itself remains contested in law.

For the agent, the position is impossible in a specific way: they cannot verify most of what they are deciding, and the cost of being wrong falls almost entirely on someone whose rent depends on it.

## Why It Matters to the Worker
Both workers in this situation are poorly served. The courier has lost their income to an automated determination they cannot inspect, with an appeal that returns a template. The agent is asked to make a livelihood decision in minutes on unverifiable evidence, repeatedly, with no feedback about whether they got it right.

The volume prevents care. A queue with throughput expectations does not distinguish a plainly fraudulent account from a four-year courier with a single disputed complaint, and the agent knows the difference matters and cannot act on it within the time.

And there is no calibration. Nobody measures how often deactivations are wrong, because a wrongly deactivated courier who does not appeal — or who appeals and is refused — generates no record that contradicts the decision. The error rate of a system that removes people's incomes is unknown to the organisation operating it.

## What a Solution Looks Like
Weight review by consequence. A courier with years of history and thousands of deliveries facing deactivation on a single complaint is a different case from a two-week-old account with a pattern, and routing time and evidence depth by that difference is the most consequential change available.

Assemble real evidence. Delivery history, location and timing traces, photographic proof of delivery, the customer's own complaint and refund history, and comparable prior cases — presented as a structured case rather than a flag — let an agent decide rather than guess. A customer with an unusual refund complaint rate is highly informative and is rarely surfaced.

Measure the error rate. Sampling appeals, auditing a random selection of deactivations, and tracking reinstatement outcomes produce a false positive rate nobody currently knows. Without it, no threshold can be set responsibly.

State the reason specifically and allow a real appeal. Which delivery, which date, what the allegation is, and what evidence would change the decision. This is the direction regulation is moving in several jurisdictions and it is the minimum for a process with this consequence.

And support the agents. Consequence-weighted queues rather than uniform throughput targets, and acknowledgement that reviewing appeals from people who have lost their income is work with a psychological cost.

## Impact If Solved
Deactivation decides whether people keep working, is triggered by automated systems, adjudicated in minutes on unverifiable evidence, and has an error rate nobody has measured. Consequence-weighted review, assembled evidence including the complainant's own history, measured error rates and specific stated reasons with genuine appeal address both the injustice to couriers and the impossible position of the agents making the calls.
