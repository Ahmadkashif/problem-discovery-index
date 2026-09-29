# Very Small Balances, Real Difficulty

**Niche:** [[niches/bnpl-providers/the-collections-agent/profile|The Collections Agent]]
**Industry:** [[industries/bnpl-providers|BNPL Providers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Agents work a queue of very small delinquent balances belonging to people in genuine difficulty, under contact rules and a recovery target, with no way to tell who needs a payment plan and who needs to be left alone.
**Tags:** #worker-facing #gradient-boosting #survival-analysis #evaluation-metrics #confidence-intervals #compliance #workflow-orchestration #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to tell the agent who needs a payment plan and who needs to be left alone — and whoever does that changes both the recovery rate and what this job does to the people doing it.

## The Problem
The queue contains balances of forty pounds. Some belong to people who forgot, and a message resolves it. Some belong to people whose card expired. Some belong to people who have lost a job, are managing six plans across six providers, and cannot pay any of them. The agent cannot tell which is which until they make contact, the contact itself costs more than a small balance is worth, and they are measured on recovery. They spend their day pursuing people for small amounts, some of whom are in serious distress, with no information that would let them be useful to any of them.

## Why Nobody Has Built This
Collections inherited its shape from conventional lending where balances are larger and the economics support a person's attention — the practice was transplanted to a product whose unit economics are completely different and was not redesigned. The provider knows a great deal about these customers and routes them into an undifferentiated queue. Hardship is identified only when disclosed. And the agent's experience of the work is nobody's metric.

## What to Build
Segment before contacting. Predict who will self-cure, who will respond to a reminder, who needs a payment plan and who is in genuine hardship, which is well-posed from the provider's own data and is the whole difference between a humane, effective function and a dialler — the segmentation exists in the data and the queue discards it. Route accordingly, so the forgetful get a message, the card-expired get a link, the struggling get a plan offered before they have to ask, and the distressed get a human with time. Offer the payment plan proactively rather than requiring the customer to know to ask, since the people who most need it are the least likely to know it exists. Detect hardship from behaviour rather than waiting for disclosure, connecting to the prediction niche, because disclosure requires the customer to initiate a difficult conversation. Give the agent the context — what this person's pattern is, what has worked with similar customers, what they can offer — rather than a name and a balance. Respect the economics, since pursuing a small balance through a full contact sequence can cost more than writing it off and nobody has computed where that line is. Measure the agent on outcomes that include appropriate forbearance, not only on recovery, which is the fix note's subject. Comply with the tightening regulatory expectations by design rather than by rule-following, since the direction of travel is clear. Support the agent's own wellbeing, since a queue of distressed people is a documented occupational hazard and this function has high turnover for a reason. And measure recovery alongside complaint rate and hardship outcomes, because a function optimising one of those is producing the others.

## Target Customer
Collections leadership at instalment providers, the agents themselves, and the regulators forming expectations about how this sector treats people in difficulty.

## Impact If Built
Collections practice was transplanted from lending with larger balances and was never redesigned for these unit economics. The segmentation that would make the function humane and effective exists in the provider's own data and is discarded by the queue.
