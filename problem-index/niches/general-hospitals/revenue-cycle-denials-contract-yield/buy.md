# Accounts Payable Recovery Audit Adapted to Payer Remittances

**Niche:** [[niches/general-hospitals/revenue-cycle-denials-contract-yield/profile|Revenue Cycle: Denials & Payer Contract Yield]]
**Industry:** [[industries/general-hospitals|General Hospitals]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Retailers have used recovery-audit software for decades to find what suppliers overbilled them; hospitals need the same discipline pointed at what payers underpaid.
**Tags:** #large-language-models #gradient-boosting #evaluation-metrics #data-integration #automation #revenue-impact
**Contested on:** *Not terminal as stated.* The honest partial sentence is: every serious competitor in this niche is fighting to collect what the hospital is owed on each claim. Clinical denials are won by whoever builds the strongest chart-and-policy argument before the appeal deadline, and contract yield by whoever models every payer's contract terms against every remittance. Decomposed into contested sub-niches.

## The Problem
Payers pay most claims correctly, but a few percent of lines are paid short: a carve-out rate missed, an outlier threshold misapplied, a new CPT code paid at a default. Each line is small, there are millions of them, and contract dispute windows close.

## What Already Exists
Recovery-audit platforms and firms in retail and corporate accounts payable (PRGX-style contingency audit) compare invoices against contracts and claw back overbilling. In hospitals, contract-management modules (Epic, FinThrive, Experian) compute expected reimbursement, and contingency underpayment firms work the variances.

## The Customization Gap
Hospital remittances need rules that AP audit tools lack: DRG and APC groupers, outlier and transfer formulas, lesser-of-charges clauses, per-diem stepdowns, implant carve-outs, and Medicare-percentage contracts that change with every IPPS and OPPS rule. Expected payment must be recomputed with the rule versions in force on the date of service. Each payer's dispute window and resubmission format is different, and the recovered amount must be posted back to the patient account.

## Target Customer
Directors of patient financial services and revenue integrity at community and regional hospitals that cannot staff a contract-modelling team.

## Impact If Solved
Recovering an extra ~0.3–0.8% of commercial net revenue (estimate) on lines currently accepted as paid is pure margin for a hospital running at 2–3%.
