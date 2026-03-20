# Walk-In + Reservation Hybrid Table Management

**Industry:** [[independent-restaurants|Independent Restaurants]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Casual independents that are 70% walk-in and 30% reservation need table management that handles both flows without the cost or rigidity of OpenTable.
**Tags:** #markov-decision-processes #dynamic-programming #linear-regression #optimization-fundamentals #gradient-boosting #feature-engineering #workflow-orchestration

## The Problem
Most independent restaurants outside the fine-dining segment operate with a mix of walk-ins and reservations, yet the available table management tools were designed for one mode or the other. Walk-in-heavy restaurants (neighborhood bistros, ethnic restaurants, family spots) use a paper wait list or a basic iPad app that cannot handle the reservation component. Reservation-heavy tools like OpenTable charge $1-$2.50 per seated cover and are designed for a demand profile that assumes most tables are pre-booked — they perform poorly when 60-70% of covers walk in unpredictably. The host is left mentally juggling reservation holds, walk-in queue position, table turn estimates, and party size Tetris with no decision support.

## What Already Exists
OpenTable and Resy handle reservations well but charge per-cover fees that add up to $500-$2,000/month for a busy independent — a meaningful expense when net margins are 3-7%. Yelp Waitlist and Waitwhile handle walk-in queues but have minimal reservation capability. Toast Tables exists but is tightly coupled to the Toast POS ecosystem. None of these tools dynamically optimize the walk-in vs. reservation balance: how many tables to hold for reservations on a Tuesday vs. a Saturday, when to release unheld tables to walk-ins, or how to estimate wait times accurately when party sizes are mixed.

## The Customisation Gap
An independent restaurant needs a hybrid system that learns its specific walk-in/reservation ratio by day of week and season, dynamically adjusts how many tables to hold for reservations vs. release to walk-ins, provides accurate wait time estimates by incorporating real-time kitchen pace (not just table occupancy), and costs a flat monthly fee rather than per-cover. The system must handle the chaotic reality of independent dining: irregular table shapes, parties that merge or split, regulars who expect their usual table, and the owner's kid doing homework at the corner two-top.

## Impact If Solved
Hosts make better seating decisions, average table turn time drops 10-15 minutes, walk-in abandonment decreases, and the restaurant captures 5-10 additional covers per night on busy evenings — worth $200-$500 in incremental daily revenue without adding a single seat.
