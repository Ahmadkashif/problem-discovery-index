# The Late Name Change That Never Reached the Hotel

**Niche:** [[niches/tour-operators/rooming-lists-manifests/profile|Rooming Lists, Manifests & Supplier Reconfirmation]]
**Industry:** [[industries/tour-operators|Tour Operators]]
**Type:** Fix (Pain Point)
**One-liner:** A traveller cancels or changes room-mate after the rooming list went out, the reservation system updates, and the hotel never hears.
**Tags:** #workflow-orchestration #automation #data-integration #quick-win #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to get every hotel, coach company, restaurant and guide the final names, rooms, numbers and needs without a discrepancy on arrival, and whoever delivers the most departures with zero arrival-day manifest errors takes the account.

## The Problem
Rooming lists are sent at the supplier's deadline. Changes keep coming: cancellations, share changes, a late single, a spelling correction. Each must be re-sent to every affected supplier, from the next hotel to the last. Coordinators update the booking and forget one of the six hotels.

## Why It's Still Broken
The reservation system records the change but does not know which documents have already been sent and to whom. Re-sending is a manual decision.

## What a Fix Looks Like
Every outgoing supplier document is versioned against the departure. Any change that affects a document already sent automatically produces a corrected version for each affected supplier and a confirmation request. It stays on the coordinator's list until confirmed.

## Who Feels the Pain
Coordinators blamed for missed changes, tour directors fixing rooms at reception, and travellers sharing with the wrong person.

## Impact If Fixed
Late changes reach every supplier the same day, removing one of the commonest arrival-day failures.
