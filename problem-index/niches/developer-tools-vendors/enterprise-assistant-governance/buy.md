# Supply Chain Provenance Applied to Generated Code

**Niche:** [[niches/developer-tools-vendors/enterprise-assistant-governance/profile|Enterprise Assistant Governance]]
**Industry:** [[industries/developer-tools-vendors|Developer Tools Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Software supply chain security built attestation, signed provenance and bill-of-materials standards for exactly the question of where code came from, and generated code sits entirely outside all of it.
**Tags:** #graph-theory #bert #word-embeddings #evaluation-metrics #confidence-intervals #compliance #data-integration #cross-validation
**Contested on:** Every serious competitor here is fighting to make an assistant approvable by a security and legal function — provenance, licence exposure, data boundaries and audit — and whoever does that takes the enterprise, because a blocked tool has no adoption to win.

## The Problem
An adjacent industry has spent several years building precisely the machinery this needs: signed build provenance, attestation frameworks, software bills of materials, and dependency origin tracking, driven by regulation and by high-profile incidents. Its entire premise is knowing where each component came from. Code produced by an assistant inside the organisation's own repository is invisible to every one of those mechanisms.

## What Already Exists
Provenance attestation frameworks and their specifications; software bill-of-materials formats with tooling; signing and verification infrastructure; dependency and licence scanning products; and code clone detection, which is a mature research area directly applicable to matching generated output against public corpora. The adjacent industry is documented as its own entry in this vault.

## The Customization Gap
The adaptation is to code fragments rather than to packaged components. It requires: (1) sub-file granularity, since a bill of materials describes dependencies and the unit here is a region within a file that was partly generated and subsequently edited, which existing formats have no representation for; (2) a decay model for human modification, because a region rewritten by a person is progressively less generated and asserting a binary is dishonest in both directions; (3) clone detection against public corpora tuned for short fragments, where the false positive rate on common idioms is the practical difficulty and must be handled by whitelisting genuinely idiomatic constructs; (4) licence inference from a match, since the match is only the first step and what matters is the obligation it would import, which requires the matched source's licence and its terms; and (5) evidence retained under the enterprise's control rather than the vendor's, because the audit is theirs to answer.

## Target Customer
Software supply chain security vendors, assistant vendors building enterprise tiers, licence compliance vendors, and enterprise security organisations.

## Impact If Solved
A regulation-driven provenance discipline exists next door and generated code is outside it entirely, which is the gap security functions are reacting to. Sub-file granularity and honest decay are the two adaptations, and short-fragment clone detection is the piece requiring the most care.
