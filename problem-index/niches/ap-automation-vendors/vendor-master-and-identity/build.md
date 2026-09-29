# The Record at the Root of Everything

**Niche:** [[niches/ap-automation-vendors/vendor-master-and-identity/profile|Vendor Master & Identity]]
**Industry:** [[industries/ap-automation-vendors|AP Automation Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The vendor record causes most of the exceptions and absorbs most of the fraud, and it is maintained by whoever onboarded the supplier that year.
**Tags:** #graph-theory #evaluation-metrics #data-integration #confidence-intervals #compliance #gradient-boosting #automation #word-embeddings
**Contested on:** Every serious competitor in this niche is fighting to know who a vendor actually is and whether their payment details are real — and the contest splits cleanly enough that it is not terminal.

## The Problem
Two failures trace to the same record. Exceptions occur because the invoice says one name and the master says another, because the tax identifier differs, because the purchase order was raised against a different record for the same supplier. Fraud succeeds because a convincing email changes a bank account on a record nobody independently verifies. Both are treated as operational problems in separate parts of the product, and both are consequences of a master file nobody owns.

## Why Nobody Has Built This
The vendor master is the customer's data in the customer's ERP, so the platform positioned itself as a consumer of it rather than as a steward — and a consumer has no mandate to fix it. Cleaning it is a project with no obvious owner and no immediate payoff. Fraud is addressed with training because training is cheap. And the cross-buyer evidence that would settle both questions was never assembled.

## What to Build
Treat the record as the product's foundation and resolve both halves. Resolve vendor identity across records, since the duplicates are the root of the exception problem and the ambiguity is what fraud exploits. Verify payment details against evidence the attacker cannot forge, which is the security half and is where the cross-buyer view is decisive. Use the platform's cross-customer view for both, because the same supplier invoices hundreds of buyers and their real identity and real bank details are visible in aggregate in a way they are not to any single customer. Score every change to a vendor record for risk rather than treating changes as routine maintenance, as that reframing is what makes detection possible. Measure master data quality and report it, since customers do not know how bad theirs is and cannot prioritise what they cannot see. Attribute exceptions to master data defects, which quantifies the cost and funds the cleanup. Maintain the resolved identity as a persistent entity that survives record changes. Handle mergers, rebrands and entity restructuring, as those are the legitimate cases that look like anomalies. Keep the customer's ERP as the system of record while supplying the resolution, which is the practical deployment path. And build the verification network as a shared asset, since its value grows with participation.

## Target Customer
Data and risk leadership, AP and procurement teams, finance leaders who have suffered a payment fraud loss, and master data vendors with no cross-buyer evidence.

## Impact If Built
The platform positioned itself as a consumer of the customer's vendor data rather than a steward, and a consumer has no mandate to fix anything. The cross-buyer view resolves identity and verifies payment details in ways no single customer's file can.
