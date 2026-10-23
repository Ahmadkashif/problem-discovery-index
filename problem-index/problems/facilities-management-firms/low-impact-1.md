# Subcontractor Invoices Checked Against the Work Order

**Industry:** [[facilities-management-firms|Facilities Management Firms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every IFM account checks thousands of subcontractor invoices a year against work orders, rate cards and not-to-exceed limits before rebilling them with markup, and the accounts-payable tools built for purchase orders do not understand any of those three.
**Tags:** #large-language-models #gradient-boosting #k-nearest-neighbors #descriptive-statistics #data-integration #automation #revenue-impact

## The Problem
On an IFM account, a large share of the work is subcontracted: elevator maintenance, fire protection inspection, roofing, specialist HVAC repairs, pest control, and much of the reactive work in regions where the provider has no technicians of its own. More than half of CBRE's 2025 Building Operations & Experience revenue was pass-through cost. Each job produces an invoice, usually a PDF, against a work order issued with a not-to-exceed (NTE) amount. Before the invoice is paid and rebilled to the client, someone has to confirm that the work order exists and was completed, that the labour hours and trip charges match the subcontractor's rate card for that trade and region, that after-hours multipliers apply only to after-hours work, that parts markup is within the agreed percentage, that the job was not covered by a warranty or by the client's own service contract, and that the total sits under the NTE or has an approved increase.

That checking is done by account coordinators and AP clerks reading PDFs beside the CMMS. Errors go both ways. Overbilling passes through to the client, who finds it in an audit and treats it as the provider's failure. Valid invoices sit in dispute for weeks, and the best subcontractors stop answering the provider's calls.

## What Already Exists
Accounts-payable automation (Coupa, SAP Ariba and Concur invoice processing, and OCR capture tools) handles three-way matching of invoice, purchase order and goods receipt. Facility-specific platforms such as ServiceChannel and Corrigo include invoice modules that check an invoice against its work order and NTE.

## The Customisation Gap
Generic AP matching assumes a purchase order with fixed lines. A facilities job has none: the NTE is a ceiling, not a price, and the correct amount depends on the trade's rate card, the time of day, the region, travel rules, parts markup caps and the client contract's own pass-through terms, which differ by account. The CMMS invoice modules check the NTE and little else. What is missing is per-account contract logic: rate cards by trade, region and hour band; warranty and service-contract coverage by asset; the client's markup and approval thresholds; and a comparison of the invoice against what similar jobs on similar assets usually cost, so an outlier is flagged even when it sits under the NTE.

## Impact If Solved
Account coordinators would stop reading PDFs line by line, and the provider would catch overbilling before the client's audit does, which protects both the margin and the renewal. On a large account the leakage caught could run to a low single-digit percentage of pass-through spend (estimate).
