# The Shift Handoff Rebuilt From Memory

**Niche:** [[niches/general-hospitals/bedside-nurses-med-surg/profile|Bedside Nurses on Med-Surg Units]]
**Industry:** [[industries/general-hospitals|General Hospitals]]
**Type:** Fix (Pain Point)
**One-liner:** At 07:00 and 19:00 every nurse reconstructs her patients' last twelve hours from a paper "brain sheet" and memory, and the oncoming nurse gets whatever she remembers.
**Tags:** #large-language-models #seq2seq #worker-facing #quick-win #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to cut the bedside nurse's documentation time without degrading the flowsheet data that quality measures, audits and billing depend on, and whoever gives back the most charting minutes per shift with audit-clean flowsheets takes the account.

## The Problem
Handoff takes ~30–45 minutes per shift change on a busy unit (estimate) and is where information is lost: a pending lab, a family concern, a subtle change in mental status. Structured handoff tools exist but are filled in by hand.

## Why It's Still Broken
Handoff tools sit beside the chart, not on top of it, so nurses fill them in by hand or skip them. The shift's changes are scattered across flowsheets, orders, results and notes.

## What a Fix Looks Like
A handoff summary drafted from the shift's documentation, orders and results: what changed, what is pending, what is overdue, and anything the nurse flagged. She edits it in two minutes, and the oncoming nurse sees it before bedside report.

## Who Feels the Pain
Nurses staying late to finish report; oncoming nurses starting blind; patients whose change in condition was mentioned but not passed on.

## Impact If Fixed
Shorter, more complete handoffs give back ~10–15 minutes per nurse per shift (estimate) and close a known gap where patient-safety events start.
