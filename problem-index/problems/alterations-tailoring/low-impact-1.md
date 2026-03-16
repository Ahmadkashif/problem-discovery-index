# Order Tracking and Workflow Management

**Industry:** [[alterations-tailoring|Alterations & Tailoring]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Project management tools exist for every other workflow, but none handle the alterations shop's unique reality — 50-200 active garments hanging on a rack with paper tickets, due dates in the tailor's memory, and no system to track which garment is at which stage (intake → marking → sewing → pressing → pickup) or notify the customer when it's ready.
**Tags:** #gradient-boosting #regression #tabular-ml #workflow-orchestration

## The Problem
An active alterations shop has 50-200 garments in various stages of completion at any given time. Each garment has a paper ticket pinned to it listing the customer name, requested alterations, due date, and price. The garments hang on a rack in roughly chronological order by due date. The tailor works through the rack based on due dates, adjusting priority when walk-in customers request rush service. There is no system to track which garments are in progress, which are waiting for second fittings, which are completed and awaiting pickup, or which are overdue. Customer inquiries ("Is my dress ready?") require the tailor to physically walk to the rack and check — interrupting active sewing. Rush orders get lost in the middle of the rack. Garments left for 30+ days without pickup accumulate, consuming rack space and creating awkward conversations.

## What Already Exists
Generic project management tools (Trello, Asana) can track tasks through stages. POS systems (Square, Clover) track transactions but not work-in-progress. iRoar and a handful of niche alterations apps exist but have minimal adoption — most were built by developers who don't understand the physical workflow (garments on racks, not tasks on screens). Dry cleaning management software (SPOT, Compassmax) handles garment tracking but is designed for high-volume standardized processing, not custom alteration work where each garment requires unique instructions.

## The Customisation Gap
An alterations workflow system needs to: (1) digitize the paper ticket with photo-based intake (snap photos of the garment and annotate alteration areas directly on the image), (2) track garments through alteration-specific stages (intake → measured/marked → in-progress → first fitting → final sewing → pressing → ready for pickup), (3) predict completion dates based on the shop's current workload, the specific alterations required, and historical completion times, (4) send automated customer notifications at stage transitions ("Your dress is ready for pickup"), (5) manage the physical reality of rack organization (suggesting optimal rack positioning by due date and work sequence), and (6) handle the customer-facing communication that currently interrupts sewing.

## Impact If Solved
Eliminates the 15-20 daily customer status inquiries that interrupt sewing, saving 1-2 hours of productive work time. Reduces missed due dates from 10-15% of orders to under 3% through proactive workload visibility. Recovers revenue from unpicked-up garments through automated reminders. Enables the tailor to accept 15-20% more work by providing clear workload visibility instead of gut-feel capacity estimation.
