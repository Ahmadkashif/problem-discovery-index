# Every Prior-Year Return Is a Test Case and the Season Is Tested by Hand

**Niche:** [[niches/accounting-firms-smb/tax-software-content-teams/profile|Tax Software Content & Compliance Teams]]
**Industry:** [[industries/accounting-firms-smb|SMB Accounting Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The team re-implements every changed form in fifty-two jurisdictions before an immovable date, holds millions of prior-year returns that exercise every path through the code, and allocates testing by judgment.
**Tags:** #gradient-boosting #evaluation-metrics #automation #workflow-orchestration #causal-inference

## The Problem
Every autumn, taxing authorities release changed forms, revised instructions, new schedules and updated e-file schemas across the federal system and fifty states. Every winter, a content organisation re-implements all of it before the filing season opens on a date nobody can move. Accounting firms buy the software on the implicit promise that the arithmetic is right.

The organisation's core risk is a defect that reaches production — a calculation wrong in a way that produces incorrect returns at scale, discovered mid-season when returns are already filed. Everything about how the team works is shaped by avoiding that.

The tool for avoiding it is testing, and testing is allocated by experience. Senior analysts know which forms are historically fragile, which interactions between schedules cause trouble, and where last year's problems were. That knowledge directs the regression effort.

Meanwhile the organisation holds two datasets that would answer the question directly and are not used for it.

The first is the prior-year return corpus. Millions of real returns exercise every combination of forms, elections and edge cases that taxpayers actually produce — a naturally occurring test suite far richer than anything a test team would write, with the previous year's computed results as a baseline. It is used for regression in a limited way and not as the basis for coverage measurement: nobody can say which paths through the calculation engine are exercised by real filings and which are not.

The second is the rejection and notice record. E-file rejections arrive by code, in volume, in real time during the season, and they say precisely which return constructions the authority refused. Downstream, notices tell you which accepted returns were wrong. Both are treated as support volume rather than as defect signal.

## Why Nobody Has Built This
The season dictates everything. From October to April the organisation is executing against a fixed date, and there is no capacity for work that does not ship a form. The remaining months go to planning the next season.

Defect prediction also sounds like an admission. A model that forecasts where defects will occur is an artefact stating that defects occur, in a product sold on correctness, to accountants who carry professional liability.

And the corpus is sensitive. Prior-year returns are taxpayer data under strict confidentiality, which makes using them for anything beyond direct processing a governance project before it is a technical one.

## What to Build
Defect risk as a measured, predicted quantity.

**Measure coverage against real filings.** Which calculation paths the return corpus actually exercises, and which changed forms are covered thinly. This alone reallocates testing effort from intuition to evidence.

**Predict defect risk per form change.** Magnitude of change, interaction count, historical defect record for that form, analyst experience and time remaining. The label is the organisation's own defect history, which it has by form and by season.

**Treat rejections as a live detector.** Rejection codes spiking on a construction, within hours, is the earliest possible signal of a content defect. Today that surfaces through support escalation over days.

**Differential-test against the prior engine.** Run the corpus through last year's and this year's logic and examine every material divergence. Most are intended; the unintended ones are exactly what the process exists to catch, and they can be surfaced automatically.

**Model notice outcomes back to content.** Which return constructions generated authority notices is the strongest available evidence of a wrong interpretation rather than a wrong calculation.

## Target Customer
VP of Tax Content or Director of Compliance Engineering at a tax software vendor. The argument is that the season is fixed, the volume of change is growing, and the only lever left is knowing where to look.

## Impact If Built
An entire profession files on software whose correctness is assured by expert intuition about where to test, against a deadline that does not move. Turning the prior-year corpus into measured coverage and the rejection stream into a live detector attacks the organisation's only real risk with data it already holds.
