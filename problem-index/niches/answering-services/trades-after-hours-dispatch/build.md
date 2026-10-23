# Booked Revenue per After-Hours Call

**Niche:** [[niches/answering-services/trades-after-hours-dispatch/profile|Home Services & Trades Answering]]
**Industry:** [[industries/answering-services|Telephone Answering Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Contractors pay their answering service by the minute and cannot say how much revenue its calls produced, which leaves the live service defenceless when an AI agent quotes a fraction of the price.
**Tags:** #gradient-boosting #logistic-regression #causal-inference #evaluation-metrics #data-integration #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to turn each after-hours call to a contractor into either a booked job on the contractor's dispatch board or a page for a genuine emergency, and whoever books the most billable jobs without waking a technician for a non-emergency takes the account.

## The Problem
A residential service contractor's after-hours calls range from emergencies (no heat, burst pipe, sparking panel) and next-day bookings to price shoppers and existing customers with questions. The answering service takes a message or pages. Whether that call became a job, at what ticket, or went to a competitor is recorded in the contractor's field-service platform, if at all, and never joined back to the call.

## Why Nobody Has Built This
The answering service and the field-service platform do not share identifiers, and the contractor has no time to reconcile them. Live services have avoided outcome measurement because per-minute billing does not need it.

## What to Build
A call-to-job join: each after-hours call matched to the customer and job records in ServiceTitan, Housecall Pro or Jobber, with booked revenue, cancellation and callback outcomes attached. Conversion is modelled by call type, script path and operator, and nuisance pages (pages that did not produce a dispatch) are reported alongside. The contractor gets a monthly statement of revenue booked against fees paid.

## Target Customer
Answering services with 50+ trades accounts; owners and call-centre managers at contractors running 10-100 trucks.

## Impact If Built
The live service competes on booked revenue rather than price per minute, scripts improve where conversion is low, and the contractor can compare live and AI answering on the measure that matters to it.
