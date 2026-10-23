# Dictionary Updates Emailed as Files

**Niche:** [[niches/court-reporting-firms/steno-scoping-proofreading/profile|Steno Scoping & Proofreading Networks]]
**Industry:** [[industries/court-reporting-firms|Court Reporting Firms]]
**Type:** Fix (Pain Point)
**One-liner:** The reporter adds entries on Monday, the scopist adds others on Tuesday, and by Friday their dictionaries disagree and the same mistranslation is fixed twice.
**Tags:** #data-integration #workflow-orchestration #worker-facing #quick-win #automation
**Contested on:** Every serious competitor in this niche is fighting to edit a reporter's raw CAT file into a certifiable transcript overnight in that reporter's own dictionary and style, and whoever needs the fewest audio checks per page in that reporter's writing takes the account.

## The Problem
A reporter's main dictionary and job dictionaries change after nearly every job. Scopists receive copies by email or cloud folder, add entries of their own, and send them back. Conflicting definitions and lost entries are routine.

## Why It's Still Broken
CAT software was designed for one writer on one machine, and dictionary files are personal assets that reporters guard.

## What a Fix Looks Like
A versioned dictionary store owned by the reporter. The scopist proposes entries, the reporter approves them, and both machines sync automatically, with conflict detection that shows which definition each recent job used.

## Who Feels the Pain
Reporters and scopists on every job; clients receiving inconsistent spellings across days of the same deposition.

## Impact If Fixed
Fewer repeat corrections and fewer inconsistencies across multi-day transcripts, for the cost of a sync service.
