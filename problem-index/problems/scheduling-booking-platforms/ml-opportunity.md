# Machine Learning Opportunities — Scheduling & Booking Platforms

**Industry:** [[scheduling-booking-platforms|Scheduling & Booking Platforms]]
**Derived from:** [[problems/scheduling-booking-platforms/high-impact|High Impact]], [[problems/scheduling-booking-platforms/low-impact-1|Low Impact 1]], [[problems/scheduling-booking-platforms/low-impact-2|Low Impact 2]], [[problems/scheduling-booking-platforms/worker-life-1|Worker Life 1]], [[problems/scheduling-booking-platforms/worker-life-2|Worker Life 2]]

---

## 1. Attendance Probability with Fairness Constraints
#logistic-regression #gradient-boosting #survival-analysis #causal-inference #confidence-intervals #hypothesis-testing #feature-engineering #evaluation-metrics #revenue-impact

**Problem statement:** No-shows are the largest unrecoverable loss for any business selling time, and the universal response is one reminder sent to everyone twenty-four hours ahead — a fifteen-year-old convention that has never been compared against an alternative. The predictive signal is abundant and unused.

**ML task:** Calibrated binary classification of attendance, with explicit group fairness evaluation and an intervention policy constrained to accommodating rather than penalising actions
**Input data:** Lead time from booking to appointment; customer tenure and attendance history; booking channel (self-service or staff); deposit taken; appointment type, duration and price; time of day and day of week; reminder delivery and open events; reschedule history; weather for travel-dependent services; business sector and location.
**Target:** Attendance, cancellation with notice, or no-show.
**Evaluation metric:** Calibration rather than discrimination, because the score drives a decision about an individual and a miscalibrated probability produces unfair treatment at a fixed threshold. Report calibration and error rates separately across demographic proxies available in the data, and treat divergence as a blocking finding rather than a footnote.
**Scope:** The fairness constraint is a design requirement, not a caveat. Attendance risk correlates with transport, childcare, inflexible work and income, so penalising interventions — deposits, overbooking against the individual — convert the model into a mechanism that disadvantages the already disadvantaged, and in healthcare that directly affects access. The defensible intervention set is accommodation: easier rescheduling, a channel this person actually reads, a better slot offered proactively. Waitlist activation recovers capacity without overbooking. 2-3 ML engineers plus an ethicist or clinical advisor for health deployments, 5-6 months.
**Data availability:** Excellent volume across sectors. Demographic attributes are largely absent, which makes fairness auditing harder rather than unnecessary and argues for proxy-based auditing with appropriate caution.

---

## 2. Reminder Sequence Experimentation
#causal-inference #hypothesis-testing #logistic-regression #gradient-boosting #confidence-intervals #evaluation-metrics #revenue-impact

**Problem statement:** Reminder timing, channel, count and wording are configured by convention at every business in the sector and have never been tested. There is no published evidence and apparently no vendor-internal evidence on whether twenty-four hours beats forty-eight, whether SMS is worth its cost, or whether a second reminder helps or annoys.

**ML task:** Randomised experimentation at platform scale with heterogeneous treatment effect estimation across segments
**Input data:** Randomised assignment of reminder timing, channel, count, wording and confirmation requirement; delivery, open and click events; appointment attributes and customer history; attendance outcome; business sector and size.
**Target:** Attendance, with cancellation-with-notice treated as a distinct and partially positive outcome since it frees the slot.
**Evaluation metric:** Average treatment effect per variant, and conditional effects by segment — lead time, customer tenure, sector, channel responsiveness. The result of practical value is a per-segment policy, since a uniform improvement is unlikely and a segmented one is very likely.
**Scope:** This is primarily an experimentation programme rather than a modelling one, and it is the highest-value work in the category because the evidence does not exist anywhere. A single business cannot run it; a vendor with tens of millions of appointments can settle it in a quarter. Cancellation-with-notice must be modelled as its own outcome or a reminder that prompts a cancellation looks like a failure when it is a success. 1-2 ML engineers plus an experimentation platform, 4 months to first results, ongoing thereafter.
**Data availability:** Complete, and the randomisation infrastructure is trivial to add to systems that already send the messages.

---

## 3. Constrained Slot Generation as Optimisation
#optimization-fundamentals #convex-optimization #dynamic-programming #gradient-boosting #evaluation-metrics #workflow-orchestration #revenue-impact

**Problem statement:** Availability is computed as a calendar lookup while real businesses have staff skills, room and equipment constraints, service-specific buffers and travel time. Owners cannot express this in the configuration interface, so they simplify their availability and lose capacity invisibly.

**ML task:** Constrained assignment and slot generation, combined with predicted service duration and a fragmentation cost on the remaining day
**Input data:** Staff qualifications and working hours; room and equipment inventory with service compatibility; historical service durations by service, staff member and customer; travel distances for mobile services; booking demand patterns by slot; historical overruns.
**Target:** Feasible start times with a complete resource assignment, ranked by expected revenue including the fragmentation cost of the residual day.
**Evaluation metric:** Realised utilisation and revenue per available hour against the business's prior configuration, ideally with a holdout of comparable businesses. Overrun rate is the guardrail — an optimiser that packs the day perfectly and then cascades on the first overrun is worse than a conservative one.
**Scope:** Predicted duration is the input that makes the optimisation honest: booking a service for its nominal length when this practitioner reliably takes longer is what causes the cascade. Fragmentation cost — offering a slot that strands an unusable forty-five minutes — is a real cost no platform models. Travel time for mobile services deserves proper treatment rather than a fixed buffer. 2 ML engineers plus an operations research background, 5 months.
**Data availability:** Booking and duration history is complete. Resource inventories and compatibility rules are configured inconsistently and often incorrectly, which is itself part of the problem being solved.

---

## 4. Gap Fill and Waitlist Matching
#gradient-boosting #logistic-regression #k-nearest-neighbors #time-series-forecasting #feature-engineering #evaluation-metrics #automation

**Problem statement:** A cancellation leaves a hole that could be filled by working a list, and the practitioner is with a client. For solo practitioners this is the sharpest recurring loss, and for multi-practitioner businesses it is capacity the coordinator has no time to recover.

**ML task:** Acceptance probability prediction for a short-notice offer, per candidate customer, with a ranking and outreach policy
**Input data:** Waitlist entries and their stated preferences; existing bookings that could move earlier; historical short-notice offers with accepted or declined outcomes; customer responsiveness by channel and time of day; distance or travel requirement; appointment type compatibility; time remaining before the slot.
**Target:** Acceptance of a short-notice offer within the available window.
**Evaluation metric:** Fill rate on cancelled slots against the manual baseline, and offers made per filled slot — the second matters because over-offering annoys the customer base and is the failure mode that gets the feature disabled. Time to fill is the operational measure.
**Scope:** The time constraint shapes everything: a slot two hours away needs a different outreach strategy than one next week, and acceptance probability rises and falls with notice in ways that must be conditioned on. Offering a slot to a customer with an existing later booking is the highest-yield move and is rarely considered, since it fills the gap and frees a future slot. 1-2 ML engineers, 3-4 months.
**Data availability:** Cancellation and rebooking history is complete. Short-notice offer outcomes barely exist because the outreach is currently done by text message outside the platform, so instrumenting the offer is the prerequisite.
