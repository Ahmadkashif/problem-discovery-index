# Report Production

**Parent Industry:** [[industries/penetration-testing-firms|Penetration Testing Firms]]
**Category:** Highly Automatable
**Contested on:** Whether the document is assembled from structured findings captured during the engagement, or retyped into a different client's template every time.

## Profile

**Market Size:** ~$540M
**Share of Parent Industry:** ~9%
**Digital Adoption:** Low — a word processor and last month's report
**Target Buyer:** Firm operations, practice leadership, quality reviewers
**Automation Potential:** Very high — it is assembly, formatting and consistency work

## What Makes This a Distinct Niche

A quarter to a third of a tester's billable-equivalent effort goes into writing up findings they already understand, in a format that changes per client. That is the niche: not the analysis, not the judgement, but the production of the artefact.

The work is almost entirely mechanical. Describing a cross-site scripting flaw for the four-hundredth time. Rebuilding the executive summary after a late finding changes a severity. Reformatting into a client's required template, which differs from the last client's in ways that matter to nobody. Redacting credentials from screenshots by hand. Cross-checking that the severity in the summary matches the severity in the body. Producing the shorter version for the client's board.

It is a distinct market because the buyer is firm operations rather than a tester, and the value is measured in recovered days rather than in better findings. It sits alongside [[niches/penetration-testing-firms/compliance-driven-testing/profile|⚡ Compliance-Driven Testing]] as the mechanical pair in an industry that otherwise sells expert judgement, and it is the direct cause of the working pattern described in [[niches/penetration-testing-firms/the-tester/profile|🟣 The Tester]].

## Current Tools & Gaps

Word processors and a firm template, plus a folder of previous reports functioning as the real template library. A minority of firms run reporting platforms — Dradis, PlexTrac, AttackForge, Ghostwriter and the reporting modules inside delivery platforms — which structure findings and generate documents, with real adoption at larger firms and thin adoption below that. Peer review is a manual pass. Screenshot capture and redaction are manual.

The gaps: evidence is not bound to findings, so every request, response and screenshot is placed by hand and every number is retyped. The firm's accumulated language for recurring finding classes is not a library, so each is rewritten. Client-specific formats mean the same content is reassembled per engagement rather than rendered per template. Nothing checks internal consistency, which is where reports actually embarrass their authors. And redaction is manual, which is why credentials occasionally ship in a security firm's own deliverable.

## Problems

- [[niches/penetration-testing-firms/report-production/build|🔨 Build: Findings as Objects, Reports as Renders]]
- [[niches/penetration-testing-firms/report-production/buy|🛒 Buy: Reporting Platforms the Small Firms Never Adopted]]
- [[niches/penetration-testing-firms/report-production/fix|🔧 Fix: A Different Template for Every Client]]
