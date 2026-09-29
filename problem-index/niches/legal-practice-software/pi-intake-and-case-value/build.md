# Case Value and Duration Estimated at Intake

**Niche:** [[niches/legal-practice-software/pi-intake-and-case-value/profile|Personal Injury — Intake Selection & Case Value]]
**Industry:** [[industries/legal-practice-software|Legal Practice Software]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The most consequential decision a personal injury firm makes is taken in a four-minute phone call by the least experienced person in the building, against no estimate of what the case is worth or how long it will take.
**Tags:** #gradient-boosting #survival-analysis #confidence-intervals #bayesian-inference #evaluation-metrics #cross-validation #revenue-impact #tacit-knowledge-ml
**Contested on:** Every serious competitor in personal injury firm software is fighting to tell a firm which of this week's intakes to sign and what each is worth against this venue and this carrier — and whoever predicts that best takes the account.

## The Problem
An intake specialist takes a call: rear-end collision, county, treating chiropractor, three weeks post-accident, carrier named. She runs the script, checks the boxes, and the case is signed or referred out based on a threshold somebody set years ago. The managing partner would have asked two different questions and reached a different answer, because he has seen four thousand of these and knows that this carrier in this county on these facts pays a particular way. That knowledge is not in the system, is not transferable, and leaves when he does.

## Why Nobody Has Built This
The selection problem is the technical obstacle and it is serious: the firm only observes outcomes for cases it signed, so a model trained on signed cases learns the value of cases that passed the existing filter and says nothing useful about the ones that did not. Ignoring this produces a model that confidently reproduces the firm's current criteria, including their errors. Handling it properly requires either deliberate exploration — signing some marginal cases to learn — or a referral-outcome feedback path, and neither exists today. On top of that, outcomes are heavily censored and heavy-tailed, and the ethical surface is real: a system that scores an injured person's call is a system that decides who gets counsel, which is a reason for care in the interface rather than a reason to avoid the problem.

## What to Build
An intake estimator that returns a value distribution and a duration distribution rather than a score, conditioned on the facts available in the first call — venue, carrier, mechanism, reported injury, treatment status, liability posture, policy information where known — and updated as records arrive so the firm can see a case revalue rather than carry an intake number forever. It is trained on the firm's resolved history with cross-firm base rates where the firm's own data is thin, with the shrinkage visible. The selection problem is addressed head-on: referred-out cases are tracked to outcome through referral agreements the firm already has, and a small, deliberate exploration budget signs marginal cases to keep the filter honest. The interface never says decline; it says what the case is likely worth, how long it is likely to take, and how confident the estimate is, and leaves the decision with a lawyer.

## Target Customer
Personal injury firms signing 50+ cases a month, and the intake and case management vendors selling to them who currently compete on pipeline workflow.

## Impact If Built
Firms that quantify intake typically find their existing thresholds are wrong in both directions — declining a recoverable segment and signing a segment that consistently loses money — and correcting both is worth more than any change in marketing spend. Attaching a value distribution to each open case also feeds the portfolio view directly, which makes this the load-bearing piece of the parent niche.
