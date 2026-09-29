# Framework Mapping & Crosswalks

**Parent Industry:** [[industries/grc-compliance-platforms|GRC & Compliance Platforms]]
**Category:** Low Digitized
**Contested on:** Whether an organisation pursuing several frameworks implements one control set once, or implements substantially the same things repeatedly and reconciles them by hand.

## Profile

**Market Size:** ~$1.08B
**Share of Parent Industry:** ~12%
**Digital Adoption:** Very low — crosswalk spreadsheets
**Target Buyer:** Compliance managers, framework specialists, platform product teams
**Automation Potential:** High — the mapping is a semantic problem over stable texts

## What Makes This a Distinct Niche

An organisation selling into several markets pursues SOC 2, ISO 27001, HIPAA, PCI, a sector framework and increasingly a regional one. The controls overlap substantially — access control, change management, logging, vendor management and incident response appear in all of them with different wording, different granularity and different evidence expectations.

The promised consolidation has not happened. In practice the organisation implements a control, produces evidence for one framework, and then does adjacent work to satisfy the next framework's version of the same requirement. Reconciliation is performed with crosswalk spreadsheets — maintained by hand, sourced from a vendor or a consultant, and stale the moment a framework revises.

This is a distinct market because the work is semantic rather than technical. It is not about collecting evidence, which is largely solved; it is about establishing that this requirement and that one are asking for the same thing, and that this evidence satisfies both. Every serious platform claims multi-framework support and delivers it as parallel checklists with a shared evidence pool, which is not the same as a unified control set — and the difference is most of the duplicated effort.

## Current Tools & Gaps

Crosswalk mappings published by standards bodies and consultancies, and maintained by platforms as internal mapping tables. Common control frameworks — the Secure Controls Framework, the Unified Compliance Framework, NIST's own mappings — which attempt a canonical control set with mappings outward. Platform multi-framework support with shared evidence.

The gaps are consistent across the category. Mappings are hand-built and go stale at revision, and framework revision cadences are unsynchronised. Mapping granularity is coarse — a requirement mapped to a requirement, when the real relationship is partial, conditional or one-to-many. Evidence sufficiency is not modelled, so the same artefact is accepted for one framework and rejected for another with no stated reason. The delta at framework revision — what actually changed and which of my controls are affected — is worked out by reading. And nothing tells an organisation what adding a fifth framework would genuinely cost given what it already has.

## Problems

- [[niches/grc-compliance-platforms/framework-mapping/build|🔨 Build: One Control Set, Many Frameworks]]
- [[niches/grc-compliance-platforms/framework-mapping/buy|🛒 Buy: Common Control Frameworks, Made Live]]
- [[niches/grc-compliance-platforms/framework-mapping/fix|🔧 Fix: The Crosswalk Is a Spreadsheet From 2022]]
