# OEM Incentive and Stair-Step Reconciliation

**Industry:** [[franchised-car-dealers|Franchised Car Dealers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Accounting tools reconcile receivables in general, but the money an OEM owes a store for each sale sits under dozens of monthly programmes whose eligibility rules arrive as bulletins nobody turns into checks.
**Tags:** #large-language-models #seq2seq #transformers #data-integration #revenue-impact #automation #quick-win

## The Problem
Each month an OEM publishes a stack of programme bulletins: consumer cash and bonus cash by model and model year, dealer cash, subvented rate and lease support through the captive, loyalty and conquest offers, demonstrator and loaner programmes, CSI-gated payments, facility programme payments and stair-step volume bonuses that pay a per-unit amount only if the store reaches a retail target. Incentive spending averaged 6.6% of the transaction price in September 2026, about $3,359 a vehicle (Kelley Blue Book), and much of it flows through the dealer as a claim.

Someone in the office, often the controller or an incentive clerk, has to match each sale to every programme it qualifies for, claim it in the OEM portal with the right documents, post the receivable to the DMS incentive schedule, and reconcile the OEM's payments and adjustments against it. Programmes overlap, change mid-month and have stacking rules. Misses are silent (money never claimed) and errors are loud (OEM audits charge back incentives on deals that did not qualify, including sales reported to hit a stair-step target that the audit does not accept).

## What Already Exists
DMS accounting holds incentive receivable schedules; spreadsheets track stair-step progress; general reconciliation tools match payments to receivables; incentive data services, such as the Chrome-branded rebates-and-incentives data J.D. Power gained in its December 2019 merger with Autodata Solutions (Thoma Bravo release), feed programme amounts into desking tools so the salesperson can quote them; OEM portals accept claims and post statements.

## The Customisation Gap
What is missing is the programme logic itself. A dealer-side tool needs to turn each bulletin into a machine-checkable rule (eligible models, trims, VIN ranges, model years, sale dates, customer types, documents required, stackability), test every delivered deal against every live rule, flag unclaimed eligibility, and project the month-end stair-step position so the store knows how many more retail units it needs. It also needs the audit side: the documents each programme requires, and the state limit on sales-compensation chargebacks (six months in Virginia, for example) so exposure can be tracked deal by deal. Incentive data feeds were built to quote programmes to customers, not to reconcile what the OEM owes the store.

## Impact If Solved
Claiming every programme dollar a deal earns and defending it through audit is pure margin, and the volume makes small rates matter: a store retailing ~950 new units a year (derived from NADA Data 2025) recovering even ~$50 more per unit net of chargebacks (estimate) gains ~$47,000 a year, while the controller's month-end reconciliation shrinks from days to a review of exceptions.
