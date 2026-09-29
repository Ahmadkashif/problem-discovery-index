# Adaptive Authentication, Applied to Signing

**Niche:** [[niches/esignature-document-workflow/risk-based-identity-assurance/profile|Risk-Based Identity Assurance]]
**Industry:** [[industries/esignature-document-workflow|E-Signature & Document Workflow]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Banks have escalated authentication by transaction risk for twenty years with mature tooling and regulatory frameworks behind it, and signature platforms apply one setting to everything.
**Tags:** #gradient-boosting #logistic-regression #bayesian-inference #dbscan #evaluation-metrics #confidence-intervals #cross-validation #compliance
**Contested on:** Every serious competitor in signing assurance is fighting to set the verification level per transaction from its actual risk rather than per account from a default — and whoever does that gives customers both lower fraud and less friction, which are currently traded against each other.

## The Problem
Risk-based authentication is a solved and regulated discipline in financial services: score the transaction, step up when the score warrants it, keep the ninety-five percent of low-risk interactions frictionless. The tooling is commercial and mature, the fraud modelling literature is extensive, and the regulatory frameworks prescribe when escalation is required. Signature platforms, which mediate transactions of comparable and often greater consequence, use a single configured setting.

## What Already Exists
Adaptive and risk-based authentication products; device fingerprinting and behavioural signals; fraud scoring models with decades of applied literature; step-up authentication patterns standardised across payments and banking; and assurance level frameworks from standards bodies that define the rungs explicitly. Identity verification vendors supply the upper rungs already and integrate with the platforms.

## The Customization Gap
The adaptation is to a legal instrument rather than a payment. It requires: (1) a risk definition centred on repudiation rather than on immediate loss, since the harm here is a signature later disputed and the time horizon is years rather than seconds, which changes which features matter; (2) features drawn from the agreement itself — value, irreversibility, document type, whether it creates an ongoing obligation — which payments risk models have no analogue for and which are the strongest available signals; (3) an evidentiary output, because the purpose of assurance is to be defensible later, so the record of what was verified and why must be built for a court rather than for a fraud analyst; (4) a labelling strategy under near-total absence of confirmed fraud labels, which means starting with expert-defined risk tiers and a rules layer, and moving to learned models only as outcome data accumulates — stating that honestly rather than presenting a model with no labels behind it; and (5) accessibility as a hard constraint, since step-up verification methods fail disproportionately for some populations and a signing flow that cannot be completed denies access to an agreement rather than to a convenience.

## Target Customer
Signature platform vendors, identity verification vendors selling into them, and the fraud and risk functions at enterprises with high-value agreement volume.

## Impact If Solved
An entire discipline exists next door with mature tooling and a regulatory precedent, and the transfer has not been made. The repudiation framing and the evidentiary output are the two real adaptations; the label scarcity is the honest constraint and dictates a rules-first approach.
