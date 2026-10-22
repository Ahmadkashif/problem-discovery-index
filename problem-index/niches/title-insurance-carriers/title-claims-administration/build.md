# A Claim Ledger From Notice to Final Cost

**Niche:** [[niches/title-insurance-carriers/title-claims-administration/profile|Title Claims Administration & Litigation]]
**Industry:** [[industries/title-insurance-carriers|Title Insurance Carriers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No title underwriter keeps one record per claim that joins what counsel predicted at intake, what path the claim took, what it finally cost and what caused it.
**Tags:** #survival-analysis #gradient-boosting #large-language-models #feature-engineering #evaluation-metrics #data-integration #tacit-knowledge-ml
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor in this niche is fighting to resolve title claims at the lowest total cost of loss and expense. That splits into two contests with different winners: deciding coverage and setting the first reserve correctly inside the statutory clock at intake, and curing or defending covered claims through counsel for less than paying them. Decomposed into contested sub-niches below.

## The Problem
A title claim's story is spread across the notice, the coverage letter, the reserve history, panel-counsel invoices, settlement papers and payments, often in several systems. Intake staff need fast coverage calls. Litigation managers need cheaper resolutions. Actuaries need earlier, better-labelled reserves. Underwriting needs to know what caused the loss. All four lack the same thing, a single structured record of each claim from notice to final cost.

## Why Nobody Has Built This
Claim systems are built to pay and reserve, not to explain. The history sits in free text, and the claims departments that own it are lean legal teams without data engineers.

## What to Build
A ledger built from existing claim files by document extraction and kept current going forward. Each claim gets its notice facts, policy and exceptions, counsel's intake read (path, severity, confidence), the path actually taken, legal spend by phase, indemnity, time to close and a root-cause code. Both sub-niches' tools draw on it: intake triage on one side, litigation management on the other. The actuaries get claim-type emergence patterns from it.

## Target Customer
Chief claims officers and chief actuaries at the four families and regional underwriters.

## Impact If Built
One record serves intake, litigation, reserving and underwriting feedback, and lets the underwriter grade the judgements that drive its loss costs.
