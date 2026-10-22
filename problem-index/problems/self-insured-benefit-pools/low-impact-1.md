# Filing Stop-Loss Reimbursements Inside the Contract Window

**Industry:** [[self-insured-benefit-pools|Self-Insured Benefit & Risk Pools]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** A health fund that pays a $1.4M claim is owed most of it back by its stop-loss carrier, but only if a complete claims packet reaches the carrier inside a contract window that generic claims and accounts-receivable tools do not model.
**Tags:** #large-language-models #transformers #feature-engineering #evaluation-metrics #automation #workflow-orchestration #revenue-impact

## The Problem
A Taft-Hartley health fund or a public school employees' health pool carries specific stop-loss: above a deductible per person per year, say $300,000, the carrier reimburses eligible paid claims. Some also carry aggregate cover for the whole plan. Large claims are growing: Sun Life reported million-dollar stop-loss claims up 29% in one year and 61% over four, and paid $6.8M for a single gene therapy in June 2024. For each claimant past the deductible, the fund's administrator must assemble a packet. It holds the paid-claims history, itemised bills, proof of eligibility on every date of service, the plan document provisions that applied, and any case-management or pre-certification notes. The packet must be submitted within the contract's incurred-and-paid basis (12/12, 12/15, 24/12) and its filing deadline. The carrier asks for missing records, disputes eligibility or plan-document language, and pays months later.

At a fund office the work falls to one or two people at the TPA, tracked in a spreadsheet of open claimants, deductibles, lasers (a claimant the carrier carved out with a higher deductible at renewal) and amounts filed, paid and disputed. A claim paid after the contract's paid-through date, an eligibility gap the carrier finds in the hour-bank record, or a packet filed a week late can cost the fund hundreds of thousands of dollars. Nobody notices until the year-end reconciliation.

## What Already Exists
TPA claims platforms flag claimants approaching the specific deductible and produce standard large-claim reports. Generic accounts-receivable and claims-recovery tools track amounts owed and aging. Stop-loss carriers and MGUs run portals for filing, and some TPAs have stop-loss units that file on clients' behalf. Document AI products extract fields from bills.

## The Customisation Gap
What none of them carries is the stop-loss contract itself as logic: the incurred-and-paid basis and run-out, the specific and aggregate deductibles, lasers by claimant, the definition of eligible expense, the plan-document conformity requirement (the carrier reimburses only what the plan document says the fund must pay), and the filing deadline. For multiemployer funds, eligibility comes from an hour bank rather than an HR feed, so proving eligibility on each date of service means tracing hours and self-payments. A customised tool would read each contract into rules, follow every claimant against them from the 50%-of-deductible notice onward, assemble the packet automatically from claims, eligibility and plan-document sources, predict which items the carrier will query, and alert before any paid-through or filing date passes.

## Impact If Solved
A fund with eight to fifteen specific claimants a year (estimate) stops losing reimbursements to missed windows and incomplete packets, and recovers cash months sooner. The trustees see a reconciled stop-loss position each month instead of discovering a shortfall when the auditor tests the receivable.
