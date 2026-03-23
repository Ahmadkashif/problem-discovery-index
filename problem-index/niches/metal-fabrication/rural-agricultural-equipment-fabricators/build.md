# Farm Equipment Repair History and Parts Database

**Niche:** [[niches/metal-fabrication/rural-agricultural-equipment-fabricators/profile|Rural Agricultural Equipment Fabricators]]
**Industry:** [[industries/metal-fabrication|Metal Fabrication]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No system records the custom parts and repairs a rural fab shop has produced for each customer's equipment — meaning when the same farmer needs the same replacement part re-fabricated three years later, the shop rebuilds the design from scratch instead of pulling up the previous job's specifications.
**Tags:** #data-integration #automation #tacit-knowledge-ml #worker-facing

## The Problem
A rural agricultural fabricator's institutional memory lives entirely in the owner's head. Over 20-30 years, the owner has fabricated custom parts for hundreds of local farmers' equipment — replacement auger flights, custom hitch modifications, wear plates, bucket edges, livestock gate components. When a farmer calls needing the same or similar part again, the owner tries to remember what they built last time — material, dimensions, fit details. If they can't remember, they re-engineer from scratch. When the owner retires, this accumulated knowledge of every farmer's equipment and every custom part ever produced is lost entirely. The next owner starts from zero.

## Why Nobody Has Built This
Rural fab shops represent an extremely fragmented market with low technology adoption and limited willingness to pay for software. The work is too varied to catalog in a standard parts database — every piece is custom, with notes about how it was modified to fit specific equipment configurations. Building a useful system requires understanding that the database entry isn't "auger flight, 14-inch OD" but "auger flight for John Deere 7720 header auger, modified OD to 13.875 to clear the retract mechanism, 3/8 AR400 wear plate welded to leading edge per farmer request."

## What to Build
A mobile-first customer and equipment database: for each customer, record their equipment (make, model, year). For each repair or custom fabrication, capture: photos (before and after), material spec, dimensions, notes on modifications and fit details, and a searchable description. When a farmer calls about a repeat job or similar repair, the fabricator searches by customer name, equipment model, or part description and retrieves the complete previous job record. Offline-capable for areas without reliable cellular data. Simple enough to update from the shop floor in 2 minutes per job — phone photo plus a voice-to-text note.

## Target Customer
Owner-operators of rural fabrication shops serving agricultural customers, with 10-30 years of accumulated custom fabrication knowledge at risk. Approximately 8,000-12,000 shops in the US.

## Impact If Built
Preserves decades of custom fabrication knowledge that currently exists only in the owner's head. Reduces repeat job engineering time from 30-60 minutes (re-measuring, re-designing) to 5 minutes (pulling up the previous job record). Enables succession — the next owner inherits a complete database of every custom part and repair, rather than starting from zero. For a shop where repeat and similar jobs represent 30-40% of revenue, the time savings alone justify the tool.
