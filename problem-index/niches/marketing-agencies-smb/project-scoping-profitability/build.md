# Data-Driven Project Estimator from Historical Effort Data

**Niche:** [[niches/marketing-agencies-smb/project-scoping-profitability/profile|Project Scoping, SOW Generation, and Profitability Tracking]]
**Industry:** [[industries/marketing-agencies-smb|SMB Marketing Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool uses an agency's historical project data to predict effort for new projects — every estimate is made from memory, leading to 30-40% of projects scoped below actual effort.
**Tags:** #gradient-boosting #regression #tabular-ml #tacit-knowledge-ml #revenue-impact

## The Problem
An agency owner scoping a new engagement asks themselves: "How many hours will a 5-page website redesign take? What about a monthly SEO retainer for a 50-page site? How long does a brand identity project take when the client is indecisive?" The answers come from experience — the owner remembers that "website projects usually take about 80-100 hours" but does not remember that the last 5 websites they scoped at 80 hours actually averaged 115 hours. This systematic under-estimation is the primary source of margin erosion at agencies. Experienced agency owners develop calibrated estimates over time (tacit knowledge), but this calibration is personal, not transferable, and not data-driven even for the experienced owner.

## Why Nobody Has Built This
Building an estimator requires joining two data sets that agencies rarely connect: the project scope (deliverables, client size, complexity indicators) from the proposal system, and the actual hours by deliverable type from the time tracking system. Most agencies do not tag time entries at the deliverable level (they log time against the client, not against "homepage design" vs. "about page copywriting"), so the historical data lacks the granularity needed for accurate estimation. Building the estimator also requires enough historical data to train on — an agency that has done 20 website projects has enough data; an agency that has done 3 does not.

## What to Build
A project estimation engine that ingests the agency's historical time tracking data (at the deliverable level), maps it to project scope features (number of pages, industry, client decision-making speed, revision history), and produces effort estimates with confidence ranges for new projects. When the agency owner scopes a "5-page website redesign for a law firm," the system shows: "Based on your last 12 website projects, estimated effort is 95-125 hours. Your 3 most similar projects (law firms, 4-6 pages) averaged 115 hours. The main variable is client revision rounds — projects with 2 rounds average 100 hours, projects with 4+ rounds average 130 hours." The system learns from each completed project, improving estimates over time.

## Target Customer
Agency owners scoping 3-10 new projects per month who currently estimate from memory and discover the actual effort only after the project closes.

## Impact If Built
Reduces project under-scoping from 30-40% of projects to under 10%, improving portfolio margins by 10-20 percentage points. Enables the agency to price projects accurately, reducing the scope creep conflicts that damage client relationships.
