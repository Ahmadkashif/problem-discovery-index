# The RFE That Nobody Learns From

**Niche:** [[niches/legal-practice-software/immigration-practice-platforms/profile|Immigration Practice Platforms]]
**Industry:** [[industries/legal-practice-software|Legal Practice Software]]
**Type:** Fix (Pain Point)
**One-liner:** A request for evidence is the adjudicator telling the firm exactly what its filing lacked, arriving as a structured, categorised, free lesson — and every firm files the response and throws the lesson away.
**Tags:** #bert #large-language-models #descriptive-statistics #evaluation-metrics #hypothesis-testing #compliance #automation #quick-win
**Contested on:** Every serious competitor in immigration case management is fighting to keep an open case's forms, evidence set and procedural posture correct when the policy underneath it changes mid-case — and whoever propagates a policy change across an active caseload fastest takes the account.

## The Problem
An RFE arrives. A paralegal reads it, assembles the requested material, files a response, and moves on. The case eventually approves. What is never recorded is what the RFE asked for, in a form that can be counted — so the firm cannot say that 40% of its RFEs in one benefit category concern the same evidentiary element, which would tell it precisely what to change in every future filing of that type. Each RFE is treated as an event about one case rather than as a measurement of the firm's filing practice, and the information is thrown away hundreds of times a year.

## Why It's Still Broken
RFEs arrive as PDFs and are stored as documents. Nobody has classified them because nobody's job is to, and because the benefit is diffuse — the paralegal handling this RFE gains nothing from the classification, and the firm's gain accrues to filings that have not happened yet. There is also a mild reluctance to look: a partner who discovers that a recurring RFE pattern was avoidable has discovered that the firm has been costing its clients months, repeatedly, for years.

## What a Fix Looks Like
Classify every RFE against a taxonomy of evidentiary elements, which is ordinary text classification on documents the firm already holds, and join the classification to the case's benefit type, service center, filing date and the evidence that was actually submitted. That produces the firm's standing RFE report: the most common elements challenged, by benefit type, with trend — and the trend matters, because a rising element usually means an adjudicative standard shifted before any policy document said so, which is the earliest signal available of exactly the change the build note is trying to catch. Feed the top elements straight into the pre-filing checklist so the correction is applied rather than merely known. The backfill over the last two years of stored RFEs is a weekend of work and produces the whole picture immediately.

## Who Feels the Pain
Paralegals assembling the same missing element for the fiftieth time without anyone noticing it is the fiftieth; clients whose cases are delayed months by an omission the firm could have anticipated; and lawyers who sense a standard has tightened and have no evidence to act on.

## Impact If Fixed
Firms that classify their RFE history typically find a small number of elements accounting for most requests in their highest-volume benefit types, and correcting those at the checklist level is immediate. The rising-element signal is the more interesting output: it is the only mechanism in this practice area for detecting an unannounced change in adjudicative practice from a firm's own data.
