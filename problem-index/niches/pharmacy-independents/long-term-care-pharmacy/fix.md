# Medication Pass Timing Optimization for Nursing Workflow

**Niche:** [[niches/pharmacy-independents/long-term-care-pharmacy/profile|Long-Term Care Pharmacy]]
**Industry:** [[industries/pharmacy-independents|Independent Pharmacies]]
**Type:** Fix (Pain Point)
**One-liner:** Blister cards are organized alphabetically by resident name, but nurses perform medication passes by room number and administration time — forcing them to sort through 30-50 blister cards per pass to find the right medications for each resident at each scheduled time.
**Tags:** #optimization-fundamentals #feature-engineering #worker-facing #automation #workflow-orchestration

## The Problem
A medication pass in a 40-bed nursing unit takes 60-90 minutes because the nurse must: pull the correct blister card from the medication cart (organized alphabetically), verify the resident identity, punch out the medications for the current administration time, administer them, document administration in the eMAR, and move to the next room. The alphabetical organization means the nurse for rooms 201-220 must search through cards for all 40 residents to find her 20, then within each card locate the correct time slot. During the 8am pass (the busiest, with 70-80% of medications scheduled), a nurse handling 20 residents touches 20+ blister cards and punches out 60-100 individual medication doses. The current packaging does not optimize for the nurse's physical workflow — it optimizes for the pharmacy's production workflow (alphabetical is easiest to package and verify).

## Why It's Still Broken
Pharmacies know that room-number-based organization would help nurses, but it creates a significant challenge for the pharmacy: room assignments change when residents transfer, are hospitalized, or new residents are admitted to empty beds. An alphabetical system is stable regardless of room changes. Implementing room-based packaging requires the pharmacy to maintain real-time census data with room assignments — information that changes multiple times per week and is not reliably communicated. Additionally, packaging equipment is optimized for sequential production runs (all of Resident A's cards, then Resident B's), not for grouping by room and administration time.

## What a Fix Looks Like
A packaging optimization system that receives real-time room assignment data from the facility (via PointClickCare integration or a simple facility-facing update interface) and generates medication cart loading maps that organize blister cards by nursing station, room number, and administration time — even if the cards themselves are produced alphabetically. The pharmacy produces cards in their optimal production sequence, but includes a sorting guide with each delivery: "Room 201 - 8am pass: pull cards for Johnson (slot 3), Martinez (slot 7)." For pharmacies with advanced packaging equipment, the system generates production sequences that group by room-and-time, with automatic re-sequencing when room assignments change. The nurse receives a cart with medications pre-sorted for their assigned rooms and current pass time.

## Who Feels the Pain
The floor nurse spending 60-90 minutes per medication pass (4 passes per shift = 4-6 hours of a 12-hour shift) physically searching for the right blister cards, and the DON (Director of Nursing) who can't reduce medication pass time without pharmacy packaging changes.

## Impact If Fixed
Reduces medication pass time by 20-30% (saving 15-25 minutes per pass, or 1-1.5 hours per nursing shift) by eliminating the search-and-sort step. Reduces medication administration errors caused by pulling the wrong blister card from an alphabetically organized cart — a category of error responsible for 5-10% of LTC medication incidents. Strengthens the pharmacy's facility contract by directly improving nursing workflow efficiency.
