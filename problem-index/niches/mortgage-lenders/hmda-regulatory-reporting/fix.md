# The February Scrub

**Niche:** [[niches/mortgage-lenders/hmda-regulatory-reporting/profile|HMDA & Regulatory Data Reporting]]
**Industry:** [[industries/mortgage-lenders|Mortgage Lenders]]
**Type:** Fix (Pain Point)
**One-liner:** Every year the compliance team spends the weeks before March 1 re-checking a year of HMDA records against the files, because nobody checked them when the loans were made.
**Tags:** #workflow-orchestration #compliance #automation #descriptive-statistics #quick-win
**Contested on:** Every serious competitor in this niche is fighting to produce a HMDA register and NMLS Mortgage Call Report that pass every edit and an examiner's sample test without a pre-deadline scrub, and whoever catches data-field errors at the point of origination rather than in February takes the account.

## The Problem
The annual register is due March 1. Compliance staff and temporary help pull samples or full populations, compare fields with the closing disclosure, the lock record and the application, correct errors and re-run edits. The same mistakes appear every year from the same sources.

## Why It's Still Broken
HMDA accuracy belongs to compliance, but the data is entered by loan officers, processors and closers who are measured on volume and turn time. Corrections are made in the register, not fed back to the people or the system that produced them.

## What a Fix Looks Like
Run the scrub monthly on loans that reached final action that month, send each correction back to the originating team with the reason, track error rates by field and team, and fix the system mappings behind recurring errors.

## Who Feels the Pain
Compliance officers working late in February; HMDA analysts; lenders facing resubmission after an examination.

## Impact If Fixed
The year-end crunch becomes a monthly routine, error rates fall as sources are fixed, and the March filing is a formality.
