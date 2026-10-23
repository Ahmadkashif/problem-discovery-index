# The Cancellation That Needs a Phone Call

**Niche:** [[niches/travel-agencies/mid-market-self-service-booking/profile|Mid-Market Self-Service Booking Adoption]]
**Industry:** [[industries/travel-agencies|Travel Agencies]]
**Type:** Fix (Pain Point)
**One-liner:** A traveller cancels a trip online, the airline credit or refund disappears into a queue, and finance never learns how much unused ticket value it is holding.
**Tags:** #large-language-models #evaluation-metrics #workflow-orchestration #automation #quick-win
**Contested on:** Every serious competitor in this niche is fighting to get a growing company's employees to book and change their own trips in the tool without calling an agent, and whoever keeps the highest share of trips booked and serviced touchless takes the account.

## The Problem
When a trip is cancelled, the ticket may be refundable, voidable within the day, or convertible to a credit tied to the traveller's name and the airline. Self-service tools often void or cancel correctly but leave credits untracked, so they expire unused and the company pays again for the next trip.

## Why It's Still Broken
Unused-ticket credits live in airline and GDS records, not in the booking tool's front end; the rules differ by airline and fare; and reapplying a credit on the next booking requires the agent to notice it.

## What a Fix Looks Like
Track every unused credit by traveller, airline and expiry; apply it automatically at the next eligible booking; warn finance and the traveller before expiry; and report the company's outstanding credit balance monthly.

## Who Feels the Pain
Finance directors paying twice; travellers who don't know they hold a credit; TMC agents asked to find it.

## Impact If Fixed
Unused credits become a tracked asset rather than a silent loss, and one more reason to call an agent disappears.
