# Technical Assessment

**Parent Industry:** [[industries/fractional-cto-services|Fractional CTO Services]]
**Category:** High Market Share
**Contested on:** Whether the advisor's picture of the system, the team and the delivery process is built from evidence the organisation already produces or from two weeks of reading and asking.

## Profile

**Market Size:** ~$800M
**Share of Parent Industry:** ~27%
**Digital Adoption:** Very low — the instrument is a practitioner reading code and interviewing people
**Target Buyer:** Practice leadership at boutique advisory firms, independent fractional CTOs, private equity technical operating groups
**Automation Potential:** High for evidence derivation, low for the judgement it feeds

## What Makes This a Distinct Niche

Every fractional CTO engagement opens the same way. Someone arrives at a system nobody documented, a team they have just met and a set of decisions already queued — rebuild or refactor, hire or restructure, consolidate or leave alone — and has days rather than months to form an opinion that will move real money. The assessment is the product. Everything else the engagement produces is downstream of it.

What makes it a market rather than a task is that the assessment is sold repeatedly, by many firms, to buyers who cannot evaluate it directly, and the quality difference between a good one and a bad one is enormous and almost invisible at the time of purchase. Firms compete on the reputation of the individual, because there is nothing else to compete on.

The distinctive property is that the evidence is right there. How the codebase is structured, where change actually concentrates, which components consume the most effort, how work flows and where it stalls, what the team's real capacity looks like against what the plan assumes — all of it is substantially derivable from repository history, issue trackers and delivery data the client already generates. The profession forms its opinions by reading and asking anyway.

### Contested sub-niches

- [[niches/fractional-cto-services/evidence-extraction/profile|🎯 Evidence Extraction]]
- [[niches/fractional-cto-services/assessment-calibration/profile|🎯 Assessment Calibration]]

## Current Tools & Gaps

Static analysis tools report code quality metrics that practitioners largely distrust, because a maintainability index says nothing about whether this particular system can absorb the change the business needs. Code complexity dashboards exist and go unused in advisory work. Engineering analytics products aimed at internal teams — DORA metrics, cycle time, review latency — are built for continuous use by the team itself rather than for a stranger assessing the team in two weeks, and require an install and a quarter of data.

The gaps: nothing derives an assessment picture from a repository clone and an issue export in an afternoon. Nothing maps effort concentration onto business capability so the advisor can say which part of the system is eating the budget. Nothing surfaces the discrepancy between what the team says the bottleneck is and what the delivery record shows it is. And nothing anywhere records what the advisor concluded so that a later engagement can check whether that kind of conclusion tends to be right.

## Problems

- [[niches/fractional-cto-services/technical-assessment/build|🔨 Build: The Engagement Instrument]]
- [[niches/fractional-cto-services/technical-assessment/buy|🛒 Buy: Engineering Analytics Turned Outward]]
- [[niches/fractional-cto-services/technical-assessment/fix|🔧 Fix: The Assessment That Leaves With the Assessor]]
