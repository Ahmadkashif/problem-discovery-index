# Vendor Risk Management, Applied to Runtime Dependencies

**Niche:** [[niches/api-infrastructure-providers/the-api-consumer/profile|The API Consumer]]
**Industry:** [[industries/api-infrastructure-providers|API Infrastructure Providers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Third-party risk management assesses vendors annually with a questionnaire, and the runtime dependency that can take a product down in the next ten minutes is not on the register.
**Tags:** #change-point-detection #descriptive-statistics #graph-theory #time-series-forecasting #evaluation-metrics #confidence-intervals #compliance #data-integration
**Contested on:** Every serious competitor that takes this seriously is fighting to give the developer integrating against somebody else's API the visibility and control they have over their own systems — and whoever does that takes the integration layer, because the consumer currently operates blind against a dependency they cannot change.

## The Problem
Third-party risk management is an established discipline with a product category: maintain a vendor register, assess criticality, collect attestations, review annually. It is oriented to suppliers of services procured through a contract process. The six APIs a product calls on every request — chosen by an engineer in an afternoon, sometimes on a free tier — are frequently not on that register at all, and are the dependencies most able to take the product down today.

## What Already Exists
Third-party risk platforms with vendor registers and criticality scoring; business continuity methodology; dependency mapping from the software supply chain category; monitoring and anomaly detection for the runtime half; and contract term extraction, which is documented in the contract lifecycle industry in this vault.

## The Customization Gap
The adaptation is from procured suppliers to runtime dependencies. It requires: (1) discovery from traffic rather than from procurement, since the register built from purchase orders misses the free-tier service a developer integrated last month, and outbound traffic analysis finds them all; (2) criticality derived from observed blast radius — what fails when this provider does, measured from the call graph and from past incidents — rather than from a questionnaire answer; (3) continuous rather than annual assessment, because the relevant facts change weekly and an annual review describes a vendor that no longer behaves the same way; (4) observed reliability as the primary evidence, since a provider's attested uptime and their delivered uptime against this consumer's traffic are different numbers and only the second matters; and (5) contractual terms joined to observed behaviour, so a service level breach produces a credit claim rather than a shrug, which is where the commercial value sits and requires the two halves to meet.

## Target Customer
Engineering and risk functions at companies with material API dependencies, third-party risk vendors with an unserved runtime dimension, and observability vendors.

## Impact If Solved
An established risk discipline covers procured suppliers and misses the dependencies most able to cause an outage today. Traffic-based discovery and observed-reliability evidence are the two adaptations, and joining to contractual terms is what converts monitoring into recovery.
