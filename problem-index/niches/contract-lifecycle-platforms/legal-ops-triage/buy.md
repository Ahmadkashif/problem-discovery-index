# Triage Patterns From Support and Clinical Practice

**Niche:** [[niches/contract-lifecycle-platforms/legal-ops-triage/profile|Legal Operations Triage]]
**Industry:** [[industries/contract-lifecycle-platforms|Contract Lifecycle Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Customer support and emergency medicine both built rigorous triage disciplines with explicit categories, evidence-based criteria and audited accuracy, and legal intake sorts by whoever asked.
**Tags:** #gradient-boosting #logistic-regression #bert #k-nearest-neighbors #evaluation-metrics #confidence-intervals #cross-validation #workflow-orchestration
**Contested on:** Every serious competitor here is fighting to tell a routine agreement from a genuinely dangerous one at the moment it arrives — and whoever does that takes legal operations, because everything downstream depends on the first thirty seconds being right.

## The Problem
Triage as a discipline — sorting an arriving stream by urgency and complexity using explicit criteria, with defined categories and a measured rate of under- and over-triage — is mature in emergency medicine and in customer support, both of which audit their accuracy as a matter of routine. Legal intake sorts by requester seniority and declared contract type, and audits nothing.

## What Already Exists
Clinical triage frameworks with validated scales and published accuracy measurement; support ticket classification and priority prediction with commercial and open implementations; skills-based routing from contact centre practice; text classification models; and queueing theory for the capacity side. The methodological questions — how to define categories, how to measure under-triage, how to trade the two error types — are all settled elsewhere.

## The Customization Gap
The adaptation is to documents rather than to symptoms or tickets. It requires: (1) the document as the primary signal rather than the request text, since the risk is in the agreement and the request describes it inaccurately — which inverts the usual triage input and is the central change; (2) an asymmetric error model made explicit, because sending a dangerous agreement to a junior queue and sending an NDA to the general counsel are both errors with very different costs, and the threshold must reflect that rather than maximising accuracy; (3) categories defined by what should happen next rather than by contract type, since the point is routing and a taxonomy of agreement types does not determine who should handle one; (4) effort estimation alongside risk, which clinical triage has no analogue for and which legal operations needs for capacity; and (5) accuracy auditing against the reviewing lawyer's assessment, which is the practice medicine and support have and legal does not, and is the only way the system improves.

## Target Customer
CLM vendors with intake modules, legal operations platforms, legal service management vendors, and large in-house legal functions.

## Impact If Solved
Two mature triage disciplines have solved the methodological questions and neither has been applied here. Document-primary input and an explicit asymmetric error model are the adaptations, and routine accuracy auditing is the practice that is missing entirely.
