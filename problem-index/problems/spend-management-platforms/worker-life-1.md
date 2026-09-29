# The Controller in the Exception Queue

**Industry:** [[spend-management-platforms|Spend Management Platforms]]
**Type:** Worker Life Changing
**One-liner:** Controllers spend their month approving spend they were always going to approve and chasing receipts, then compress the actual accounting into the last week.
**Tags:** #gradient-boosting #bert #large-language-models #k-nearest-neighbors #k-means-clustering #evaluation-metrics #worker-facing #automation

## The Problem
The queue holds flagged transactions, uncoded items, missing receipts and approval requests. It refills continuously.

Most of it requires no judgement. The exception is legitimate, the coding is obvious, the receipt exists somewhere in an employee's inbox. The controller processes it because someone must, and because the audit trail requires a named approver.

Chasing is the demoralising part. Sending the fourth reminder to the same salesperson about the same receipt is not accounting, and it consumes real hours.

Month end concentrates everything. Accruals, reclassifications, reconciliations, the report the CFO needs, and the backlog of coding that accumulated while the controller was chasing receipts — all in a week, at the end of which the cycle restarts.

The actual expertise — knowing whether something is capitalised or expensed, when to accrue, how to treat a prepaid, whether a cost belongs in cost of goods sold or operating expense — is exercised in a small fraction of the time and is the reason the person was hired.

## Why It Matters to the Worker
The ratio of judgement to processing is wrong and everyone in the role knows it. Controllers are qualified accountants performing data entry and follow-up for most of the month.

Chasing carries a social cost. The controller is the person who nags, across the whole company, forever, about small amounts. It affects how colleagues treat them and it is nobody's idea of a career.

Month end is a recurring crunch that cannot be smoothed, because the work that could have been spread through the month was displaced by processing that could not wait.

And the knowledge is invisible. The controller's coding conventions, their judgement about capitalisation, their understanding of which vendors mean what — all tacit, all lost on departure, and rediscovered by their successor over a painful quarter.

## What a Solution Looks Like
Auto-approval by resemblance. Exceptions that look like a thousand previously approved exceptions do not need a human; post-hoc sampling preserves the control. This alone removes most of the queue.

Coding trained on the company's own history rather than on rules, with ambiguity routed to the employee at the point of spend instead of to the controller at month end.

Receipt reconstruction where the underlying facts are known, and targeted chase where they are not, so the reminder loop stops being uniform and endless.

Anomaly detection that actually looks for misuse — duplicates, splitting below thresholds, personal spend patterns, unusual vendor relationships — as a distinct rare-event problem rather than as a by-product of rule breaches. That is the work the controller should be doing and currently has no time for.

Month-end load spread by continuous accrual and reclassification during the period, which is possible only once the processing burden is lifted.

Conventions captured. Every coding decision and correction, with the reasoning where it can be captured, becomes the institutional memory that currently walks out of the door.

## Impact If Solved
The controller is the platform's actual user and spends most of their month on work the platform created. Auto-approving by resemblance, coding from history and reconstructing documentation returns them to accounting, and gives the company the fraud detection it currently assumes the exception queue is providing.
