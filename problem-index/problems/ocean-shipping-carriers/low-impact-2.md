# Demurrage and Detention Invoices Under the FMC Rule

**Industry:** [[ocean-shipping-carriers|Ocean Shipping Carriers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Billing and receivables software can issue an invoice, but a US demurrage or detention invoice now has to carry a dozen regulated data elements and go out within 30 days, or the charge is void.
**Tags:** #large-language-models #logistic-regression #evaluation-metrics #compliance #automation #workflow-orchestration

## The Problem
Demurrage accrues when an import container stays in the terminal past its free time; detention accrues when the customer keeps the carrier's equipment past free time outside the terminal. In US trades the Federal Maritime Commission's billing rule (46 CFR 541, effective 28 May 2024) sets the terms. Carriers must invoice within 30 calendar days of the day the charge stopped accruing. The invoice must go to a party with a stated basis for liability and carry the B/L and container numbers, free time and its start and end dates, the container availability or earliest return date, the dates charged, the tariff or contract rate applied, dispute contacts with a URL or QR code, and certifications that the charges comply and that the carrier's own performance did not cause them. An invoice that is late or missing an element need not be paid. The billed party then has at least 30 days to request a waiver or refund, and the carrier must try to resolve the request within 30 days.

## What Already Exists
Carrier billing modules, ERP receivables (SAP, Oracle) and general dispute-management tools handle invoice generation, collections and case tracking. Visibility platforms such as project44, Portcast and Vizion supply container milestones. Terminal operators run their own demurrage billing.

## The Customisation Gap
The FMC rule turns a billing job into an evidence job. The carrier has to assemble the free-time clock from contract or tariff terms, terminal availability (including appointment shortages and terminal closures that should stop the clock), customs and holds data, and its own vessel delays. It then has to prove the billed party is the right one, and certify that nothing it did caused the charge. Generic receivables software has none of that logic. Disputes arrive as emails citing closed terminals or missing appointments, and each needs the specific milestone evidence pulled before the 30-day resolution window closes. The customisation is a rules layer for the FMC elements and deadlines, plus evidence retrieval and draft responses for each dispute type.

## Impact If Solved
Rebuilding a free-time clock for a dispute takes ~30–60 minutes today (estimate). At ~5,000–10,000 disputes a year for a large carrier (estimate), that is ~2,500–10,000 staff hours a year, and most of it goes away when the clock is built before the invoice. The carrier stops losing charges to technicalities, and shippers and truckers see fewer invoices for days when they could not have returned the box.
