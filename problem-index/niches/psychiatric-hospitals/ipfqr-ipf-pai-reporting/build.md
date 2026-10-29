# IPFQR Peer Benchmark and IPF-PAI Pre-Submission Validator

**Niche:** [[niches/psychiatric-hospitals/ipfqr-ipf-pai-reporting/profile|IPFQR Reporting & IPF-PAI Submission]]
**Industry:** [[industries/psychiatric-hospitals|Psychiatric Hospitals]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool tells a psychiatric facility where it stands against comparable facilities in CMS's public data, or which of its IPF-PAI records will fail CMS's checks before it submits, and the benchmark half is a two-week MVP on public data.
**Tags:** #bayesian-inference #descriptive-statistics #hypothesis-testing #k-means-clustering #compliance #quick-win #automation
**Contested on:** Every serious competitor in this niche is fighting to produce a psychiatric facility's IPFQR measures and its new IPF-PAI assessments straight from the record, and whoever submits the highest share of fully complete IPF-PAI assessments takes the account.

## The Problem
A quality director sees her restraint hours, follow-up and readmission rates once a year, against national averages that mix 10-bed units with 300-bed hospitals. From 1 July 2028 she must also submit an assessment her EHR does not yet produce, voluntarily from October 2027, with at least half of all assessments fully complete (Federal Register 2026-15588).

## Why Nobody Has Built This
The instrument is new, the public file is used mostly by journalists and ratings sites, and behavioral EHR vendors are busy with the core record.

## What to Build
The MVP: download the by-facility IPFQR file (1,410 facilities), form peer groups, fit beta-binomial and gamma-Poisson models so small units are shrunk toward their peers, and produce each facility's percentiles with intervals and a one-page summary (ml entry 3). The validator follows: map EHR assessment fields to IPF-PAI items, check every record for missing items and CMS's published edits before submission, report the share fully complete against the 50% and later 70% thresholds, and export the FHIR payload once the specification is final.

## Target Customer
Quality directors at freestanding hospitals and chains; behavioral EHR vendors adding the IPF-PAI.

## Impact If Built
If validation keeps every record inside CMS's checks, a facility with ~$10M of Medicare IPF payments protects the ~$200,000 that a 2-point penalty would cost (estimate).
