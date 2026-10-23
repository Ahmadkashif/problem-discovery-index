# Two Auditors, Two Scores

**Niche:** [[niches/document-preparation-services/transcript-qa-accuracy-scoring/profile|Transcript QA & Accuracy Scoring]]
**Industry:** [[industries/document-preparation-services|Document Preparation Services]]
**Type:** Fix (Pain Point)
**One-liner:** The same report scored by two auditors can pass with one and fail with the other, and the editor's pay depends on which auditor drew it.
**Tags:** #hypothesis-testing #descriptive-statistics #evaluation-metrics #worker-facing #quick-win
**Contested on:** Every serious competitor in this niche is fighting to produce an accuracy score that the client, the vendor and the editor all accept as the basis for service credits and pay, and whoever scores every transcript by error severity, not a hand-checked sample, at auditor-level agreement takes the account.

## The Problem
Severity calls are judgement calls: is a misheard drug name with the right dose critical or noncritical, is a missing qualifier a meaning change? Under a scoring method where one critical error fails a report, a single disagreement flips the result. Editors dispute scores, and auditors hold calibration meetings that rarely produce numbers.

## Why It's Still Broken
Agreement between auditors is seldom measured, so drift is invisible. Disputes are resolved case by case without updating the rubric.

## What a Fix Looks Like
Double-score a small random share of audits blind, compute agreement by category and auditor each month, and publish it to the QA team and editors. Turn resolved disputes into worked examples in the rubric, and weight scores so that no single auditor's strictness moves an editor's pay.

## Who Feels the Pain
Editors whose income depends on the score; auditors defending calls they can't prove; vendors arguing service credits with clients.

## Impact If Fixed
A score editors can trust, fewer disputes, and a QA programme that can show its own consistency to a client.
