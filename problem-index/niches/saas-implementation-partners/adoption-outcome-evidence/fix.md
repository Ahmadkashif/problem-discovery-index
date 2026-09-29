# The Workflow Nobody Has Used Since March

**Niche:** [[niches/saas-implementation-partners/adoption-outcome-evidence/profile|Adoption Outcome Evidence]]
**Industry:** [[industries/saas-implementation-partners|SaaS Implementation Partners]]
**Type:** Fix (Pain Point)
**One-liner:** The approval workflow that took three weeks to configure has not been triggered in eight months and nobody has noticed.
**Tags:** #quick-win #descriptive-statistics #evaluation-metrics #data-integration #automation #confidence-intervals #revenue-impact #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to know which of its configurations were actually adopted, when the evidence accumulates in the client's tenant the day after the partner leaves — and whoever collects it takes the account.

## The Problem
Implementations contain configurations that are never used. A workflow that took weeks to build and test is triggered twice and abandoned; fields designed in a workshop are never populated; a module the client insisted on sits idle. The client pays for it, maintains it through every release, and nobody ever looks. The usage data showing this is in the tenant and takes minutes to query.

## Why It's Still Broken
Nobody queries usage after go-live — a configuration that nobody looks at looks exactly the same whether it is used daily or never, and no step in any process looks. The partner has left. The client has no reason to audit. And unused configuration costs nothing visibly while costing real maintenance.

## What a Fix Looks Like
Run the usage query, which the platform already supports. Query object, field and workflow usage against the configuration as a standard post-go-live review, which is the fix and takes an afternoon on any of these platforms. Do it at ninety days rather than during hypercare, since abandonment happens after the initial push. Report unused configuration to the client with the option to retire it, which is a service they value and rarely receive. Identify fields never populated, which are the most common and most invisible waste. Compare against what the design said would be used, so the gap is attributable. Feed the finding into the next engagement's design, which is where the firm improves. Offer the review as a paid service, which makes it sustainable. Look at depth of use rather than only whether something was touched, as light use and real use are different outcomes. Record the result against the configuration pattern so the evidence accumulates. And repeat it annually for managed services clients, where it is straightforwardly billable.

## Who Feels the Pain
Clients maintaining configuration nobody uses; consultants who built it and never learned; firms whose design decisions never improve; and every subsequent engagement that repeats the same design.

## Impact If Fixed
A configuration that nobody looks at looks exactly the same whether it is used daily or never, and no step in any process looks. An afternoon's usage query at ninety days makes abandonment visible and retirable.
