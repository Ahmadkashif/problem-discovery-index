# Core and Warranty Credits Reconciled by Hand

**Industry:** [[auto-parts-distributors|Auto Parts Distributors & Stores]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Returns and reconciliation software exists everywhere; none of it knows that a starter core has a deposit, an acceptance test, a supplier-specific core bank and an ageing clock.
**Tags:** #gradient-boosting #logistic-regression #k-nearest-neighbors #feature-engineering #automation #data-integration #revenue-impact

## The Problem
A large share of hard parts sold to shops carry a core: starters, alternators, brake calipers, steering racks, AC compressors, batteries. The store charges a core deposit, and credits it when the shop brings back the old unit. That unit then goes back up the chain to the warehouse distributor and on to the supplier or remanufacturer, who inspects it and issues a credit if it is the right family, complete and not cracked or burned. Warranty returns follow a parallel path with defect codes and labour claims. Each step happens on paper tags, in a returns cage and in a spreadsheet maintained by a returns or core clerk, and the controller learns months later that a supplier rejected a batch of "dirty" cores or never issued a credit at all. Advance Auto Parts' $28M charge in 2025 for expected losses on receivables from a supplier in Chapter 11 shows how much sits in supplier-owed balances; core and warranty credits are a slice of that exposure at every distributor.

## What Already Exists
ERP return-merchandise modules in Epicor and other distributor systems log returns and issue credit memos. Reverse-logistics platforms built for retail e-commerce route returned goods, and account reconciliation tools such as BlackLine match ledger balances. Remanufacturers run their own core-acceptance portals. Each covers a step, and none follows a core from the shop's counter through to the supplier's credit memo.

## The Customisation Gap
The logic that matters is core-specific. Each supplier keeps its own core bank and acceptance rules (which casting numbers or part families are interchangeable, what damage voids credit, how long a core can age before it is refused); credits arrive as lump memos that must be split back to individual units; shops return cores against invoices months old or against a different store; and the same physical unit can be eligible for one supplier's credit and not another's. Warranty adds defect coding, labour allowances and the rule that a returned part must match the lot sold. A useful tool needs a core-family table per supplier, unit-level tracking from tag scan to credit, matching of lump credits to units, and an ageing view that flags cores about to lose eligibility.

## Impact If Solved
If a distributor recovering ~$5M a year of core and warranty credits lifts its recovery rate from ~95% to ~99% (estimate), it books ~$200K a year that is now written off, and its returns clerks stop spending a day a week chasing supplier memos.
