# Machine Learning Opportunities — Fitness & Wellness Software

**Industry:** [[fitness-wellness-software|Fitness & Wellness Software]]
**Derived from:** [[problems/fitness-wellness-software/high-impact|High Impact]], [[problems/fitness-wellness-software/low-impact-1|Low Impact 1]], [[problems/fitness-wellness-software/low-impact-2|Low Impact 2]], [[problems/fitness-wellness-software/worker-life-1|Worker Life 1]], [[problems/fitness-wellness-software/worker-life-2|Worker Life 2]]

---

## 1. Membership Lapse Hazard from Attendance Decay
#survival-analysis #gradient-boosting #change-point-detection #logistic-regression #feature-engineering #confidence-intervals #evaluation-metrics #revenue-impact

**Problem statement:** Cancellation is preceded by weeks of declining attendance and the decision is effectively made long before the member calls. The check-in record captures the whole decay curve and is used to print class rosters.

**ML task:** Survival modelling of time to cancellation with time-varying attendance covariates, plus change point detection on individual attendance patterns
**Input data:** Check-in events per member with class, time slot, instructor and location; membership type, tenure, price and contract terms; booking and cancellation behaviour; waitlist entries; payment history; instructor departures and schedule changes as external events; whether the member attends alone or with a consistent companion.
**Target:** Cancellation, freeze, or non-renewal, with the date. Payment failure that is never recovered counts as a separate outcome, since the mechanism differs.
**Evaluation metric:** Lead time on correctly identified lapses is the metric that matters — a model that flags a member thirty days after their last visit is describing the past. Report precision@k for a realistic daily outreach capacity at a studio, and calibration of the hazard. The eventual business metric is retention lift under a randomised intervention, not prediction accuracy.
**Scope:** The prediction is the easy half and is likely to work well, because the signal is unusually clean. The hard and genuinely novel half is the intervention: nobody knows what recovers a lapsing member, and with tens of thousands of studios the platform can run properly randomised trials on outreach type, timing and sender. That experimentation programme is the actual product. 2-3 ML engineers plus an experimentation lead, 5-6 months to a first model, ongoing for the trials.
**Data availability:** Excellent and unusually clean — a timestamped record of whether the customer did the thing they pay for. The main gap is that cancellation reasons are captured inconsistently and often as free text at the desk, which limits diagnosis rather than prediction.

---

## 2. Class Demand Forecasting for Schedule Construction
#time-series-forecasting #gradient-boosting #optimization-fundamentals #feature-engineering #confidence-intervals #evaluation-metrics #causal-inference

**Problem statement:** A studio's grid is inherited and adjusted by instructor availability, not by demand. The valuable question — what would attend a class of this type at this time that we have never run — cannot be answered from one studio's history, and waitlists, the clearest evidence of unmet demand, are treated as a queue rather than as data.

**ML task:** Attendance forecasting for hypothetical class-slot-instructor combinations, pooled across comparable studios, with a member-level substitution model to separate new demand from cannibalisation
**Input data:** Historical class attendance with type, time, day, instructor, capacity and waitlist depth; member-level attendance patterns; studio attributes (location, size, member base composition, market density); comparable studios across the platform base; local seasonality.
**Target:** Attendance for a given class configuration; and at member level, whether a new class draws incremental attendance or displaces an existing booking.
**Evaluation metric:** Forecast accuracy on genuinely new class configurations — held out by configuration rather than randomly, since predicting attendance for a class that has run fifty times is not the problem. Waitlist depth provides a censored-demand correction that must be handled explicitly or every full class is under-measured.
**Scope:** Censoring is the central statistical issue: a class at capacity tells you demand was at least capacity, not what it was, and waitlists only partially reveal the remainder. The instructor effect is real, measurable and politically sensitive; the defensible framing models instructor-and-class-type combinations for scheduling rather than ranking individuals. 2 ML engineers, 5 months.
**Data availability:** Attendance and waitlist data is complete across the platform base. Studio comparability requires attributes that are inconsistently recorded and partly inferable from member behaviour.

---

## 3. Engagement-Aware Payment Recovery
#gradient-boosting #logistic-regression #time-series-forecasting #feature-engineering #confidence-intervals #evaluation-metrics #revenue-impact

**Problem statement:** Failed payments and lapsing members look identical to a generic dunning flow and require opposite responses. Aggressive recovery on a disengaged member converts a quiet lapse into a chargeback and a bad review; frictionless recovery on an engaged member whose card expired is simply the right answer. Attendance is the discriminator and sits in the same platform as the payment.

**ML task:** Recovery probability prediction conditional on decline reason, member engagement and recovery treatment; plus timing optimisation around check-in events
**Input data:** Payment attempts with decline codes, card age and issuer; membership tenure, price and type; attendance in the preceding weeks; prior recovery outcomes; check-in events in real time; communication history and response.
**Target:** Successful recovery within a horizon, and separately, whether the member remains active ninety days later — the second matters more and is routinely ignored.
**Evaluation metric:** Recovery rate is the obvious metric and the wrong one on its own. Evaluate on ninety-day retained revenue, which penalises the aggressive sequences that recover a payment and lose the member. Chargeback rate should be tracked as a guardrail.
**Scope:** The highest-value component requires no modelling at all — triggering a card update prompt at check-in, when the member is physically present and it takes fifteen seconds. That the payment and check-in systems do not talk at that moment despite living in the same product is a plumbing failure worth fixing before any model. 1-2 ML engineers, 3-4 months.
**Data availability:** Complete within the platform, since most of these vendors are also the payment processor. Decline code granularity varies by processor and issuer, which limits how finely retry timing can be tuned.

---

## 4. Sub Request Matching Across Studios
#gradient-boosting #k-nearest-neighbors #optimization-fundamentals #logistic-regression #feature-engineering #evaluation-metrics #workflow-orchestration

**Problem statement:** An instructor who cannot teach triggers a broadcast to a group chat until someone volunteers. Unfilled classes get cancelled, which is a poor experience for every member who booked. Instructors working across several studios have no coordinated view of their own week and get double-booked.

**ML task:** Acceptance probability prediction for a given instructor and class offer, combined with a matching optimisation over qualification, availability and travel feasibility
**Input data:** Instructor qualifications and class type history; teaching schedules across studios where visible; historical sub request offers with accepted or declined outcomes; travel distance and time between locations; time of offer relative to class; pay rate; instructor's typical weekly load.
**Target:** Offer acceptance, and whether the class was ultimately covered.
**Evaluation metric:** Fill rate and time to fill against the broadcast baseline, plus the number of instructors contacted per filled class — the last one is the measure of how much interruption the system removes from everyone who was not the right match.
**Scope:** The cross-studio view is the structural obstacle rather than the modelling one: each platform sees only its own studios, and instructors work across platforms. A version confined to one platform's studio base is still useful and is where this starts. Travel feasibility is a hard constraint that the group-chat process ignores entirely and that causes a meaningful share of late cancellations. 1-2 ML engineers, 3-4 months.
**Data availability:** Sub request history exists where the platform handles requests and is absent where studios use group chats, which is most of them — so instrumenting the request flow is the prerequisite and is itself the product improvement.
