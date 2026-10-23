# Scoping by Where Red Flags Have Actually Been Found

**Niche:** [[niches/investigation-and-screening-firms/corporate-due-diligence-vetting/profile|Corporate Due Diligence & Executive Vetting]]
**Industry:** [[industries/investigation-and-screening-firms|Investigation & Background Screening Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Due diligence firms scope every report by analyst habit and price tier, when their own history could say which sources produce red flags for which kind of subject in which country.
**Tags:** #tacit-knowledge-ml #gradient-boosting #feature-engineering #evaluation-metrics #compliance #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to surface the disqualifying fact about a person or counterparty that a database screen misses before the signing or appointment date, and whoever delivers the most corroborated red flags inside that date takes the account.

## The Problem
A senior analyst scoping a report on a distributor in Southeast Asia or a founder with a career in three countries knows from experience that the corporate registry will be thin, the local-language business press is where disputes surface, and that insolvency filings in one jurisdiction are worth the retrieval fee. A junior analyst follows the tier template and searches everything at the same depth. Neither has data on which searches have historically produced findings for similar subjects.

## Why Nobody Has Built This
Findings sit in client-confidential reports, written as prose. Firms rightly will not reuse one client's findings for another, and nobody has separated the reusable part — which source types produced findings, for what subject profile, at what cost — from the confidential part.

## What to Build
An anonymised source-yield record kept per engagement: subject type, jurisdictions, sources searched, time and cost per source, and whether each produced a finding graded by severity, with no subject identities or findings carried across. A model on that record recommends scope for a new engagement by risk tier and jurisdiction, highlights sources with high historical yield, and flags low-yield searches that consume budget.

## Target Customer
Heads of due diligence practices and research directors at corporate investigation firms producing hundreds to thousands of reports a year.

## Impact If Built
Analyst time moves to the sources most likely to find something, junior analysts scope like senior ones, and fixed-fee tiers become more profitable without becoming shallower.
