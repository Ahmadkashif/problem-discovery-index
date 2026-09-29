# Fix: Six Dropdown Options Are the Entire Explanation

**Niche:** [[niches/recruiting-tech-vendors/compliance-and-records/profile|Compliance, Records & Audit Trail]]
**Industry:** [[industries/recruiting-tech-vendors|Recruiting Tech Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** The rejection reason field offers "not qualified", "other candidates more qualified" and four equally uninformative options, and most rejections use the same one.
**Tags:** #descriptive-statistics #evaluation-metrics #compliance #workflow-orchestration #confidence-intervals #quick-win #worker-facing #data-integration
**Contested on:** Whether the reason captured will be specific enough to be worth capturing.

## The Problem

Every applicant tracking system has a rejection reason field. It is a dropdown with five or six options that are the same in every deployment: not qualified, other candidates more qualified, failed screening, withdrew, position closed, other.

Recruiters select whichever is nearest, usually the same one every time. The resulting data supports no analysis, explains no individual decision, and satisfies no regulatory question. It is a field that has been filled in for twenty years and has never been read.

Meanwhile the specific reason is known at the moment of rejection — the candidate lacks the licence, the experience is in a different domain, the salary expectation is outside the band, the requirement about the specific system is unmet — and there is nowhere to put it that anyone will ever look at.

## Why It's Still Broken

The dropdown was designed as a compliance checkbox rather than as data, so its options were chosen to be quick rather than informative, and being quick is why it gets completed at all.

Making it specific means making it longer, which is friction on a task performed hundreds of times a week by someone under volume pressure, so every attempt to improve it has failed on adoption.

And nobody reads the output, so there has been no pressure to improve the input.

## What a Fix Looks Like

Derive the options from the requisition, keep the interaction to one click, and read the results.

Generate the reason options from the requisition's own requirements. Rejecting a candidate for a role requiring a licence, five years of a specific experience and a location offers those three as options plus a comparative one. Specific, requisition-aware, and no longer than the generic dropdown because the list is short and relevant.

Pre-select the likely reason where the screen produced one. If a filter removed the candidate, the reason is known exactly and should be recorded automatically with no human action at all — which covers the majority of rejections and requires nothing from anyone.

Offer two or three candidate-specific options for human rejections, derived from the application against the requirements. One click, specific, informative.

Then read the output. Rejection reasons by requisition, by stage, by reviewer, by group. Distributions that concentrate on one requirement point at a requirement worth questioning; distributions that differ by group point at something that needs investigating; distributions that differ by reviewer point at calibration.

Use it in the candidate communication, where the reason is safe to give. "The role required a licence that your application did not indicate" is a far better rejection than silence and is generated from the same field.

And retain it with the decision record, where it becomes the human-side basis that any reconstruction needs.

## Who Feels the Pain

Candidates, rejected for a reason that exists and is recorded as "other". Recruiting leaders, unable to learn anything from twenty years of accumulated reason data. Compliance functions, holding a field that answers no question anyone asks. And the employer, who cannot say why they rejected someone when asked.

## Impact If Fixed

The reason becomes specific because the options come from the requisition rather than from a generic list, at no extra cost in clicks. Automated rejections record their exact basis with no human action. And the accumulated data becomes readable — requirements worth questioning, reviewers worth calibrating, patterns worth investigating — for the first time.
