# Who Breaks If We Change This

**Niche:** [[niches/api-infrastructure-providers/breaking-change-and-deprecation/profile|Breaking Change & Deprecation]]
**Industry:** [[industries/api-infrastructure-providers|API Infrastructure Providers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every breaking change is a negotiation with counterparties the provider cannot enumerate, so nothing is ever removed — and the traffic flowing through the gateway identifies exactly who breaks and how.
**Tags:** #graph-theory #descriptive-statistics #k-means-clustering #evaluation-metrics #confidence-intervals #data-integration #automation #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to tell a provider exactly which consumers a proposed change would break, before it ships — and whoever does that takes the platform, because the inability to answer it is why nothing is ever retired.

## The Problem
A team wants to remove a field that has been deprecated for two years. The analytics show the endpoint gets four million calls a day. Nobody can say how many of those consumers read the field, which of them would fail if it disappeared, or who they are. The change is postponed. Three years later the field is still there, along with the two versions of the endpoint that were supposed to be retired alongside it, and a new engineer asks why the response contains a field whose name refers to a product line discontinued in 2019.

## Why Nobody Has Built This
Gateway analytics were built for operations — traffic, errors, latency — and the operational questions are all endpoint-level, so field-level analysis was never a requirement. Response bodies are frequently not inspected at all for performance and privacy reasons, which removes the strongest evidence unless it is deliberately sampled. Consumer identity is available through the credential and is rarely joined to an owning team or organisation, so even a complete usage picture cannot be converted into a list of people to contact. And the cost of never removing anything accumulates invisibly, while the risk of a breaking change is concrete and personal to whoever ships it.

## What to Build
Field-level consumer mapping as the product. Sample requests and responses to determine which fields each consumer actually sends and receives, which is where the evidence is and requires deliberate sampling rather than full inspection — a modest sample answers the question at very low cost. Infer which consumers would break, distinguishing those who use a field from those who merely receive it, since strict parsers break on removal and tolerant ones do not, and that distinction is often observable from behaviour across previous changes. Resolve consumers to owners by joining credentials to accounts, teams and contacts, which is usually possible and almost never done. Simulate the change: given this proposed modification, these consumers are affected, at these volumes, with these owners. Track migration as a measured curve rather than a deadline — what share of affected traffic has moved, by consumer — which converts an anxious guess into a decision. And quantify the cost of not changing: the versions carried, the fields maintained, the branches kept alive, which is the number that lets a provider argue for acting.

## Target Customer
API product managers and platform teams unable to retire anything, and the gateway and management vendors for whom this is the unexploited use of traffic they already terminate.

## Impact If Built
The inability to answer who breaks is the root cause of accumulated versions across the entire category, and the answer is in traffic every gateway already handles. Field-level sampling plus consumer-to-owner resolution converts an unanswerable question into a list, and migration curves convert an indefinite deadline into a decision.
