# A Clean Report That Means Nothing

**Niche:** [[niches/ai-red-teaming-firms/coverage-measurement/profile|Coverage Measurement]]
**Industry:** [[industries/ai-red-teaming-firms|AI Red Teaming Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A clean report tells a client nothing unless somebody can say what fraction of the risk surface was examined, and no method exists for stating that about a system with an unbounded input space.
**Tags:** #evaluation-metrics #confidence-intervals #hypothesis-testing #monte-carlo-methods #compliance #descriptive-statistics #probability-distributions #graph-theory
**Contested on:** Every serious competitor in this niche is fighting to say what fraction of a system's risk surface an assessment examined — and whoever does that takes the market, because without it a clean report is an assertion and with it it is evidence.

## The Problem
A board receives an assessment reporting no critical findings on a customer-facing assistant. The board's question is whether the system is safe to deploy. The report's answer is that a team of skilled people spent four weeks and did not find anything critical. Whether that means the system is robust or that four weeks was not enough, or that the team's expertise did not cover the harm category that will matter, is unknowable from the document and unknowable to the firm that wrote it. The board approves the deployment. The same document satisfies a regulator, which is the demand driving the market, and nobody in the chain can say what it establishes.

## Why Nobody Has Built This
The input space genuinely is unbounded, so a literal coverage fraction is not available, and the field has treated that as the end of the discussion rather than as a reason to define a tractable proxy. Reporting coverage means reporting what was not covered, which weakens the reassurance clients are buying. No standard exists, so a firm that reports coverage looks worse than one that does not. And the regulatory demand is satisfied by documented testing rather than by measured testing, which removes the pressure.

## What to Build
Define coverage against stated dimensions rather than against the input space. Report coverage over an explicit harm taxonomy — which categories were examined, which were not, and why — which is immediately constructible, is what a reader actually needs, and is the foundation of everything else here. Report technique coverage against a published catalogue of attack classes, so a reader can see which approaches were attempted. Report effort per cell of that grid, since effort is the third dimension and a category examined for an hour and one examined for a week are not equivalent. Show the elicitation curve — findings against effort applied — because a curve still rising at the end of an engagement means something completely different from one that plateaued, and this single artefact changes how a clean result should be read. Report the residual: the categories and techniques not examined, stated plainly, which is the honest content of a clean report. Use a shared reference taxonomy so assessments become comparable across firms and over time, which is a field-level coordination problem and is what a standards body or a leading firm would have to start. State a decay estimate, since a report's validity has a half-life as models and techniques move and nobody currently says so. And commission an independent replication on a sample of engagements, since the strongest evidence about coverage is whether another team finds what the first missed.

## Target Customer
Boards and regulators receiving these reports, deploying enterprises, the firms whose thorough work is currently indistinguishable from cursory work, and the standards bodies defining what documented testing means.

## Impact If Built
Regulatory demand is producing documents whose meaning nobody can establish. Coverage over a stated harm taxonomy and technique catalogue is immediately constructible, and the effort-to-findings curve is what tells a reader whether a clean result means robust or unfinished.
