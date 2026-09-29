# Release Regression Management

**Parent Industry:** [[industries/saas-implementation-partners|SaaS Implementation Partners]]
**Category:** 🟠 Low Digitized
**Contested on:** Every serious competitor in this niche is fighting to establish whether three platform releases a year have broken any of hundreds of client customisations, using manual test scripts — and whoever automates that takes the account.

## Profile
**Market Size:** ~$7B US
**Share of Parent Industry:** ~12% of category revenue
**Digital Adoption:** Low — manual scripts
**Target Buyer:** Delivery and managed services
**Automation Potential:** Very high — automated regression across tenants

## What Makes This a Distinct Niche
The platform ships three major releases a year, every customisation is a candidate for breakage, and regression testing is a spreadsheet of manual scripts that gets cut when the window is tight. The partner carries the risk across every client it supports, the testing cost scales with the client count, and the thing that actually happens is that a subset of clients discover breakage in production. It is the most predictable recurring cost in the business and the least industrialised.

## Current Tools & Gaps
A test script spreadsheet, a sandbox, and a scramble in the release window. The gaps: no automated regression suites; no impact analysis of what a release affects; no prioritisation of which customisations are at risk; no shared testing across clients with the same pattern; and no record of what broke last time.

## Problems
- [[niches/saas-implementation-partners/release-regression/build|🔨 Build: Testing Every Client Before the Release Lands]]
- [[niches/saas-implementation-partners/release-regression/buy|🛒 Buy: Regression Automation From Software Delivery]]
- [[niches/saas-implementation-partners/release-regression/fix|🔧 Fix: Finding Out From the Client]]
