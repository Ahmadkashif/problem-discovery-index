# It Passed the Tests and Broke the Dashboard

**Niche:** [[niches/data-platform-integrators/deployment-automation/profile|Environment & Deployment Automation]]
**Industry:** [[industries/data-platform-integrators|Data Platform Integrators]]
**Type:** Fix (Pain Point)
**One-liner:** The model change was correct, the tests passed, and a finance dashboard has been showing the wrong total since Tuesday.
**Tags:** #quick-win #automation #workflow-orchestration #evaluation-metrics #data-integration #change-point-detection #descriptive-statistics #compliance
**Contested on:** Every serious competitor in this niche is fighting to ship a change to the model layer without breaking a report, and whoever makes that deployment path safe takes the account.

## The Problem
A change to a shared model is correct in its own terms — better logic, a fixed edge case, a new column — and it changes a number that a downstream report depends on. The tests verified the model, not the report. Nobody told the report's owner. The wrong total is discovered by a business user days later, and the conversation that follows damages trust in the platform far more than the error itself warrants.

## Why It's Still Broken
Nobody knows who the consumers are — a change tested at the model level is tested at the wrong level, because the thing anybody experiences is a report and nothing checks reports. Lineage stops before the reporting tool. Consumers are not notified. And the engineer had no way to know.

## What a Fix Looks Like
Check the reports and tell the people who read them. Compare key report outputs before and after the change in a staging run, which is the fix and catches the class directly. Use lineage to identify affected reports and their owners, extending it into the reporting tool where possible. Notify the owners of affected reports before deploying, which converts a shock into a heads-up. Keep a small set of golden numbers that must not move without explanation, which is a cheap and effective guard. Flag changes to shared models for extra scrutiny, since those are where the blast radius is. Deploy changes to widely-used models at a time when somebody is available, rather than overnight. Provide a clear rollback, so the response to a surprise is quick. Record every break and its cause, which shows where the testing is weakest. Ask report owners which numbers they watch, which most will answer and nobody asks. And treat a changed number as a deployment event requiring communication rather than as an internal detail.

## Who Feels the Pain
Business users acting on wrong numbers; engineers who made a correct change and caused an incident; report owners who found out from a colleague; and the platform's credibility, which absorbs each occurrence.

## Impact If Fixed
A change tested at the model level is tested at the wrong level, because the thing anybody experiences is a report and nothing checks reports. Comparing key report outputs in staging catches the class directly.
