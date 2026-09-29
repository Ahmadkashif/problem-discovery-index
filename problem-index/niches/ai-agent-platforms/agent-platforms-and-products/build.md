# Selling Plumbing and Selling Outcomes

**Niche:** [[niches/ai-agent-platforms/agent-platforms-and-products/profile|Agent Platforms & Products]]
**Industry:** [[industries/ai-agent-platforms|AI Agent Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A framework is bought by engineers who want control over what the agent does and a vertical agent is bought by a business owner who wants a number, and the two purchases share a runtime and no other requirement.
**Tags:** #workflow-orchestration #evaluation-metrics #data-integration #large-language-models #automation #revenue-impact #graph-theory #compliance
**Contested on:** Not terminal — the contest differs by whether the buyer is building the agent or buying its output, and the decomposition is recorded in the profile.

## The Problem
A vendor demonstrates to an engineering team and to a head of customer support. The engineers ask about state persistence across restarts, how to debug a trajectory that went wrong three steps back, and whether they can version and test the graph. The support lead asks what share of tickets will be resolved without a human, what happens when it is wrong, and what it costs per resolution compared to an outsourcer. The product answers the first set and not the second, or the reverse, and the pitch that wins one loses the other.

## Why Nobody Has Built This
The technology genuinely is shared, which makes one product look efficient. The framework business has developer adoption and the outcome business has revenue per customer, and both are attractive. But the sales motions, the proof required and the support models differ completely, and firms attempting both usually end up with a framework that is hard to sell to a business buyer and an outcome product whose margins are eaten by a delivery organisation.

## What to Build
Build the runtime properly and let the two businesses diverge above it. The genuinely shared requirement is a durable, inspectable execution substrate: state that survives restarts, a complete trajectory record, the ability to resume from any step, deterministic replay of a past run, and versioning of the agent definition — which both sides need and which most stacks handle poorly. Make replay exact, because debugging a non-deterministic multi-step failure without it is the single largest source of wasted engineering time in this category. Model the task as a durable workflow with checkpoints rather than as a conversation, so a failure mid-task is resumable rather than restarted, which the fix note develops. Record every tool call with its arguments, response and effect, since that record is the basis for debugging, for audit, for undo and for the trajectory corpus. Version the agent definition and bind each trajectory to a version, so a regression is attributable. Separate the runtime from the domain logic, which is what lets a vertical product be built quickly and a framework be embedded. And be explicit about which business a given company is in, because the framework's buyer and the outcome buyer will each discover the mismatch eventually.

## Target Customer
Engineering teams building agents, business functions buying outcomes, and the vendors deciding which of those they serve.

## Impact If Built
The shared layer is a durable, replayable execution substrate, and most stacks handle it poorly. Exact replay of a non-deterministic trajectory is the single largest available saving in engineering time across the whole category.
