# Reason Codes That Say Nothing

**Niche:** [[niches/sales-finance-companies/indirect-auto-contract-decisioning/profile|Indirect Auto Contract Decisioning]]
**Industry:** [[industries/sales-finance-companies|Sales Finance Companies]]
**Type:** Fix (Pain Point)
**One-liner:** Manual decisions are recorded with a handful of default reason codes chosen in a hurry, so the record can neither explain a decision to an examiner nor teach the next analyst.
**Tags:** #large-language-models #bert #evaluation-metrics #compliance #quick-win #workflow-orchestration
**Contested on:** *Not terminal as stated.* The honest partial sentence is "every serious competitor is fighting to give the dealer a workable decision before another lender does," but prime and non-prime paper are won differently — prime by deciding the most applications automatically at a stable loss rate, non-prime by structuring counteroffers the dealer can close and the borrower can pay — with different inputs, staff and winners. Decomposed into contested sub-niches below.

## The Problem
An analyst declines a deal because the stated income is implausible for the job and the dealer's last five deals had the same pattern. The system records "insufficient income" or "credit history". The adverse-action notice is technically correct and the institutional knowledge is lost.

## Why It's Still Broken
Reason-code lists were designed for adverse-action notices, not for learning. Typing free text slows a queue competing on minutes.

## What a Fix Looks Like
Draft the reason from the file — the specific cue, the evidence and the regulatory reason code it maps to — for the analyst to confirm in one click. Keep the cue separately from the notice language, so the lender gains a searchable, consistent record without telling the borrower anything inaccurate.

## Who Feels the Pain
Credit policy teams trying to learn from overrides; compliance teams defending adverse-action accuracy; new analysts with no record of how seniors decided.

## Impact If Fixed
A near-zero-effort change in capture turns every manual decision into a labelled example and a defensible record.
