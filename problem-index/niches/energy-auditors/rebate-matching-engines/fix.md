# Stale Incentive Information in Proposals

**Niche:** [[niches/energy-auditors/rebate-matching-engines/profile|Rebate & Incentive Matching Engines]]
**Industry:** [[industries/energy-auditors|Energy Auditors]]
**Type:** Fix (Pain Point)
**One-liner:** Auditors include rebate and tax credit information in homeowner proposals, but by the time the homeowner decides (4-12 weeks later), the incentive details may have changed — undermining trust and the financial case.
**Tags:** #automation #data-integration #revenue-impact

## The Problem
An auditor delivers a proposal in March showing $4,200 in available rebates and tax credits. The homeowner considers the proposal for 8 weeks and decides to proceed in May. By then, the utility has exhausted its quarterly rebate budget (reducing the rebate from $800 to $0 until July), and a state program has updated its qualifying equipment list (the recommended heat pump model no longer qualifies). The homeowner expected $4,200 in incentives and is now told they will receive $2,800. The homeowner feels misled, the auditor's credibility is damaged, and the sale may collapse. This scenario plays out on 10-15% of proposals with incentive information, especially for programs with annual budget caps that run out mid-year.

## Why It's Still Broken
Proposals are static documents (PDFs, printed reports) that represent a point-in-time snapshot of incentive availability. No mechanism exists to update a delivered proposal when underlying incentive programs change. Auditors would need to actively monitor every cited incentive program and proactively notify every open proposal's homeowner when something changes — a monitoring task that is impossible to do manually across dozens of programs and dozens of open proposals.

## What a Fix Looks Like
An incentive monitoring system that tracks all incentive programs cited in open (unaccepted) proposals. When a cited program changes (budget exhausted, dollar amount modified, qualifying criteria updated, program deadline passed), the system notifies the auditor, generates an updated financial summary, and optionally alerts the homeowner with the revised incentive information. For programs with budget caps, the system provides estimated exhaustion dates based on historical spending rates, allowing auditors to communicate urgency ("this $800 rebate typically runs out by June — decide by May to maximize your savings").

## Who Feels the Pain
Auditors who lose homeowner trust when delivered incentive estimates prove inaccurate, homeowners who feel deceived by changing incentive amounts, and home performance contractors whose close rates drop 15-25% when incentive discrepancies surface during the sales cycle.

## Impact If Fixed
Maintains incentive accuracy throughout the 4-12 week homeowner decision window, preserving 10-15% of proposals that currently fall through due to stale incentive information. Creates urgency that accelerates homeowner decisions on time-limited programs.
