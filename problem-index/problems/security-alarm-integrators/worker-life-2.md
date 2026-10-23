# The Service Tech Chasing a Ghost Zone

**Industry:** [[security-alarm-integrators|Security Alarm Integrators]]
**Type:** Worker Life Changing
**One-liner:** A service technician returns for the third time to a fifteen-year-old system that false-alarms at random, with no record of what the last two techs tried, and is judged on whether the customer cancels.
**Tags:** #large-language-models #k-nearest-neighbors #hidden-markov-models #feature-engineering #tacit-knowledge-ml #worker-facing #quick-win

## The Problem
The customer has had three false alarms in a month and a fine of ~$100 from the city's alarm billing vendor. The account manager has a cancellation request on hold. The service technician gets the ticket: zone 7 trips intermittently, usually overnight. The system was installed by a dealer the company bought four years ago, the wiring runs through an unheated garage, and the panel's event buffer holds only the last few hundred events. The previous two visits replaced the motion detector and then the battery, and the notes say "replaced sensor, tested OK".

The causes of intermittent faults are a short list on paper and a long hunt in practice. They include a pinched wire that opens when the garage door vibrates, a corroded splice, condensation at a contact, a spider in a motion lens, and a wireless sensor at the edge of its range when the house's Wi-Fi mesh is busy. On fire systems, ground faults come and go with humidity. Experienced techs say they get a feel for where to look. They read the timing of trips in the central-station log, the pattern of restore times, the season and the building. Newer techs replace parts until the problem goes away or the customer gives up.

## Why It Matters to the Worker
Callbacks are the most demoralising part of the job. The tech drives back to a customer who is already angry, often unpaid for the repeat visit and sometimes docked on a callback metric, to work on a problem with no clear starting point. A ghost zone can eat half a day and still not be fixed. Senior techs end up on the phone coaching juniors through problems they solved years ago, and when they leave, that experience leaves with them.

## What a Solution Looks Like
Before the truck rolls, the tech sees the full history of the zone: every trip and restore from the central-station log plotted against time of day, temperature and other zones, every prior visit and what was replaced. It comes with ranked likely causes drawn from similar cases across the company's service history, and the test to confirm each. After the visit, the fix that actually stopped the signals is recorded against the pattern. Tickets that say "tested OK" become a searchable record of what works.

## Impact If Solved
Cutting repeat visits on intermittent faults by even a third saves the tech hours of drive time and frustration per week. It saves the account that was about to cancel, and it gives junior techs the senior's starting point instead of a parts bin.
