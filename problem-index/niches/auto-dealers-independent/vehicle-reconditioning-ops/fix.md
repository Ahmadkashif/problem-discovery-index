# Vendor Coordination and Vehicle Location Tracking

**Niche:** [[niches/auto-dealers-independent/vehicle-reconditioning-ops/profile|Vehicle Reconditioning Operations]]
**Industry:** [[industries/auto-dealers-independent|Independent Auto Dealers]]
**Type:** Fix (Pain Point)
**One-liner:** Recon managers spend 1-2 hours daily texting and calling vendors to check on vehicle status and location because there's no shared system for tracking which cars are where and what's done.
**Tags:** #automation #workflow-orchestration #worker-facing #quick-win

## The Problem
On any given day, a dealer might have 15 vehicles in reconditioning spread across 5 locations: 3 at the on-site mechanic, 2 at the body shop down the street, 4 at the detail shop across town, 1 at the tire shop, and 5 waiting in queue. The recon manager's morning routine is a round of texts and phone calls: "Hey Joe, is the Camry done?" "Mike, when will the F-150 be ready?" "Tony, did you pick up the Accord?" This takes 1-2 hours daily and produces unreliable answers — vendors say "tomorrow" and mean "next Thursday." When a customer asks about a specific vehicle, the sales manager has to track down the recon manager who has to call the vendor to find out if it's ready.

## Why It's Still Broken
External vendors have no incentive to update a dealer's tracking system — they manage their own workload across multiple clients and communicating status to each client is an administrative burden they avoid. Building a system that vendors will actually use requires extreme simplicity: a vendor who responds to a text with "DONE" or a photo of the completed work is realistic; a vendor who logs into a portal daily is not. Most recon tracking tools assume internal staff who can be compelled to use the system — external vendors cannot.

## What a Fix Looks Like
An SMS/WhatsApp-based vendor update system: each morning, the system auto-texts each vendor a list of their active vehicles with a one-tap status update request ("Reply 1 if the 2018 Camry VIN#1234 is done, 2 if still in progress, 3 if you need parts"). Vendor responses auto-update the recon dashboard. If no response by noon, an automatic follow-up fires. The recon manager sees a real-time board showing all vehicles, their location, status, and elapsed time — without making a single phone call.

## Who Feels the Pain
Recon managers who spend 1-2 hours every morning on vendor status calls, and sales managers who cannot answer customer questions about vehicle availability because recon status is unknown.

## Impact If Fixed
Recovers 5-10 hours/week of recon manager time. Reduces average recon cycle time by 1-3 days by eliminating "forgotten" vehicles sitting completed at vendor locations. Enables accurate frontline availability dates for customers, reducing the "it should be ready tomorrow" disappointment cycle that loses sales.
