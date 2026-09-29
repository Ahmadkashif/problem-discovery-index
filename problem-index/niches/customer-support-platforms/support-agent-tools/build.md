# Measure Resolution, Support the Agent

**Niche:** [[niches/customer-support-platforms/support-agent-tools/profile|Support Agent Tools]]
**Industry:** [[industries/customer-support-platforms|Customer Support Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Agents are managed by handle time and a satisfaction score, neither of which measures whether the customer's problem was solved, and the thing that would measure it — whether the customer came back — is in the same database.
**Tags:** #survival-analysis #gradient-boosting #descriptive-statistics #evaluation-metrics #confidence-intervals #hypothesis-testing #worker-facing #automation
**Contested on:** Every serious competitor building for support agents is fighting to measure and support whether the customer's problem was actually solved rather than how long it took — and whoever the agents experience as help rather than surveillance takes the deployment.

## The Problem
An agent takes eleven minutes with a customer, understands the underlying problem, fixes the immediate issue and prevents the next two. Another agent takes four minutes, answers the literal question, and the customer returns twice more. The second agent's metrics are better. Both are reviewed against a handle time target, and the target does what targets do. Meanwhile the measure that distinguishes them — whether the customer came back about the same thing — is computable from the ticket record and is not computed, so the organisation manages its support function against a number that is inversely related to the thing it wants.

## Why Nobody Has Built This
Handle time is trivially computable and has been the industry's operating metric since the contact centre was invented; resolution requires linking a later contact to an earlier one, which requires the identity and issue clustering this industry's channels niche describes. Satisfaction was adopted as the counterweight and is statistically inadequate at the individual level, which everyone half-knows. And changing the metric changes the workforce management model, the staffing calculation and the bonus scheme, which is an organisational project rather than a product feature.

## What to Build
Resolution as the primary measure, with support built around it. An issue is resolved if the customer does not return on the same matter within a window, computed from issue clustering rather than from ticket closure — which is the correction and is available today. Report it per agent with volume-appropriate uncertainty, and alongside it the things an agent can influence and currently cannot see: their own repeat rate by topic, which topics they resolve well and which they escalate, and how their conversations compare on resolution rather than on speed. Then build the support: context assembled before the agent opens the conversation, drafting grounded in the customer's own state, after-work generated rather than typed. And handle the part no product addresses — the emotional load — by detecting abusive interactions automatically and routing them away rather than leaving an agent to absorb them, by making a break after a difficult conversation a normal and unpenalised part of the workflow rather than an adherence failure, and by not showing an agent a satisfaction score from a customer who was abusive to them.

## Target Customer
Support platform vendors, support operations leaders whose attrition is high and whose metrics they privately distrust, and the workforce management functions that would have to change with them.

## Impact If Built
Resolution measurement changes what the function optimises for, which is the largest available improvement in customer experience and costs a clustering computation. The agent-facing half matters at least as much: support attrition is high, the emotional load is the dominant cause, and no product in the category has treated it as something to design for rather than as a fact about the labour market.
