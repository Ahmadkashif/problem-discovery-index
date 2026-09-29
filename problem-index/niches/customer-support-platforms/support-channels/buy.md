# Identity Resolution for the Contacting Customer

**Niche:** [[niches/customer-support-platforms/support-channels/profile|Support Channels]]
**Industry:** [[industries/customer-support-platforms|Customer Support Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Resolving a person across phone numbers, email addresses, device identifiers and account logins is a mature commodity in marketing and fraud, and support treats each channel's identifier as a separate customer.
**Tags:** #graph-theory #k-nearest-neighbors #bert #evaluation-metrics #confidence-intervals #data-integration #compliance #automation
**Contested on:** *Not terminal as stated* — see the sub-niches for the two distinct forms this contest takes.

## The Problem
A customer contacts support from a work email, a personal email, a phone number registered to their partner and an in-app session on an account in a company name. Support sees four customers. The agent handling the fourth contact has no visibility of the previous three, the history that would explain the issue is fragmented, and any analysis of repeat contact rates is understated because the repeats look like new people.

## What Already Exists
Identity resolution across channels and identifiers is a mature discipline with commercial products and open tooling, deployed at scale in marketing, fraud prevention and customer data platforms. Deterministic and probabilistic matching, household and account grouping, and identity graph maintenance are standard. Telephony platforms expose caller identifiers; digital channels expose session and account identifiers. Every component is available and frequently already licensed elsewhere in the same company.

## The Customization Gap
The adaptation is to a support context where a wrong match discloses one person's information to another. It requires: (1) an asymmetric confidence threshold — a match that merges two customers' histories is far more damaging than a missed match, so the bar for automatic linkage must be high and the failure mode must be separate records rather than a merge; (2) account and organisation structure modelled, since in business support several individuals legitimately contact about one account and the useful grouping is the account with the individuals distinguished, not a single merged person; (3) verification integrated with authentication, because a support contact frequently requires identity verification anyway and that step is the natural, consented point to confirm a link; (4) a privacy boundary on what the resolution produces — the purpose is conversation continuity, not a behavioural profile, and the product should be architected to that scope; and (5) correction available to the agent and to the customer, since a wrong link should be reversible by the person who notices it.

## Target Customer
Support platform vendors, contact centre operators, and the customer data platform vendors for whom support is an adjacent and unserved use of capability they already sell.

## Impact If Solved
Identity resolution is the prerequisite for conversation continuity, for honest repeat-contact measurement and for any analysis of how customers actually move between channels. The asymmetric threshold is the specific adaptation that matters, since the cost of a false merge in support is a privacy incident rather than a marketing inefficiency.
