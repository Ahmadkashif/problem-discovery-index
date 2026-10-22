# The Producer Rationale Pasted Into Forty Files

**Niche:** [[niches/life-insurance-carriers/annuity-suitability-review/profile|Annuity Suitability & Best-Interest Review]]
**Industry:** [[industries/life-insurance-carriers|Life Insurance Carriers]]
**Type:** Fix (Pain Point)
**One-liner:** The best-interest rule requires a rationale specific to the client, and reviewers see the same paragraph from the same producer file after file without any tool to notice.
**Tags:** #word-embeddings #k-nearest-neighbors #large-language-models #compliance #quick-win
**Contested on:** Every serious competitor in this niche is fighting to clear each annuity sale's best-interest review before issue with a record a market conduct examiner accepts, and whoever auto-clears the most files without missing an escalation a senior reviewer would have caught takes the account.

## The Problem
A producer's rationale field reads "client wants guaranteed growth and protection from market loss" on every application, whatever the client's age, liquidity or existing contracts. Each file, reviewed alone, looks acceptable.

## Why It's Still Broken
Review queues present files one at a time, assigned to whichever reviewer is free. Nothing compares text across a producer's history.

## What a Fix Looks Like
Embed every rationale and flag near-duplicates within and across producers. Show the reviewer the producer's history beside the file, and require a specific rationale before clearing where boilerplate is detected.

## Who Feels the Pain
Reviewers; compliance officers facing market conduct exams; consumers sold products on a template.

## Impact If Fixed
A cheap check turns a blind spot into a producer-level supervision signal examiners will recognise.
