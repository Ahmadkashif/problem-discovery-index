# Forecast From Behaviour Rather Than Self-Report

**Niche:** [[niches/crm-platforms/enterprise-sales-forecasting/profile|Enterprise Sales Forecasting]]
**Industry:** [[industries/crm-platforms|CRM Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The CRM predicts from the one input that is systematically corrupted — the representative's own stage and close date — while carrying the engagement, response latency and buying-committee data that cannot be gamed.
**Tags:** #gradient-boosting #survival-analysis #logistic-regression #confidence-intervals #evaluation-metrics #cross-validation #causal-inference #revenue-impact
**Contested on:** Every serious competitor in sales forecasting is fighting to produce a number a sales leader will submit without rebuilding it in a spreadsheet — and whoever forecasts most accurately from unfalsifiable behaviour rather than from self-reported stage takes the account.

## The Problem
A deal sits at 80% probability with a close date at the end of the quarter, where it has sat for three quarters, moving its close date forward by three months each time. Meanwhile: the economic buyer has not replied to an email in five weeks, the number of people from the customer side on any thread has dropped from six to one, the last two meetings were rescheduled by the customer, and no pricing document has been opened since March. Every one of those facts is in the platform. The forecast uses the 80%.

## Why Nobody Has Built This
The incumbents built the system of record and treated the record as the input, which was a reasonable architectural assumption in 2005 and has been wrong since email and calendar became capturable. Changing it means telling customers that the data their representatives enter is unreliable, which is an awkward sales conversation for a vendor whose product is that data entry. There is also a genuine measurement problem that the category has avoided: nobody records the manager's override as a prediction, so there is no baseline to beat and no way to demonstrate improvement, which makes the investment unjustifiable in the terms the organisation uses.

## What to Build
A deal-level probability estimated from behaviour, with the self-reported stage as one weak feature among many rather than as the spine. Engagement breadth and depth on the customer side, response latency and its trend, meeting cadence and who reschedules, document and pricing engagement, the presence and activity of the roles a deal of this type usually requires, and time-in-stage against the distribution for comparable deals. Survival methods handle the censoring properly, since open deals are the entire question and treating them as missing is the error every naive approach makes. Output is a calibrated probability with an interval, aggregated into a forecast distribution rather than a point — because the question a leader actually faces is the probability of making the number, not the expected value. Calibration is reported continuously and prominently, because the only route to a forecast a leader will submit is a visible track record of being right.

## Target Customer
CRM platform vendors, whose failure to do this created an entire competing category on their own data; revenue intelligence vendors extending from capture into prediction; and directly the enterprise sales organisations rebuilding the number by hand every quarter.

## Impact If Built
The forecast is the most consequential number a revenue organisation produces and the process that produces it is universally distrusted by the people who run it. A calibrated behavioural forecast replaces a week of quarter-end reconstruction and, more importantly, surfaces deal risk weeks earlier than a stage-based view — which is the difference between a deal that can still be saved and a miss explained after the fact.
