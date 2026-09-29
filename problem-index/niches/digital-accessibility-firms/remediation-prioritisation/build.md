# A List Somebody Can Work Through

**Niche:** [[niches/digital-accessibility-firms/remediation-prioritisation/profile|Remediation Prioritisation]]
**Industry:** [[industries/digital-accessibility-firms|Digital Accessibility Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Four thousand findings in an unranked list is not a plan, it is a document.
**Tags:** #optimization-fundamentals #evaluation-metrics #graph-theory #workflow-orchestration #descriptive-statistics #automation #confidence-intervals #compliance
**Contested on:** Every serious competitor in this niche is fighting to get four thousand findings into a backlog in an order somebody can work through, and whoever makes that list actionable takes the account.

## The Problem
A remediation report arrives as thousands of instance-level findings, each located and rated against a criterion. They are imported into a backlog that already contains the roadmap. The engineering team has no basis for ordering them, no way to see that three hundred of them are the same component, and no statement of which ones block a task. The programme stalls, and the organisation concludes that accessibility remediation is intractable.

## Why Nobody Has Built This
The report's structure follows the standard's structure, which is criterion-first and instance-level. Grouping by cause requires knowing the codebase. The audit firm's engagement ends at delivery. And a large finding count has historically looked like thorough work.

## What to Build
Group by cause, route by owner, rank by impact. Group findings by root cause — a shared component, a template, a pattern — rather than listing instances, which is the core and typically collapses thousands of findings into dozens of fixes. Route each group to the team that owns the code, since an unrouted finding belongs to nobody. Rank by task impact and user reach rather than by criterion, so the team works on barriers first. Estimate remediation effort per group, which is what allows accessibility work to be planned against everything else. Identify the fixes that resolve the most findings, as those are the obvious first moves and are invisible in an instance list. Deliver into the client's own issue tracker in their own format rather than as a spreadsheet. Track closure by group and re-verify, rather than closing on assertion. Report progress in terms of barriers removed rather than findings closed, which is the honest measure. Separate the quick pattern fixes from the genuine design changes, since they need different people. And hand over a plan rather than a list, which is the difference between a report and a programme.

## Target Customer
Accessibility firms, client engineering and accessibility leadership, issue tracking and programme tooling vendors, and remediation service providers.

## Impact If Built
Thousands of instance-level findings in a backlog is a document rather than a plan, and the programme stalls there. Grouping by root cause typically collapses them into dozens of fixes with owners and an order.
