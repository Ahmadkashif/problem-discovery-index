# A Denial Ledger Joined to What Happened Next

**Niche:** [[niches/health-insurance-carriers/utilization-management/profile|Utilization Management & Prior Authorization]]
**Industry:** [[industries/health-insurance-carriers|Health Insurance Carriers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Plans record every denial and almost never learn whether it was right, because appeals, resubmissions, readmissions and the care delivered anyway live in other systems.
**Tags:** #causal-inference #survival-analysis #gradient-boosting #evaluation-metrics #data-integration #compliance #revenue-impact
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor is fighting to decide authorization requests inside the CMS-0057-F clocks with determinations that survive appeal. But outpatient prior authorization and inpatient and post-acute concurrent review are won on different inputs, clocks, vendors and outcomes, so the niche is decomposed into contested sub-niches below.

## The Problem
A denial has several possible futures. It may be appealed and overturned (80.7% of appealed MA denials were in 2024, KFF), or reversed in a peer-to-peer call. The provider may resubmit with an extra note and win approval, or the service may be delivered anyway and billed. Or the member may go without and end up in the emergency department. Each future is recorded somewhere: the appeals system, the UM case, the claims platform. None of them is joined back to the original denial, its criterion, its reason code or the medical director who signed it. Only 11.5% of MA denials were appealed in 2024, so the plan knows the fate of roughly one denial in nine.

## Why Nobody Has Built This
UM platforms are case management systems, appeals sit in a separate department, and claims belong to operations. Vendors sell into one of the three. Building the join also means confronting an uncomfortable number: the share of denials that would not have survived a challenge.

## What to Build
A ledger keyed on the authorization request that collects every downstream event for the same member and service within a defined window. It models appeal propensity so that unappealed denials can be weighted honestly, and it estimates overturn-if-appealed rates by criterion, reason code, service, provider type and signer. Survival models track time to resubmission and time to adverse events. Reports flag criteria and denial reasons whose denials reliably fail, for medical policy committees to withdraw or rewrite.

## Target Customer
Chief medical officers and UM leaders at MA and Medicaid plans facing public prior authorization metrics and program audits; specialty benefit managers defending delegated programmes to plan clients.

## Impact If Built
A plan could withdraw the denials that cost it appeals, provider abrasion and regulatory risk while keeping the ones that hold up. It would also have, for the first time, evidence that its medical-necessity decisions are sound.
