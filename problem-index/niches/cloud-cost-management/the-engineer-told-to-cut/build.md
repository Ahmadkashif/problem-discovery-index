# Cut Something, We Cannot Tell You What

**Niche:** [[niches/cloud-cost-management/the-engineer-told-to-cut/profile|The Engineer Told to Cut]]
**Industry:** [[industries/cloud-cost-management|Cloud Cost Management]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Engineers receive periodic instructions to reduce spend with no information about what is safe to cut, and are blamed for a bill they had no way to see.
**Tags:** #gradient-boosting #graph-theory #descriptive-statistics #confidence-intervals #evaluation-metrics #worker-facing #revenue-impact #automation
**Contested on:** Every serious competitor that takes this seriously is fighting to show an engineer the cost of their own decisions at the moment they make them — and whoever does that takes the engineering organisation, because the alternative is a periodic instruction to cut something with no way to know what is safe.

## The Problem
An engineer receives a message: the team's cloud spend is up and needs to come down fifteen percent this quarter. They open the cost portal and see a list of resource types. They do not know which of their services is expensive, which of the expensive things are load-bearing, what the retention policy on that storage bucket is for, or whether the environment that costs the most is still used by anybody. They make a guess, delete something, and either save a little or cause an incident. Meanwhile the change they made last month that doubled a data transfer cost is still there and nobody has connected it to anything.

## Why Nobody Has Built This
Cost tooling was built for a finance workflow, so it reports monthly to a portal, and an engineer's decisions happen daily in a pull request. Estimating the cost of a proposed change requires parsing the infrastructure definition and pricing it, which is entirely feasible and has not been productised into the review flow by the cost vendors. Knowing what is safe to remove requires dependency and usage information that lives in observability and deployment systems. And the engineer is not the buyer, so their experience has never determined a roadmap.

## What to Build
Put cost where the decisions are. Estimate the cost of a proposed change in the pull request, from the infrastructure definition and the expected usage — this instance type, this retention setting, this cross-region transfer will cost approximately this much per month — which is the single highest-leverage delivery change available and requires no new data. Attribute cost increases to the specific merge that caused them, so the feedback loop closes and an engineer learns from their own changes rather than from a quarterly aggregate. Give a continuous per-service view in the engineer's own units and in their own tools, so cost is a property of the system they own rather than an external demand. Answer the safety question explicitly: for each expensive resource, what depends on it, when was it last accessed, what is its retention obligation, and what would break — which is the question they actually have and is answerable from dependency and access data. Rank by saving available rather than by cost, since the largest resource is frequently the least reducible. And frame the ask as an efficiency target for a system they own rather than as a cut imposed from outside, which is both more accurate and the only framing that produces sustained behaviour.

## Target Customer
Platform engineering teams, cost management vendors whose engineering-facing half has no audience, and the developer platform vendors into whose surfaces this belongs.

## Impact If Built
Engineers make every decision that determines spend and are the only participants with no cost information when they make it. Estimating cost in the pull request and attributing increases to merges together close a feedback loop that currently does not exist at all.
