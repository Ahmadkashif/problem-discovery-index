# The Slot Cannot Be Sold Twice

**Niche:** [[niches/scheduling-booking-platforms/no-show-and-attendance/profile|No-Show & Attendance]]
**Industry:** [[industries/scheduling-booking-platforms|Scheduling & Booking Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No-show rates run into double digits across several sectors, attendance is highly predictable from data every platform already holds, and the industry's entire response is one reminder sent to everybody.
**Tags:** #gradient-boosting #logistic-regression #survival-analysis #causal-inference #evaluation-metrics #confidence-intervals #revenue-impact #automation
**Contested on:** Every serious competitor in this niche is fighting to predict which bookings will not be honoured and intervene on the ones worth intervening on — and whoever raises attendance takes the account, because the slot cannot be sold twice and the operator counts the loss every week.

## The Problem
A clinic has forty appointments on Tuesday. Five will not show. The owner knows the rate and treats it as a cost of doing business, because nothing distinguishes the five in advance. Yet the differences are stark and recorded: the booking made six weeks ago by a first-time customer at 8am on a Monday is not the same risk as the one made on Thursday by a regular of four years for their usual slot. The platform has both bookings, the full history behind them, and every prior outcome, and sends both the same message at the same hour.

## Why Nobody Has Built This
Scheduling products were built as calendar tools, and attendance was framed as the customer's behaviour rather than as something the product could influence. The category also commoditised early and competes on price and simplicity, which pushes against anything requiring modelling. Individual operators have too little data to build this themselves and the vendors, who have enormous amounts of it across every sector, have not treated it as an asset. And the strongest intervention — requiring a deposit — creates booking friction that operators fear, so it is left off, which removes the one lever that would work if it were applied selectively.

## What to Build
Risk-scored bookings with matched interventions. Score every booking at the moment it is made and again as it approaches, from lead time, customer history, service type, slot timing, booking channel, prior rescheduling, payment status and weather-independent seasonality — a well-posed problem with abundant labels, since every appointment resolves into attended or not. Match the intervention to the risk and to what the slot is worth: a low-risk regular gets the ordinary reminder; a high-risk booking gets a confirmation request that requires a response, a deposit prompt, or a personal contact; a high-risk booking in an expensive slot gets the strongest available. Consider controlled overbooking where the economics support it, which several industries do routinely and this one does not, with the risk model making it defensible rather than reckless. Track the effect of each intervention rather than the accuracy of the prediction, since the operator's question is whether attendance improved and not whether the model was right — which means measuring uplift with proper controls, not correlations. And report the loss honestly in money: this many slots, this much revenue, this much recoverable, which is the number that gets the operator's attention.

## Target Customer
Any business selling time — clinics, salons, studios, trades, professional services — and the platform vendors, for whom attendance is the only differentiator left in a commoditised category.

## Impact If Built
The problem is well-posed, the labels are complete, the data is already collected, and the incumbent solution has never been evaluated. Matching intervention strength to risk and slot value is the whole design, and measuring uplift rather than accuracy is what makes it credible to an operator.
