# Two LPs, Two Answers

**Niche:** [[niches/private-equity-firms/lp-reporting-and-ddq/profile|LP Reporting & Fundraising Due Diligence]]
**Industry:** [[industries/private-equity-firms|Private Equity Firms]]
**Type:** Fix (Pain Point)
**One-liner:** During a fundraise, the same question about a deal's performance or a team departure gets answered slightly differently to different LPs, and nobody notices until one LP compares notes.
**Tags:** #large-language-models #word-embeddings #evaluation-metrics #compliance #quick-win
**Contested on:** Every serious competitor in this niche is fighting to answer the same LP questions consistently — across quarterly reports, forty due diligence questionnaires and the data room — with every track-record figure reconciling to the administrator, because inconsistency is what an LP or examiner notices first.

## The Problem
IR staff and partners answer questionnaires and follow-ups under time pressure, often from memory or from a previous answer that has since been updated. Numbers move as quarters close. LPs talk to each other and to consultants who see many DDQs.

## Why It's Still Broken
No system holds the set of answers given; each DDQ is a separate Word file. Reviewing all of them for consistency is a manual task nobody has time for in a fundraise.

## What a Fix Looks Like
Store every answer sent, per LP and date, in one index. Before sending, compare each new answer semantically against prior answers to the same question and numerically against the track-record master, and flag differences for review.

## Who Feels the Pain
IR leads and CCOs carrying the reputational and regulatory exposure; partners whose credibility suffers from inconsistent numbers.

## Impact If Fixed
A simple consistency check removes one of the most avoidable sources of LP mistrust in a fundraise.
