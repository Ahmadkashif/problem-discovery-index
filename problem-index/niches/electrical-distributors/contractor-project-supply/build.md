# One Job Record From Bid Package to Final Release

**Niche:** [[niches/electrical-distributors/contractor-project-supply/profile|Contractor Project Supply]]
**Industry:** [[industries/electrical-distributors|Electrical Distributors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A distributor quotes a job, wins it, orders the gear and ships it for a year, and the quote, the SPA, the submittal and the releases never sit in one record.
**Tags:** #large-language-models #feature-engineering #survival-analysis #gradient-boosting #data-integration #workflow-orchestration #revenue-impact
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor in this niche is fighting to win and keep the electrical contractor's project business, but that splits into two contests with different winners: putting the complete, winning quote in the contractor's hands by bid day, and getting the long-lead gear to the jobsite on the date the schedule needs after award. Decomposed into contested sub-niches below.

## The Problem
Project business passes through four systems and several people. The quote lives in a spreadsheet or the ERP's quote module, the SPA in a manufacturer portal, the submittal in email and the contractor's project platform, and the orders and releases in the ERP under a job name typed slightly differently each time. Nobody can answer simple questions: which quotes became jobs, what the job's realised margin was against the quoted margin, which SPAs were used, and where change orders came from.

## Why Nobody Has Built This
ERPs were built around orders, not projects, and project add-ons stop at job costing. Quoting vendors stop at the quote; order-status tools start at the purchase order. Joining them needs fuzzy job matching across documents that were never designed to link.

## What to Build
A job record keyed on the project, created when the bid package arrives and carried through quote versions, SPA requests and grants, award (inferred from orders when the contractor doesn't say), submittals, purchase orders, acknowledgements, releases, returns and change orders. Language models match documents to the job; the record feeds win-rate and margin-leak analytics by contractor, engineer and package type.

## Target Customer
VPs of construction sales and project managers at distributors with large project books, from chains to regional independents.

## Impact If Built
The distributor finally sees its project business end to end: hit rates, margin from quote to close, and where jobs leak. If quote-to-close margin leakage runs ~1–3 points on project sales (estimate), seeing it by contractor and package is worth ~$1–3M a year on a $100M project book (estimate), and it supplies the evidence both sub-niches' contests need.
