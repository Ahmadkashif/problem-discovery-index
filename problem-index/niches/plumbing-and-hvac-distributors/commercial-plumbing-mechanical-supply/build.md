# One Job Record From Schedule to Final Release

**Niche:** [[niches/plumbing-and-hvac-distributors/commercial-plumbing-mechanical-supply/profile|Commercial Plumbing & Mechanical Project Supply]]
**Industry:** [[industries/plumbing-and-hvac-distributors|Plumbing & HVAC Distributors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A commercial job passes through bid, selection, submittal, award, price hold and a dozen releases, and the supply house keeps each stage in a different place.
**Tags:** #large-language-models #transformers #k-nearest-neighbors #data-integration #workflow-orchestration #revenue-impact
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor in this niche is fighting to win the mechanical or plumbing contractor's material package on a commercial job, but contractors routinely split that package, and the two halves are won differently: the equipment and fixtures go to whoever re-selects the engineer's schedule in its own lines and gets the substitutions approved, and the pipe, valves and fittings go to whoever holds the lowest firm price across a release schedule that runs for months while copper and PVC move. Decomposed into contested sub-niches below.

## The Problem
The bid package sits in email, the selections in an OEM program, the quote in the ERP, the submittal response in the contractor's project platform, the price hold in the PVF manager's head and the releases in sales orders keyed months later under a job name spelled three ways. Nobody can say which jobs were won, which halves of a package were lost, or why.

## Why Nobody Has Built This
ERPs were built around orders, not jobs, and construction CRMs were built for contractors. The joining key — the job — is typed by hand at each stage.

## What to Build
A job graph that starts when a bid package arrives: it extracts the job's name, address, engineer, contractors bidding and schedules; links each quote line and selection to it; attaches submittal responses as they arrive; records price holds with their terms; and matches later orders and releases to the job by ship-to, name similarity and products, inferring wins and partial wins. A demo can run on public bid documents and a synthetic order history.

## Target Customer
Commercial and mechanical sales leaders at multi-branch plumbing and HVAC distributors.

## Impact If Built
If a house can infer the outcome of ~70–80% of its commercial quotes instead of ~20–30% (estimate), it learns its hit rate by contractor, engineer and package half, and stops spending quote-desk hours on jobs it never wins.
