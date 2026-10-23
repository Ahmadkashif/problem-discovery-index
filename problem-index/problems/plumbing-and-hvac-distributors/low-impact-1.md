# Warranty Claims Keyed Into Every Manufacturer's Portal

**Industry:** [[plumbing-and-hvac-distributors|Plumbing & HVAC Distributors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Claims and returns software exists in every ERP and every manufacturer runs a portal, but nothing turns a dealer's failed compressor, a serial number and a tagged part into a claim that each manufacturer's rules will pay the first time.
**Tags:** #large-language-models #transformers #logistic-regression #gradient-boosting #data-integration #automation #revenue-impact

## The Problem
When an HVAC dealer replaces a failed compressor, coil, control board or ECM motor under warranty, the part usually comes from the distributor's shelf and the claim usually goes through the distributor. The warranty clerk has to establish that the unit is covered — model and serial number, the manufacturing date encoded in the serial, the install date, whether the homeowner registered the product within the manufacturer's window (often ~60 days to unlock a 10-year parts warranty instead of 5, estimate), and whether the claim concerns a matched system — then key the claim into that manufacturer's portal, issue a replacement or a credit, tag the failed part, hold it for the manufacturer's return or scrap decision and chase the credit. Water heaters, boilers, pumps and faucet cartridges add their own rules on the plumbing side. A busy branch files hundreds of claims a month in peak season (estimate), across a dozen portals with different fields, labour allowance tables and return windows.

Claims are rejected for reasons the clerk could have caught: an unregistered unit, a serial outside the covered range, a missing failed-part photo, an expired return window, the wrong defect code. Each rejection is a part the distributor has already given away. The A2L launch made it harder, because thousands of new model numbers arrived at once and older R-410A units remain in service under the old rules.

## What Already Exists
Distributor ERPs (Epicor Eclipse, Infor CSD, Prophet 21) carry return-authorisation and credit modules; manufacturers run their own warranty portals and dealer programmes; generic claims and RMA platforms and document-AI tools can read a claim form or a nameplate photo. Field-service platforms used by dealers record the repair but not the distributor's claim.

## The Customisation Gap
The missing layer is manufacturer-specific claim logic joined to the distributor's records: serial-number decoding for each brand, registration lookups, warranty-term tables by model family and install date, the matched-system rules, labour allowance codes, failed-part return and scrap instructions, and each portal's required fields and rejection reasons. It has to read what arrives at the counter — a phone photo of a nameplate, a technician's text, a tagged part — match the replacement to the invoice line, pre-check the claim against that manufacturer's rules, and file it with evidence attached, flagging only the claims likely to fail. Rejection histories by reason code are the training data, and each manufacturer's rules change with each model year.

## Impact If Solved
If ~5–15% of warranty claims are now rejected or abandoned (estimate), pre-checking them before submission recovers credits worth tens of thousands of dollars a year at a mid-size house, and frees a clerk from re-keying claims into a dozen portals during the summer peak.
