# Utilisation, Turnover and Vehicle Allocation

**Industry:** [[rideshare-fleet-operators|Rideshare Fleet Operators]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** A vehicle idle between renters earns nothing and depreciates anyway, and the gap between one driver leaving and the next starting is managed by whoever answers the phone.
**Tags:** #survival-analysis #gradient-boosting #time-series-forecasting #convex-optimization #confidence-intervals #evaluation-metrics #optimization-fundamentals #revenue-impact

## The Problem
Fleet economics are utilisation economics. Each vehicle has a fixed monthly cost — finance, insurance, depreciation, compliance — and earns only while rented. Turnover is high in this business: drivers try rideshare and stop, move markets, buy their own vehicle, or are deactivated by a platform, and each departure leaves a vehicle idle until the next renter is found and onboarded.

The idle period is managed reactively. A driver returns a vehicle, the operator starts looking, and onboarding — documentation, platform approval, background check, insurance, deposit — takes days to weeks during which the asset earns nothing. Nobody forecasts which drivers are about to leave, although the signals are visible: declining hours, falling mileage, late payments, reduced app activity.

Allocation is similarly ad hoc. Which vehicle to give which driver is decided by what is available rather than by fit — an electric vehicle to a driver without home charging is a poor match, a large vehicle to a driver doing short urban trips wastes fuel, and a high-mileage vehicle given to a heavy user accelerates its way out of the fleet.

And fleet composition decisions — how many vehicles, of what type, in which market — are made on intuition and a spreadsheet, in a business where the capital commitment is large and the exit is slow.

## What Already Exists
Rental management software handles agreements, billing, deposits and returns. Telematics provides utilisation and mileage. Platform-affiliated programmes assist with driver onboarding and approval. Vehicle remarketing channels exist for fleet disposal. General fleet management tools offer utilisation reporting, usually as a retrospective dashboard rather than as a forecast.

## The Customisation Gap
Churn prediction is entirely absent and entirely feasible. Hours driven, trips completed, mileage trend, payment timeliness and communication responsiveness are all observable, and a driver about to stop is identifiable weeks in advance. That lead time is the difference between a scheduled handover and a fortnight of idle asset, and it also creates the opportunity to intervene — a rate adjustment, a vehicle swap, a conversation — before the driver leaves.

Onboarding duration is predictable and compressible. The steps have known distributions and known failure points; forecasting a start date and identifying which documents will cause a delay lets the pipeline be managed rather than watched.

Allocation is a matching problem with real structure: driver home charging access, typical trip profile, market, expected hours and vehicle characteristics including current mileage and remaining component life. Matching on fit rather than availability improves both parties' economics and extends vehicle life.

And fleet composition should be modelled. Expected utilisation, revenue and total cost of ownership by vehicle type and market, with the electric versus internal combustion comparison done on actual fleet data rather than on manufacturer claims, is the analysis behind the largest capital decisions these businesses make.

## Impact If Solved
Idle days are pure loss on an asset with a fixed cost, and they are produced by departures nobody forecast and onboarding nobody managed. Churn prediction with weeks of lead time, forecast onboarding with delay causes identified, and fit-based allocation address the three components of utilisation directly — and fleet composition modelling puts evidence behind capital decisions currently made on intuition.
