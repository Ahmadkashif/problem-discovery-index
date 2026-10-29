# Restraint Hours Abstracted From Handwritten Logs

**Niche:** [[niches/psychiatric-hospitals/ipfqr-ipf-pai-reporting/profile|IPFQR Reporting & IPF-PAI Submission]]
**Industry:** [[industries/psychiatric-hospitals|Psychiatric Hospitals]]
**Type:** Fix (Pain Point)
**One-liner:** HBIPS restraint and seclusion hours are counted by an abstractor reading handwritten start and stop times, so the published numbers depend on handwriting and on whoever did the counting.
**Tags:** #descriptive-statistics #large-language-models #compliance #automation #quick-win
**Contested on:** Every serious competitor in this niche is fighting to produce a psychiatric facility's IPFQR measures and its new IPF-PAI assessments straight from the record, and whoever submits the highest share of fully complete IPF-PAI assessments takes the account.

## The Problem
Restraint orders, monitoring flowsheets and release times sit on paper or in scanned documents. A missing stop time can turn a 20-minute hold into a four-hour one in the count.

## Why It's Still Broken
Restraint documentation is completed during a crisis, and the EHR forms that would capture times automatically are often bypassed for paper.

## What a Fix Looks Like
Structured restraint and seclusion events on a tablet with start, checks and release time-stamped; for legacy scans, an extractor that reads times and flags gaps for the nurse manager before abstraction.

## Who Feels the Pain
Chart abstractors, quality directors and nurse managers answering for outliers.

## Impact If Fixed
If a hospital with ~300 restraint and seclusion episodes a year saves ~20 minutes of abstraction each (estimate), that is ~100 abstractor hours, plus numbers it can trust.
