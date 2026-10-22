# Conjunction Assessment & Collision Avoidance

**Parent Industry:** [[industries/satellite-operators|Satellite Operators]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in this niche is fighting to tell an operator, before the manoeuvre deadline, which of its conjunction warnings are real, and whoever does it with the fewest false alarms and no missed events takes the operator's screening account.

## Profile
**Market Size:** ~$300M a year in commercial tracking, screening and collision-avoidance services and software bought by operators (estimate; SIA put all space-sustainability revenue at ~$500M in 2025)
**Share of Parent Industry:** ~0.3% of global satellite services revenue (estimate)
**Digital Adoption:** High — warnings arrive as structured messages; the triage and coordination around them are manual at most operators
**Target Buyer:** Head of Flight Dynamics
**Automation Potential:** Very high for screening and triage; the manoeuvre decision keeps a human sign-off

## What Makes This a Distinct Niche
Low Earth orbit is crowded and getting more so: SIA counted 14,266 operational satellites at the end of 2025, and Starlink alone made 207,152 avoidance manoeuvres between December 2025 and May 2026. Every operator receives conjunction data messages from the Space Force's Space-Track, the Office of Space Commerce's TraCSS (more than 11,000 satellites covered, but on uncertain funding after the FY2027 request) and commercial trackers. Each warning has a hard deadline — the time of closest approach, less the time needed to plan and upload a manoeuvre — and most turn out to be false alarms once better data arrives. The work is mechanical, frequent and well defined, which makes it the most automatable task in satellite operations.

## Current Tools & Gaps
Space-Track and TraCSS screening; commercial services from LeoLabs, Slingshot, COMSPOC, ExoAnalytic and Kayhan; Ansys STK and ODTK; NASA CARA's published methods; Starlink's in-house autonomy. The gaps: no graded record of which data source's covariance can be trusted, duplicate warnings from several services, and operator-to-operator coordination by email.

## Problems
- [[niches/satellite-operators/conjunction-assessment/build|🔨 Build: A Covariance Realism Scorecard for Every Data Source]]
- [[niches/satellite-operators/conjunction-assessment/buy|🛒 Buy: Commercial Screening Wired to the Operator's Manoeuvre Planner]]
- [[niches/satellite-operators/conjunction-assessment/fix|🔧 Fix: Manoeuvre Coordination by Email to an Address in a Catalogue]]
