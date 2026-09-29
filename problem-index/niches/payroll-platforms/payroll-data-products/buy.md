# Privacy-Preserving Statistics Infrastructure

**Niche:** [[niches/payroll-platforms/payroll-data-products/profile|Payroll Data Products]]
**Industry:** [[industries/payroll-platforms|Payroll Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Statistical disclosure control, differential privacy and secure computation are mature, deployed at national statistical agencies and in large technology companies, and the payroll industry's reason for not publishing is a privacy concern these methods exist to resolve.
**Tags:** #descriptive-statistics #confidence-intervals #hypothesis-testing #evaluation-metrics #monte-carlo-methods #compliance #data-integration #probability-distributions
**Contested on:** Every serious competitor sitting on payroll data is fighting to turn the highest-frequency wage panel in the country into a product people pay for, without compromising employer or worker confidentiality — and whoever publishes credibly takes a market nobody currently serves.

## The Problem
The stated obstacle to publishing payroll-derived statistics is that doing so might reveal something about an individual employer or worker. That is a legitimate concern and it is also the exact problem that national statistical agencies have solved for decades while publishing detailed economic data from confidential business and household records. The methods are public, the practice is established, and the payroll industry has not adopted them — which means the concern is operating as a reason rather than as a constraint to be engineered around.

## What Already Exists
Statistical disclosure control — cell suppression, thresholds, dominance rules, noise addition — is standard practice at statistical agencies with substantial published methodology. Differential privacy is deployed at national statistical scale and in large technology companies, with mature open implementations. Secure multi-party computation and clean room infrastructure are commercially available. Synthetic data generation for research access is an active and usable field. Every method required is documented, implemented and in production somewhere.

## The Customization Gap
The adaptation is to a panel whose units are employers rather than households. It requires: (1) employer dominance rules, since a cell containing one large employer is disclosive even at a headcount threshold, and the dominance criteria used in business statistics are the right precedent; (2) longitudinal disclosure control, because a series published repeatedly permits differencing attacks that a single release does not — this is the specific technical risk and it has established answers; (3) a privacy budget managed across the whole publication programme rather than per release, which is what differential privacy requires and what an ad hoc approach cannot provide; (4) a research access tier separate from the public series, using synthetic data or a secure enclave, since the methodological credibility of the whole exercise depends on external researchers being able to examine it; and (5) client consent and contractual basis established explicitly, since publishing derived statistics from customer payroll data requires a defensible position that most existing agreements do not clearly provide and that should be sought openly rather than assumed.

## Target Customer
Payroll providers, and the statistical agencies and academic institutions who would be both users and credibility partners.

## Impact If Solved
The privacy methods are the stated blocker and they are entirely available, which means the blocker is soluble with bought infrastructure and a decision. The research access tier is the element that converts a commercial data product into a credible statistical one, and it is also the cheapest way to establish that the disclosure control is adequate — by letting people check.
