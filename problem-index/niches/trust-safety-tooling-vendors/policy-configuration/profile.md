# Policy Configuration & Deployment

**Parent Industry:** [[industries/trust-safety-tooling-vendors|Trust & Safety Tooling Vendors]]
**Category:** Highly Automatable
**Contested on:** Whether a written policy becomes a classifier configuration that faithfully implements it, or something approximate that nobody has checked.

## Profile

**Market Size:** ~$90M
**Share of Parent Industry:** ~3%
**Digital Adoption:** Moderate — rules into configuration
**Target Buyer:** Policy specialists, solutions engineers, platform policy teams
**Automation Potential:** Very high — it is translation and verification

## What Makes This a Distinct Niche

Between the platform's written policy and the classifier's behaviour sits a translation. A policy says what is not allowed, in prose, with definitions and exceptions. The classifier is configured with categories, thresholds and custom-trained rules. Somebody maps one to the other.

It is the smallest niche in the industry and it is where policy becomes operational reality. A policy carefully drafted by a specialist team is implemented by a solutions engineer selecting from available categories and setting numbers, and the gap between what the policy says and what the system does is nobody's responsibility to measure.

The contest is fidelity. A policy exception — satire is permitted, quotation is permitted, discussion of harm is permitted — is a condition the classifier may or may not honour. A policy distinction between two categories may map to one classifier category. And a policy change, drafted and approved, reaches the system through a configuration update that may or may not implement it as intended.

Nobody tests whether the configuration implements the policy. It is the most testable thing in the industry and it is not tested.

## Current Tools & Gaps

Category selection and threshold configuration in vendor products. Custom category training for policy-specific rules. Solutions engineers translating customer policy into configuration. Policy documentation maintained separately. Change deployment through the vendor's configuration interface.

The gaps are that the translation is unverified. Nothing tests whether the configuration implements the written policy — a test set of policy-relevant examples, run against the configuration, comparing the system's decisions to the policy's, is entirely achievable and is done nowhere. Policy exceptions are frequently not representable in the configuration and the gap is not recorded. Policy changes are deployed without regression testing. Version alignment between policy and configuration is not tracked. And the solutions engineer making the translation is not a policy specialist and the policy specialist does not see the configuration.

## Problems

- [[niches/trust-safety-tooling-vendors/policy-configuration/build|🔨 Build: Test the Translation]]
- [[niches/trust-safety-tooling-vendors/policy-configuration/buy|🛒 Buy: Policy as Code From Infrastructure]]
- [[niches/trust-safety-tooling-vendors/policy-configuration/fix|🔧 Fix: The Policy Changed and the Configuration Did Not]]
