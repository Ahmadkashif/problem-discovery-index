# A Commercial Decision With an Operations Mandate

**Niche:** [[niches/ai-inference-providers/the-capacity-sre/profile|The Capacity SRE]]
**Industry:** [[industries/ai-inference-providers|AI Inference Providers]]
**Type:** Fix (Pain Point)
**One-liner:** Reliability engineers are repeatedly asked to choose which customer relationship to damage, which is a commercial judgement they have no authority to make and no policy to point at.
**Tags:** #worker-facing #compliance #descriptive-statistics #evaluation-metrics #workflow-orchestration #quick-win #automation #confidence-intervals
**Contested on:** Every serious competitor in this niche is fighting to make contention a policy the system executes rather than a decision a person makes at three in the morning — and whoever does that takes the account, because the arbitration is currently a human bottleneck with commercial consequences.

## The Problem
An engineer throttles a customer at four in the morning to protect two others. At nine the account manager for that customer arrives at their desk angry, having heard from the customer first. The engineer made a defensible call with the information available and is now defending a commercial decision they were never authorised to make, in a meeting about an incident that was caused by a fleet size somebody else chose. This happens often enough that people leave over it, and the company experiences it as reliability attrition rather than as a governance failure.

## Why It's Still Broken
The decision has to be made in seconds and the commercial owners are asleep, so delegation to operations is the only workable arrangement in the moment. Nobody wants to write the policy that ranks customers explicitly, because the document is uncomfortable and might leak. The absence of a policy is experienced as flexibility by the commercial side and as exposure by the engineer. And the cost lands on individuals, who do not have standing to escalate it.

## What a Fix Looks Like
Give the decision an owner and the engineer a mandate. Write the priority policy explicitly, approved by the commercial leadership, so the engineer executes a decision rather than making one — this is the whole fix, and its difficulty is organisational rather than technical. Put the policy in the tooling at the moment of decision, so it does not depend on recall under pressure. Record every arbitration with its inputs and its rationale, which protects the engineer, builds the policy empirically, and turns the morning meeting into a review of the policy rather than of the person. Notify the account owner automatically when their customer is affected, so nobody learns from the customer. Establish who to wake for a genuine exception and make waking them normal rather than a failure. Review the arbitration log with the commercial side monthly, which is what converts a repeated incident into a capacity decision. Report the frequency of these events as a capacity metric, since they are a symptom of provisioning rather than of operations and are currently attributed to the wrong function. And stop treating the resulting attrition as ordinary reliability turnover, because it is a specific and fixable cause.

## Who Feels the Pain
Reliability engineers making and then defending commercial decisions; the account teams hearing from customers before their own company; and the customers throttled on a policy that did not exist.

## Impact If Fixed
The engineer is executing an unwritten commercial policy and then being held accountable for it. Writing and approving the policy transfers the decision to its owner, and logging every arbitration turns the morning meeting into a review of the policy rather than of the person.
