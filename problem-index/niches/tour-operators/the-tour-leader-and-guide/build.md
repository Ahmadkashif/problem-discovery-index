# A Guide Rating That Separates the Guide From the Weather

**Niche:** [[niches/tour-operators/the-tour-leader-and-guide/profile|The Tour Leader & Local Guide]]
**Industry:** [[industries/tour-operators|Tour Operators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Guides are hired, ranked and rebooked on raw survey averages that blame them for the hotel, the coach, the itinerary and the rain.
**Tags:** #bayesian-inference #linear-regression #large-language-models #bert #causal-inference #worker-facing #evaluation-metrics
**Contested on:** Every serious competitor in this niche is fighting to lock in the tour leaders and guides travellers rate highest before rival operators book their season, and whoever confirms those guides' seasons first takes the account.

## The Problem
A tour director who draws a demanding itinerary in a heatwave, with a hotel that lost rooms, scores lower than one who drew an easy route in May. Operators rank guides on these averages, offer the best days to the top of the list, and sometimes drop guides near the bottom. Guides know the measure is unfair, and good ones leave for operators that treat them better.

## Why Nobody Has Built This
Separating guide effect from everything else needs departure-level linkage of surveys to guides, suppliers, itinerary and conditions, plus enough departures per guide. Operators have the data but treat surveys as a customer-service report. Survey vendors see responses, not departures.

## What to Build
Aspect extraction from survey comments and reviews (guide, hotel, coach, meals, pacing, weather, disruption), feeding a mixed-effects model with crossed effects for guide, supplier, itinerary and conditions. Each guide gets an adjusted rating with an interval and a breakdown of strengths. The guide sees it too, with the comments that drove it. Staffing uses it to offer days. Coaching uses it to target development. Supplier management gets the hotel and coach effects free.

## Target Customer
Directors of tour operations at operators fielding a hundred or more guides and leaders a season (estimate).

## Impact If Built
Fairer allocation of the best days, better retention of top guides, and earlier detection of supplier problems that were being blamed on guides (estimate).
