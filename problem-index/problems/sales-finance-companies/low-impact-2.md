# Add-On Refunds When a Contract Ends Early

**Industry:** [[sales-finance-companies|Sales Finance Companies]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** When a financed contract is paid off, totalled or repossessed, the unearned part of every GAP, service contract and other add-on sold with it must be cancelled and refunded, and loan servicing systems leave the calculation and the chasing to staff with spreadsheets.
**Tags:** #large-language-models #decision-trees #evaluation-metrics #automation #workflow-orchestration #compliance #quick-win

## The Problem
A large share of indirect contracts carry products sold in the F&I office and financed in the amount financed: GAP waivers or insurance, vehicle service contracts, tyre-and-wheel, appearance protection, theft deterrent. Each has its own contract with its own administrator, term, cancellation provisions and refund method — pro rata, a Rule-of-78 style schedule, or a time-and-mileage formula — minus a cancellation fee that varies by product and state. When the loan terminates early, through refinance, trade-in, payoff, insurance total loss or repossession, the unearned portion is owed back to the borrower or credited to the account, and the lender often has to request the cancellation from the administrator and chase the dealer's share of the commission.

In practice the servicing team finds out the product exists by reading the contract image, looks up the administrator, computes or requests the refund, posts it, and follows up when the money does not arrive. Missed refunds are a recurring supervisory and litigation theme: regulators have repeatedly cited servicers for failing to refund unearned GAP and add-on fees after repossession or payoff, and some states now require the refund by statute.

## What Already Exists
Loan servicing systems (Shaw Systems, Nortridge, LoanPro and others) post payments, compute payoffs and generate letters; F&I product administrators run their own cancellation portals; menu-selling and F&I platforms at the dealer record what was sold. Some administrators and third parties offer cancellation processing as an outsourced service.

## The Customisation Gap
The servicing system knows a dollar amount was financed, not which products it bought or under which terms. The missing layer reads the product contracts at funding and stores them as structured terms (administrator, term in months and miles, refund method, cancellation fee, state endorsements); triggers the cancellation automatically on every termination event, including repossession sale and total loss; computes the refund by the contract's own method and the state's rule; files the cancellation with the administrator; tracks receipt and dealer chargebacks; and produces an audit trail showing each refund was calculated and applied on time.

## Impact If Solved
Refunds would stop depending on someone noticing a product on a contract image. For a lender terminating tens of thousands of contracts a year, that removes a standing source of supervisory findings and class actions and gives borrowers money they are owed without a complaint.
