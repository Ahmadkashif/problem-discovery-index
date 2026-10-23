# Warranty Claims & Defective-Part Returns

**Parent Industry:** [[industries/plumbing-and-hvac-distributors|Plumbing & HVAC Distributors]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in this niche is fighting to turn each warranty replacement handed across the counter into a claim the manufacturer pays on first submission, and whoever posts the highest first-pass paid-claim rate takes the account.

## Profile
**Market Size:** ~$300M a year of distributor warranty-desk labour plus ~$1–2B of claim credits flowing through HVAC, water-heater and boiler distribution (estimate)
**Share of Parent Industry:** ~0.2% of the three codes' receipts in cost (estimate)
**Digital Adoption:** Low-Medium — every manufacturer runs a portal, but claims are keyed by hand from counter tickets, photos and tagged parts
**Target Buyer:** Warranty manager or controller at the distributor; the OEM's warranty department on the other side
**Automation Potential:** Very High — coverage checks, serial decoding, field population and pre-submission checks are rule-based; only disputed failures need judgement

## What Makes This a Distinct Niche
In two-step HVAC distribution the distributor is the manufacturer's warranty agent: it hands the dealer a replacement compressor, coil, board or motor, files the claim, holds the failed part and waits for the credit. Plumbing houses do the same for water heaters, boilers, pumps and faucet cartridges. Each manufacturer has its own registration rules, serial-number formats, labour allowances, defect codes and return windows, and the A2L launch added thousands of new model numbers (Watsco added more than 10,000 SKUs) while older units stay under older terms. The work is mechanical and voluminous in peak season, which places it on the automatable axis, and the contest is measurable: credits paid on first submission. Claims for extended service contracts are a separate payer layer, logged at [[niches/hvac-contractors/extended-service-contract-administrators/profile|Extended Service Contract Administrators]]; manufacturers' reliability analysis of the same claims is [[niches/hvac-contractors/oem-connected-equipment-data/profile|HVAC OEM Connected Equipment Data]].

## Current Tools & Gaps
Manufacturers' warranty portals, ERP return-authorisation and credit modules, field documentation apps used by dealers, spreadsheets for credit ageing. The gaps: no pre-check against each manufacturer's rules, no join between the counter ticket and the claim, and no reason-coded rejection history.

## Problems
- [[niches/plumbing-and-hvac-distributors/warranty-claims-returns/build|🔨 Build: A Claim Pre-Checker Trained on Each Manufacturer's Rejections]]
- [[niches/plumbing-and-hvac-distributors/warranty-claims-returns/buy|🛒 Buy: Document AI Taught to File in Twelve Portals]]
- [[niches/plumbing-and-hvac-distributors/warranty-claims-returns/fix|🔧 Fix: The Failed Part Scrapped Before the Credit Arrived]]
