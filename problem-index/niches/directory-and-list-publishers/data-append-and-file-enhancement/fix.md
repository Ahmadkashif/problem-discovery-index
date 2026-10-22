# The Test File Won on Match-Rate Arithmetic

**Niche:** [[niches/directory-and-list-publishers/data-append-and-file-enhancement/profile|Data Append & File Enhancement]]
**Industry:** [[industries/directory-and-list-publishers|Directory & List Publishers]]
**Type:** Fix (Pain Point)
**One-liner:** Clients choose append vendors on match rate alone, so the vendor that matches most loosely wins and the client finds out on the campaign.
**Tags:** #evaluation-metrics #hypothesis-testing #descriptive-statistics #quick-win #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to append the most correct fields to a client's file — a match rate at a stated accuracy — and whoever proves the higher verified match rate on the client's own test file wins the job.

## The Problem
In a test, each vendor counts a match differently — some include household-level matches as individual matches, some include low-confidence fuzzy matches. The client compares headline percentages that are not comparable.

## Why It's Still Broken
There is no common definition of a match in append tests, and clients lack the ground truth to check correctness.

## What a Fix Looks Like
Seed the test file with records whose true values the client knows, require vendors to report match rate by confidence band and match level, and score vendors on matched-and-correct for the seeded records.

## Who Feels the Pain
Database marketers and nonprofit data managers whose campaigns run on appended fields, and accurate vendors who lose tests.

## Impact If Fixed
Tests start measuring what clients actually need, at the cost of a few hundred seeded records.
