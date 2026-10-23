# Match Rate Measured on the Distributor's Own Inbox

**Niche:** [[niches/industrial-distributors/rfq-and-order-intake-automation/profile|RFQ & Order Intake Automation]]
**Industry:** [[industries/industrial-distributors|Industrial Distributors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every quoting vendor claims a high touchless rate; no distributor can compare them on its own emails before signing, and none of them keeps the hard lines as training data.
**Tags:** #large-language-models #transformers #k-nearest-neighbors #evaluation-metrics #cross-validation #automation #ai-agent
**Contested on:** Every serious competitor in this niche is fighting to turn a customer's RFQ or purchase order — email body, PDF, spreadsheet or scanned fax — into a priced ERP draft quote or order that the rep releases without retyping a line, and whoever posts the highest no-touch line-match rate on the distributor's own inbox takes the account.

## The Problem
A distributor evaluating AI order entry hears 85%-plus touchless claims from several vendors (vendor figures), each measured on different documents with different definitions of "touchless." The distributor's real mix decides the result. An industrial house gets plant POs with customer stock codes, multi-page PDFs and handwritten faxes. An electrical ([[industries/electrical-distributors|Electrical Distributors]]), plumbing/HVAC ([[industries/plumbing-and-hvac-distributors|Plumbing & HVAC Distributors]]) or building-material ([[industries/building-material-dealers|Building Material Dealers]]) house gets contractor bid lists and schedule lines for a straight resale quote as spreadsheets and PDFs, where a line to be matched to a stocked SKU reads "Type F3, 2x4 LED troffer, 4000K, qty 46" or "Ball valve, 1/2 in. sweat, lead-free brass, full port, qty 24" on a plumbing PO; agency-priced lighting packages, full plan-and-spec takeoffs and HVAC schedule entries that must be re-selected against performance requirements are not in this test set. Pilots run one vendor at a time over weeks.

## Why Nobody Has Built This
Vendors have no incentive to publish comparable numbers, and distributors lack the staff to build a test set. The historical alignment between inbound documents and the quotes and orders reps actually keyed exists in every distributor's systems but has never been assembled.

## What to Build
An evaluation harness built from the distributor's own history: a few thousand past POs, RFQs and emailed straight-resale bid lists or schedule lines, each paired with the order or quote reps actually entered, split by customer and by time. It scores header accuracy, line-match accuracy, unit-of-measure errors, schedule-tag resolution and the no-touch rate at a fixed error ceiling, reported separately for purchase orders and project lists because their difficulty differs. The same harness becomes the production loop: every rep correction is stored as a labelled resolution. For an engineer, this is a two-week demo on public manufacturer catalogues, synthetic POs and a sample fixture schedule.

## Target Customer
Operations and inside sales leaders at mid-market distributors choosing among AI order-entry vendors; the vendors themselves, as a shared evaluation standard.

## Impact If Built
Cutting a vendor selection from ~2–3 sequential pilots of ~4–6 weeks each to one ~2-week side-by-side test (estimate) saves ~2–4 months of evaluation, and every stored correction lifts the chosen system's no-touch rate on the lines that used to fail.
