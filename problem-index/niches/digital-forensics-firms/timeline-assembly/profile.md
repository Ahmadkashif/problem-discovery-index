# Evidence Collection & Timeline Assembly

**Parent Industry:** [[industries/digital-forensics-firms|Digital Forensics Firms]]
**Category:** Low Digitized
**Contested on:** Whether a defensible sequence of events emerges from tooling, or from one examiner reconciling a dozen formats and three disagreeing clocks by hand.

## Profile

**Market Size:** ~$750M
**Share of Parent Industry:** ~15%
**Digital Adoption:** Low — parsers exist, assembly is manual
**Target Buyer:** Forensic examiners, response leads, firm tooling teams
**Automation Potential:** Very high — normalisation and correlation are mechanical

## What Makes This a Distinct Niche

Underneath every conclusion is a timeline. What happened, in what order, on which systems. Building it means collecting evidence from endpoints, servers, cloud platforms, identity providers, network devices and applications, parsing a dozen formats, reconciling timestamps that disagree, and assembling millions of events into a sequence a human can reason about.

The collection and parsing are largely tooled. The assembly is not. An examiner works through parsed output, correlating activity across sources by hand, building the sequence in a spreadsheet or a timeline tool, resolving clock discrepancies by inference, and carrying the emerging picture in their head.

The contest is over that middle step. Every firm has parsers and every firm assembles by hand, which means the scarce resource — experienced examiner attention — is spent on correlation rather than on interpretation. And because the assembly is manual, it is slow, it is difficult to review, and it is hard to reproduce if challenged in litigation two years later.

## Current Tools & Gaps

Forensic suites with parsers for common artefact types. Timeline tools that merge parsed output into a chronological view. Log analysis platforms for volume. Scripts and internal tooling, extensive and firm-specific. Artefact reference knowledge, substantially held by practitioners.

The gaps are in correlation and provenance. Timestamp reconciliation across sources with different clocks, timezones and precision is done by inference and is a known source of error. Nothing correlates related activity across sources automatically — the login, the process execution and the network connection that are one event appear as three unconnected rows. Evidence volume overwhelms review, so examiners filter by intuition and may filter out the thing that mattered. Artefact interpretation knowledge is tacit and varies by examiner. And the assembly leaves no reproducible record, so the reasoning cannot be replayed.

## Problems

- [[niches/digital-forensics-firms/timeline-assembly/build|🔨 Build: Correlation Before Interpretation]]
- [[niches/digital-forensics-firms/timeline-assembly/buy|🛒 Buy: Observability Correlation for Forensic Sources]]
- [[niches/digital-forensics-firms/timeline-assembly/fix|🔧 Fix: Three Clocks That Disagree]]
