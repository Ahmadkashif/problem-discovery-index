# Field Ticket Digitization

**Parent Industry:** [[industries/oil-gas-field-services|Oil & Gas Field Services]]
**Category:** Highly Automatable

## Profile
**Market Size:** Embedded across the $150B oilfield services industry (estimated $2-4B in annual billing disputes originate from handwritten field tickets)
**Share of Parent Industry:** Cross-cutting — field tickets are the universal transaction record for every service category
**Digital Adoption:** Low-Medium — FieldFX and ServiceMax offer digital ticketing, but 60-70% of field tickets in the US are still handwritten on multi-part carbon forms and manually keyed into accounting systems hours or days later.
**Target Buyer:** Field supervisor / revenue accountant / accounts receivable manager
**Automation Potential:** High — Field tickets follow a predictable structure (date, well name/API number, service description, hours, equipment, materials) that is well-suited to OCR and structured extraction.

## What Makes This a Distinct Niche
The field ticket is the atomic unit of revenue in oilfield services — every pumping job, wireline run, chemical treatment, and equipment rental is documented on a field ticket that the operator's company man signs at the wellsite. Despite being the basis for billions of dollars in annual invoicing, the majority of these tickets are handwritten on paper forms in harsh field conditions (mud, grease, rain, poor lighting). The handwriting is often illegible, service codes are inconsistent, well identifiers are abbreviated differently by each tech, and the carbon copies degrade. When these tickets reach the back office 1-3 days later, revenue accountants spend hours deciphering them, calling field techs for clarification, and resolving discrepancies against purchase orders. The result is delayed invoicing (average 15-30 days), billing disputes ($2-4B annually industry-wide), and incomplete maintenance histories.

## Current Tools & Gaps
FieldFX (now part of ServiceMax) offers tablet-based digital field ticketing, but adoption is limited by poor cellular connectivity at remote wellsites, field tech resistance to typing on tablets with gloved/greasy hands, and the cost of equipping every truck. OpenInvoice handles the invoice matching side but requires structured digital input it rarely receives. Generic OCR tools (Adobe, ABBYY) cannot parse the domain-specific abbreviations, well identifiers, and service codes unique to oilfield tickets.

## Problems
- [[niches/oil-gas-field-services/field-ticket-digitization/build|🔨 Build: Oilfield-Specific Handwriting OCR with Domain Vocabulary]]
- [[niches/oil-gas-field-services/field-ticket-digitization/buy|🛒 Buy: Digital Field Ticketing for Disconnected Wellsites]]
- [[niches/oil-gas-field-services/field-ticket-digitization/fix|🔧 Fix: Field Ticket to Invoice Reconciliation Pipeline]]
