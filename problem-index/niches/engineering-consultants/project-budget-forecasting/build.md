# Predictive Project Budget Health Score

**Niche:** [[niches/engineering-consultants/project-budget-forecasting/profile|Project Budget Forecasting & Change Orders]]
**Industry:** [[industries/engineering-consultants|Engineering Consultants]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A system that assigns each active project a weekly health score based on burn rate trajectory, communication pattern analysis, and comparison to historical projects of the same type — alerting the PM when a project is heading toward a fee overrun before the overrun actually occurs.
**Tags:** #gradient-boosting #time-series-forecasting #anomaly-detection #tabular-ml #tacit-knowledge-ml #revenue-impact

## The Problem
An experienced firm principal can look at a project's timesheet data, glance at the email thread with the client, and *know* whether the project is going to lose money — long before the numbers confirm it. They read patterns: the junior engineer is spending too many hours on a task that should be routine, the client is sending emails every day instead of weekly, the scope description is getting reinterpreted in meeting minutes. This intuition is built from running hundreds of projects over decades. Junior PMs don't have it, and the firm's financial health depends on it. Currently, firms discover fee erosion at project closeout — when a $50,000 project has consumed $65,000 in labor. A predictive model would surface these trajectories in week 3, not month 6.

## Why Nobody Has Built This
Building a predictive budget health model requires joining three data sources that engineering firms have never integrated: (1) timesheet data showing hour-by-hour burn by person and phase, (2) communication metadata showing client interaction frequency and tone, and (3) historical project outcomes showing which burn patterns preceded which financial outcomes. The data exists across Deltek, Outlook, and QuickBooks — but no firm has ever assembled it into a training dataset. The tacit knowledge component (reading communication patterns as scope creep indicators) is the hardest to encode because PMs don't consciously track these signals.

## What to Build
A lightweight SaaS that ingests timesheet data (via Deltek/Ajera/BST API or CSV upload) and email metadata (via Outlook/Gmail integration, not email content — just frequency, thread length, and participant count). The system compares each project's burn curve against historical projects of the same type and flags deviations. It assigns a weekly health score (Green/Yellow/Red) with a predicted cost-at-completion and specific indicators driving the score. PM receives a push notification when a project transitions from Green to Yellow, with a dollar amount at risk and a recommended action.

## Target Customer
Engineering firm principals and PMs at firms running 15+ active fixed-fee projects, currently discovering budget overruns at invoicing rather than in real time.

## Impact If Built
Enables PMs to intervene 4-8 weeks earlier on at-risk projects, recovering an estimated 3-5% of annual revenue that is currently lost to undetected fee erosion. For a $5M/year firm, this represents $150K-250K in recaptured margin.
