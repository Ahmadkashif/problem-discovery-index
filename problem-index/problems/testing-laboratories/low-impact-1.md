# Scheduling Against Holding Times on Generic Planning Tools

**Industry:** [[testing-laboratories|Testing Laboratories]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Production planning software solved finite-capacity scheduling decades ago, but none of it knows that a lab's work orders expire, travel in QC batches of twenty and can only be run by analysts with a current demonstration of capability.
**Tags:** #gradient-boosting #survival-analysis #time-series-forecasting #optimization-fundamentals #feature-engineering #workflow-orchestration #revenue-impact

## The Problem
A mid-size environmental or food lab logs a few hundred to a few thousand samples a day. Each carries a method, a promised turnaround, and for many methods an absolute holding time — days for preserved volatiles, hours for some bacteriological tests, 48 hours for parameters such as nitrate. The operations manager and section supervisors decide each morning which samples go into which preparation batch, on which instrument, run by whom, and in what order. Most labs do this from a LIMS backlog report sorted by due date and a whiteboard. Rush requests, instrument downtime, a failed calibration or a cooler that arrives late on a Friday throw the plan out, and the first sign of trouble is often a sample that has already expired or a turnaround already missed.

Missed holding times are expensive in a specific way: the result must be qualified or the sample recollected, which the client pays for in field time and the lab pays for in reputation. Missed turnaround is the commonest reason environmental consultants move work between labs.

## What Already Exists
Finite-capacity scheduling is mature in manufacturing (advanced planning and scheduling modules from Siemens, SAP and others), in field service (dispatch optimisation), and in general resource booking. Enterprise LIMS track due dates and holding-time expiry per sample and can print a backlog. Some labs build Excel or Power BI dashboards on top.

## The Customisation Gap
The lab-specific logic is what generic planners lack: holding times that run from collection, not receipt, and differ by method and preservation; preparation batches capped at a fixed number of field samples, each needing its own method blank, LCS and matrix spike; instrument sequences that must open and close with calibration checks; analysts who may only run a method after a documented demonstration of capability; sample prep that branches (dilutions, cleanups, re-extractions) after the first look at the data; and client priorities that override due dates. The planner must also learn from history how long each step really takes for each matrix, because the method's nominal time is wrong for oily soil. Generic APS tools model none of this, and LIMS report it without planning it.

## Impact If Solved
A scheduler that plans against holding times and real step durations lets a lab see tomorrow's expiries today, cut holding-time violations toward zero, and quote turnaround it can keep — the difference, for a lab handling thousands of samples a week, between a few recollections a month and none, and between being a consultant's first call and their backup.
