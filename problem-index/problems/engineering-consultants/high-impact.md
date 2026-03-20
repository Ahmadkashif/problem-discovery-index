# Project Budget Tracking and Fee Erosion Prevention

**Industry:** [[engineering-consultants|Engineering Consultants]]
**Type:** High Impact
**One-liner:** Firms stop discovering they lost money on a project only after the final invoice goes out.
**Tags:** #gradient-boosting #feature-engineering #evaluation-metrics #time-series-forecasting #cross-validation #probability-distributions #bias-variance-tradeoff #gradient-descent #revenue-impact

## The Problem
Engineering firms quote fixed fees based on estimated hours per discipline, then track actual hours in timesheet systems that nobody reviews until month-end billing — or worse, project closeout. Scope creep is the primary margin killer: a client asks the structural engineer to "just check one more load case" or the civil team to "add an alternate stormwater layout," and the PM agrees without logging a change order. Across a portfolio of 20-50 active projects, a 15-person firm can silently lose $200K-$500K annually in unbilled scope expansion.

## Why It's Unsolved
Deltek, Ajera, and BST Global all have budget-vs-actual dashboards, but they require clean timesheet data entered promptly and coded to the correct project phase — conditions that rarely hold in small firms where engineers resist detailed time tracking. The real problem is detecting the pattern of erosion early enough to act: a project that is 40% complete but 60% through its labor budget needs an immediate client conversation, not a red cell in a spreadsheet nobody opens. Current ERP tools report what happened; they do not predict what will happen or flag anomalous burn patterns against comparable past projects.

## What a Solution Looks Like
A system ingests timesheet entries, contract fee schedules, and project milestone data in real-time, then models expected burn curves per project phase using historical data from completed projects of similar type and size. When a project's actual burn rate deviates significantly from its predicted curve — or when the ratio of unbilled hours to remaining fee crosses a threshold — the PM and principal receive an alert with a specific dollar amount at risk and a recommended action (file change order, renegotiate scope, reallocate staff). The output is a weekly project health score per project, not a dashboard the PM has to remember to check.

## Impact If Solved
Recovering even 3-5% of fee erosion on a $5M annual revenue firm yields $150K-$250K in recaptured margin — often the difference between a profitable year and a flat one. Early detection also preserves client relationships by surfacing scope issues before resentment builds on either side.
