# Import Moves the Data and Loses the Process

**Niche:** [[niches/no-code-app-builders/spreadsheet-process-migration/profile|Spreadsheet Process Migration]]
**Industry:** [[industries/no-code-app-builders|No-Code App Builders]]
**Type:** Fix (Pain Point)
**One-liner:** Every platform's spreadsheet import produces a flat table of rows and silently discards the formulas, validations, colour rules and pivots that were the actual process.
**Tags:** #descriptive-statistics #graph-theory #decision-trees #evaluation-metrics #confidence-intervals #quick-win #automation #workflow-orchestration
**Contested on:** Every serious competitor here is fighting to turn an existing spreadsheet-and-email process into a working application without the owner rebuilding it from scratch — and whoever does that takes the department, because the rebuild is the only reason the process is still a spreadsheet.

## The Problem
Someone imports their workbook. The rows appear. The three computed columns are now static text showing whatever they evaluated to at import. The status dropdown is a free-text field. The colour rules are gone. The pivot that was the weekly report does not exist. The person now has their data in a new tool and none of their process, faces a day of rebuilding, and goes back to the spreadsheet — which every vendor records as a failed activation with no idea why.

## Why It's Still Broken
Import was scoped as data ingestion and has never been revisited, because it appears to work: the rows arrive and the operation reports success. The losses are silent, so neither the user nor the vendor's telemetry registers them as failures — the user just stops. Preserving formulas means interpreting them, which is a larger piece of work than an import feature was budgeted for. And the abandonment shows up as a generic activation metric that nobody has decomposed by entry path.

## What a Fix Looks Like
Make the losses visible and convert what can be converted. Report exactly what was not carried across, per element, at import time — three computed columns, one validation list, two conditional format rules, one pivot — so the user knows what to rebuild rather than discovering it a day later, which alone changes the experience from silent failure to an honest checklist. Convert the mechanical cases, which are most of them: validation lists become select fields with the same options, simple formulas become computed fields, lookups between sheets become relationships, and pivots become grouped views. Offer the interpretive cases as suggestions to confirm, such as a colour rule proposed as a conditional view or a status automation. Preserve the original workbook alongside the app for reference and for reversal. And measure abandonment by entry path, which would show every vendor that import-led onboarding fails at a rate its aggregate activation number conceals.

## Who Feels the Pain
Operations people who imported their work and lost the parts that mattered; vendors whose import-led signups churn silently; and departments that concluded the category does not work for them on the basis of one afternoon.

## Impact If Fixed
Reporting the losses costs nothing and converts a silent failure into an honest one, and the mechanical conversions cover the majority of what is currently discarded. The abandonment-by-entry-path measurement is the number that would make any vendor prioritise this.
