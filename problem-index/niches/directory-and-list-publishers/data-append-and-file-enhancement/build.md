# Match Confidence Disclosed per Appended Field

**Niche:** [[niches/directory-and-list-publishers/data-append-and-file-enhancement/profile|Data Append & File Enhancement]]
**Industry:** [[industries/directory-and-list-publishers|Directory & List Publishers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An append vendor returns a phone number for most of a client's file and says nothing about which of those numbers belong to the right person.
**Tags:** #logistic-regression #gradient-boosting #evaluation-metrics #confidence-intervals #feature-engineering #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to append the most correct fields to a client's file — a match rate at a stated accuracy — and whoever proves the higher verified match rate on the client's own test file wins the job.

## The Problem
A nonprofit appends phones to its donor file for a telephone campaign. The vendor reports a high match rate. Callers find that a meaningful share of numbers reach someone else with a similar name, a former household, or a disconnected line, and the campaign underperforms with no way to know which records to trust.

## Why Nobody Has Built This
Match-rate tests reward volume, and disclosing confidence would show that some of the volume is guesswork; clients rarely feed back which appended values were right.

## What to Build
Per-field match confidence calibrated on held-out truth (call outcomes, bounces, client feedback), delivered with every appended value, plus a test-file report that shows match rate at several confidence thresholds so clients can compare vendors on matched-and-correct rather than matched. The compiler learns from every client that returns outcomes.

## Target Customer
Compilers and service bureaus selling append; database marketing and nonprofit data managers who buy it.

## Impact If Built
Clients use appended data where it is reliable, and the honest matcher can finally win the test.
