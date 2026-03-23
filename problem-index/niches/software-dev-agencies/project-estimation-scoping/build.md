# Historical Estimation Intelligence for Dev Agencies

**Niche:** [[niches/software-dev-agencies/project-estimation-scoping/profile|Project Estimation & Scoping]]
**Industry:** [[industries/software-dev-agencies|Software Dev Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No product learns from an agency's historical project data to produce data-driven estimates that account for the agency's specific strengths, weaknesses, and technology-stack performance patterns.
**Tags:** #gradient-boosting #regression #tabular-ml #tacit-knowledge-ml #revenue-impact

## The Problem
A senior solutions architect at a dev agency estimates a new React + Node.js e-commerce build at 1,200 hours based on experience. The actual delivery takes 1,650 hours. The agency absorbs $45K in margin erosion. Six months later, a different architect estimates a similar project at 1,000 hours because they had a different experience with a similar (but not identical) project. The agency has delivered 200+ projects over 10 years but does not systematically use this historical data to calibrate estimates. The estimation intelligence lives entirely in individual architects' heads — when they leave, the calibration resets.

## Why Nobody Has Built This
Estimation data is rarely captured at the right granularity. Agencies track total project hours in their time tracking system but do not tag time entries against the original estimate's feature breakdown. Comparing "estimated 1,200 hours" to "actual 1,650 hours" is not actionable — the useful insight is "authentication took 3x the estimate, payments took 1.5x, CRUD screens were on target." Extracting this feature-level comparison requires linking estimation records to time tracking records at the feature level, which no agency does systematically.

## What to Build
An estimation platform that: (1) captures estimates in a structured format (feature, complexity, technology, estimated hours) at proposal time, (2) links to the agency's time tracking system (Harvest, Toggl, Clockify) to capture actual hours at the feature level, (3) builds a historical model of the agency's estimation accuracy by feature type, technology stack, and team composition, (4) produces data-driven estimates for new projects by matching proposed features to historical performance, and (5) highlights high-variance features ("your estimates for payment integrations vary 50-200%, consider adding buffer"). Over time, the model learns the agency's specific estimation biases and corrects for them.

## Target Customer
Dev agencies with 50+ completed projects and 10+ team members, where estimation accuracy directly impacts profitability and senior time spent on pre-sales.

## Impact If Built
Reduces estimation error from 20-40% to 10-15%, improving average project margin by 5-10 percentage points. For a $5M agency, that is $250K-$500K in recovered margin annually. Reduces pre-sale estimation time by 40-50% by providing data-driven starting points.
