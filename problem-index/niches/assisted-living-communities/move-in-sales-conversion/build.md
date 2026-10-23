# Pipeline-to-Census Forecast

**Niche:** [[niches/assisted-living-communities/move-in-sales-conversion/profile|Move-In Sales & Lead Conversion]]
**Industry:** [[industries/assisted-living-communities|Assisted Living Communities]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Operators find out what next month's census will be when the move-ins happen; the sales pipeline already holds most of the answer.
**Tags:** #time-series-forecasting #gradient-boosting #survival-analysis #evaluation-metrics #revenue-impact #data-integration
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor is fighting to turn a family's search into a signed move-in. That produced two contests with different winners: which channel gets credit and a fee for the family, settled by whoever holds a first-contact record both sides accept, and what share of the inquiries it already owns the community turns into tours, won by sales teams and response tools. Decomposed into contested sub-niches below.

## The Problem
Executive directors staff the building, order food and set prices on last month's census and the sales director's optimism. Move-outs, often from death, hospital stays or a move to a higher level of care, arrive unannounced. A community that misreads its next 60 days over-schedules caregivers or, worse, runs short when three move-ins land in one week.

## Why Nobody Has Built This
CRMs report funnels; EHRs know residents' health; finance systems hold the budget. Nobody joins inquiries, tours and deposits with the acuity of current residents to forecast both move-ins and move-outs. Each operator's data is small, so the model must pool patterns across communities.

## What to Build
A weekly forecast of move-ins by care type from the pipeline (stage, source, days since inquiry, care need), and of move-outs from current residents' acuity trends, hospital stays and hospice enrolment. It outputs a 30/60/90-day census range per community, the staffing hours it implies, and the units most likely to sit empty, with the pipeline actions that would close the gap.

## Target Customer
COOs and regional VPs at chains of 10–100 communities; REIT asset managers overseeing operators under RIDEA management agreements.

## Impact If Built
Matching caregiver schedules to forecast census within ±2 residents (estimate) avoids ~2–4% of overtime and agency hours in an 80-unit building, ~$40,000–80,000 a year (estimate, against labour at ~56% of budget per Ziegler), and gives sales leaders 60 days' warning of a soft month.
