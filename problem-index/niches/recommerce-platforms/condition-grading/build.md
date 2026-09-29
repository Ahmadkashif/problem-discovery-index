# Two Graders, One Jacket, Two Grades

**Niche:** [[niches/recommerce-platforms/condition-grading/profile|Condition Grading]]
**Industry:** [[industries/recommerce-platforms|Recommerce Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Grading rubrics are written, trained and audited at every serious platform, and two graders looking at the same jacket still assign different grades — which propagates into price, listing and returns.
**Tags:** #cnns #evaluation-metrics #confidence-intervals #hypothesis-testing #descriptive-statistics #object-detection #automation #worker-facing
**Contested on:** Every serious competitor in this sub-niche is fighting to make the same item receive the same grade from any grader at any site — and whoever does that fixes the whole pipeline, because grading is the input that price, listing, buyer expectation and returns all depend on.

## The Problem
The rubric says excellent means minimal signs of wear. One grader reads minimal as almost none; another reads it as consistent with light use. Both are defensible readings of the same sentence, applied at different sites by people trained in different cohorts, and the difference is a whole grade band on a substantial share of items. That band changes the price by a third, changes what the buyer expects, and changes the return rate. The platform audits by sampling and comparing a grader against a senior grader, which measures agreement with one person rather than with a standard, and reports it as accuracy.

## Why Nobody Has Built This
Consistency was never measured, so the variation is known anecdotally and quantified nowhere. There is no reference item to calibrate against because every item is unique, which made the manufacturing calibration approach look inapplicable. The grade is stored as a category and the observations behind it are discarded, which removes the evidence that would support any analysis. And the downstream consequences land in pricing and returns, which are other teams' metrics.

## What to Build
Measure the variation and calibrate against something real. Build a photographic reference library — the same items graded by consensus, circulated to every grader — which solves the unique-item calibration problem and is the foundation, since a standard you can compare to is what the rubric cannot supply in words. Measure inter-grader agreement continuously using replicated photographic grading, which is cheap, does not interrupt production, and produces the number that currently does not exist. Capture the observations rather than the grade: which defects, where, how large, on which materials — a structured record that supports the grade and feeds the pricing model, and which the grader mostly already registers. Use vision to enforce consistency rather than to replace judgement, flagging when a grader's assignment departs from what comparable images received, which is the highest-value application and is not how vision is currently used here. Feed the buyer's verdict back, which the fix note develops. Redefine the rubric in terms of observable features rather than adjectives, since minimal wear cannot be calibrated and two centimetres of pilling on the cuff can. Report per-grader and per-site calibration with drift detection. And measure the downstream effect — price, returns, complaints — by grade agreement, so the cost of inconsistency is quantified for the first time.

## Target Customer
Grading operations, quality functions, the pricing teams downstream, and the sellers and buyers on either side of an inconsistent grade.

## Impact If Built
The rubric is written in adjectives that cannot be calibrated and the audit compares graders to each other rather than to a standard. A consensus-graded photographic reference library supplies the standard, and replicated photographic grading measures the variation without interrupting production.
