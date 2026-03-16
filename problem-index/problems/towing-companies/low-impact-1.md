# Motor Club and Insurance Billing Reconciliation

**Industry:** [[towing-companies|Towing Companies]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic invoicing tools cannot handle the matrix of motor club rate tables, documentation requirements, and dispute workflows that differ across AAA, Agero, Allstate, and twenty other payers.
**Tags:** #bert #named-entity-recognition #nlp #automation #data-integration

## The Problem
A mid-size towing company bills 8–15 different motor clubs and insurance programs, each with its own rate schedule, mileage calculations (loaded vs. unloaded miles, hookup fees, storage per-diems), required documentation (photos, police report numbers, VIN verification), and submission portals. Billing staff manually cross-reference each completed job ticket against the correct payer's rate table, reformat documentation to match submission requirements, and track reimbursement timelines that range from 7 to 90 days. Discrepancies between what was billed and what was paid often go uncontested because the billing clerk lacks time to dispute $15–$40 underpayments across hundreds of monthly invoices — but these add up to $2,000–$5,000/month in leaked revenue.

## What Already Exists
QuickBooks and FreshBooks handle general invoicing. Towbook includes basic billing templates. Agero and AAA have their own vendor portals with submission interfaces. None of these systems understand the cross-payer rate matrix or automate the reconciliation between submitted charges and received payments.

## The Customisation Gap
The system needs to ingest rate tables from each motor club (often distributed as PDFs or email attachments updated quarterly), parse completed job tickets to extract billable line items (service type, mileage, wait time, after-hours surcharge), match each line item to the correct payer rate, flag underpayments against the contracted rate, and auto-generate dispute documentation with supporting evidence. NER is needed to extract structured data from unstructured job notes ("responded to AAA call #4472819, 2019 Honda Civic, flatbed 12.3 mi loaded, 35 min on-scene wait") and map it to the correct billing codes.

## Impact If Solved
A 10-truck operation recovers $3,000–$6,000/month in previously leaked revenue from underpayments and unbilled surcharges, while reducing billing staff time by 15–20 hours/week spent on manual reconciliation and portal submissions.
