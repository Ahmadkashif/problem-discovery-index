# The Peer-to-Peer Call Nobody Can Schedule

**Niche:** [[niches/health-insurance-carriers/utilization-management/profile|Utilization Management & Prior Authorization]]
**Industry:** [[industries/health-insurance-carriers|Health Insurance Carriers]]
**Type:** Fix (Pain Point)
**One-liner:** A pending denial can be reversed in a ten-minute conversation between the plan's medical director and the ordering physician, and the two spend days failing to reach each other.
**Tags:** #large-language-models #workflow-orchestration #automation #evaluation-metrics #quick-win
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor is fighting to decide authorization requests inside the CMS-0057-F clocks with determinations that survive appeal. But outpatient prior authorization and inpatient and post-acute concurrent review are won on different inputs, clocks, vendors and outcomes, so the niche is decomposed into contested sub-niches below.

## The Problem
When a nurse cannot approve, the case goes to a medical director, and many plans offer the ordering physician a peer-to-peer discussion before or after the determination. Scheduling runs by phone. The plan's line gives a window, the physician is in clinic, and the callback reaches a front desk. Under a seven-day standard clock, two missed rounds can push the case to a denial that a conversation would have prevented.

## Why It's Still Broken
Peer-to-peer is treated as a courtesy rather than a workflow, so nobody owns its scheduling. Medical directors work across time zones and plans, physicians' calendars are not reachable, and the case system has no field for "conversation pending".

## What a Fix Looks Like
Treat the peer-to-peer as a tracked step with its own clock. Offer the physician's office self-scheduled slots with a medical director licensed in the right specialty and state, sent with the specific missing evidence named, so the office can often send the document instead of calling. Record the outcome as a structured field, so reversal rates by criterion and medical director feed the denial ledger.

## Who Feels the Pain
Ordering physicians and their staff; medical directors with fragmented days; members waiting on surgery or imaging; UM managers watching decision times slip.

## Impact If Fixed
Fewer denials issued for want of a conversation, fewer appeals downstream, and a measured record of which pending denials a peer-to-peer reverses.
