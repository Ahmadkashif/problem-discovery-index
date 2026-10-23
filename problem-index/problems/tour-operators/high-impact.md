# The Departure Call Made by Feel

**Industry:** [[tour-operators|Tour Operators]]
**Type:** High Impact
**One-liner:** A small group of operations managers decide, by reading booking curves from memory, which departures to guarantee, consolidate or cancel and which rooms, coaches and guide days to give back. Every one of those decisions is a dated prediction whose outcome the operator never records beside it.
**Tags:** #tacit-knowledge-ml #survival-analysis #bayesian-inference #gradient-boosting #time-series-forecasting #dynamic-programming #revenue-impact

## The Problem
An escorted or small-group operator runs dozens to hundreds of departures of each itinerary a season. Each departure carries commitments made months earlier, typically:
- a hotel allotment in each overnight city, with a release date;
- a coach and driver;
- a tour director and local guides booked for those days;
- rail, boat or flight space;
- restaurant and attraction blocks.

The itinerary has a minimum number of travellers below which the departure loses money, and a maximum the coach, the boat or the experience can carry. Bookings arrive unevenly, early for peak dates and late for shoulder months, in bursts after a promotion or an advisor's group sale.

At fixed checkpoints, ~90, 60 and 45 days before departure (estimate), an operations or product manager reviews every departure. For each one they decide whether to guarantee it so advisors can sell it with confidence, or consolidate it into a neighbouring date and move the booked travellers. The other options are to cancel it for failing to reach minimum numbers, or to leave it open another two weeks. In the same review they decide which rooms to release before each hotel's cut-off, whether to ask for more, and whether the second coach is still needed.

Experienced managers are good at this, and they cannot say exactly why. They know a June departure of one itinerary always fills in the last six weeks while the same itinerary in September stalls at twelve. They know one advisor consortium books its groups late, and that a booking pace that looks fine in March is a warning in May. They know which hotels will extend a release date if asked and which will not. That pattern recognition is the margin of the season. It is also undocumented. The bookings, the supplier invoices and the cancellation refunds are all recorded. The decision taken at each checkpoint, and the reason for it, is not.

## Why It's Unsolved
The data collection problem is that the expert's decision has to be captured as it is made. Departure reviews happen in a spreadsheet or a meeting, under time pressure, across hundreds of departures. The reservation system records bookings over time, and the contracting spreadsheet records allotments and release dates. The decision to hold, release, guarantee or cancel lives in an email to a hotel, a note in a cell, or nowhere. Reconstructing history means joining booking snapshots, supplier correspondence and cancellation records that were never designed to be joined.

The labelling problem is selection and disagreement. A departure that was cancelled never shows whether it would have filled. A room that was released never shows whether it would have sold. The label is censored exactly where the decision was taken. Experts also disagree with themselves. The same manager guarantees a borderline departure after a strong season and cancels it after a weak one, and two managers reviewing the same curve often split. The honest labels are the final load of departures that were left open, the penalty paid on rooms held too long, and the bookings turned away for lack of space. Each has to be weighed against what the decision cost.

The deployment problem is speed and trust. A forecast that arrives after the 60-day review is useless. One that cannot explain itself in the manager's terms ("pace is behind the same week last year, and the consortium group has not named its travellers") will be overruled. It must be faster than the manager scrolling the booking report, and it must handle the many itineraries with only a few seasons of history. It also has to respect promises already made: a guaranteed departure runs at any load, so a model that pushes guarantees too early turns its errors into losses.

## What a Solution Looks Like
A departure ledger first and a model second. Every departure carries a timeline of bookings, holds, commitments and their release or penalty dates. At each checkpoint the system records the decision the manager took, captured in one click as part of the review rather than written afterwards. It also records the final outcome: load at departure, penalties paid, rooms released, bookings declined and margin.

On top of the ledger, a booking-curve model learns each itinerary-season's pattern of arrivals. It borrows strength across similar itineraries and markets where history is thin, and reports the probability that a departure reaches minimum and its expected final load with a range. A second layer turns those forecasts into recommendations at each supplier's cut-off: release this many rooms in Florence, keep the second coach, guarantee this date now, consolidate these two. The expected margin of each choice is shown next to the manager's own call. Over a season, the ledger grades both the model and the managers against what happened, so the firm learns where the expert's read beats the model and where it does not.

## Impact If Solved
For a mid-sized escorted operator running a few thousand departures a year, earlier and better calls change the season's margin in three places. Penalties fall on rooms and seats held past their cut-off, fewer late cancellations disappoint travellers and advisors, and fewer bookings are turned away on dates released too early. A swing of a point or two of gross margin (estimate) is plausible on a business that typically earns ~15-25% gross (estimate). The decision record also survives the departure of the manager who used to carry it in their head.
