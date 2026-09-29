# Twelve Statement Formats

**Niche:** [[niches/digital-audio-platforms/the-rights-operations-analyst/profile|The Rights Operations Analyst]]
**Industry:** [[industries/digital-audio-platforms|Digital Audio Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Every source sends a different file and the first week of every month is turning them into one spreadsheet.
**Tags:** #data-integration #quick-win #automation #worker-facing #workflow-orchestration #evaluation-metrics #descriptive-statistics #confidence-intervals
**Contested on:** Every serious competitor in this niche is fighting to stop analysts matching recordings to owners and reconciling statements across a dozen intermediaries by hand — and whoever equips them ends a month spent explaining a payment they cannot derive.

## The Problem
Statements arrive from a dozen sources, each with its own columns, period conventions, territory codes, deduction lines and identifier usage. The analyst's month begins with turning them into something comparable, which is manual, error-prone and repeated identically every period. Any change to a format — a new column, a renamed field — breaks the process silently and produces numbers that look plausible and are wrong.

## Why It's Still Broken
Each format is set by the sender, so the receiving party absorbs the variation — an integration cost imposed on the weaker counterparty stays with them indefinitely. The transformation is done in a spreadsheet by the person who understands it, which works and therefore persists. Industry standards exist and are applied inconsistently. And nobody has measured the time.

## What a Fix Looks Like
Normalise once and validate the result. Build a normalisation layer that maps every source format into one internal model, which is the fix and eliminates the recurring week. Validate the normalised output against expectations rather than trusting the parse, since silent breakage is the dangerous failure. Detect format changes automatically by checking structure, because a new column currently announces itself as a wrong total. Keep the raw file alongside the normalised data, so a later reconstruction is possible. Report the ingestion status per source per period, which nobody currently sees. Push for standard formats where there is leverage, as several sources will comply if asked. Handle the period and territory conventions explicitly, since those cause subtle errors rather than obvious ones. Version the mappings so a historical restatement is possible. Measure the time spent on normalisation, which will justify the work immediately. And make the normalised store the working data rather than a spreadsheet, because that is what lets everything downstream be automated.

## Who Feels the Pain
Analysts losing a week a month to transformation; rights holders receiving statements delayed by it; operations leadership with no visibility of the load; and everyone downstream of numbers produced by a manual process.

## Impact If Fixed
An integration cost imposed on the weaker counterparty stays with them indefinitely. A normalisation layer with output validation eliminates the recurring week and catches the silent breakage that manual transformation cannot.
