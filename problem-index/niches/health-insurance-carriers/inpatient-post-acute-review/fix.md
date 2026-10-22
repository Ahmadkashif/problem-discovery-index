# The Friday Cut-Off Notice

**Niche:** [[niches/health-insurance-carriers/inpatient-post-acute-review/profile|Inpatient & Post-Acute Concurrent Review]]
**Industry:** [[industries/health-insurance-carriers|Health Insurance Carriers]]
**Type:** Fix (Pain Point)
**One-liner:** Skilled nursing coverage end dates cluster on the plan's review days rather than the member's recovery, because the decision runs on a weekly cadence and last week's therapy notes.
**Tags:** #large-language-models #survival-analysis #workflow-orchestration #evaluation-metrics #compliance
**Contested on:** Every serious competitor in this niche is fighting to set each inpatient and post-acute stay's length from the clinical record in daily review, and whoever's length-of-stay decisions hold through appeals and peer-to-peer reviews with no rise in readmissions takes the account.

## The Problem
Post-acute stays are often reviewed weekly. The facility sends notes before the review, the nurse decides, and if coverage ends, the member receives a notice of non-coverage two days ahead (recalled) and can file a fast-track appeal. When the notes are stale, the decision reflects the member's condition last week. End dates then cluster on administrative days, and appeals and readmissions follow.

## Why It's Still Broken
Review cadence is set by staffing, not by clinical trajectory. Facilities send therapy notes in batches, by fax, and the plan has no early signal that a member is progressing faster or slower than expected.

## What a Fix Looks Like
Review on trajectory, not on the calendar. Request structured functional scores at short intervals, flag members whose progress departs from expectation in either direction, and schedule review when the evidence changes. Track the share of end dates falling on review days and the fast-track appeal rate as standing quality measures.

## Who Feels the Pain
Members and families facing an abrupt discharge; facility staff fighting notices; reviewers deciding on stale evidence; plans absorbing appeals and readmissions.

## Impact If Fixed
End dates that track recovery, fewer fast-track appeals, and fewer readmissions after premature discharges.
