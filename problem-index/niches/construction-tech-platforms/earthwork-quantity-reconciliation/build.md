# Four Measurements of the Same Dirt, Reconciled

**Niche:** [[niches/construction-tech-platforms/earthwork-quantity-reconciliation/profile|Earthwork & Sitework — Quantity Reconciliation]]
**Industry:** [[industries/construction-tech-platforms|Construction Tech Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Design surfaces, machine control records, drone survey and haul counts are four independent measurements of how much material moved, they are all digital, they never agree, and no product compares them.
**Tags:** #numerical-methods #confidence-intervals #hypothesis-testing #evaluation-metrics #descriptive-statistics #data-integration #revenue-impact #automation
**Contested on:** Every serious competitor in earthwork software is fighting to reconcile the material actually moved against the material paid for, across design surfaces, machine control, survey and truck counts — and whoever makes those four numbers agree takes the account.

## The Problem
A contractor's machines moved material all month. The machine control system knows where every blade was. The haul trucks logged every load. The drone flew weekly and produced measured surfaces. The owner's engineer measured quantities for the pay application and arrived at a number the contractor believes is low. To argue, the contractor's project engineer opens four systems, exports four datasets in four formats, and rebuilds a comparison in a spreadsheet over two days — for one month of one project. Most of the time the effort is not made and the number is accepted.

## Why Nobody Has Built This
Each measurement comes from a vendor with a closed ecosystem and a commercial interest in being the system of record, so the formats are exportable and not interoperable, and no vendor benefits from a product that treats its output as one input among four. The comparison is also technically finicky in ways that matter: surfaces must be compared on a common datum and a common boundary, volumes depend on the method used to compute them, haul counts need a bulking factor that varies by material, and machine data is noisy. Doing it approximately produces numbers that will lose an argument, which is worse than not doing it. Nobody has been willing to fund the precision.

## What to Build
A reconciliation engine that holds all four measurements on a common spatial frame and reports their differences as a located map rather than a total. Surface-to-surface volumes are computed with the method stated and held constant. Machine control production is aggregated into moved volume by area and period. Haul records are converted with material-specific bulking factors that the system estimates from the contractor's own paired data rather than from a handbook. The output is per-area agreement with an uncertainty band per method, and — most importantly — the residual: the material moved that no design surface accounts for, located precisely and dated. Every figure carries its provenance, because the artefact's purpose is to be presented to an owner's engineer who will question it.

## Target Customer
Earthwork and heavy civil contractors running machine control and drone survey, which is most of the mid-market and above, and the site positioning vendors who could offer reconciliation rather than another system of record.

## Impact If Built
Located, dated evidence of material moved beyond the design is the basis of every differing-site-condition claim in earthwork, and having it contemporaneously rather than reconstructing it is the difference between a recoverable claim and an absorbed cost. Routine reconciliation also catches the ordinary case — a pay quantity measured low — monthly rather than never, which for a quantity-paid contractor is a direct margin recovery.
