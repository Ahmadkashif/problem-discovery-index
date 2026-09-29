# No-Shows and the Unrecoverable Slot

**Industry:** [[scheduling-booking-platforms|Scheduling & Booking Platforms]]
**Type:** High Impact
**One-liner:** Predict which bookings will not be honoured and act on the ones that matter, because the slot cannot be sold twice and the current answer — one reminder, sent to everybody — has never been measured against anything.
**Tags:** #logistic-regression #gradient-boosting #survival-analysis #causal-inference #feature-engineering #confidence-intervals #evaluation-metrics #hypothesis-testing #revenue-impact

## The Problem
A business that sells appointments sells time, and time does not inventory. A slot that goes unused at two o'clock is not available to sell later; it is simply gone, along with whatever the practitioner was paid for being there.

No-show rates are substantial across the sectors that use these platforms — healthcare, personal services, professional services, trades — and in several of them run well into double digits. For a solo practitioner, a no-show is a meaningful fraction of a day's income. For a clinic, it is a capacity problem that lengthens waiting lists for everyone.

The industry's universal response is a reminder. Every platform sends one, usually twenty-four hours before, by email or SMS, to every booking identically.

Nobody knows whether it works, or which version works better, because nobody has run the comparison. The reminder is a convention. It was added early, it seems obviously sensible, and it has been shipped unchanged for fifteen years.

Meanwhile the signal that would let a business act is abundant. Lead time between booking and appointment is one of the strongest known predictors. Whether the customer is new or returning. Their own attendance history. Time of day and day of week. Whether the booking was self-service or made by staff. Whether a deposit was taken. Whether they opened the confirmation. Weather, for anything requiring travel.

## Why It's Unsolved
The category's economics point elsewhere. Scheduling software is cheap, competitive and increasingly free, and the vendors compete on ease of booking rather than on outcomes after the booking. No-show prevention would require measurement infrastructure and would be sold on results, which is a different business than the one they are in.

There is also a real fairness objection that deserves to be taken seriously rather than dismissed. Attendance risk correlates with circumstances — transport, childcare, inflexible work, income — that also correlate with protected characteristics. A system that imposes deposits or overbooking on people predicted not to attend can straightforwardly become a system that penalises poverty, and in healthcare that has direct consequences for access.

That objection rules out some interventions and not others, and the distinction matters. Requiring a deposit from a predicted no-show is problematic. Offering that person a more convenient slot, a different reminder channel, or an easier way to reschedule is not — it is better service aimed at the people most likely to need it.

Overbooking is a third path with its own hazard, familiar from airlines: when the prediction is wrong, someone who arrived on time waits.

## What a Solution Looks Like
A calibrated attendance probability per booking, from the features already collected, with the business deciding what to do with it.

Interventions should be tested rather than assumed. With tens of millions of appointments across a platform, reminder timing, channel, wording and count are all randomisable, and the effect on attendance is measurable per segment. That evidence does not exist anywhere and would be the category's most valuable asset.

The intervention set should default to accommodation rather than penalty. Easier rescheduling, a channel the customer actually reads, a second reminder for high-risk bookings only, and proactive offering of a better slot are all improvements to service.

Waitlist activation is the honest way to recover capacity: when a booking is predicted or reported unlikely, offer the slot to someone waiting rather than overbooking on top of the original.

And the fairness constraint should be built in — testing whether predictions and interventions differ across groups, and refusing to apply penalising interventions on the basis of the score at all.

## Impact If Solved
No-shows are the largest recoverable loss for every business that sells time, and the industry's response has been an untested convention applied uniformly for fifteen years. A calibrated prediction paired with accommodating interventions, validated by real experiments, is the first genuine improvement available — and the experimental evidence would itself be worth more than the model.
