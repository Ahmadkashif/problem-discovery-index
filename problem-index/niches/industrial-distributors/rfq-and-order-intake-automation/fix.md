# The Customer's Own Part Number and the Schedule's Own Tag

**Niche:** [[niches/industrial-distributors/rfq-and-order-intake-automation/profile|RFQ & Order Intake Automation]]
**Industry:** [[industries/industrial-distributors|Industrial Distributors]]
**Type:** Fix (Pain Point)
**One-liner:** Many PO lines carry only the plant's internal stock code, and many straight-resale bid-list lines carry only the schedule's type tag, and every automation stalls on both until someone builds the cross-reference.
**Tags:** #k-nearest-neighbors #word-embeddings #large-language-models #data-integration #quick-win #automation
**Contested on:** Every serious competitor in this niche is fighting to turn a customer's RFQ or purchase order — email body, PDF, spreadsheet or scanned fax — into a priced ERP draft quote or order that the rep releases without retyping a line, and whoever posts the highest no-touch line-match rate on the distributor's own inbox takes the account.

## The Problem
Large plant customers order from their own item master: a stock code and a short description in their style, sometimes with the manufacturer's number, often not. Contractors send emailed lists for straight resale quotes that name items by the engineer's schedule tag ("Type B2", "EF-3") with a line of attributes to be matched to stocked SKUs, and the same contractor reuses the tag set across jobs. The distributor's ERP may hold a customer part-number cross-reference, but it is incomplete and stale, and schedule tags aren't stored at all, so these lines fall out of automation and land back on a rep.

## Why It's Still Broken
Cross-references are built one line at a time when a rep happens to resolve an order, and are rarely written back to the ERP. Customers change codes when they change systems; schedule tags change per job, so nobody thinks of storing them.

## What a Fix Looks Like
Mine past orders and quotes to pair each customer code, and each tag-plus-attributes string, with the SKU the rep eventually shipped or quoted; propose matches for unmapped codes from description similarity and purchase patterns; and write every confirmed resolution back automatically. Ask plant customers for their item-master extract at onboarding and map it in bulk.

## Who Feels the Pain
Inside reps resolving the same codes repeatedly, vendors whose touchless rates collapse on these lines, and customers waiting on quotes.

## Impact If Fixed
If customer codes and tags account for ~20–40% of the lines that fall out of automation (estimate), mapping them can add ~10–20 points to a distributor's no-touch rate (estimate), and it is a data job, not a model breakthrough.
