# Five Numbers and a Thursday Deadline

**Niche:** [[niches/marketing-attribution-vendors/the-client-side-analyst/profile|The Client-Side Analyst]]
**Industry:** [[industries/marketing-attribution-vendors|Marketing Attribution Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The client-side analyst has platform numbers, site analytics, the attribution vendor, the mix model and finance, all disagreeing, and is asked which one is right before Thursday.
**Tags:** #worker-facing #data-integration #descriptive-statistics #evaluation-metrics #confidence-intervals #workflow-orchestration #automation #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to give the analyst a defensible answer to which number is right before Thursday — and whoever does that serves the person the entire category's output actually lands on.

## The Problem
The analyst opens five sources. The platforms report their own conversions. Site analytics reports sessions and goals on a different basis. The attribution vendor reports contributions. The mix model reports something else again. Finance reports revenue, which is the only number anyone else in the company recognises. None of them agree, the differences have knowable causes, and the analyst has two days to produce something the leadership meeting can use. They build a spreadsheet, make judgement calls, present it, and do the same thing next month because nothing about the exercise was retained.

## Why Nobody Has Built This
Every vendor builds to their own output and none builds to the convergence, so the integration falls on the only party with no product budget — the person the whole category's output lands on is the one nobody sells to. The differences require domain understanding of each source's definitions, which is knowledge held individually. Reconciliation is seen as a task rather than a capability. And the analyst's time is invisible.

## What to Build
Build the convergence layer. Ingest all sources and normalise their definitions explicitly — windows, conversion types, channel groupings, currencies, time zones — which is the foundation and resolves a surprising share of the apparent disagreement before any judgement is required. Reconcile everything against the financial record, since it is the one number the business recognises and it bounds all the others. Explain each difference by cause rather than presenting five numbers, which is what the analyst constructs by hand and is entirely mechanical once the definitions are mapped. Retain the reconciliation so it is updated rather than rebuilt, which is the difference between a monthly task and a maintained view. Give the analyst a defensible recommendation with reasoning, so they present a position rather than a spreadsheet. Flag which differences are definitional and which are substantive, because the first are noise and the second are findings and they are currently indistinguishable. Prepare the leadership view directly, since the deliverable is a meeting and assembling it is a large part of the work. Keep a history so a recurring difference is recognised as recurring. Alert when a source diverges from its own pattern, which is usually a data problem and is currently found during the reconciliation. And measure time to close the reconciliation, because that number is the analyst's month and nobody has ever counted it.

## Target Customer
Client-side analytics teams and their leadership, measurement vendors who could differentiate by serving the convergence, and the finance functions receiving the output.

## Impact If Built
Every vendor builds to its own output and the convergence falls on the party with no budget. Normalising definitions resolves much of the apparent disagreement mechanically, and reconciling to the financial record gives the analyst a position rather than a spreadsheet.
