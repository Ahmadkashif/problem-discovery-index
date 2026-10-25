# The Shared Enclosure Charge on the Wrong Tenant

**Niche:** [[niches/waste-haulers/overage-extra-service-capture/profile|Overage & Extra-Service Charge Capture]]
**Industry:** [[industries/waste-haulers|Waste Haulers]]
**Type:** Fix (Pain Point)
**One-liner:** At strip malls and apartment blocks several accounts share an enclosure, and an overage photo is charged to whichever account the GPS point lands on.
**Tags:** #object-detection #cnns #data-integration #quick-win #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to turn what the truck camera saw into overage and extra-service charges that stick, and whoever has the lowest share of those charges credited back after dispute takes the account.

## The Problem
Truck GPS is accurate to a few metres; enclosures holding three tenants' containers are smaller than that. Charges land on the wrong account, the right customer is never told, and the wrong one disputes and wins.

## Why It's Still Broken
Container records carry an address, not an identity the camera can read, and nobody has tagged containers at shared sites.

## What a Fix Looks Like
A visible container ID (QR code, RFID or painted number) read by the camera at each lift and stored in the account record, with unmatched events held for review instead of billed by location.

## Who Feels the Pain
Tenants charged for a neighbour's overflow; billing clerks handling the disputes; reps whose accounts are irritated by fees they did not cause.

## Impact If Fixed
If shared enclosures produce ~20% of disputed overages at a typical commercial book (estimate), tagging the containers at its ~300 shared sites removes most mis-billed charges at a hardware cost of ~$2–5 per container (estimate).
