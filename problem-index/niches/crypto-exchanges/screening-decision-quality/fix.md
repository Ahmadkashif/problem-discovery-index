# The Threshold Set in 2019

**Niche:** [[niches/crypto-exchanges/screening-decision-quality/profile|Screening Decision Quality]]
**Industry:** [[industries/crypto-exchanges|Crypto Exchanges]]
**Type:** Fix (Pain Point)
**One-liner:** Nobody at the exchange can say who chose the current screening threshold, when, or on what basis.
**Tags:** #compliance #descriptive-statistics #evaluation-metrics #quick-win #confidence-intervals #hypothesis-testing #workflow-orchestration #automation
**Contested on:** Every serious competitor in this niche is fighting to measure and defend a freeze decision whose ground truth returns on a fraction of a percent of cases — and whoever can state a precision with a defensible interval sets the threshold everyone else guesses at.

## The Problem
The number that decides whether a deposit is held was set years ago by a compliance team responding to a vendor's recommendation and an incident. It has been nudged upward after publicity and downward after an examination. There is no record of the rationale, no analysis of what a change would do, and no review cycle. When an examiner asks why it is this number, the answer is that it has been this number.

## Why It's Still Broken
Documenting the rationale was never required at the moment it was set, so the reasoning evaporated with the meeting — and every subsequent adjustment inherited the same habit. Changing it feels risky in both directions and nobody wants to own the change. There is no analysis to base a change on. And the number is invisible in ordinary operations, so nothing forces a review.

## What a Fix Looks Like
Document, analyse, and review on a cycle. Write down the current rationale, even if it is thin, which is the fix and takes an afternoon — an honest record that the basis is historical is infinitely better than an assumed one. Compute what a change would do to volume, using the historical scored cases, since that counterfactual is directly calculable and nobody has run it. Report the current queue impact per threshold band, which shows immediately where the freezes are concentrated. Set a review cadence with a named owner, because a number nobody owns never changes on evidence. Record the rationale for every adjustment going forward, so the next examiner's question has an answer. Show the distribution of scores rather than only the count above the line, since the shape reveals whether the threshold sits somewhere meaningful. Separate thresholds by amount and by customer tenure, because one number for all cases is the crudest possible policy. Track what happens after each adjustment, as the effect on freeze volume and resolution outcomes is observable within weeks. Compare against peer practice where it is discoverable, since being an outlier in either direction is worth knowing. And connect the review to the measurement work, because a threshold reviewed without an estimate is still being guessed.

## Who Feels the Pain
Compliance officers defending a number they did not set; analysts working a queue whose size is arbitrary; customers on the wrong side of an undocumented line; and examiners receiving no rationale.

## Impact If Fixed
The rationale was never required at the moment of setting and evaporated with the meeting. Writing it down and computing the volume counterfactual from historical scores makes the number a decision again rather than an inheritance.
