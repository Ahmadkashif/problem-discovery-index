# Group Block Management

**Industry:** [[travel-agencies|Travel Agencies]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Destination weddings, group cruises and alumni trips are run from spreadsheets against supplier deadlines for deposits, names and releases, because event-registration tools don't understand a room or cabin block.
**Tags:** #logistic-regression #survival-analysis #time-series-forecasting #feature-engineering #workflow-orchestration #automation #revenue-impact

## The Problem
An advisor contracts a block of 40 rooms at a Riviera Maya resort for a wedding, or 25 cabins on a sailing for a church group. The supplier's contract sets a deposit schedule, a final payment date, a name-in deadline and an attrition or release date after which unsold space goes back or must be paid for. Guests book individually over months, many at the last minute, each with their own payment plan, room type, travel dates and flight. The advisor tracks who has paid what in a spreadsheet, chases guests by text, keeps the couple or the group leader informed, and decides — usually by feel — whether to release ten rooms now or hold them and risk an attrition charge.

Group work is where advisors earn the most per hour when it goes well, through group commission and tour-conductor credits (one berth per ~8-16 paid, estimate), and where they lose the most when it doesn't. Attrition allowances are typically ~10-20% of the block (estimate), and a wedding block that picks up slowly forces a choice between paying for empty rooms and releasing rooms that guests later want.

## What Already Exists
Event registration and payment tools (Eventbrite, Cvent, Jotform with Stripe) collect sign-ups and payments. Wedding-travel platforms and supplier group desks offer microsites. Agency CRMs and itinerary tools (Travefy, Axus, ClientBase) store individual bookings. Cruise lines run group programmes in their own portals with amenity points.

## The Customisation Gap
Group travel needs: block contracts as structured objects (room or cabin categories, rates, cut-off and name-in dates, attrition rules, comp ratios); per-guest payment plans that roll up to the supplier's deposit schedule; a pickup curve compared against how similar groups filled; reminders and payment links tied to the supplier's deadlines rather than to the event date; name and document collection in the formats each supplier demands; and a release recommendation before the cut-off. Registration tools see attendees, not inventory obligations; supplier portals see their own block, not the guests' payment status; CRMs see bookings, not the block.

## Impact If Solved
For an advisor running ~10-20 group blocks a year (estimate), cutting attrition payments and last-minute releases, and removing the weekly spreadsheet reconciliation, returns several thousand dollars of commission and ~5-10 hours a week in peak season (estimate).
