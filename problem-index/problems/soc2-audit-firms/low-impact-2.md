# Scope and the Client's Own System Description

**Industry:** [[soc2-audit-firms|SOC 2 & Attestation Audit Firms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** The boundary of what gets audited is drawn in a document the client writes, and everything that matters happens before any testing.
**Tags:** #bert #large-language-models #graph-neural-networks #gradient-boosting #confidence-intervals #evaluation-metrics #compliance #data-integration

## The Problem
An attestation covers a defined system, and the definition is the client's. The system description sets out the services in scope, the infrastructure, the supporting processes and the boundaries, and the auditor reviews it for accuracy and completeness.

Everything downstream depends on where that line was drawn. A system boundary that excludes a legacy platform, an acquired company's infrastructure, a development environment with production data, or a critical vendor dependency produces a report that is accurate about what it covers and silent about what it does not. The reader, who is assessing whether it is safe to buy from this company, generally does not notice the boundary at all.

Subservice organisations are the standard mechanism for this. A client's own vendors can be carved out of the report, with the reader expected to obtain and review each vendor's report and assess whether the relevant controls are covered — a chain of inference that almost no reader performs.

Reviewing the description for completeness is genuinely difficult. The auditor is being asked to identify what is missing from a document describing an environment they know only through what the client has shown them, in a limited engagement, on a fee that assumes the description is broadly right.

## What Already Exists
Attestation standards define system description requirements and the auditor's responsibility to assess them. Complementary user entity controls and subservice carve-outs are standard mechanisms with defined disclosure. Compliance platforms hold asset inventories that could inform scope assessment and are used mainly for evidence collection. Attack surface discovery tools exist in the security market and are not part of the audit toolkit.

## The Customisation Gap
Scope completeness should be tested against discovery rather than reviewed as a document. External attack surface discovery, cloud organisation structures, DNS records, code repositories and identity system data all describe what exists, and reconciling that against the described boundary would identify the excluded systems as a finding rather than as an absence. This is the audit equivalent of the coverage problem that recurs across every assurance product in this vault.

Materiality of exclusions needs assessing. Not every excluded system matters; one holding customer data, or with a network path to systems that do, matters a great deal. Reasoning over the access and data paths between excluded and included systems is what turns a boundary into a risk statement.

Carve-out chains should be traversable. Whether a subservice organisation's own report covers the controls the client relies on is checkable, and doing that traversal once — rather than expecting every reader to — would close a gap that the mechanism's design assumes will be closed and that in practice never is.

And the description itself is a document that can be analysed. Comparing it against the evidence encountered during testing, and against the discovered estate, surfaces the divergences that a manual read will miss.

## Impact If Solved
Scope is where an attestation's meaning is actually determined, and it is set by the audited party in a document the reader does not examine. Testing the boundary against discovered reality, assessing the materiality of exclusions through access and data paths, and traversing carve-out chains would make the report's coverage explicit — which is the information the reader needs and currently has no route to.
