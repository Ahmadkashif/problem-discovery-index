# Twelve Agency Formats, Twelve Templates

**Niche:** [[niches/court-reporting-firms/administrative-arbitration-hearings/profile|Administrative, Arbitration & Public Hearings]]
**Industry:** [[industries/court-reporting-firms|Court Reporting Firms]]
**Type:** Fix (Pain Point)
**One-liner:** A regional firm serving a dozen agencies keeps a dozen hand-built transcript templates, and every rule change by one agency is found when a filing bounces.
**Tags:** #large-language-models #seq2seq #compliance #automation #quick-win
**Contested on:** Every serious competitor in this niche is fighting to be the reporter of record under a forum's or agency's master contract, delivering transcripts in its format with exhibits tied to its docket before post-hearing briefs are due, and whoever meets the forum's turnaround at the contract rate takes the account.

## The Problem
Each agency specifies its own caption, appearance page, line numbering, certificate wording, exhibit index and file format for e-filing. Production staff keep templates in the CAT software and in Word, and remember each agency's quirks. When an agency changes its rules, the first sign is often a rejected filing.

## Why It's Still Broken
Agency rules live in contract documents and procedural orders, not in machine-readable form, and the work is too small for CAT vendors to build per-agency formats.

## What a Fix Looks Like
A format library per forum, built by extracting requirements from contracts and procedural rules with a language model and checked by a production lead. Every outgoing transcript is validated against it before filing, and changes to agencies' published rules are monitored.

## Who Feels the Pain
Production coordinators; reporters re-formatting at night; agencies receiving non-conforming transcripts.

## Impact If Fixed
Fewer rejected filings, faster onboarding of new contracts, and production knowledge that survives staff turnover.
