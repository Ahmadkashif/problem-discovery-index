# Most of the Class Never Claims, and the Process Records It as Completed

**Niche:** [[niches/personal-injury-law/mass-tort-claims-administration/profile|Mass Tort & Class Action Claims Administration]]
**Industry:** [[industries/personal-injury-law|Personal Injury Law Firms]]
**Type:** Fix (Pain Point)
**One-liner:** Claim rates in consumer settlements are routinely a low single-digit percentage of the class, the administration is nonetheless reported as successful because every court-ordered step was executed, and nobody owns the number.
**Tags:** #logistic-regression #time-series-forecasting #descriptive-statistics #evaluation-metrics #compliance

## The Problem
A settlement is approved on the basis that it compensates a class. The administrator executes the notice programme, opens the claim period, reviews what arrives, and distributes. The final report records notice delivered, claims received, claims paid, funds distributed.

What it does not treat as a result is the ratio. In many consumer settlements only a small percentage of the class ever files, and a further share of those who file are denied for deficiencies they never cure. The people the settlement was for mostly do not receive anything.

There are honest reasons for low claiming. Some class members have no memory of the purchase, some awards are genuinely too small to be worth a form, and some classes are defined so broadly that most members were never really harmed. Those are legitimate and they do not account for the whole gap.

The rest is process. Notice arrives looking like the fraud people have been trained to ignore. Claim forms ask for documentation from years ago. Deadlines are short relative to how long it takes a mailed notice to prompt action. Deficiency letters are written in the register of legal correspondence and are frequently abandoned rather than cured. Each of these is a design decision made by someone, and none of them is measured against the outcome it produced.

Inside the administration operation, the effect compounds. Claim volume arrives in a spike at the deadline that staffing was guessed at rather than forecast, which means the review capacity is wrong at exactly the moment when quality matters. Reviewers work at high volume against a bespoke matrix. Deficiency notices go out in bulk. And because the count of eligible non-claimants is never computed, the loss is invisible in every report.

## Why It's Still Broken
No party is accountable for the claim rate. Class counsel's fee is generally set against the settlement fund rather than the amount that reaches people. The defendant's exposure is capped and a low claim rate is favourable. The court reviews the adequacy of notice at approval, before any of this is observable. The administrator executed the order it was given. There is genuinely no one in the structure whose job it is to care.

Reversion and cy pres arrangements can make the money go somewhere else without anyone reporting a shortfall, which removes the last pressure point.

The counterfactual is also missing. Without knowing what a well-designed programme achieves for this kind of class, a five per cent claim rate cannot be called a failure — and nobody has built that reference, which is a large part of why the question stays closed.

And the process is regarded as legally rather than empirically constrained. Claim form contents and notice language are negotiated and approved, so they are treated as fixed requirements rather than as design choices with measurable effects.

## What a Fix Looks Like
**Report the claim rate as the headline outcome.** Claims paid over class members eligible, with the denominator estimated honestly. Simply computing and publishing it, matter by matter, changes what everyone involved has to think about.

**Forecast the deadline spike and staff against it.** Claim arrival follows a shape that repeats across settlements — slow, then a wall at the deadline, modulated by reminder timing. It is forecastable, and forecasting it is the difference between careful review and triage at the moment of peak volume.

**Model who fails to cure a deficiency.** Deficiency type, notice wording, claimant channel and time remaining all bear on whether a claimant fixes their submission or gives up. Those are the legitimate claimants being lost furthest downstream, after they had already come forward, and the loss is entirely addressable.

**Test the correspondence.** Reminder timing, envelope treatment, subject line and plain-language form design are testable within the bounds of an approved notice programme, and the effects in comparable direct-response settings are large.

**Compute the interval, not just the point.** A claim rate from a class of ten million and one from a class of four thousand carry very different weight. Reporting uncertainty makes cross-matter comparison meaningful rather than anecdotal.

**Bring the evidence to approval.** A court deciding whether a proposed notice and claim process is adequate currently has affidavits and precedent. Realised claim rates from comparable settlements would let it ask a better question, and would come from the administrator.

## Who Feels the Pain
The class member, entitled to compensation, who binned the notice or abandoned the form. The reviewer, working a deadline spike at volume against a matrix written for a different purpose. The judge, approving a process whose effectiveness nobody can characterise. And, eventually, the administrator, in a field increasingly criticised for exactly this and unable to answer with data it already holds.

## Impact If Fixed
Class actions exist so that many small harms can be remedied at once. When most of the class never receives anything, the mechanism has not worked, and the only organisation in a position to measure that reports on the steps it completed instead.
