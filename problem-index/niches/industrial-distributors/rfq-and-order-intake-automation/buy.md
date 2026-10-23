# Document Extraction Turned Into an Order Desk

**Niche:** [[niches/industrial-distributors/rfq-and-order-intake-automation/profile|RFQ & Order Intake Automation]]
**Industry:** [[industries/industrial-distributors|Industrial Distributors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** General document AI reads a purchase order or a straight-resale schedule list accurately; it doesn't know that "6205 2RS C3 or equal" or "Type F3 per schedule" means a specific in-stock SKU at this customer's price.
**Tags:** #large-language-models #transformers #k-nearest-neighbors #data-integration #automation #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to turn a customer's RFQ or purchase order — email body, PDF, spreadsheet or scanned fax — into a priced ERP draft quote or order that the rep releases without retyping a line, and whoever posts the highest no-touch line-match rate on the distributor's own inbox takes the account.

## The Problem
Distributors can buy extraction cheaply: general document-AI platforms and LLM APIs pull header fields and line tables from almost any PDF or spreadsheet. What they get back is text. The rep still has to resolve each line to a SKU, apply the right price and check stock — and on a contractor's emailed bid list or schedule lines for a straight resale quote, also resolve the schedule's type tags and attribute strings (wattage, colour temperature, voltage, tonnage) into one catalogue item per tag.

## What Already Exists
General intelligent document processing platforms, LLM APIs, EDI for the few customers who use it, and Conexiom's order-automation service, which has done distributor-specific extraction for years.

## The Customization Gap
Distribution logic on top of extraction: customer and ship-to resolution; matching line text, customer codes and schedule tags to SKUs and approved equivalents; unit-of-measure conversion (each, box, foot, reel); contract, SPA and project pricing; stock and lead-time checks across branches; and drafts written into Prophet 21, Infor CSD, Eclipse, SAP or NetSuite with each line's confidence visible. Emailed project lists also need grouping by release or phase. Full plan-and-spec takeoffs stay with the bid desk and agency-priced lighting packages with the lighting desk; this layer handles lines matched to SKUs for straight resale.

## Target Customer
Distributors with in-house IT that want to assemble the capability from general tools rather than buy a vertical product.

## Impact If Solved
If the distribution layer lifts lines released without edits from ~30–40% with raw extraction to ~70%+ (estimate), a rep keying ~100 lines a day recovers ~1–2 hours, and the distributor keeps its matching data rather than renting it inside a vendor's model.
