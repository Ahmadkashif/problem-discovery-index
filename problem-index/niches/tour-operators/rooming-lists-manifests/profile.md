# Rooming Lists, Manifests & Supplier Reconfirmation

**Parent Industry:** [[industries/tour-operators|Tour Operators]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in this niche is fighting to get every hotel, coach company, restaurant and guide the final names, rooms, numbers and needs without a discrepancy on arrival, and whoever delivers the most departures with zero arrival-day manifest errors takes the account.

## Profile
**Market Size:** ~$250M of operations coordinator time and tooling spent preparing, sending and checking supplier documents (estimate)
**Share of Parent Industry:** ~3% of the ~$9.0B employer receipts (estimate)
**Digital Adoption:** Low. Documents are generated from the reservation system, then sent, corrected and confirmed by email in each supplier's format
**Target Buyer:** Operations manager at a multi-day, group or educational operator
**Automation Potential:** Very high

## What Makes This a Distinct Niche
Every multi-day departure needs supplier documents:
- rooming lists for each hotel;
- passenger manifests for coaches, boats and trains;
- dietary and accessibility lists for restaurants;
- named tickets for attractions and transport;
- a dossier for the tour director.

Each supplier has its own deadline and format, and every booking change after a document has gone out means a correction and a new confirmation. At peak season a coordinator runs hundreds of these threads at once (estimate). The output is mechanical and checkable: the names and rooms either match on arrival or they do not. That makes it the most automatable work in the industry. The neighbouring charter-coach version, coordinating hotels and restaurants on multi-state coach tours, is logged as a fix under [[niches/charter-bus-operators/multi-day-tour-operators/fix|Vendor Coordination Across Multi-State Routes]].

## Current Tools & Gaps
Reservation and tour-operations systems export rooming lists; email and spreadsheets do the rest; a few hotel groups take lists through group portals. Gaps: supplier confirmations are read by eye, changes after sending are tracked from memory, and discrepancies surface on arrival.

## Problems
- [[niches/tour-operators/rooming-lists-manifests/build|🔨 Build: Confirmations Read and Compared Automatically]]
- [[niches/tour-operators/rooming-lists-manifests/buy|🛒 Buy: EDI-Style Document Exchange for Hotels and Ground Suppliers]]
- [[niches/tour-operators/rooming-lists-manifests/fix|🔧 Fix: The Late Name Change That Never Reached the Hotel]]
