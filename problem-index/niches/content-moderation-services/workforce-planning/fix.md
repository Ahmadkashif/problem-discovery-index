# Fix: Attrition Is Forecast as Weather

**Niche:** Workforce Planning & Scheduling
**Industry:** [[industries/content-moderation-services|Content Moderation Services]]
**Type:** Fix (Pain Point)
**One-liner:** Attrition is planned for as a historical rate to be replaced rather than as an outcome the scheduling system itself partly produces.
**Tags:** #survival-analysis #gradient-boosting #evaluation-metrics #confidence-intervals #hypothesis-testing #worker-facing #revenue-impact
**Contested on:** Whether staffing is planned against a forecast that anticipates event-driven surges and the constraints of exposure and language, or against a smoothed volume curve.

## The Problem

Moderation operations lose people at rates that would be a crisis in most industries and are treated here as a planning input. Workforce models take a historical attrition percentage, apply it forward, and size the recruitment pipeline to replace the expected losses. The rate is an environmental parameter, like seasonality.

It is not environmental. A substantial part of it is produced by decisions the same planning system makes. Which reviewer gets the severe queue repeatedly because they are fast. Who is scheduled onto overtime during a surge. Whose wellness time is cancelled when volume spikes. Which sites run at occupancy levels that leave no recovery. Who has been on the worst category for eleven weeks because they are one of few cleared for it.

None of that is connected to the attrition forecast. The model does not know which individuals are at elevated risk, does not know which scheduling patterns precede departures, and therefore cannot avoid the patterns that cause them. It simply replaces the losses, hires new people, puts them through a training pipeline, and accepts that some fraction will leave — at a replacement cost per head that is large and mostly uncounted, and with a quality cost as experienced reviewers are continually swapped for new ones.

The operation is, in effect, treating a controllable output as an uncontrollable input.

## Why It's Still Broken

**Replacement cost is invisible in the accounts.** Recruitment, vetting, training, the ramp to competence, the quality deficit during ramp, and the supervisory load of a constantly new workforce are spread across several budgets and never summed. Nobody can state the cost of a departure, so nobody can justify spending to prevent one.

**Attrition is assumed to be inherent to the work.** The belief that this job simply has high turnover is widespread, partly true, and functions as a complete explanation that forecloses investigation into the controllable share.

**Prediction sounds like surveillance.** Modelling which reviewers are likely to leave, from scheduling and exposure patterns, is uncomfortable and easily misused. Done at the individual level for retention interventions it can be genuinely intrusive, which is a legitimate objection that has stopped the useful cohort-level version too.

**Short contracts blur the signal.** Much of the workforce is on fixed-term contracts through further layers of subcontracting, so departures are recorded as contract ends rather than as attrition, and the data needed to model it is fragmented across employers.

**Planning is measured on coverage, not retention.** A workforce planner is judged on whether seats were filled, which makes replacement the success condition and retention someone else's problem.

**The causes sit with the client.** Several of the strongest drivers — queue composition, exposure, the quality metric — are determined by contractual terms the vendor does not control, which makes the whole subject easier to treat as environmental.

## What a Fix Looks Like

**Cost a departure, once, properly.** Sum recruitment, vetting, training, ramp, the quality deficit during ramp and the supervisory overhead. Publishing that single number internally changes every subsequent conversation, because it converts attrition from a rate into a budget line with a size.

**Model attrition against scheduling and exposure history at cohort level.** Survival analysis over shift patterns, severe-queue exposure, overtime, wellness delivery, queue variety and tenure. Reported by cohort and pattern rather than by individual, which captures nearly all the operational value with none of the surveillance objection — the output is "this shift pattern loses people at twice the rate", which is actionable and names nobody.

**Feed it back into scheduling as a cost term.** Once the patterns that precede departure are known, the scheduler should avoid them — not as a wellness gesture but as a cost optimisation, because it now has a number for what a departure costs. This is the change that makes retention a planning objective rather than an aspiration.

**Distinguish the controllable share.** Some attrition genuinely is inherent: people take this work as a step to something else, and that is legitimate and largely fixed. Separating it from the share driven by exposure concentration, cancelled recovery and repeated overtime is what makes the controllable part actionable instead of the whole thing feeling hopeless.

**Track it across the subcontracting layers.** Departures recorded as contract ends have to be counted as attrition or the data is meaningless. This requires reporting obligations down the chain that mostly do not exist.

**Take the client-driven causes to the client.** Where the strongest drivers are queue composition or the quality metric, the vendor should bring the evidence to the contract conversation. Attrition costs the platform too, in decision quality and in the constant loss of experienced reviewers, and it is one of the few labour arguments with a clean commercial case on both sides.

## Who Feels the Pain

The reviewers, who are worn out by patterns nobody is examining, in a system that has already budgeted for their departure.

The remaining reviewers, who absorb the load of a perpetually under-experienced workforce and train their own replacements repeatedly.

The vendor, paying a large and uncounted replacement cost while treating its cause as weather.

And the platform, receiving decisions from a workforce whose median experience is kept low by a churn rate nobody is trying to reduce — which shows up in exactly the contextual judgement the operation exists to provide.

## Impact If Fixed

Costing a departure properly is a single analysis that would reframe the entire subject, because the number is almost certainly large enough to fund serious intervention and is currently unknown.

Cohort-level modelling identifies the scheduling patterns that drive avoidable losses, and those patterns are changeable at little or no cost once they are visible.

And an operation that retains people accumulates the thing this industry most lacks: experienced reviewers with a deep case library, who are the only reason human review outperforms a classifier in the first place.
