# A Tenancy Record the Resident Can Actually Read

**Niche:** [[niches/proptech-platforms/resident-facing-tools/profile|Resident-Facing Tools]]
**Industry:** [[industries/proptech-platforms|Proptech Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The operator holds a complete record of a tenancy and shows the resident a pay button, so every question a renter has about their own housing is answered by telephoning the person who is least available to answer it.
**Tags:** #large-language-models #bert #evaluation-metrics #confidence-intervals #workflow-orchestration #compliance #worker-facing #automation
**Contested on:** Every serious competitor building resident-facing software is fighting to let a renter answer a question about their own tenancy — what they owe, what was fixed, what their lease says, where their deposit is — without calling the office, and whoever makes the record genuinely legible to the resident takes the resident-experience market.

## The Problem
A resident sees a balance of $1,347 when rent is $1,250. There is a line item reading "MISC-CHG 62.00" and another reading "LTFEE 35.00". They do not know what either is, whether the late fee is correct given when they paid, or whether their lease permits the miscellaneous charge. They call the office during working hours, which they may not have free, and wait. Separately they want to know whether the work order for the bathroom fan is still open, and what their lease says about the guest policy, and whether the deposit from their previous unit was transferred. Every one of those facts is in the system and none of it is visible to the person it concerns.

## Why Nobody Has Built This
The buyer is the operator and the product's measured objectives are rent collection, ancillary revenue and staff efficiency, none of which obviously improve by showing a resident their full record — and one of which, ancillary fee revenue, is arguably served by opacity. There is also a genuine caution about exposing operator-side data that includes internal notes, and the right answer to that is a considered view rather than a closed portal. The result is a product category whose users are not its customers, which is the structural fact of this niche and is worth naming rather than working around.

## What to Build
A tenancy record designed for the resident. Every ledger line carries a plain-language explanation of what it is, which lease provision or event it arises from, and the date it was applied — so a balance is reconstructable rather than asserted. Maintenance shows what was reported, what was found, what was done, by whom and when, with the same history the operator sees. The lease is a searchable set of terms rather than a PDF, so a question about guests or parking is answered by asking it. Deposit status, including amount held, where, and what will happen at move-out, is visible throughout the tenancy. Notices and communications concerning the resident are visible to the resident. A question-answering layer over the record handles the phrasing, in the resident's language, which is the difference between data being present and being legible.

## Target Customer
Platform vendors competing on resident experience, operators whose site staff are consumed by status calls, and — indirectly but genuinely — residents, whose interest in this is stronger than anyone's.

## Impact If Built
Site managers and leasing agents lose a large share of their day to questions of this kind, so the operator's return is real and measurable. The resident's return is larger and less often counted: a person who can see their own housing record can check a fee, chase a repair, and plan around a deposit, none of which they can reliably do today.
