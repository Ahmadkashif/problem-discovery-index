# Evidence Extraction

**Parent Industry:** [[industries/fractional-cto-services|Fractional CTO Services]]
**Category:** Contested Sub-Niche
**Contested on:** Whether a stranger can derive a truthful picture of a codebase, a team and a delivery process from the artefacts that organisation already produces, fast enough to matter inside an eight-week engagement.

## Profile

**Market Size:** ~$480M
**Share of Parent Industry:** ~16%
**Digital Adoption:** Very low — the derivation is done by reading
**Target Buyer:** Fractional CTOs, technical due diligence practitioners, advisory boutiques
**Automation Potential:** Very high — the inputs are machine-readable and complete

## What Makes This a Distinct Niche

This is the measurement half of technical assessment: given a repository history, an issue tracker, a CI record and whatever delivery data exists, what can be said with confidence about this system and this team, and how quickly.

It is a self-contained problem with a self-contained buyer. Every practitioner needs it on every engagement, it produces value on the first day it exists, it requires nothing from past engagements, and it can be evaluated immediately — either the derived picture matches what the practitioner concluded after two weeks of reading, or it does not. That testability is what separates it from its sibling, [[niches/fractional-cto-services/assessment-calibration/profile|🎯 Assessment Calibration]], which cannot be evaluated for a year.

The contest is over truthfulness under a cold start. Anyone can compute commit counts. The hard question is which derived signals actually correspond to the things an advisor cares about — where a rebuild will be bounded or unbounded, whether a team's stated capacity is real, which component is quietly consuming the budget — and how those signals behave on an estate the tool has never seen, with no baseline, no configuration, and eighteen months of history that includes a migration, a reorganisation and a tooling change nobody will mention.

## Current Tools & Gaps

Behavioural code analysis — hotspots from change frequency, temporal coupling from co-change, knowledge distribution from authorship — is the mature technique here, best represented by CodeScene and by two decades of repository-mining research on defect prediction and change coupling. Engineering analytics platforms compute the flow side. Static analysers cover structure. Dependency scanners cover a slice of risk.

The gaps sit at the joins. History is discontinuous — a monorepo migration, a `git filter-branch`, a vendored directory or a bulk reformat will destroy naive change-frequency analysis, and nothing detects and corrects for those events automatically, which is the single largest source of wrong answers on an unfamiliar estate. Issue tracker semantics vary per team to the point where cycle time is not comparable without inferring what the states actually mean. Code and tickets are rarely linked well enough to attribute effort to business capability. And almost nothing quantifies its own confidence, which matters enormously when the output feeds an eight-figure recommendation and the practitioner has no way to sanity-check a number derived from data they have not seen.

## Problems

- [[niches/fractional-cto-services/evidence-extraction/build|🔨 Build: Cold-Start System Evidence]]
- [[niches/fractional-cto-services/evidence-extraction/buy|🛒 Buy: Repository Mining for the Outsider]]
- [[niches/fractional-cto-services/evidence-extraction/fix|🔧 Fix: History That Lies]]
