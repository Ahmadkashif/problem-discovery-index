# Churn Risk With Measured Lead Time

**Niche:** [[niches/crm-platforms/customer-success-post-sale/profile|Customer Success & Post-Sale]]
**Industry:** [[industries/crm-platforms|CRM Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A churn prediction is only worth anything if it arrives while the account can still be saved, and no customer success platform reports how much warning its health score actually provides.
**Tags:** #survival-analysis #gradient-boosting #change-point-detection #confidence-intervals #evaluation-metrics #cross-validation #revenue-impact #causal-inference
**Contested on:** Every serious competitor in customer success software is fighting to identify a renewal at risk early enough that intervention still works — and whoever predicts churn with real lead time takes the account.

## The Problem
An account's health score turns red six weeks before renewal. The customer success manager escalates, an executive call is arranged, a discount is offered, and the account churns anyway — because the decision was made four months earlier when the champion left and the team that used the product most moved to a competitor's tool. The signals were present then: a sharp drop in one team's usage, a cluster of support tickets about an integration, an unanswered quarterly business review invitation, and a LinkedIn change nobody noticed. The score used recency-weighted login counts and turned red when the account was already gone.

## Why Nobody Has Built This
Health scores were built as configurable weighted sums because customers wanted to encode their own beliefs about what matters, which is a reasonable product decision that removed the possibility of learning. Fitting the weights to outcomes requires enough churn events to learn from, which a single mid-size customer does not have — the answer is cross-customer modelling, which raises the same corpus governance question that recurs throughout this vault and that most vendors have declined to open. And lead time has never been the metric: accuracy is reported, if at all, as whether the score was red at renewal, which is a definition under which a score that turns red the day before is perfect.

## What to Build
A churn hazard estimated from usage, support, engagement and relationship signal, with lead time as the headline metric. Survival modelling gives a hazard over time rather than a score at a point, which is the correct shape — the question is when this account is likely to leave and how confident we are, not whether it is currently amber. Features span the systems the signal lives in: per-team and per-feature usage trajectories rather than aggregate logins, support ticket sentiment and resolution quality, executive and champion engagement, contractual and commercial events, and champion departure detected rather than noticed. Cross-customer fitting with per-customer adaptation solves the sparse-events problem the same way the vertical SaaS niches do. And the product is measured on lead time at a given precision — how many months of warning does this produce on accounts that actually churned — which is the number a customer success leader needs and no vendor publishes.

## Target Customer
Customer success platform vendors, CRM incumbents extending post-sale, and directly the recurring-revenue businesses whose renewal base is larger than their new business.

## Impact If Built
Net revenue retention is the metric that determines the valuation of a recurring-revenue business, and the function charged with it operates on a configured heuristic. Lead time is the whole value: a prediction six months out permits a relationship intervention, and one six weeks out permits a discount. Publishing lead time changes what the category competes on.
