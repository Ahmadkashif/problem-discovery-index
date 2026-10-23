# A Regime-Aware Account Register for Every Client and State

**Niche:** [[niches/professional-employer-organizations/suta-multistate-payroll-tax/profile|Multi-State Payroll Tax & SUTA Account Administration]]
**Industry:** [[industries/professional-employer-organizations|Professional Employer Organizations]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No system records, for each client and state, which unemployment account the PEO must report under, at what rate, on whose experience, and why.
**Tags:** #large-language-models #decision-trees #change-point-detection #evaluation-metrics #compliance #automation #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to report and pay unemployment tax under the right account and rate for every client in every state, whether the state wants PEO-level, client-level or hybrid reporting, and whoever closes each year with no rate-notice errors, misapplied wage bases or penalty notices takes the account.

## The Problem
A PEO with clients in forty states holds thousands of client-state combinations. For each it must know the reporting regime, the account in use, any authorisation on file, the current rate and its source, and what happens when the client leaves. Vendor summaries of the regimes disagree: Deel and Justworks classify states differently in places, and the rules change. Analysts carry the exceptions in memory.

## Why Nobody Has Built This
Payroll tax engines store rates per account but not the reasoning, the regime or the lifecycle. The regime rules sit in state statutes, agency bulletins and NAPEO state updates, never compiled into one maintained rule set.

## What to Build
A register keyed by client and state. It holds a maintained rule set per state (regime, exceptions, authorisation forms, successor and transfer rules, SUTA-dumping guardrails) with citations. Each client-state entry carries its account, rate, rate source and effective dates. Lifecycle workflows cover onboarding, a new work state and termination. Every rate notice and agency letter is extracted and reconciled against the register, and changes in a client's effective rate that no notice explains are flagged.

## Target Customer
Directors of payroll tax at PEOs with multi-state client books, and PEO platform vendors that could license it.

## Impact If Built
Accounts and rates right from day one, notices answered from a record rather than a search, and knowledge that survives when the analyst who held it leaves.
