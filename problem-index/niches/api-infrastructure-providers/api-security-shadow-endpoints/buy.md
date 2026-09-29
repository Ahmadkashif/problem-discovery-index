# Attack Surface Management, One Layer Deeper

**Niche:** [[niches/api-infrastructure-providers/api-security-shadow-endpoints/profile|API Security & Shadow Endpoints]]
**Industry:** [[industries/api-infrastructure-providers|API Infrastructure Providers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** External attack surface management discovers an organisation's internet-facing assets and stops at the host, and the exposure lives in the endpoints behind it.
**Tags:** #graph-theory #k-means-clustering #bert #logistic-regression #evaluation-metrics #confidence-intervals #compliance #cross-validation
**Contested on:** Every serious competitor here is fighting to produce a complete inventory of an organisation's exposed endpoints and what each one does with sensitive data — and whoever does that takes the security account, because nobody can currently produce the list.

## The Problem
Attack surface management is an established category: enumerate the organisation's internet-facing assets from certificate transparency, DNS, cloud accounts and scanning, and report what is exposed. It resolves to hosts and services. The question security actually needs answered is which endpoints those hosts expose, what each one does, and which of them handle sensitive data — one layer deeper, where the incidents are.

## What Already Exists
Attack surface management platforms with asset discovery; certificate transparency and passive DNS data; cloud resource inventory APIs; network flow logs; specification parsers; and data classification tooling from the privacy category. Traffic analysis from the gateway and mesh. Every ingredient exists in some product.

## The Customization Gap
The adaptation is from hosts to endpoints and their semantics. It requires: (1) endpoint enumeration without relying on documentation, which means combining observed traffic with route definitions extracted from code and configuration, since neither alone is complete; (2) grouping endpoints into logical APIs, because a list of eleven thousand paths is not an inventory and the useful unit is the service and its versioned interface; (3) data classification from observed structure rather than from field names alone, since names lie and value shapes do not, and this is what turns an endpoint list into a compliance answer; (4) authorisation behaviour observation — which endpoints require which credentials and what happens when a credential from one tenant is used on another's resource — which is the vulnerability class that dominates reported API breaches and is testable rather than inferable; and (5) change detection as the primary output, since the inventory will be wrong the week after it is produced and the alert on a newly exposed endpoint is the operationally valuable artefact.

## Target Customer
API security vendors, attack surface management vendors, cloud security posture vendors, and enterprise security functions.

## Impact If Solved
The adjacent category resolves to hosts and the exposure is in the endpoints, which is a one-layer gap with a large consequence. Structure-derived data classification and observed authorisation behaviour are the two adaptations that make the inventory actionable rather than merely complete.
