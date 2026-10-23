# Measured Accessibility Records for Rooms, Cabins and Transfers

**Niche:** [[niches/travel-agencies/accessible-travel-specialists/profile|Accessible Travel Specialists]]
**Industry:** [[industries/travel-agencies|Travel Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Supplier accessibility data is a checkbox, while a wheelchair user needs door widths, bed heights and shower thresholds that only specialist advisors collect, one property at a time.
**Tags:** #tacit-knowledge-ml #cnns #object-detection #large-language-models #evaluation-metrics #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to verify that a room, cabin, transfer or excursion is actually usable for a specific traveller's disability before departure, and whoever's verification holds up on arrival most often takes the account.

## The Problem
A specialist advisor booking a power-chair user into a Lisbon hotel asks the property for photos and measurements of the specific room type, checks the bathroom from the photos, confirms the transfer vehicle has a ramp, and still worries. The knowledge of what to look for in a photo — the lip on the shower, the space beside the bed, the step at the entrance — is the specialist's skill, built over years and rarely written down.

## Why Nobody Has Built This
The market looks small to booking platforms, measurement requires someone on site, and suppliers prefer a checkbox to a measurement that might disqualify the room.

## What to Build
A measured accessibility record: structured fields (door width, bed height, turning space, shower type and threshold, entrance steps) captured from photos and measurements contributed by properties, advisors and travellers, with computer vision trained on specialist advisors' annotations to read features and flag barriers in supplier photos. Each record carries its evidence and its date, and is matched against a traveller's own needs profile.

## Target Customer
Accessible-travel specialists, the hosts and consortia that want to offer the capability to all their advisors, and cruise lines and hotel groups seeking to publish credible data.

## Impact If Built
Fewer trips where the room doesn't work on arrival, faster verification for specialists, and general advisors able to serve travellers they now turn away.
