# Subcontractor Invoice Validation & Pass-Through Billing

**Parent Industry:** [[industries/facilities-management-firms|Facilities Management Firms]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in this niche is fighting to validate every subcontractor invoice against its work order, rate card and not-to-exceed before it is rebilled to the client, and whoever catches the overbilling before the client's audit does takes the account.

## Profile
**Market Size:** ~$700M a year of coordinator, accounts-payable and audit labour spent validating and rebilling subcontractor invoices on US FM accounts (estimate)
**Share of Parent Industry:** ~1% of US integrated facility services revenue (estimate)
**Digital Adoption:** Medium — invoices are captured electronically, but validation is a person reading a PDF beside the CMMS
**Target Buyer:** Account finance leads and AP managers at IFM providers
**Automation Potential:** High — extraction, rule checks and outlier detection are mechanical once the contract logic is encoded

## What Makes This a Distinct Niche
Pass-through is the largest single flow of money through an IFM provider: more than half of CBRE's 2025 Building Operations & Experience revenue was pass-through cost. Every subcontractor invoice has to be matched to a completed work order, checked against the subcontractor's rate card by trade, region and hour band, tested for warranty or service-contract coverage, kept under the not-to-exceed, then rebilled at the markup the client contract allows. This is a document-processing contest decided by volume and accuracy, distinct from the strategic choice of what to subcontract, which is profiled at [[niches/facilities-management-firms/self-delivery-subcontract-mix/profile|🎯 Self-Delivery vs Subcontract Delivery Mix]].

## Current Tools & Gaps
AP automation (Coupa, SAP Ariba, OCR capture), CMMS invoice modules (ServiceChannel, Corrigo) that check the NTE, and spreadsheets of rate cards. The gaps: no per-account contract logic, no check against similar jobs, and disputes worked by email.

## Problems
- [[niches/facilities-management-firms/subcontractor-invoice-validation/build|🔨 Build: A Should-Cost for Every Reactive Job]]
- [[niches/facilities-management-firms/subcontractor-invoice-validation/buy|🛒 Buy: Three-Way Match Rebuilt for Not-to-Exceed Work Orders]]
- [[niches/facilities-management-firms/subcontractor-invoice-validation/fix|🔧 Fix: Warranty Work Paid Twice]]
