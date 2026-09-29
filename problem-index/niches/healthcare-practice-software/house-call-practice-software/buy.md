# Field Service Routing Adapted to Clinical Priority

**Niche:** [[niches/healthcare-practice-software/house-call-practice-software/profile|House-Call & Mobile Practice Software]]
**Industry:** [[industries/healthcare-practice-software|Healthcare Practice Software]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Route optimisation is a mature commodity sold to every delivery and field service business, and house-call practices schedule by hand because no routing engine understands that the fourth stop is a patient who was discharged from hospital yesterday.
**Tags:** #dynamic-programming #combinatorics-and-counting #gradient-boosting #time-series-forecasting #evaluation-metrics #optimization-fundamentals #workflow-orchestration #automation
**Contested on:** Every serious competitor selling to house-call and mobile practices is fighting to make a visit charted in a basement with no signal reconcile cleanly — right patient, right place of service, right time, no lost data — and whoever makes the offline round-trip trustworthy takes the account.

## The Problem
A house-call practice's scheduler builds tomorrow's routes in a spreadsheet with a map open in another window. She knows that the Tuesday patient in the north of the county takes forty minutes rather than twenty-five, that two patients must be seen before noon because of caregiver availability, and that the post-discharge patient added this morning has to be seen within seventy-two hours or the practice loses both the clinical window and the transitional care management code. No tool holds any of that, so it lives in her head, and the practice's capacity is bounded by one person's knowledge.

## What Already Exists
Vehicle routing is one of the most commoditised optimisation products in software. Route4Me, Onfleet, the Google and HERE routing APIs, and every field service management platform solve the travelling-salesman-with-time-windows problem well, with live traffic, at low cost. Home health agencies use scheduling tools built around visit frequency and discipline mix. None of these model the two things that decide a medical route: how long *this* patient takes, and how much it matters that they are seen today rather than Thursday.

## The Customization Gap
The adaptation is mostly in the objective function and the duration model, not in the solver. It requires: (1) a learned visit-duration estimate per patient from the practice's own history, conditioned on complexity, caregiver presence, whether the visit includes a procedure, and the clinician — because the variance between patients dwarfs the variance between routes; (2) clinical urgency as a real term rather than a priority flag, with post-discharge windows, wound-care intervals and medication-titration follow-ups expressed as deadlines with costs for missing them; (3) continuity as an explicit objective, since sending the same clinician is clinically valuable and routing engines will happily trade it away for four minutes; (4) caregiver and facility access windows as hard constraints, which is what actually makes a plan fail on the day; and (5) same-day reoptimisation when a visit runs long or a patient is not home, which is the normal case rather than the exception.

## Target Customer
House-call and home-based primary care groups with four or more clinicians in the field, mobile diagnostic providers, and the practices currently bounded by one scheduler's memory.

## Impact If Solved
Practices that replace spreadsheet routing with a duration-aware, urgency-aware engine typically fit one to two additional visits per clinician per day out of recovered drive time — which in a fee-for-service house-call practice is the whole economics of the model. Encoding the scheduler's knowledge also removes a single point of failure that every practice in this segment quietly has.
