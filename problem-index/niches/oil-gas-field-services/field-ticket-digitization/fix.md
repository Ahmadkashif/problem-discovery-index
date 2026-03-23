# Field Ticket to Invoice Reconciliation Pipeline

**Niche:** [[niches/oil-gas-field-services/field-ticket-digitization/profile|Field Ticket Digitization]]
**Industry:** [[industries/oil-gas-field-services|Oil & Gas Field Services]]
**Type:** Fix (Pain Point)
**One-liner:** Matching field tickets to purchase orders and generating invoices takes 15-30 days because revenue accountants manually cross-reference tickets, POs, rate schedules, and AFEs line by line.
**Tags:** #bert #text-classification #nlp #automation #revenue-impact

## The Problem
After a field ticket is submitted (paper or digital), it must be matched against the operator's purchase order, the master service agreement rate schedule, and the authorization for expenditure (AFE) to generate an invoice. This matching is manual: a revenue accountant reads the ticket, looks up the PO number, verifies the rate for each service line item, checks that the total does not exceed the AFE authorization, and flags discrepancies for resolution. A typical mid-size service company processes 2,000-5,000 tickets per month, and each takes 10-20 minutes to reconcile. Discrepancies — wrong rate applied, service code mismatch, missing PO number — account for 15-25% of tickets and require back-and-forth calls with field supervisors and operator company men.

## Why It's Still Broken
The reconciliation requires matching unstructured ticket descriptions to structured PO line items using domain knowledge. A ticket might say "P/U 2-7/8 tbg x 4,000'" while the PO says "Pull tubing, 2-7/8 inch, est. 4,000 feet" — a revenue accountant knows these are the same service, but simple string matching fails. Rate schedules vary by operator, by basin, and by contract vintage. AFE structures differ between operators and are often amended mid-job without updating the service company's system. No existing tool handles this multi-document matching with oilfield domain understanding.

## What a Fix Looks Like
An NLP-powered reconciliation engine that ingests field tickets, POs, rate schedules, and AFEs, performs semantic matching between ticket service descriptions and PO line items, applies the correct rate from the contract-specific rate schedule, validates against AFE limits, and auto-generates invoices for clean matches while routing discrepancies to revenue accountants with specific flags (rate mismatch, PO not found, AFE exceeded). The system learns from accountant corrections to improve matching accuracy over time.

## Who Feels the Pain
Revenue accountants who spend 60-80% of their time on ticket-to-invoice reconciliation instead of exception handling and cash collection, and CFOs who see $2-4M in annual revenue delayed 15-30 days by the manual pipeline.

## Impact If Fixed
Automates 70-80% of ticket-to-invoice matching, reduces invoice cycle time from 15-30 days to 3-5 days, and frees revenue accountants to focus on the 15-25% of tickets that genuinely require human judgment on discrepancies.
