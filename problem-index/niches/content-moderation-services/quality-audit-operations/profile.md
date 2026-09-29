# Quality Audit Operations

**Parent Industry:** [[industries/content-moderation-services|Content Moderation Services]]
**Category:** Highly Automatable
**Contested on:** Whether audit effort is spent where it would change a judgement, or spread uniformly across a sample drawn at a rate the contract specified.

## Profile

**Market Size:** ~$600M
**Share of Parent Industry:** ~5%
**Digital Adoption:** Low — random sampling and manual re-review
**Target Buyer:** Vendor quality operations, platform audit teams
**Automation Potential:** Very high — it is sampling, routing and consistency checking

## What Makes This a Distinct Niche

Underneath the quality metric is an operation: auditors pulling samples, re-reviewing items, scoring against policy, running calibration sessions, compiling reports and feeding results into performance management. It is a substantial function — commonly several per cent of total headcount — and it runs on a design that has not changed in a decade.

The design is uniform random sampling at a contractually specified rate. Every reviewer's decisions are sampled at the same rate, items are drawn without regard to how likely they are to be wrong, and auditors spend the bulk of their time re-reviewing decisions that were obviously correct. The information content of the audit programme is concentrated in a small fraction of the items it examines, and the sampling has no way to find them.

This is a separate market from the measurement question because the contest here is operational rather than methodological. [[niches/content-moderation-services/decision-quality/profile|🔵 Decision Quality Measurement]] argues about what quality means; this niche argues about how to spend a fixed auditing budget to learn the most. Sitting alongside [[niches/content-moderation-services/workforce-planning/profile|⚡ Workforce Planning & Scheduling]], it is pure efficiency work in an industry that otherwise sells judgement.

## Current Tools & Gaps

Quality management modules inside the contact-centre platforms these vendors run — sample selection, scorecards, evaluator workflow, reporting — supplemented by spreadsheets and by client-supplied audit tooling. Calibration sessions where auditors discuss contested items and try to align. Client-side audits running in parallel on their own samples, sometimes reaching different conclusions on the same reviewers.

The gaps are mostly about where effort goes. Sampling is uniform when it could be risk-weighted, so auditing spends most of its capacity confirming the obvious. Auditors are themselves unaudited in most operations, so auditor drift and severity differences go undetected and are silently attributed to the reviewers they grade. Nothing checks the audit programme's own statistical adequacy — whether the sample can distinguish the reviewers it is used to rank. Calibration is a discussion rather than a measurement, so alignment is asserted rather than demonstrated. And auditors, who are experienced reviewers doing re-review, carry substantial exposure that no exposure programme counts.

## Problems

- [[niches/content-moderation-services/quality-audit-operations/build|🔨 Build: Risk-Weighted Audit Sampling]]
- [[niches/content-moderation-services/quality-audit-operations/buy|🛒 Buy: Statistical Sampling From Financial Audit]]
- [[niches/content-moderation-services/quality-audit-operations/fix|🔧 Fix: Nobody Audits the Auditors]]
