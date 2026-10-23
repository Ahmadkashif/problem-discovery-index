# One Traveller Location Record From Every Source

**Niche:** [[niches/travel-agencies/traveller-tracking-duty-of-care/profile|Traveller Tracking & Duty of Care]]
**Industry:** [[industries/travel-agencies|Travel Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Traveller tracking is only as good as the itinerary feed, and the feed misses the hotel booked on a brand app, the train taken on the road and the contractor who isn't in HR.
**Tags:** #k-nearest-neighbors #bayesian-inference #large-language-models #data-integration #compliance #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to tell a company within minutes of an incident which of its people are in the affected area, including those who booked outside the programme, and whoever accounts for every traveller fastest takes the account.

## The Problem
When an incident hits a city, the security team pulls a list from the tracking platform: travellers with a TMC booking there today. It omits everyone whose hotel came from a consumer site, whose itinerary changed after ticketing, or who travels on a client's booking. The team then spends the first critical hours on email and phone confirming locations.

## Why Nobody Has Built This
Each data source belongs to someone different — TMC, card issuer, expense platform, HR system, hotel loyalty programme — and no vendor is paid to stitch them. Tracking vendors take the TMC feed as given.

## What to Build
A location resolver that fuses TMC itineraries, card and expense transactions, calendar entries, email confirmations forwarded by travellers, and app check-ins into one probabilistic record of where each person is, with a confidence score and the evidence behind it. During an incident it ranks people by likelihood of being affected and sends check-ins to the uncertain ones first.

## Target Customer
Heads of global security and travel risk managers at multinationals with frequent travel to higher-risk regions.

## Impact If Built
The affected-traveller list is complete within minutes rather than hours, the first calls go to the people most likely to need help, and the company can show its board and insurers how it knows.
