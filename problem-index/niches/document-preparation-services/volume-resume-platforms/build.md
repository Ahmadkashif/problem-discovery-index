# Writer Matching on Predicted Revision Risk

**Niche:** [[niches/document-preparation-services/volume-resume-platforms/profile|Volume Resume Platforms & Writer Networks]]
**Industry:** [[industries/document-preparation-services|Document Preparation Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Platforms assign orders by industry tag and availability, though their own order history shows which writer-client pairings end in extra revisions and refunds.
**Tags:** #gradient-boosting #logistic-regression #feature-engineering #evaluation-metrics #revenue-impact #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to turn a questionnaire and an old resume into a keyword-matched, ATS-readable resume in the fewest paid writer-hours, and whoever holds revision and refund rates down at a flat per-order writer fee takes the account.

## The Problem
A mid-career nurse moving into health IT, a laid-off engineering manager and a new graduate land in the same queue. The platform matches each to an available writer tagged for the field. Some pairings go smoothly; others run to extra revision rounds, escalations and refunds, and each one eats the order's margin and the writer's unpaid time.

## Why Nobody Has Built This
Matching has been treated as dispatch, not prediction. The outcome signals (revision count, escalation, refund, satisfaction) sit in support tickets and order logs that were never joined to writer and client features.

## What to Build
A model trained on order history that predicts revision and refund risk for each candidate writer on an incoming order. It uses client features (career change or not, seniority, gaps, questionnaire completeness, tone of intake messages), writer features (per-segment revision history, current load) and package. Orders go to the writer with the lowest predicted cost at acceptable turnaround, and high-risk orders get a senior writer or an intake call before drafting.

## Target Customer
Writer-operations and finance leads at volume resume platforms.

## Impact If Built
Fewer revision rounds and refunds per hundred orders, writers paid for work that ends, and margin recovered without cutting writer fees.
