# An Acceptance Ledger That Grades Every Quote

**Niche:** [[niches/professional-employer-organizations/new-client-health-underwriting/profile|New-Client Health Underwriting]]
**Industry:** [[industries/professional-employer-organizations|Professional Employer Organizations]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** PEOs keep every quote file and every client's claims, and have never joined the two to learn which underwriting calls, risk flags and overrides predict a group that blows up the plan.
**Tags:** #tacit-knowledge-ml #gradient-boosting #survival-analysis #bayesian-inference #large-language-models #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to decide, from a census, a few health questionnaires and a prescription-history score, which 25-person prospects to admit to the master plan and at what rate before the broker's quote deadline, and whoever's admitted groups run closest to their priced loss ratio in the first plan year takes the account.

## The Problem
An underwriter approves, rates up or declines dozens of groups a week in quote season. Sales leadership overrides some declines to close a deal. A year later a few of those groups are running at 150% MLR, but nobody can say whether the underwriter flagged them, whether they were overrides, or whether the morbidity score had already warned. The deck that reported 25 of every 165 groups running far worse than forecast also says plainly: "we shouldn't override declines". Without a ledger, nobody can show how often overrides cost money.

## Why Nobody Has Built This
Quote files live in one system and claims in the carrier's reports. Decision reasons are in notes and email. Small-group outcomes are noisy enough that a naive scorecard would punish good underwriters for bad luck, so actuaries distrust the idea. Questionnaire data is protected health information, which keeps it out of general analytics.

## What to Build
A ledger capturing every quote's inputs, decision, price relative to manual, override and approver, plus two or three reason tags the underwriter confirms in a click, drafted by a language model from their notes. Each admitted group is followed through credibility-weighted loss ratios, with reject inference for declines and survival handling for early leavers. The ledger then grades underwriters, brokers, risk flags and overrides, and serves comparables at quote time: "the twelve most similar groups we admitted, and how they ran."

## Target Customer
Heads of new-business underwriting and chief underwriting officers at the top 30 PEOs, each writing thousands of quotes a year.

## Impact If Built
A PEO can show its board which overrides and channels cost money and stop them, and a new underwriter inherits the best underwriter's track record rather than starting cold.
