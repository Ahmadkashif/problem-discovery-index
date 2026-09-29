# Recovery Without a Person

**Niche:** [[niches/data-platform-integrators/the-oncall-pipeline-engineer/profile|The On-Call Pipeline Engineer]]
**Industry:** [[industries/data-platform-integrators|Data Platform Integrators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The same failure, the same recovery, the same message, several times a week, at four in the morning.
**Tags:** #worker-facing #automation #workflow-orchestration #change-point-detection #evaluation-metrics #data-integration #descriptive-statistics #graph-theory
**Contested on:** Every serious competitor in this niche is fighting to stop one engineer rerunning, backfilling and explaining overnight failures before the morning reports go out — and whoever automates that recovery takes the account.

## The Problem
Overnight pipeline failures follow a small number of patterns: an upstream extract arrived late, a source was briefly unavailable, a schema changed, a job hit a resource limit, a dependency ran long. The recovery is equally patterned: establish what failed and what it blocked, rerun in the right order, backfill the missed window, verify, and tell the people whose reports are affected. All of it is done manually by one person under time pressure.

## Why Nobody Has Built This
Orchestrators retry naively and stop there. Backfill logic is written per pipeline or not at all. Impact assessment requires lineage nobody has wired into the alert. And the engineer absorbing it means the recurrence never surfaces as a problem worth engineering.

## What to Build
Automate the recovery for the causes that recur and tell people automatically. Classify failures by cause and apply the known recovery automatically for the recurring ones, which is the core and removes most of the night work. Handle late-arriving upstream data with dependency-aware waiting and rescheduling rather than failing, since that is the commonest cause and is not a failure at all. Backfill automatically with correct windowing rather than leaving it to a person to reason about at four in the morning. Assess and report impact from lineage — which reports are affected, which consumers should be told — so the alert arrives with its consequences. Notify affected consumers automatically, which is the task the engineer does last and worst. Escalate only the genuinely novel failures to a person, which is what makes on-call sustainable. Record every failure and recovery so the recurring set is known and shrinking. Fix the recurring causes rather than automating around them indefinitely, which is where the actual improvement is. Report overnight incident volume per week as a metric leadership sees. And schedule around the upstream reality rather than a window somebody chose years ago.

## Target Customer
Data platform teams and integrators, platform operations leadership, orchestration and observability vendors, and managed services providers.

## Impact If Built
The same handful of causes produce the same recovery sequence several times a week at an unsociable hour. Automatic classification and recovery, with impact-aware notification, removes most of it and makes the rest sustainable.
