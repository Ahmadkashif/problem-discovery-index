# Conjunction Warnings Screened Against the Operator's Own Plans

**Industry:** [[satellite-operators|Satellite Operators]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Free and commercial screening services already send every operator its close-approach warnings; what they don't do is screen against the operator's own planned manoeuvres and covariance, so flight dynamics teams re-run every warning by hand.
**Tags:** #monte-carlo-methods #gradient-boosting #probability-distributions #evaluation-metrics #automation #workflow-orchestration #compliance

## The Problem
Every operator in low Earth orbit receives conjunction data messages (CDMs): predicted close approaches between its satellites and other objects, with a time of closest approach, a miss distance and a probability of collision. They come from the US Space Force through Space-Track, from the Office of Space Commerce's TraCSS service (62 pilot users and more than 11,000 satellites covered by mid-2026), and from commercial trackers. A large constellation sees enormous volumes: Starlink made 207,152 avoidance manoeuvres in the six months to May 2026. A mid-size constellation of a few hundred satellites still sees many high-interest events a week (estimate).

For each, a flight dynamics analyst must decide whether the warning is real. The screening service used its own orbit solution for the operator's satellite, which may be days stale and ignore a manoeuvre the operator has already planned. The covariance — the uncertainty around both objects — may be unrealistic, which makes the probability meaningless. The other object may be an active satellite whose operator is about to manoeuvre too. The analyst re-screens using the operator's own ephemeris and planned burns, judges the covariance, contacts the other operator if needed, and decides whether to plan an avoidance manoeuvre before a deadline set by orbital mechanics.

## What Already Exists
Space-Track's free screening and CDMs; TraCSS; commercial screening and tracking from LeoLabs, Slingshot, COMSPOC and ExoAnalytic; analysis software such as Ansys STK and ODTK and NASA's CARA tools and published methods; and, for big constellations, in-house automation such as Starlink's autonomous avoidance.

## The Customisation Gap
The generic services screen the catalogue. The operator needs screening of its own predicted trajectory, including planned station-keeping and orbit-raising burns, against the catalogue, with each source's covariance realism scored by its track record against later tracking. It needs its own decision thresholds and manoeuvre constraints (propellant, payload outage windows, ground contact availability). It needs a record of operator-to-operator coordination that FCC rules and the industry's best-practice commitments expect. And it needs one queue that de-duplicates the same event reported by three services with three different probabilities. Mid-size and NewSpace operators assemble this from scripts and spreadsheets.

## Impact If Solved
Screening against the operator's own plans removes most false alarms before an analyst sees them, shrinks the manoeuvre decision from hours to minutes, and lets a two-person flight dynamics team cover a growing constellation without a matching rise in avoidance burns, each of which costs propellant, payload time and satellite life.
