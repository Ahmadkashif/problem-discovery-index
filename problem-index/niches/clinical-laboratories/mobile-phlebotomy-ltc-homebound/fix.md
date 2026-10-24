# The Missed Draw Nobody Told the Facility About

**Niche:** [[niches/clinical-laboratories/mobile-phlebotomy-ltc-homebound/profile|Mobile Phlebotomy for Nursing Homes & Home-Bound Patients]]
**Industry:** [[industries/clinical-laboratories|Clinical Laboratories]]
**Type:** Fix (Pain Point)
**One-liner:** A resident refuses or a vein can't be found at 5 a.m., and the nurse learns there is no INR result only when the physician asks for it at 10.
**Tags:** #workflow-orchestration #large-language-models #automation #worker-facing #quick-win
**Contested on:** Every serious competitor in this niche is fighting to complete each draw ordered for a nursing-home resident or home-bound patient, and whoever loses the fewest ordered draws to missed visits and recollections takes the account.

## The Problem
Draws fail for ordinary reasons: the resident refused, was at dialysis, was asleep and agitated, or had no accessible vein. The phlebotomist notes it on a sheet and moves on. The facility discovers the gap hours later and calls the lab, which then has to send someone back.

## Why It's Still Broken
There is no shared, live status between lab and facility. The phlebotomist's device, if any, feeds the lab's LIS, not the facility's EHR or the charge nurse.

## What a Fix Looks Like
The phlebotomist records the failed draw and the reason in one tap. The facility's charge nurse receives an immediate message with options: redraw later this morning, nurse-collected specimen picked up by courier, or reschedule. The response flows back into the route plan.

## Who Feels the Pain
Charge nurses chasing missing results, physicians delaying dose decisions, residents redrawn at awkward times, and phlebotomists blamed for refusals they cannot control.

## Impact If Fixed
The facility hears about a missed draw minutes after it happens instead of hours later. On ~50 failed draws a day (estimate), that turns most of them into same-morning redraws rather than next-day ones.
