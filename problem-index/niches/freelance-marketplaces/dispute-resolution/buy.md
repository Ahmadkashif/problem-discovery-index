# Buy: Online Dispute Resolution Adapted to Work That Was Delivered or Was Not

**Niche:** [[niches/freelance-marketplaces/dispute-resolution/profile|Dispute Resolution]]
**Industry:** [[industries/freelance-marketplaces|Freelance Marketplaces]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Online dispute resolution products are built around a transaction that either arrived or did not; services disputes turn on scope, which was never written down precisely enough to check.
**Tags:** #large-language-models #evaluation-metrics #workflow-orchestration #descriptive-statistics #confidence-intervals #compliance #automation #worker-facing
**Contested on:** Whether goods-oriented dispute tooling can adjudicate a claim whose subject was defined in a paragraph of prose.

## The Problem

Online dispute resolution is a real category. Payment networks, e-commerce marketplaces and ODR vendors have well-developed products: intake, evidence submission windows, structured claim types, decision workflows, appeals, and integration with chargeback and refund machinery.

All of it is built around a goods transaction. The claim types are did-not-arrive, not-as-described, unauthorised, damaged — each with a decision procedure resting on an objective, checkable fact like a tracking number. A services dispute on a freelance marketplace has no equivalent fact. The question is whether what was delivered matches what was agreed, and what was agreed exists as a paragraph the client wrote before the work started and both parties have since reinterpreted.

## What Already Exists

Chargeback management platforms, ODR vendors serving e-commerce and small claims, arbitration providers with online filing, and the case management layer inside every major support suite. Evidence collection, deadline management, structured workflow and audit trails are all mature and worth keeping.

## The Customization Gap

**Scope is the contested object and it is unstructured.** Goods disputes anchor on an order record. Services disputes anchor on a prose description, plus six weeks of messages in which the scope moved without anyone marking that it had. No ODR product has a representation for a scope that drifted, and building one — deliverables, changes, acknowledgements, with a timeline — is the substantive work.

**Partial outcomes are the norm.** ODR workflows are built to refund, deny or split at fixed proportions, because a delivered good is binary. Here the common true answer is that 70% of the work was done to standard and the rest was not, and the decision space is continuous. Milestone structure gives a natural discretisation the tooling does not use.

**The counterparties continue to exist.** A chargeback ends a relationship with an anonymous merchant. Here both parties remain on the platform, keep ratings, and one of them is the platform's supply. A dispute outcome has reputational consequences — whether the dispute is visible on a profile, whether it affects a score, whether a pattern of disputes by one client is surfaced — that no ODR product models.

**The escrow is the platform's own.** Payment-network ODR operates on someone else's funds under network rules. Here the platform holds the money, wrote the terms, and decides — so it is adjudicating a contract to which it is a party. The independence and audit requirements that follow have no analogue in bought tooling, and the consistency measurement that would demonstrate fairness is not a feature any vendor ships.

**Amounts are too small for any escalation path that exists.** External arbitration costs more than the dispute is worth, which means the platform's internal decision is final in practice however the terms are worded. That makes internal quality assurance the entire due process, and bought ODR products assume an escalation ladder that in this market is decorative.

## Target Customer

Marketplace operations teams evaluating ODR vendors after dispute volume outgrew the support queue, and discovering in the pilot that the claim taxonomy does not fit. Also platforms whose escrow terms are being examined by a regulator or a class action, where the audit trail and consistency record become the deliverable.

## Impact If Solved

The bought layer handles intake, deadlines, evidence windows and audit, and the adaptations make it about services. The practical difference is a dispute record organised around scope-versus-delivery with a continuous outcome space, rather than a goods claim type that nobody's dispute actually is.
