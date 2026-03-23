# Prosthetic Fund Authorization Tracking and Follow-Up

**Niche:** [[niches/medical-supply-retail/veterans-dme-providers/profile|Veterans DME Providers]]
**Industry:** [[industries/medical-supply-retail|Medical Supply Retail]]
**Type:** Fix (Pain Point)
**One-liner:** VA prosthetic fund authorizations (the VA's equivalent of prior authorization) get stuck in the VA's internal approval process for weeks with no status visibility for the DME supplier — delaying equipment delivery to veterans who are waiting.
**Tags:** #automation #workflow-orchestration #compliance #worker-facing

## The Problem
Before a DME supplier can deliver equipment to a veteran, the VA's Prosthetic & Sensory Aids Service (PSAS) must issue a purchase authorization funded from the prosthetic fund. This authorization can take 3-15 business days depending on the dollar amount, the VA facility's workload, and whether the request requires additional clinical justification. The DME supplier has no visibility into where the authorization is in the VA's internal process — they submit the request and wait, calling the VA prosthetics office periodically to ask for updates. The prosthetics office may handle 200+ authorization requests per week and cannot provide individual status updates to every supplier. Meanwhile, the veteran is waiting for equipment they were told would arrive "next week."

## Why It's Still Broken
VA's internal authorization workflow runs through VistA and eCMS — systems the DME supplier cannot access for status tracking. There is no supplier-facing portal showing authorization status (pending, in review, approved, funded, or denied). Communication between the supplier and the VA prosthetics office happens via phone, fax, and secure email with no structured status update mechanism. The VA's PSAS staff are overwhelmed with requests and have no automated workflow to push status updates to suppliers. The DME supplier must allocate staff time (15-20 hours/week at a mid-size VA supplier) to call the VA for status on pending authorizations.

## What a Fix Looks Like
A prosthetic fund authorization tracker that: logs each authorization request with submission date, dollar amount, and veteran information; tracks expected approval timeline based on historical patterns (requests under $5K typically approved in 3 days, over $25K takes 10-15 days); schedules automated follow-up calls/emails at appropriate intervals; escalates stalled authorizations (beyond expected timeline) with suggested actions; and provides the veteran with status updates ("Your equipment order is in VA approval, expected authorization by Friday"). Even without VA system integration, a well-managed follow-up cadence based on historical timing patterns would eliminate 80% of the status uncertainty.

## Who Feels the Pain
DME supplier staff who spend 15-20 hours/week calling the VA for authorization status updates, and veterans who wait weeks for equipment without any communication about why it's delayed.

## Impact If Fixed
Recovers 10-15 hours/week of staff time from manual VA follow-up calls. Reduces average equipment delivery time by 3-5 days through systematic follow-up that prevents authorizations from stalling. Improves veteran satisfaction by providing status updates during the wait — the veteran knows what's happening even if the timeline hasn't changed. Demonstrates supplier responsiveness to VA prosthetics staff, strengthening the contract relationship.
