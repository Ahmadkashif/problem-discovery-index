# Licensure, Scheduling and Clinician Supply Matching

**Industry:** [[telehealth-platforms|Telehealth Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** A clinician can only see patients in states where they hold a licence, demand varies by state and hour, and matching the two is done with a rules engine and a staffing spreadsheet.
**Tags:** #convex-optimization #time-series-forecasting #gradient-boosting #confidence-intervals #optimization-fundamentals #evaluation-metrics #compliance #automation

## The Problem
Virtual care is constrained by state licensure: a clinician may treat a patient only in a state where they are licensed, which makes the supply pool for any given patient a subset of the workforce rather than all of it. Multi-state licensure is expensive and slow to acquire, and the interstate compacts that ease it cover some professions and states and not others.

The consequence is a matching problem with hard constraints and uneven supply. Demand varies by state, hour, day and season; clinician availability varies by individual; and licensure determines who can serve whom. A platform can be simultaneously over-staffed nationally and unable to serve a patient in a particular state at a particular hour.

Most platforms manage this with rules-based routing and manual staffing plans built from historical averages. The result is queues in some states and idle clinicians in others, with the mismatch absorbed as patient wait time and as clinician downtime that contractors are frequently not paid for.

Credentialing and payer enrolment add a second layer. Each clinician must be credentialed with each payer in each state, a process measured in months, and a platform's ability to serve an insured patient depends on that paperwork being complete.

## What Already Exists
Scheduling and routing systems handle licensure constraints as rules. Credentialing platforms — Medallion, Verifiable and others — automate primary source verification and payer enrolment, which is a genuine improvement on a manual process. Interstate compacts for medicine, nursing and psychology reduce but do not remove the constraint. Workforce management tooling from contact centre vendors is sometimes repurposed and fits poorly, since a clinician is not interchangeable with another clinician in the way an agent is.

## The Customisation Gap
The forecasting is the gap. State-level demand at hourly granularity is forecastable — seasonality, respiratory season, weather events, employer enrolment cycles and marketing activity all drive it — and staffing against a forecast rather than a historical average is an ordinary operations research problem that most platforms are not doing.

The licensure portfolio decision is the more interesting one. Which additional state licences to acquire for which clinicians is a capital allocation question with a computable answer: the expected value of a licence is the unserved demand it would unlock, weighted by how persistent that gap is. Platforms decide this by intuition, and licences are expensive enough for the difference to matter.

Matching should also account for clinician fit rather than only licensure and availability. Language, specialty experience, prior contact with the same patient where continuity is possible, and demonstrated outcomes on comparable presentations are all relevant and are mostly not used.

And the downtime should be visible. A contractor clinician logged on and receiving no patients is bearing the cost of a forecasting failure, and measuring paid-versus-idle time per clinician is the number that would force the staffing problem to be taken seriously.

## Impact If Solved
Licensure-constrained matching produces simultaneous queues and idle capacity, paid for in patient wait times and in clinician downtime that contractors absorb. Hourly state-level forecasting with constrained staffing optimisation addresses both, and modelling the licence portfolio as a capital decision puts evidence behind a recurring expense currently allocated on intuition.
