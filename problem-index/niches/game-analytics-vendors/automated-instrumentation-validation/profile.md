# Automated Instrumentation Validation

**Parent Industry:** [[industries/game-analytics-vendors|Game Analytics Vendors]]
**Category:** ⚡ Highly Automatable
**Contested on:** Every serious competitor in this niche is fighting to catch broken instrumentation when it breaks rather than when a metric looks wrong weeks later — and whoever automates that check takes the account.

## Profile
**Market Size:** ~$70M US
**Share of Parent Industry:** ~6% of category revenue
**Digital Adoption:** Low — manual
**Target Buyer:** Data engineering
**Automation Potential:** Very high — continuous validation

## What Makes This a Distinct Niche
The first sign that instrumentation broke is usually a metric that looks wrong. An event stops firing after a refactor, a parameter starts arriving null, a client change alters a value's meaning — and the data flows into every downstream report until someone notices something implausible, typically weeks later, after decisions have been made on it. Every one of these failures is detectable within hours by comparing what arrives against what is expected.

## Current Tools & Gaps
A pipeline that accepts what it is sent, and an analyst who notices eventually. The gaps: no expected-volume baselines per event; no null and distribution checks; no per-version validation; no alerting on instrumentation failure; and no test of instrumentation before a build ships.

## Problems
- [[niches/game-analytics-vendors/automated-instrumentation-validation/build|🔨 Build: Catching the Break When It Breaks]]
- [[niches/game-analytics-vendors/automated-instrumentation-validation/buy|🛒 Buy: Data Quality Monitoring From Data Engineering]]
- [[niches/game-analytics-vendors/automated-instrumentation-validation/fix|🔧 Fix: The Event That Stopped Firing in March]]
