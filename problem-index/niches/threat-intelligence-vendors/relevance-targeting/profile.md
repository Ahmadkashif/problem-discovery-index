# Relevance & Customer Targeting

**Parent Industry:** [[industries/threat-intelligence-vendors|Threat Intelligence Vendors]]
**Category:** Low Digitized
**Contested on:** Whether relevance is assessed against what the customer actually runs and faces, or approximated by a sector label.

## Profile

**Market Size:** ~$600M
**Share of Parent Industry:** ~12%
**Digital Adoption:** Very low — sector tags and geography
**Target Buyer:** Vendor product leadership, customer intelligence functions
**Automation Potential:** High — the customer's exposure is largely observable

## What Makes This a Distinct Niche

Relevance is the filter that determines whether intelligence is useful or noise. An organisation's actual exposure depends on the software they run, the services they expose, their sector, their geography, their supply chain and the adversaries who target organisations like them.

The industry approximates all of that with a sector tag. Financial services. Healthcare. Manufacturing. These buckets contain organisations with nothing operationally in common, and they are applied to reporting and indicators alike as the primary relevance signal.

So the filtering falls to the customer, whose analysts must decide what applies to them — which requires knowing both their own estate and the threat landscape, and is precisely the expertise they bought a subscription to supplement.

The contest is over whether a vendor will do this work. The information needed is largely available: attack surface data is observable from outside, technology stacks are partly inferable, and which adversaries target which organisational profiles is what the vendor's own reporting is about. A vendor that assessed relevance properly would be delivering a fundamentally different product, and would also be delivering less of it.

## Current Tools & Gaps

Sector and geography tagging on indicators and reports. Adversary group profiles stating targeting patterns in prose. Some customer profile forms capturing declared technology. Subscription tiers by sector. ATT&CK mapping, which describes techniques rather than relevance.

The gaps are large. Customer environment is captured as a self-declared form if at all, so relevance is assessed against a description rather than against the estate. Attack surface data — what the organisation actually exposes — is observable and unused for targeting. Targeting patterns are prose in adversary profiles rather than structured attributes that could be matched. Supply chain exposure is not modelled, though it determines a substantial share of real risk. And nothing measures whether the relevance assessment was right, so the tagging never improves.

## Problems

- [[niches/threat-intelligence-vendors/relevance-targeting/build|🔨 Build: Relevance From the Customer's Real Exposure]]
- [[niches/threat-intelligence-vendors/relevance-targeting/buy|🛒 Buy: Attack Surface Data as a Targeting Input]]
- [[niches/threat-intelligence-vendors/relevance-targeting/fix|🔧 Fix: The Sector Tag Contains Everybody]]
