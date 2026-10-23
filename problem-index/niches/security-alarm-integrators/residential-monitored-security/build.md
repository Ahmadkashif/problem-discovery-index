# A Departure Signal for Every Monitored Home

**Niche:** [[niches/security-alarm-integrators/residential-monitored-security/profile|Residential Monitored Security & Smart Home]]
**Industry:** [[industries/security-alarm-integrators|Security Alarm Integrators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A home security account signals its departure months ahead in how the panel is used, and no dealer turns that into a ranked list in time to act.
**Tags:** #survival-analysis #gradient-boosting #feature-engineering #causal-inference #evaluation-metrics #revenue-impact #data-integration
**Contested on:** Every serious competitor in this niche is fighting to keep a monitored home paying through its contract term, its owner's move and the next communicator sunset, and whoever holds gross attrition lowest for each dollar spent acquiring the account takes the account.

## The Problem
Retention desks work accounts that have already decided: cancellation requests, 60-day past-dues, contracts ending next month. The earlier evidence sits in systems the desk never sees. Arming frequency falls for months before a cancellation. Trouble signals go unresolved, false alarms bring a city fine, communicators fail after a carrier cutover, and a house appears on a listing site.

## Why Nobody Has Built This
The data is split three ways. The signal log sits with the central station, which is often a wholesale provider. Billing and contracts sit with the dealer, and app engagement sits with the interactive platform. Dealers buy software by function, and no vendor owns all three. The large dealers that hold everything in-house have treated attrition as a finance metric rather than a modelling problem.

## What to Build
An account-level survival model with time-varying covariates: arming trend, trouble backlog, false-alarm count and fines, communicator type and sunset date, service visits, payment pattern, contract term and renewal terms, and listing or change-of-address signals. It outputs a 90- and 180-day cancellation hazard with the drivers named. On top sits an uplift layer that learns which action works for which driver: a service visit, a fine waiver after repair, a mover offer, or a price hold.

## Target Customer
VP of retention or chief customer officer at dealers with 50,000+ accounts, and the operations heads of dealer programmes and rollups whose purchased books carry unknown attrition.

## Impact If Built
One point of gross attrition on a book with ADT's $359M of monthly RMR is about $40M of annual revenue (estimate). For a 50,000-account dealer at ~$45 a month, it is ~$270K a year of revenue and ~$0.7–1.2M of portfolio value at 30–55× RMR (estimate).
