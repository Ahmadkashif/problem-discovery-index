# The Rule Everyone Overrides

**Niche:** [[niches/spend-management-platforms/spend-policy-and-control/profile|Spend Policy & Control]]
**Industry:** [[industries/spend-management-platforms|Spend Management Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** One threshold generates half the exceptions in the company and has never once resulted in a denial.
**Tags:** #descriptive-statistics #quick-win #evaluation-metrics #automation #workflow-orchestration #confidence-intervals #worker-facing #compliance
**Contested on:** Every serious competitor in this niche is fighting to make control mean something better than a rule engine that generates exceptions humans rubber-stamp — and the contest splits cleanly enough that it is not terminal.

## The Problem
A company set a per-transaction limit during implementation, based on a number someone suggested. Prices rose, the team grew, and that limit now flags a large share of routine spend. Every flagged transaction interrupts an employee, waits for a manager, and is approved. Nobody has ever looked at the distribution of exceptions by rule, so the fact that one threshold is generating half of them — with a one hundred percent approval rate — is known to nobody.

## Why It's Still Broken
Rules were configured at implementation and the implementation ended, so nothing in the product ever revisits them — the configuration is treated as a setup step rather than as a living policy. Exception volume falls on managers rather than on a budget. The platform does not report rule-level statistics. And changing a limit feels like loosening control.

## What a Fix Looks Like
Report by rule and act on the obvious. Show exception volume and approval rate per rule, which is the fix and is a single report that will immediately identify two or three rules generating most of the friction. Flag any rule approved above a very high rate as a candidate for adjustment, since a control that never denies anything is documentation rather than control. Show the manager hours each rule consumes, because converting exception counts into time makes the case instantly. Recommend a threshold from the observed distribution, as the right limit is visible in the data and the current one was a guess. Prompt a policy review on a schedule rather than never, which is the structural fix. Alert when exception volume shifts materially, since it usually means the business changed rather than that behaviour worsened. Let the customer see benchmark thresholds from similar companies, which is the platform's unique advantage and is entirely absent. Distinguish rules that catch something from rules that only interrupt, because both currently look identical. Make the change easy and reversible, so a controller will actually try it. And report exception rate as a product health metric, since a platform generating enormous exception volume is not delivering control.

## Who Feels the Pain
Employees interrupted for routine spend; managers approving without reading; controllers whose month is exceptions; and companies believing they have a control that has never denied anything.

## Impact If Fixed
Rules are treated as a setup step rather than as living policy, so nothing ever revisits them. A per-rule exception and approval report identifies the handful of thresholds generating most of the friction in a single view.
