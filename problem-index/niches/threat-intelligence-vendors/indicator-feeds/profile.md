# Indicator Feeds

**Parent Industry:** [[industries/threat-intelligence-vendors|Threat Intelligence Vendors]]
**Category:** High Market Share
**Contested on:** Whether a feed delivers what a particular customer should act on, or everything the vendor collected with the filtering left to the buyer.

## Profile

**Market Size:** ~$1.30B
**Share of Parent Industry:** ~26%
**Digital Adoption:** High — delivery and integration are solved
**Target Buyer:** Security operations leadership, detection engineering
**Automation Potential:** High — selection and prioritisation are modelling problems

## What Makes This a Distinct Niche

The indicator feed is the volume product of this industry: addresses, domains, hashes, certificates and infrastructure attributes associated with malicious activity, delivered continuously into the customer's detection stack.

Delivery is genuinely solved. Feeds arrive in standard formats, integrate with every major platform, deduplicate reasonably and scale. The commercial competition is over collection — who has underground access, whose incident response practice produces the best telemetry, who tracks which adversary groups.

The contest that matters is what gets shipped. A feed of several million indicators represents a collection achievement and a delivery decision: send everything and let the customer filter. That decision pushes the hardest analytical work — determining what this particular organisation should care about — onto a security team that is already the constraint, and it is made because volume is what procurement compares.

A vendor that shipped less, selected better, and could demonstrate the selection was right would be competing on a different axis entirely. Nobody does, because the demonstration requires the quality measurement the category does not have.

## Current Tools & Gaps

Feed delivery in STIX, TAXII and simpler formats. Integrations with SIEM, endpoint and network platforms. Deduplication and normalisation. Confidence scoring based on collection method. Sector and geography tagging. Some tiering into high-confidence and broader sets.

The gaps are in selection and expression. Confidence reflects how an indicator was collected rather than how it has performed, so it is an input property presented as an output property. Tagging is coarse, so a customer receives a sector bucket rather than an assessment of relevance to their stack. Nothing expresses what an indicator is for — blocking, alerting, hunting or context — though those imply completely different precision requirements. Retirement is weak, so feeds accumulate. And nothing tells a customer which indicators in the feed are unique to it, so a buyer with four subscriptions cannot see the overlap.

## Problems

- [[niches/threat-intelligence-vendors/indicator-feeds/build|🔨 Build: Shipping Less, Selected Better]]
- [[niches/threat-intelligence-vendors/indicator-feeds/buy|🛒 Buy: Recommendation Practice for Indicator Selection]]
- [[niches/threat-intelligence-vendors/indicator-feeds/fix|🔧 Fix: Confidence Describes the Collection, Not the Indicator]]
