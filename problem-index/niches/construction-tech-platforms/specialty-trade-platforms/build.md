# Earned Value at the Crew-Week, Not the Project-Month

**Niche:** [[niches/construction-tech-platforms/specialty-trade-platforms/profile|Specialty Trade Contractor Platforms]]
**Industry:** [[industries/construction-tech-platforms|Construction Tech Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A specialty contractor's profitability is decided by installed quantity per labour hour, and the number is assembled monthly by a project manager from a foreman's estimate and a timecard export, which is too late and too coarse to change anything.
**Tags:** #time-series-forecasting #gradient-boosting #change-point-detection #evaluation-metrics #confidence-intervals #descriptive-statistics #revenue-impact #worker-facing
**Contested on:** *Not terminal as stated* — see the sub-niches for the trade-specific form of this contest.

## The Problem
A trade contractor bids a job at a production rate: so many units installed per crew hour. Whether the job makes money depends almost entirely on whether that rate holds. The contractor finds out in the monthly cost report, six weeks into an eight-week scope, by which point the rate is what it is. The foreman knew in week two that the crew was running behind because of a stacked-trade condition in one area, and had no mechanism to say it in a form that reached anyone except as a complaint.

## Why Nobody Has Built This
Measuring installed quantity at crew-week granularity means measuring quantity, which is the hard part in every trade and is hard differently in each — counting installed hangers is not counting placed cubic yards is not counting pulled feet of cable. Vendors that tried to build one generic quantity-tracking product produced something that fit nobody, and vendors that went deep on one trade found the work did not transfer. The labour side is easier but also fragmented: timecards live in payroll systems with no scope attribution, so hours are known and what they were spent on is not. Solving it generically is the mistake; solving it per trade is the only thing that works and is why this niche decomposes.

## What to Build
A production baseline and an earned-value engine at the granularity the foreman works in: crew, area, scope item, week. Budgeted quantities and hours come from the estimate rather than being re-entered, which requires the estimating system to be treated as the source of the baseline rather than as a document that produced a number. Actual quantity comes from whatever the trade's reliable source is — the sub-niches are precisely about what that source is. Actual hours come from timecards attributed to scope, which needs the field capture to ask one extra question rather than none. The output is a weekly rate per crew per area against baseline, with a forecast of the scope's final hours if the current rate holds, and an alert when a rate changes rather than when a threshold is crossed.

## Target Customer
Specialty trade contractors with self-performed labour at scale, and the trade-vertical platform vendors serving them.

## Impact If Built
Detecting a production rate problem in week two instead of week six is the difference between resequencing a crew and eating the loss, and on a labour-intensive scope the difference is most of the job's margin. The baseline-from-estimate link is also a permanent improvement to estimating, because for the first time the estimator learns which of their assumed rates hold.
