# Every Enterprise Reviews the Same Component

**Niche:** [[niches/open-source-commercial-vendors/enterprise-procurement-compliance/profile|Enterprise Procurement & Compliance]]
**Industry:** [[industries/open-source-commercial-vendors|Open Source Commercial Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A few hundred open-source components are reviewed independently by thousands of enterprises for the same licence, security and sustainability questions, and every review starts from nothing.
**Tags:** #bert #large-language-models #graph-theory #descriptive-statistics #evaluation-metrics #confidence-intervals #compliance #automation
**Contested on:** Every serious competitor here is fighting to get open-source software through an enterprise's legal, security and procurement review without a three-month project — and whoever does that takes the enterprise adoption, because the review is where it currently stops.

## The Problem
An engineering team wants to use a widely adopted open-source component. The review begins: legal reads the licence and assesses the obligations for this usage, security reviews the vulnerability history and the project's disclosure practices, architecture assesses whether the project is maintained and what happens if it is not, and procurement asks whether support is available. Eleven weeks later it is approved. The same component was reviewed by four hundred other enterprises in the same period, reaching substantially the same conclusions, and every one of those reviews started from a blank page.

## Why Nobody Has Built This
Legal review is treated as necessarily bespoke, because the obligations depend on the usage context — which is true for some licences and materially untrue for the permissive ones that constitute most of the estate. The sustainability question has no established methodology, so each reviewer invents one. Sharing review outcomes between enterprises raises a liability question nobody has resolved, which has prevented the obvious cooperative solution. And the vendors, who would benefit most from faster reviews, treat each one as a sales support exercise rather than as a repeated process to be industrialised.

## What to Build
Industrialise the repeated parts and localise the genuinely specific ones. Build a component dossier that assembles everything a review needs from public sources: licence and its obligations by usage pattern, full dependency tree with transitive licences, vulnerability history and disclosure practice, maintainer count and concentration, release cadence and responsiveness, governance structure, and support availability — which is a substantial but finite assembly per component and is currently done thousands of times. Assess sustainability explicitly, since project abandonment is the enterprise's real risk and is the question with no established method: maintainer concentration, contribution trend, funding, and whether a single person could stop the project are all measurable and are what the reviewer is actually trying to determine. Distinguish the generic conclusions from the context-specific ones clearly, so the enterprise's legal team reviews the small residue rather than the whole question. Let vendors supply their evidence into a structured format rather than into a bespoke document per deal, which accelerates their own sales. Keep it current, since a dossier is a snapshot and the sustainability picture changes. And make the shared portion genuinely shared, because the duplication is the entire waste.

## Target Customer
Enterprise legal, security and architecture review functions; open-source vendors whose enterprise deals stall in review; and the software composition analysis vendors whose products stop one layer short.

## Impact If Built
A few hundred components absorb the overwhelming majority of enterprise review effort and every review starts from nothing. The sustainability assessment is the question with no methodology and the highest real risk, and it is entirely measurable from public signals.
