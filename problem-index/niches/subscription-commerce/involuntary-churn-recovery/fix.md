# Involuntary Churn Pooled With Voluntary

**Niche:** [[niches/subscription-commerce/involuntary-churn-recovery/profile|Involuntary Churn Recovery]]
**Industry:** [[industries/subscription-commerce|Subscription Commerce]]
**Type:** Fix (Pain Point)
**One-liner:** The churn rate combines subscribers who decided to leave with subscribers whose card failed, which are unrelated problems with unrelated owners, and the combined figure directs effort at the wrong one.
**Tags:** #descriptive-statistics #evaluation-metrics #confidence-intervals #revenue-impact #hypothesis-testing #survival-analysis #quick-win #automation
**Contested on:** Every serious competitor in this niche is fighting to recover the subscriber whose card failed rather than the one who chose to leave — and whoever does that keeps the revenue, because a payment failure is a large, mechanical share of churn from customers who never decided anything.

## The Problem
A company reports six percent monthly churn and runs a retention programme against it: better emails, a win-back campaign, a loyalty tier. A quarter of that six percent is payment failure, which none of those things address and which a two-week project on the dunning configuration would substantially reduce. Nobody knows the split, because the churn report counts cancellations and the payment failures arrive as cancellations. The cheapest and most mechanical quarter of the problem is invisible inside a number that directs all the effort at the hardest part.

## Why It's Still Broken
Payment failures terminate as cancellations in the billing system, so they appear in the churn figure with the same event type. The split requires joining the cancellation to its cause, which is a field nobody added. Retention is a marketing function and payment operations is a finance one, so neither owns the combined figure. And the reported number is stable, which reads as correct.

## What a Fix Looks Like
Split the number. Tag every cancellation with voluntary or involuntary at the moment it occurs, which is a single field derived from the cause and is the entire fix — it takes an afternoon and immediately redirects effort toward the cheaper half. Report the two separately in every churn view, since they have different owners, different remedies and different economics. Size the involuntary share and its recoverable portion, which is what makes the business case for the dunning work. Measure the recovery rate as its own metric with a target, rather than as an absence inside a churn figure. Report voluntary churn cleanly, since it is the product signal and is currently contaminated by a payment problem that has nothing to do with the product. Track the involuntary rate by cohort and tenure, since long-standing subscribers' cards fail too and losing them is the most expensive version. Assign clear ownership of the involuntary figure, because it currently sits between two functions and is worked on by neither. And check the split before designing any retention programme, since a programme aimed at a six percent problem that is really a four and a half percent problem plus a mechanical one is misdirected from the start.

## Who Feels the Pain
Retention teams working on the hard half while the easy half goes unaddressed; subscribers cut off without deciding anything; and operators whose product signal is contaminated by a payments problem.

## Impact If Fixed
One field derived from the cause splits a number that currently directs all the effort at the hardest part. Reporting voluntary churn cleanly also decontaminates the product signal that the retention work depends on.
