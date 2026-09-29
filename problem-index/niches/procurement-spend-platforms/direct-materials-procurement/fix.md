# Tooling Ownership in a Spreadsheet

**Niche:** [[niches/procurement-spend-platforms/direct-materials-procurement/profile|Direct Materials Procurement]]
**Industry:** [[industries/procurement-spend-platforms|Procurement & Spend Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A manufacturer owns tooling sitting in suppliers' factories worth a great deal of money, and the record of what exists, where it is, what condition it is in and who owns it is a spreadsheet maintained by whoever last cared.
**Tags:** #descriptive-statistics #evaluation-metrics #confidence-intervals #compliance #data-integration #workflow-orchestration #automation #revenue-impact
**Contested on:** Every serious competitor in direct materials software is fighting to get an engineering change into sourcing before it reaches production — and whoever closes the loop between design and supply takes the manufacturer.

## The Problem
A manufacturer decides to move a part to a second supplier for resilience. The question of whether it owns the tooling, where that tooling physically is, whether it is in a condition to be moved, how many cycles it has run against its rated life, and whether the contract permits removal turns out to have no authoritative answer. The tooling was paid for across several purchase orders over a decade; the ownership terms are in three different contracts; the physical location is known to a former engineer; and the condition is whatever the incumbent supplier says. The move takes nine months and costs more than the tooling did, and the resilience it was intended to create does not arrive.

## Why It's Still Broken
Tooling is an asset that lives at a supplier's site, which fits neither the fixed asset register nor the inventory system, so it ends up in a spreadsheet. It is acquired incrementally through purchase orders rather than as a capital project, which means no single record is created. And its importance is invisible until a supplier change, a supplier failure or a dispute, at which point the absence of a record is the binding constraint — which is exactly the moment it is most expensive to reconstruct.

## What a Fix Looks Like
Make tooling an asset record with a lifecycle. Every tool created with an identity, linked to the parts it produces, the purchase orders that funded it, the contract clauses that establish ownership and removal rights, its physical location, its rated life and its cycle count. Condition and cycle count updated periodically, which requires asking the supplier — a request that is entirely reasonable, is rarely made, and is far easier to make routinely than in the middle of a transition. Ownership and removal terms extracted from the contracts and attached, so the answer to "can we move this" is a field rather than a legal review. Amortisation tracked, since tooling cost recovered through piece price is a common arrangement whose completion nobody monitors and which occasionally means a buyer pays for the same tool twice. And the resilience view: which parts depend on tooling the manufacturer does not own or cannot move, which is a concentration risk of exactly the kind the supplier risk niche is about and is invisible in every risk assessment that looks only at suppliers.

## Who Feels the Pain
Supply chain teams discovering during a crisis that they cannot move production; finance carrying assets it cannot locate; and the manufacturer's resilience posture, which assumes a flexibility the tooling position does not support.

## Impact If Fixed
A tooling register with ownership terms attached converts a nine-month archaeology exercise into a query at exactly the moment speed matters most. The resilience finding is the one with the broadest value: a substantial share of apparent dual-sourcing options turn out to be unavailable because of tooling, and no risk assessment currently checks.
