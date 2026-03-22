# DBE/MBE/WBE Subcontracting Goal Tracking

**Niche:** [[niches/general-contractors/government-public-works/profile|Government & Public Works Contractors]]
**Industry:** [[industries/general-contractors|General Contractors]]
**Type:** Fix (Pain Point)
**One-liner:** Government contractors stop scrambling at project close-out to prove they met the 15% DBE subcontracting goal — because a dashboard tracked actual vs. required percentages in real time from day one.
**Tags:** #gradient-boosting #feature-engineering #compliance #data-integration #revenue-impact

## The Problem
Most government construction contracts include Disadvantaged Business Enterprise (DBE), Minority Business Enterprise (MBE), or Women Business Enterprise (WBE) subcontracting goals — typically 10-25% of the contract value must be awarded to certified firms. The prime contractor commits to specific DBE subcontractors and dollar amounts in their bid. During construction, the actual spend must track against those commitments. But change orders shift scope, subcontractors get replaced, and work quantities change — so the original DBE commitment percentages drift from reality. The prime contractor doesn't discover the gap until close-out, when the agency requires final DBE utilization documentation. Failing to meet the goal can trigger penalties, reduce the contractor's scoring on future bids, or result in a finding of non-compliance that affects bonding and prequalification.

## Why It's Still Broken
DBE tracking requires connecting three data streams: (1) the original bid commitment (which DBE firms were listed, for what dollar amounts, on which scopes of work); (2) the current contract value (which changes with every change order); and (3) actual payments to DBE subcontractors (which lag behind work completion). No construction accounting system natively tracks "DBE vs. non-DBE" as a subcontractor attribute linked to contractual commitment percentages. Compliance officers maintain spreadsheets that compare committed DBE amounts to actual payments, updating manually after each pay application. When the contract value increases by $200K due to change orders, nobody recalculates whether the DBE percentage still meets the goal against the new total.

## What a Fix Looks Like
A DBE/MBE/WBE tracking module that connects to the contractor's accounting system and maintains a real-time dashboard: original DBE commitment by firm and scope, current contract value (auto-updated with change orders), actual DBE payments to date, projected final DBE percentage based on remaining work, and a gap analysis showing whether the contractor is on track to meet the goal. Alerts fire when: a change order shifts work away from a DBE sub without replacing the DBE commitment, actual DBE payments fall below the pro-rata pace needed to meet the final goal, or a DBE sub's certification is expiring (which would disqualify their payments from counting toward the goal). The system generates agency-required DBE utilization reports (typically monthly) from the tracked data automatically.

## Who Feels the Pain
Compliance officers and project managers who manually track DBE utilization across 3-10 government projects and face personal accountability for compliance failures. Estimators who must identify and recruit qualified DBE subcontractors during the bid phase without a reliable database of certified firms and their capabilities.

## Impact If Fixed
Prevents DBE compliance failures that result in penalties of 1-5% of contract value (on a $5M project, that's $50-250K). Eliminates 4-6 hours per week of manual DBE tracking and reporting per project. Protects the contractor's prequalification status for future government bids — a single DBE non-compliance finding can reduce bid scoring for years.
