# Build: Churn Prediction and Turnaround Scheduling

**Niche:** [[niches/rideshare-fleet-operators/utilisation-and-turnover/profile|Fleet Utilisation & Turnover]]
**Industry:** [[industries/rideshare-fleet-operators|Rideshare Fleet Operators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Predict which drivers will return the vehicle in the next fortnight and schedule the turnaround against that forecast, so the next renter starts the day after rather than the week after.
**Tags:** #survival-analysis #gradient-boosting #time-series-forecasting #confidence-intervals #evaluation-metrics #dynamic-programming #revenue-impact #automation
**Contested on:** Whether rental termination can be predicted early enough to have the next driver ready.

## The Problem

A driver hands back the keys. The operator finds out that day, or the day before. The vehicle then needs inspection, cleaning, any deferred maintenance, possibly a registration or insurance update, and a new renter who has been screened, approved by the platform and had their documents checked. That sequence, started from a standing stop, takes days to a week.

Meanwhile the vehicle finance payment, insurance and depreciation continue. A fleet of two hundred vehicles losing an average of six idle days per turnover, with turnovers every five months, is losing several percent of its annual revenue to a scheduling problem.

The information that would prevent it exists weeks earlier. Drivers who are about to stop renting behave differently first: hours decline, weekend activity drops, payments become later, communication gets shorter, mileage patterns change. These are visible in telematics and payment records and nobody looks.

## Why Nobody Has Built This

Utilisation is tracked as a lagging percentage rather than managed as a process, and the losses are distributed across many small gaps rather than concentrated in a visible event. An operator can name their default rate and usually cannot name their average turnaround time.

The prediction has not been attempted because the fleet's data has never been arranged for it. Contract histories with end dates and reasons exist in the fleet management system, telematics in another, payments in a third, and nobody has built the driver-week table that makes a survival model possible.

And the operational half — having a screened, approved renter ready on the day — requires a pipeline rather than a waiting list, which is a change in how the business is run rather than a piece of software.

## What to Build

A churn forecast feeding a turnaround schedule.

**Predict termination as a hazard.** Time-to-return with covariates from telematics (hours trend, productive fraction, daypart mix, geography), payments (days late, arrears trend, payment method changes), interaction (contact frequency, maintenance requests), and contract features (tenure, rate as a share of modelled earnings, vehicle age). Survival modelling is the right frame because the output needed is "probability this vehicle comes back in the next 14 days", not a binary label.

Distinguish the reasons, because they call for different responses. A driver leaving for a better rate elsewhere is a retention problem. A driver leaving because they cannot make the economics work is a pricing problem. A driver leaving because they got a salaried job is neither. The features separate these reasonably well, and the distinction determines whether the operator should intervene or prepare.

**Schedule the turnaround as a process with a target.** Inspection, cleaning, maintenance, documentation, platform re-approval, handover — each with a duration and dependencies, planned against the predicted return date rather than triggered by the actual one. Maintenance in particular should be pulled forward into the gap, since a vehicle that is already idle is the cheapest possible time to service it, and deferred work is a common cause of the gap extending.

**Run a renter pipeline, not a waiting list.** Prospects screened, platform-approved and document-complete ahead of time, with a predicted ready date, matched to vehicles by class and location. The screening and platform approval are the long poles and both can be done before a vehicle is available.

**Optimise the assignment.** Which renter to which vehicle, given predicted tenure, vehicle condition, maintenance schedule and location. A simple assignment optimisation over the predicted-churn and pipeline data outperforms first-come-first-served meaningfully, particularly in matching high-mileage drivers to vehicles nearer a service interval.

**Measure idle days by cause.** Awaiting renter, awaiting maintenance, awaiting documentation, awaiting recovery, awaiting repair parts. Most operators have no idea which category dominates, and the answer determines where the effort goes.

## Target Customer

Fleet operators from roughly thirty vehicles upward, where turnover is continuous enough for a forecast to be actionable. Also the fleet management software vendors, for whom churn prediction and turnaround scheduling are a natural and absent module in products that already hold the contract and vehicle data.

## Impact If Built

Idle days fall because the next renter is ready when the vehicle is, which converts directly to revenue on a cost base that does not change. Maintenance moves into gaps that were happening anyway. And the operator learns which of their turnovers are retention failures and which are economics failures — two problems currently indistinguishable and requiring opposite responses.
