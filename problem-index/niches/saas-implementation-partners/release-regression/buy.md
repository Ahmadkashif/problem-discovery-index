# Regression Automation From Software Delivery

**Niche:** [[niches/saas-implementation-partners/release-regression/profile|Release Regression Management]]
**Industry:** [[industries/saas-implementation-partners|SaaS Implementation Partners]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Software made automated regression testing on every change routine, and configured enterprise platforms are tested by hand three times a year.
**Tags:** #automation #workflow-orchestration #evaluation-metrics #compliance #data-integration #change-point-detection #descriptive-statistics #graph-theory
**Contested on:** Every serious competitor in this niche is fighting to establish whether three platform releases a year have broken any of hundreds of client customisations, using manual test scripts — and whoever automates that takes the account.

## The Problem
Software delivery made automated regression testing universal: suites run on every change, across a matrix of configurations, with failures attributed to what changed and test selection narrowing the run. It is inexpensive, commoditised and expected. Configured enterprise platforms — where the risk is identical and the client count multiplies it — are tested by people running scripts from a spreadsheet during a release window.

## What Already Exists
Automated regression suites; matrix execution across configurations; change-scoped test selection; failure attribution; and continuous execution against pre-release builds.

## The Customization Gap
The adaptation is to configuration in client-owned tenants rather than code in a repository. It requires: (1) the system under test being a client's live tenant configuration rather than a build the partner controls, so tests must be generated per tenant and run in client environments — this is the substantive difference; (2) tests derived from configuration metadata rather than written alongside code; (3) a release schedule set by the platform vendor rather than by the team; (4) hundreds of separate tenants multiplying the matrix; and (5) client data and access constraints governing what can be tested and where.

## Target Customer
Implementation partners and managed services providers, platform vendors, enterprise clients, and test automation vendors.

## Impact If Solved
Software made regression automation commoditised and expected on every change. Tests generated per client tenant from configuration metadata, run on the vendor's release schedule, is what the enterprise version requires.
