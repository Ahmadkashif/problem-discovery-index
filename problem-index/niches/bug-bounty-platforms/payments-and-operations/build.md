# Build: The Invisible Operations Layer

**Niche:** Payments & Programme Operations
**Industry:** [[industries/bug-bounty-platforms|Bug Bounty Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Programme operations that run without attention — policy-driven payout approval, budget controls a manager can express in rules, and reward tables that reconcile against what was actually paid.
**Tags:** #evaluation-metrics #confidence-intervals #time-series-forecasting #workflow-orchestration #automation #compliance #revenue-impact
**Contested on:** Whether the administrative shell around a programme runs itself or consumes staff attention every cycle.

## The Problem

A programme manager's week contains a surprising amount of administration. Payout approvals, individually, because the budget control is a total rather than a policy. Budget reconciliation against accruals that do not match because severity was revised after the accrual. Reward table questions from researchers whose finding falls between bands. Quarterly forecasting for a spend whose driver — how many valid findings arrive — nobody models.

None of it is the job. The job is scope, triage quality and the researcher relationship, and every hour of administration is taken from those.

The researcher side has its own friction. A finding is accepted, then approved, then paid, and the intervals between those events are unpredictable and unreported. For someone whose income is irregular and international, that uncertainty is a real cost, and it is one platforms consider solved because the money does arrive.

And the reward table — the document that determines what everything pays — is typically set at launch and left. Nobody reconciles what the programme actually paid against what the table says, so the stated ranges drift away from reality and researchers make decisions on numbers that no longer describe anything.

## Why Nobody Has Built This

**It is already good enough.** Cross-border payment works, budgets are tracked, and nothing is visibly broken. Incremental operational polish competes badly against features that affect the marketplace directly.

**The remaining friction is distributed.** No single operational annoyance is large enough to fund a project; the cost is the sum of many small ones spread across many programmes.

**Researcher-side friction is not the platform's cost.** Payment timing uncertainty and tax complexity are absorbed by the supply side, which does not pay fees and does not appear in the operational budget.

**Budget policy needs severity to be stable and it is not.** A rule-based spending policy depends on severity assessments that get revised, which makes accruals and forecasts genuinely harder than they look.

**Programme configuration is bespoke by nature.** Every programme has a different scope, reward structure and workflow, which resists productisation into a launch template.

## What to Build

**Policy-driven payout approval.** Instead of approving each payout, a programme expresses rules: auto-approve below a threshold, auto-approve for this severity band from researchers above a reputation level, escalate anything above an amount or outside policy. Most approvals stop requiring attention and the exceptions get real scrutiny, which is a better allocation of both.

**Budget controls a manager can actually express.** Caps per period, per finding class and per asset tier, with alerting on trajectory rather than only on the total. Programmes currently manage spend by watching a number and reacting.

**Forecast spend from the arrival process.** Valid findings per period, modelled from the programme's own history plus scope changes and researcher participation, producing an expected spend range rather than last year's number. Finance asks for this every quarter and programme managers guess.

**Reconcile the reward table against reality.** What each finding class actually paid over the last period against what the table says. Drift is universal and invisible, and correcting it makes the table an honest statement of what a researcher can expect — which is the information they most need before choosing a target.

**Publish payment timing to researchers.** Median and distribution of accepted-to-paid interval, per programme, visible in advance. This costs nothing, and for people with irregular income it is one of the more valuable things a platform could surface.

**Extend tax support past the form.** Partnership with the independent-worker financial services that already exist, offered to researchers. The platform does not need to build it, only to connect it.

**Template programme launch.** A configuration flow that produces scope, reward table, workflow and disclosure terms from a small number of decisions, with sensible defaults drawn from comparable programmes. Every programme rebuilds this and most would rather not.

## Target Customer

Platform operations, where the payout policy engine and the budget tooling reduce support load and programme-manager friction directly.

Programme managers as the users, particularly those running several programmes or a programme alongside another full-time role — which is most of them.

Finance functions, for the forecasting, which is currently a recurring annoyance with no analytical basis.

## Impact If Built

Programme managers get their week back for the work that actually determines programme quality, which is scope, triage and the researcher relationship.

Reconciling the reward table against actual payments makes the single most consulted document in the programme honest, which improves researcher targeting decisions at no cost.

And publishing payment timing removes a real, unacknowledged friction from the supply side of a market whose supply is its product.
