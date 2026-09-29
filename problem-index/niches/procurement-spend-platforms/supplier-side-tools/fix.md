# The Small Supplier Chasing Payment

**Niche:** [[niches/procurement-spend-platforms/supplier-side-tools/profile|Supplier-Side Tools]]
**Industry:** [[industries/procurement-spend-platforms|Procurement & Spend Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A small supplier's invoice is somewhere in a buyer's approval process, the supplier cannot see where, and the only mechanism available is telephoning an accounts payable line — which is how a solvent small business ends up with a cash flow problem.
**Tags:** #descriptive-statistics #survival-analysis #evaluation-metrics #confidence-intervals #workflow-orchestration #automation #worker-facing #revenue-impact
**Contested on:** Every serious competitor building for suppliers is fighting to let a small supplier transact with a large buyer without absorbing the buyer's process cost — and whoever reduces the supplier's cost of being a supplier takes the network.

## The Problem
A supplier invoices a large customer on net-45 terms. Sixty days later nothing has arrived. They call accounts payable, who cannot see the invoice, because it is sitting unapproved with a manager who has been travelling and who is the only person who can confirm receipt. Nobody in the buyer's organisation knows this, because nothing surfaces an invoice stalled in approval as a problem — the metric that exists is days payable outstanding, and a stalled invoice improves it. The supplier, who has payroll, borrows or delays their own suppliers. The buyer's process caused a financing cost at a business far less able to carry it.

## Why It's Still Broken
Approval delay is invisible to the buyer because nobody owns invoice cycle time, and it is quietly beneficial to working capital metrics, which is an uncomfortable observation and a real one. Supplier visibility into approval status is not provided because it would surface exactly this, and because the portals were built to receive invoices rather than to report on them. And the affected suppliers have no leverage: a small business chasing a large customer's accounts payable department is not in a position to escalate.

## What a Fix Looks Like
Give the supplier the status and give the buyer the metric. Invoice status visible to the supplier at every stage — received, matched, awaiting approval by whom, approved, scheduled for payment on this date — which removes the telephone call and, more importantly, makes the stall visible. Approval ageing surfaced inside the buyer as an exception with an escalation path, because an invoice sitting with a travelling manager is a solvable problem that nobody currently sees. Report days-to-approve separately from days-to-pay, since the first is entirely within the buyer's control and is hidden inside the second. And segment the payment performance reporting by supplier size, which is the number that matters: a buyer with good average payment performance may be systematically slow with its smallest suppliers, and that is both the group least able to absorb it and the group whose participation the buyer's own small business programme is trying to increase.

## Who Feels the Pain
Small suppliers financing a large customer's approval process; accounts payable staff who cannot answer a status question; and the buyer's own supplier diversity and small business objectives, which are undermined by the payment experience.

## Impact If Fixed
Status visibility removes the chasing and converts an invisible delay into a managed exception. Reporting days-to-approve separately from days-to-pay, segmented by supplier size, is the measurement that would let a buyer see what its process costs its smallest suppliers — which is a number no large organisation currently computes and most would want to know.
