# Carrier Program Compliance Scorecards

**Industry:** [[insurance-restoration|Insurance Restoration]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic project management tools track tasks and deadlines, but they don't know that State Farm's preferred vendor program requires a 2-hour response time acknowledgment, specific Xactimate line-item formatting, and a customer satisfaction score above 4.5 — and that falling below threshold for two consecutive quarters means losing 40% of your revenue.
**Tags:** #gradient-boosting #decision-trees #feature-engineering #evaluation-metrics #cross-validation #descriptive-statistics #expectation-variance-covariance #compliance

## The Problem
Restoration companies depend on carrier preferred vendor programs (State Farm, Allstate, USAA, Liberty Mutual, Travelers) for 50-80% of their job volume. Each carrier has different compliance requirements: response time SLAs (acknowledge within 1-2 hours, on-site within 4-24 hours), documentation standards (photo quantity and format, moisture reading frequency, daily updates), Xactimate estimating rules (approved line items, pricing databases, supplement formatting), and customer satisfaction thresholds. A mid-size restoration company may participate in 5-8 carrier programs simultaneously, each with different scorecards and reporting periods. Falling below threshold on any single metric can trigger probation, reduced referral volume, or program termination.

## What Already Exists
Job management platforms (PSA, DASH, Next Gear Solutions) track response times and job milestones. Xactimate handles estimating. Customer survey tools (SurveyMonkey, carrier-specific portals) collect satisfaction data. No system aggregates all carrier-specific KPIs into a single compliance dashboard that predicts whether the company is trending toward threshold violations before they happen.

## The Customisation Gap
A restoration compliance system needs to: (1) maintain carrier-specific scorecards with exact KPI definitions and thresholds for each program, (2) track real-time performance against each carrier's metrics across all active jobs, (3) predict end-of-quarter scores based on current trajectory, flagging at-risk programs early enough to course-correct, (4) identify which specific jobs are dragging down scores (e.g., a single low satisfaction rating that drops the quarterly average below threshold), and (5) auto-generate carrier-specific documentation packages in the exact format each program requires.

## Impact If Solved
Reduces carrier program compliance management from 5-8 hours/week of manual scorecard tracking to automated monitoring. Prevents program termination events that cost $200K-$500K in annual revenue. Enables the operations manager to focus remediation efforts on the specific jobs and metrics that are at-risk rather than retrospectively discovering problems after quarterly reviews.
