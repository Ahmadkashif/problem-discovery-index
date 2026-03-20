# HOS-Aware Load Planning

**Industry:** [[owner-operator-trucking|Owner-Operator Trucking]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Hours-of-service regulations cap driving time, but current ELD systems only count down the clock — they don't help operators plan loads around remaining hours to avoid getting stranded mid-route with an expired clock.
**Tags:** #gradient-boosting #decision-trees #feature-engineering #evaluation-metrics #cross-validation #probability-distributions #bias-variance-tradeoff #gradient-descent #compliance

## The Problem
Federal HOS regulations allow 11 hours of driving within a 14-hour on-duty window, with a mandatory 30-minute break after 8 hours and a required 10-hour off-duty reset. Owner-operators must mentally calculate whether they can complete a load — including pickup wait time, driving time, and delivery appointment — within their remaining hours. Miscalculation means parking on a highway shoulder or truck stop 50 miles short of the receiver, burning a full 10-hour reset, and potentially missing the delivery window (which triggers detention fees or load rejection). This is especially acute for operators running loads with tight appointment windows or navigating congested urban delivery zones.

## What Already Exists
ELD platforms (Motive, Samsara, KeepTruckin) display remaining drive time and on-duty time as countdown timers. Google Maps and Trucker Path provide route time estimates. Some TMS platforms used by carriers offer basic HOS feasibility checks against planned routes.

## The Customisation Gap
No current tool combines real-time HOS status with route-specific transit time predictions (accounting for truck speed limits, not car speed limits), historical dwell time at the specific shipper/receiver facility, weather and traffic delays on the planned route, and the operator's personal driving patterns (some drivers consistently run 55 mph, others run 65 mph). The system needs to answer: "If I accept this load right now, what is the probability I complete it within my remaining hours, and if not, where is the optimal point to take my 10-hour break to still make the appointment?"

## Impact If Solved
Prevents 2-3 forced roadside resets per month (each costing $200-$500 in lost productivity), reduces HOS violation risk ($16,000 maximum fine per occurrence), and gives operators confidence to accept loads closer to their hour limits — unlocking revenue they currently leave on the table out of caution.
