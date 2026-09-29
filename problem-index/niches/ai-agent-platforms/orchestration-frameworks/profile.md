# Orchestration Frameworks

**Parent Industry:** [[industries/ai-agent-platforms|AI Agent Platforms]]
**Category:** Contested Sub-Niche
**Contested on:** Every serious competitor in this sub-niche is fighting to let an engineer understand and control what their agent actually did — and whoever does that takes the adoption, because the buyer is building the agent themselves and debuggability is what they run out of.

## Profile
**Market Size:** ~$310M US, much of the value captured indirectly
**Share of Parent Industry:** ~12% of category revenue
**Digital Adoption:** High
**Target Buyer:** Engineering teams building their own agents
**Automation Potential:** High

## What Makes This a Distinct Niche
A framework is bought — or adopted for free and monetised elsewhere — by engineers who will build the agent themselves. Their requirements are a programmer's requirements: control flow they can reason about, explicit state, testability, the ability to replay a run, versioning, and a path from a prototype to something they can operate. The competitive alternatives are another framework and writing it themselves, and the second is a genuine option that many teams take after a framework's abstraction gets in the way. The contest is therefore whether an engineer can understand what happened in a failed run and change the agent's behaviour deliberately — which is where most adoption is won and lost.

## Current Tools & Gaps
Graph-based control flow with explicit state, tool calling abstractions, streaming, tracing integrations, and prebuilt patterns. The gaps: no deterministic replay of a past run, which is what debugging actually requires; no unit-testing story for a component whose behaviour is stochastic; versioning of an agent definition is ad hoc; state persistence and resumption are usually left to the application; and abstractions frequently obscure the model call an engineer needs to see.

## Problems
- [[niches/ai-agent-platforms/orchestration-frameworks/build|🔨 Build: Debugging a Run You Cannot Reproduce]]
- [[niches/ai-agent-platforms/orchestration-frameworks/buy|🛒 Buy: Testing and Debugging Practice for Nondeterministic Systems]]
- [[niches/ai-agent-platforms/orchestration-frameworks/fix|🔧 Fix: The Abstraction That Hides the Prompt]]
