# Scope & System Description

**Parent Industry:** [[industries/soc2-audit-firms|SOC 2 & Attestation Audit Firms]]
**Category:** Low Digitized
**Contested on:** Whether the boundary of the audit is derived from where the data actually goes, or drawn in a document the audited party writes.

## Profile

**Market Size:** ~$450M
**Share of Parent Industry:** ~15%
**Digital Adoption:** Very low — a client document, reviewed
**Target Buyer:** Audit partners, client leadership, relying parties
**Automation Potential:** High — the actual boundary is observable

## What Makes This a Distinct Niche

The system description is the client's document. It states what the system is, where its boundaries lie, which subsystems and subservice organisations are in scope, and which controls are being asserted. The auditor reviews it and tests against it.

Everything consequential is decided there, before any testing happens. A boundary drawn to exclude an awkward subsidiary, a legacy platform, a recently acquired entity or a third-party processor removes those from the audit entirely — and the resulting report is clean, accurate and about a smaller system than the reader assumes.

The reader has no reliable way to detect it. The scope is stated in the description, which is prose in a long document, and the parts that matter — what was excluded and why — are the parts least likely to be stated plainly.

Every serious competitor is fighting the same thing: how hard to push on a scope the client has drawn, for a client who selected them and is paying, in a market where the report looks identical either way.

## Current Tools & Gaps

The system description prepared by the client, reviewed and challenged by the auditor. Scope discussions at engagement planning. Subservice organisation treatment, carved out or inclusive, disclosed in the report. Complementary user entity controls listed for the reader.

The gaps are that the boundary is asserted rather than derived. Nothing checks the described system against the organisation's actual estate — the cloud accounts, the data flows, the third-party integrations that would show what is really in the path. Exclusions are not stated prominently, so a reader must infer them from what the description does not mention. Carve-outs are disclosed in a form most readers do not fully register. Nothing tracks whether the scope changed between periods. And the auditor's challenges to the description are not recorded anywhere the reader can see.

## Problems

- [[niches/soc2-audit-firms/scope-and-description/build|🔨 Build: The Boundary, Derived]]
- [[niches/soc2-audit-firms/scope-and-description/buy|🛒 Buy: Data Flow Observation From Privacy Engineering]]
- [[niches/soc2-audit-firms/scope-and-description/fix|🔧 Fix: The Reader Cannot See What Was Left Out]]
