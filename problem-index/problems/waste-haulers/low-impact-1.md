# Overage Charges That Survive a Dispute

**Industry:** [[waste-haulers|Waste Haulers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Haulers already have cameras that see every overfilled commercial container; turning those images into overage and extra-service charges that meet each franchise's notice and evidence rules is still a manual, dispute-prone billing job.
**Tags:** #cnns #object-detection #large-language-models #evaluation-metrics #workflow-orchestration #compliance #revenue-impact

## The Problem
A commercial customer pays a monthly rate for a container of a given size emptied on given days. When the lid will not close because bags are piled on top, the driver dumps the extra and the contract allows an overage charge; when the customer calls for an unscheduled lift, there is an extra-service charge; when a recycling container is full of trash, there may be a contamination fee. Historically the driver noted these on a paper route sheet or tapped a button on the tablet, and a billing clerk decided what to charge. Many were never billed. Safe Fleet's WasteVision AI says overflows occur on 8–12% of commercial bins while haulers typically charge for ~1% of lifts (search summary; a vendor claim in sponsored content). When charges are billed without evidence, customers dispute them, sales reps credit them back to protect the account, and some end up in court.

The evidence standard is now being set by litigation and contracts. A 2025 class settlement in northern Nevada requires WM to give each customer one warning a year before any overage fee, to email notice with photo documentation within 24 hours, to wait seven days between warning and fee, to keep a three-hour service window, never to charge overages after its own missed pickups, and not to pay drivers incentives tied to overage fees, for ten years. Each franchise agreement and city ordinance has its own definitions and caps, so the same image can be a billable overage in one city and a warning-only event in the next.

## What Already Exists
On-truck cameras with AI detection: AMCS Vision AI, Safe Fleet's WasteVision AI, Prairie Robotics, Terex's 3rd Eye and WM's in-house Smart Truck; Compology's in-container cameras under RoadRunner Recycling. Hauler billing systems (Soft-Pak, Routeware, AMCS, Hauler Hero, Cairn) can post a charge if someone keys it. Fleet video platforms such as Lytx and Samsara capture footage for safety, not billing.

## The Customisation Gap
The camera vendors detect an overfilled container; they do not decide whether that event may be billed. The hauler-specific logic is: the customer's contract container size and service days; the franchise or ordinance definition of an overage and any fee cap; whether the customer has had this year's warning; notice timing and channel; whether the hauler missed the previous scheduled pickup, which voids the charge; matching the image to the right container at a multi-tenant enclosure; and a recurring-overflow rule that recommends a larger container or an extra pickup instead of charging the same customer every week. The workflow also needs a dispute path in which the photo, the contract clause and the notice history appear in one record a customer service rep can show. That logic sits between the camera feed and the billing system, and neither vendor builds it per franchise.

## Impact If Solved
A hauler servicing ~10,000 commercial containers twice a week makes ~1M lifts a year; billing two more points of overflowing lifts at ~$25–50 each is ~$0.5–1M a year (estimate), and documented, rule-compliant charges cut the credits sales reps give back and the exposure that produced the Nevada settlement's $2.2M fee award.
