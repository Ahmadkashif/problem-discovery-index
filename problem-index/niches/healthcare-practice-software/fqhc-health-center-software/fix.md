# The UDS Season

**Niche:** [[niches/healthcare-practice-software/fqhc-health-center-software/profile|FQHC & Community Health Center Software]]
**Industry:** [[industries/healthcare-practice-software|Healthcare Practice Software]]
**Type:** Fix (Pain Point)
**One-liner:** Every health center spends the first quarter of the year reconstructing a year of care into the Uniform Data System's definitions, by hand, and then waits twelve months to find out whether the numbers it reported were the numbers it could have improved.
**Tags:** #descriptive-statistics #evaluation-metrics #hypothesis-testing #change-point-detection #compliance #automation #worker-facing #quick-win
**Contested on:** Every serious competitor selling to health centers is fighting to make the UDS report, the sliding-fee determination and the 340B claim all derive from the same encounter record without a parallel data collection exercise — and whoever removes that second exercise takes the account.

## The Problem
UDS reporting runs from January into the spring. A quality analyst pulls extracts, applies definitions that do not match the EHR's, chases charts where a measure's numerator is documented in a place the report cannot see, and assembles tables. The clinical quality measures in the report describe care delivered up to fifteen months earlier. If the health center's hypertension control rate is below its peer group, it learns this after the year in which it could have acted has closed. The analyst knows by March what the number will be and has no mechanism to have known it the previous March.

## Why It's Still Broken
The report is annual because the programme is annual, and vendors have built to the deadline rather than to the measure. Computing UDS measures continuously is not hard — the definitions are published and stable — but it requires implementing them once, properly, against the live record, and vendors have preferred an annual extract that can be reconciled manually because reconciliation is billable services rather than product risk. The health center side has its own inertia: the analyst's role is defined around the season, and a continuous number is a different job.

## What a Fix Looks Like
Compute the measures continuously and show the gap list, not the rate. A rate is a scoreboard; a list of the 140 patients with uncontrolled hypertension who have not been seen in six months is an action. The same machinery that produces the annual tables can produce a monthly view, with the numerator and denominator traceable to the encounters that populate them so the analyst can settle a definitional question in minutes rather than by chart review. Peer comparison should follow the same cadence where network data allows. The season then becomes a submission rather than a reconstruction, and the analyst's year changes shape from one quarter of extraction to twelve months of gap closure.

## Who Feels the Pain
Quality analysts who lose a quarter to reconstruction every year; clinical directors told in April how they performed fifteen months ago; and patients in the gap list nobody could see.

## Impact If Fixed
Monthly measure computation with a patient-level gap list moves quality work from retrospective reporting to prospective outreach, which is the only mechanism by which the rate actually changes. It returns most of a quarter of analyst capacity, and it makes definitional disputes — the single largest time sink in the season — resolvable against the record instead of by argument.
