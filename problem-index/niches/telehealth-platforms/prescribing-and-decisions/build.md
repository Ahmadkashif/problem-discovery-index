# Build: Decision Quality as a Measured Property

**Niche:** [[niches/telehealth-platforms/prescribing-and-decisions/profile|Prescribing & Clinical Decision-Making]]
**Industry:** [[industries/telehealth-platforms|Telehealth Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Make the clinical decision the measured unit — what was decided, on what information, and what happened next — rather than measuring the visit that contained it.
**Tags:** #bayesian-inference #gradient-boosting #causal-inference #confidence-intervals #evaluation-metrics #hypothesis-testing #compliance #worker-facing
**Contested on:** Whether decision quality can be measured when the counterfactual is unobservable and outcomes arrive elsewhere.

## The Problem

Everything a telehealth platform measures is about the container rather than the contents. Visit volume, time to appointment, visit duration, satisfaction, completion rate. The decision inside the visit — prescribe this, refer here, reassure and wait — is the only thing that matters clinically and is not a measured object at all.

The consequence is that nobody can tell a good decision from a bad one at any level. The clinician does not know; they see the patient once. The medical director does not know; they see aggregate volume. The platform cannot defend its clinical model to a regulator except by pointing at satisfaction scores, and cannot identify the clinician whose prescribing is far outside the norm except when a complaint arrives.

## Why Nobody Has Built This

The measurement is genuinely hard. The right decision for a given presentation is often not knowable even in retrospect — a patient who recovered might have recovered anyway, a prescription that was unnecessary does no visible harm, and the counterfactual is never observed. Outcomes frequently occur outside the platform, in an emergency department or a pharmacy or a primary care office it has no connection to.

Underneath the difficulty is a strong commercial reason to leave it alone. A platform that measured decision quality would produce a record of decisions it later judged poor, attributable to named clinicians, in a segment already under regulatory scrutiny. Every incentive points toward measuring throughput, which is easy, defensible and correlated with revenue.

## What to Build

A decision-level data model and a measurement programme that is honest about what it can establish.

**Make the decision the record.** Every encounter produces a structured decision object: presenting complaint, the information available at the moment of deciding, the differential considered, the decision taken, and the reasoning. Much of this can be extracted from the encounter rather than typed, which matters because a clinician under throughput pressure will not complete another form.

**Link to what happened next, using everything available.** The platform's own signals first — return visits for the same complaint, refills, escalations, follow-up responses. Then external linkage where it can be obtained: pharmacy fill data showing whether the prescription was ever collected, claims or health information exchange data showing an emergency department presentation in the following fortnight. Each source needs an agreement and none is impossible, and the fill data alone is highly informative and often already accessible through the e-prescribing network.

**Measure at the pattern level, not the case level.** Individual decisions are mostly unjudgeable. The distribution is not: what share of visits for this presentation ended in an antibiotic, and how does that compare to guideline-concordant rates and to in-person benchmarks; which clinicians sit far outside the distribution after adjusting for their case mix. Case-mix adjustment is essential and non-trivial — a clinician working evenings in one state sees a different population — and without it the measurement punishes the wrong people.

**Feed it back to the clinician first.** A clinician who can see their own patterns against their peers, privately, with the case mix adjusted, is receiving the professional feedback that the entire virtual care workforce currently lacks. This framing is both the most useful and the most likely to be built, because it is coaching rather than audit.

**Design the governance before the measurement.** What happens when a clinician is an outlier, what evidence standard applies, who reviews it, and what is retained. Deciding this in advance is what makes the programme survivable; deciding it during the first difficult case is what ends it.

## Target Customer

Platform clinical leadership and medical directors, and particularly platforms contracting with payers and employers, where clinical quality reporting is contractual and throughput metrics are increasingly insufficient. The regulatory environment is the other driver: a platform that can characterise its own prescribing is in a materially different position when asked about it.

## Impact If Built

The decision becomes a measured object, which is the precondition for every other clinical improvement in this industry. Clinicians get feedback on their own practice for the first time. And the platform can describe its clinical model in terms of what it decided and what followed, rather than in terms of how quickly it answered the phone.
