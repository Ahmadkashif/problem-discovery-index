# Diagnose the Condition, Not the Person

**Niche:** [[niches/hr-tech-platforms/people-analytics-attrition/profile|People Analytics & Attrition]]
**Industry:** [[industries/hr-tech-platforms|HR Tech Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Attrition is produced by structural conditions that are computable months in advance, and the products that have attempted prediction have produced individual flight-risk scores — which is the same data pointed at the wrong object.
**Tags:** #survival-analysis #gradient-boosting #causal-inference #confidence-intervals #evaluation-metrics #hypothesis-testing #compliance #revenue-impact
**Contested on:** Every serious competitor in people analytics is fighting to diagnose the structural conditions that produce attrition months before the resignations — and whoever names the condition rather than scoring the person takes the account.

## The Problem
An engineering team loses five people in a quarter. The post-mortem identifies a manager problem. The actual conditions, visible in the system for the preceding year: everyone on that team was hired more than three years ago and is paid twelve percent below what the last four external hires into the same level received; the manager's span went from six to nineteen after a reorganisation; nobody on the team has been promoted in two years while the adjacent team promoted four; and there is no defined path from their job family into any other. Each of those is a condition with a name, a measurement and a remedy, and each was computable in month two.

## Why Nobody Has Built This
The obvious product — a flight risk score per employee — is easier to build and sells more readily, and several vendors have built it. It is also the wrong thing, and the reasons are not merely ethical: a score without a cause supports no action except a retention bonus or a quiet decision to stop investing in someone, the second of which is the use it will actually be put to in some organisations. Building the diagnostic version requires modelling conditions rather than people and requires the vendor to take a position about what the product must not do, which is a harder product to specify and an easier one to defend.

## What to Build
A diagnosis of conditions at the unit level, with the individual-level modelling used internally and never exposed as a per-person score. Pay compression measured against the organisation's own external hiring, which is the most consequential and most computable driver and is one almost no company monitors. Span of control against the distribution for comparable roles, with the attrition effect estimated from the organisation's own history. Promotion velocity by cohort, surfacing groups whose progression has stalled relative to comparable groups. Mobility path presence per job family, which is a structural property rather than a statistic. Manager change and reorganisation exposure. Each condition is reported per team with its estimated attrition contribution, an interval, and the remedy — which is a compensation adjustment, a span correction, a promotion review or a mobility path, all of which are actions an organisation can take. The architectural commitment is that individual risk is never surfaced; it exists in the model and terminates there, and the product should say so plainly and make it structurally true rather than a policy.

## Target Customer
People analytics vendors, HCM incumbents whose retention capability is a turnover report, and directly the chief people officers who are asked about attrition and can currently answer only with a number.

## Impact If Built
Attrition costs are large and the drivers are actionable, which is an unusual combination — pay compression and span of control in particular are correctable with decisions rather than with culture programmes. The design constraint is the product's credibility: an organisational diagnostic gets adopted by leaders and tolerated by employees, and a flight risk score gets leaked and poisons the category for everyone.
