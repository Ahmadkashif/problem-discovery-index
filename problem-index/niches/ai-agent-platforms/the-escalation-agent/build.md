# An Action They Did Not Take and Cannot Explain

**Niche:** [[niches/ai-agent-platforms/the-escalation-agent/profile|The Escalation Agent]]
**Industry:** [[industries/ai-agent-platforms|AI Agent Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** When an agent does something wrong on a customer's behalf, a human support agent inherits an angry customer, an action they did not take and cannot explain, and no clear path to undo it.
**Tags:** #worker-facing #large-language-models #data-integration #evaluation-metrics #workflow-orchestration #automation #descriptive-statistics #compliance
**Contested on:** Every serious competitor in this niche is fighting to hand a human the full account of what the agent did and a way to put it right — and whoever does that takes the account, because this handoff is where every agent failure becomes a customer's experience.

## The Problem
A customer calls, furious, because their subscription was cancelled and their data is gone. The support agent opens the ticket and sees a conversation between the customer and the agent that reads reasonably, and a note saying the request was completed. They cannot see that the agent called a cancellation tool with a flag that also purges data, that it did so because the customer's phrasing matched a pattern in a way nobody anticipated, or that a restore is possible for seven days through a path nobody has told them about. They apologise for something they cannot describe and promise to find out.

## Why Nobody Has Built This
The escalation interface was inherited from the era when the thing being escalated was a conversation. Trajectory data lives in an engineering observability tool, not in the support console. Building the handoff means integrating an agent platform with a ticketing system in a way both vendors treat as the other's job. And the support agent is nobody's buyer, so the requirement is never in a specification.

## What to Build
Deliver the trajectory to the person who inherits it. Put a human-readable account of what the agent did in the support console: the steps taken, the tools called with their arguments, what changed in which system, and the point at which it went wrong — assembled from a record that already exists and is currently delivered to nobody, which is the entire build. Explain the agent's reasoning in plain language, since the support agent's first task is telling the customer why, and having an answer changes the conversation entirely. List the concrete effects in downstream systems, because the agent's account of what it did and what actually happened can differ and the support agent needs the second. Offer the undo path directly, with the compensating actions and their consequences, which is where the platform work on compensation pays off for the person who needs it most. Flag the escalation as agent-caused and prioritise it, since these are the highest-risk contacts a support organisation handles and are currently queued as ordinary tickets. Give the support agent a one-click route to report the failure back into the agent's improvement loop, which is the highest-quality failure signal the vendor will ever receive and is currently discarded. Preserve the conversation context so the customer does not repeat themselves. And measure resolution time and outcome on agent-caused escalations separately, because they behave differently and are the deployment's true cost.

## Target Customer
Support organisations and the agents handling escalations, the buyers whose customer relationships depend on this moment, and the vendors whose failures land here.

## Impact If Built
The record needed to handle the escalation already exists and is delivered to nobody. Putting the trajectory and the concrete downstream effects in the support console, with an undo path attached, changes the one conversation that determines whether the customer forgives the deployment.
