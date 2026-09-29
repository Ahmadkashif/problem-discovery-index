# Feed Quality Measurement

**Parent Industry:** [[industries/threat-intelligence-vendors|Threat Intelligence Vendors]]
**Category:** High Market Share
**Contested on:** Whether a feed's value can be stated as a number, or remains a matter of collection breadth and analyst reputation.

## Profile

**Market Size:** ~$1.00B
**Share of Parent Industry:** ~20%
**Digital Adoption:** Very low — no vendor publishes quality metrics
**Target Buyer:** Vendor leadership, security operations buyers, procurement
**Automation Potential:** High for match rate, moderate for precision

## What Makes This a Distinct Niche

Threat intelligence is bought on the belief that it prevents incidents and sold on collection breadth, analyst credentials and the plausibility of the reporting. Nobody publishes a quality measure, because the outcome the product claims — an attack that did not happen — is unobservable.

But two proxies are observable and neither is published. The first is whether an indicator ever matched anything in any customer's telemetry. A feed of several million indicators, of which some large fraction has never matched anything at any organisation, is measurably different from one where most indicators fire. The second is whether a match corresponded to genuinely malicious activity, which is precision.

Vendors bundled with endpoint telemetry could compute both across a large installed base. The resulting statement — this feed's indicators match at this rate with this precision for organisations of this shape — is the closest thing to a product measurement the field can have, and no vendor makes it.

The contest is over whether any vendor will move first. The market currently rewards volume because volume is the only comparable attribute, which is precisely the equilibrium a quality measure would break.

### Contested sub-niches

- [[niches/threat-intelligence-vendors/match-rate-measurement/profile|🎯 Match Rate Measurement]]
- [[niches/threat-intelligence-vendors/precision-verification/profile|🎯 Precision Verification]]

## Current Tools & Gaps

Threat intelligence platforms ingesting multiple feeds with deduplication, scoring and routing. Some customer-side analytics on which feeds produced alerts. Vendor-published collection statistics — sources, volumes, coverage claims. Community feed comparison efforts and academic studies, which have found substantial disagreement between feeds and low overlap.

The gaps are what the category does not report. No vendor publishes a match rate or a precision figure for its own feed. Customers rarely measure it themselves, though they hold the telemetry to do so. Feed overlap and uniqueness are not disclosed, so a customer buying four feeds cannot tell how much they are paying for duplication. Confidence and age are inconsistently expressed. And nothing relates a feed's characteristics to outcomes, so procurement decisions are made on collection narrative and price.

## Problems

- [[niches/threat-intelligence-vendors/feed-quality/build|🔨 Build: The Feed Scorecard]]
- [[niches/threat-intelligence-vendors/feed-quality/buy|🛒 Buy: Diagnostic Test Evaluation, Applied to Feeds]]
- [[niches/threat-intelligence-vendors/feed-quality/fix|🔧 Fix: Sold on Volume Because Volume Is Comparable]]
