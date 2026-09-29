# Testing Every Client Before the Release Lands

**Niche:** [[niches/saas-implementation-partners/release-regression/profile|Release Regression Management]]
**Industry:** [[industries/saas-implementation-partners|SaaS Implementation Partners]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Three releases a year against hundreds of client configurations, tested by hand in whatever time is left.
**Tags:** #automation #workflow-orchestration #evaluation-metrics #graph-theory #data-integration #compliance #change-point-detection #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to establish whether three platform releases a year have broken any of hundreds of client customisations, using manual test scripts — and whoever automates that takes the account.

## The Problem
Each platform release is a potential break for every customisation the partner has built, across every client it supports. Testing is manual scripts run by people in a sandbox during a short window. The arithmetic does not work at any meaningful client count, so testing is partial and prioritised by intuition, and some proportion of clients find the breakage in production — which costs the partner its reputation and its managed services margin.

## Why Nobody Has Built This
Test automation on configured enterprise platforms is genuinely awkward, and each client's configuration differs. Testing is a cost centre inside a fixed managed services fee. Nobody has framed the release cycle as a recurring engineering problem. And the client usually blames the platform vendor.

## What to Build
Automate the suites and target them using what the release actually changes. Build automated regression suites per client from the configuration rather than writing scripts by hand, which is the core and is the only approach that scales past a handful of clients. Analyse each release's change notes against each client's configuration to identify what is actually at risk, since testing everything is impossible and testing at random is what happens now. Share test assets across clients using the same patterns, which is where the economics come from. Run against the release preview environment before the release reaches production, which is the entire point. Report per client what was tested, what passed and what is at risk, which is a managed services deliverable clients will pay for. Record what broke in each release so the risk model improves. Prioritise by business criticality rather than by ease of testing. Cover integrations as well as configuration, as those break at least as often. Produce the client-facing release readiness statement automatically. And run it as a service across the client base rather than as a project per client, which is the business this becomes.

## Target Customer
Implementation partners and managed services providers, platform vendors with partner ecosystems, enterprise clients, and test automation vendors.

## Impact If Built
Manual testing does not scale past a handful of clients, so testing is partial and some clients find breakage in production. Configuration-derived automated suites, targeted by what the release actually changes, is what makes the cycle survivable.
