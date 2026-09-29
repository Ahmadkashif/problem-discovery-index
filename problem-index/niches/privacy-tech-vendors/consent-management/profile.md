# Consent Management

**Parent Industry:** [[industries/privacy-tech-vendors|Privacy Tech Vendors]]
**Category:** High Market Share
**Contested on:** Whether the consent record reflects an informed choice, or an interface optimised until enough people clicked accept.

## Profile

**Market Size:** ~$1.68B
**Share of Parent Industry:** ~24%
**Digital Adoption:** High — banners at internet scale
**Target Buyer:** Privacy counsel, marketing operations, web teams
**Automation Potential:** High — and the automation is pointed at acceptance

## What Makes This a Distinct Niche

The banner is this category's most visible product and its least examined. Vendors supply a configurable consent interface; customers configure it; the platform records the outcome and produces an auditable consent record.

The configuration is where the contest lives. Banners are measured on acceptance rate and optimised toward it — through button prominence, colour, the number of clicks required to reject, the framing of the choice, and the bundling of purposes. Regulators across several jurisdictions have issued a consistent enough body of decisions on these patterns that the law on them is now reasonably settled, and the patterns persist because acceptance rate is what the customer's marketing function is measured on.

The vendors supply the configurability and the customer selects the configuration, which distributes responsibility neatly and leaves the underlying question unexamined: whether the person understood what they agreed to. Nobody measures comprehension. Nobody measures whether a person who accepted could describe what they accepted. The consent record satisfies an audit, and the thing the record is evidence of is not measured by anyone in the chain.

## Current Tools & Gaps

Consent management platforms delivering configurable banners at enormous scale, with purpose and vendor granularity, geographic rule variation, consent storage and proof, and integration with tag management and advertising frameworks. Acceptance rate analytics and A/B testing of banner variants. Compliance templates reflecting regulatory guidance by jurisdiction.

The gaps are conspicuous given the telemetry available. Comprehension is unmeasured, though the vendors hold interaction data that would support studying it — hesitation, scroll depth, time on the detail panel, whether anyone opened it. Optimisation tooling points at acceptance and could equally point at informed choice, and does not. Enforcement is weak: consent is recorded and the systems that should honour it frequently never learn, so a rejection is an entry in a database rather than a change in behaviour. Withdrawal is harder than granting almost everywhere. And nothing checks that the vendors listed in the banner match the vendors actually receiving data.

## Problems

- [[niches/privacy-tech-vendors/consent-management/build|🔨 Build: Measuring Whether They Understood]]
- [[niches/privacy-tech-vendors/consent-management/buy|🛒 Buy: Informed Consent Practice From Research Ethics]]
- [[niches/privacy-tech-vendors/consent-management/fix|🔧 Fix: Rejecting Is Recorded and Not Enforced]]
