# Litigation Budget and Phase-Based Cost Tracker

**Niche:** [[niches/small-law-firms/small-litigation-firms/profile|Small Litigation Firms]]
**Industry:** [[industries/small-law-firms|Small Law Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Projects and tracks litigation costs against case value and fee arrangements by phase (pleading, discovery, depositions, motions, trial prep), giving the managing partner real-time visibility into whether a case is on budget before it's too late to course-correct.
**Tags:** #gradient-boosting #time-series-forecasting #feature-engineering #evaluation-metrics #revenue-impact #data-integration #tacit-knowledge-ml

## The Problem
Small litigation firms routinely discover that a case has exceeded its budget only after the final invoice is assembled. A commercial dispute budgeted at $75K in fees can quietly balloon to $120K during discovery when the associate spends 3x the estimated hours reviewing documents, the paralegal processes twice the expected volume of discovery requests, and expert witness fees exceed projections. Corporate clients with outside counsel billing guidelines increasingly demand phase-based budgets at engagement — but the firm has no tool to track actual spend against those phase budgets in real time. The managing partner relies on periodic "gut checks" with the billing attorney: "How's the Smith case looking?" The honest answer — "I haven't added up the time entries in 6 weeks" — is the norm. Experienced managing partners develop intuition for which cases are running hot based on associate activity patterns and discovery volume, but this tacit judgment cannot scale to 20+ active matters.

## Why Nobody Has Built This
Enterprise litigation management tools (Litify, TeamConnect) include budget tracking but cost $50K-200K/year and require Salesforce infrastructure. Clio has basic matter budgeting (set a budget, see a progress bar) but no phase decomposition, no projection modeling, and no early warning system. Building litigation budget intelligence requires three hard components: (1) mapping every time entry to a litigation phase automatically (the attorney records "drafted motion for summary judgment" — the system must classify this as "motions" phase), (2) learning from completed matters to set realistic phase-level budget baselines by case type and complexity, and (3) projecting remaining cost based on current trajectory and historical patterns. The classification step requires NLP on time entry narratives, which are notoriously terse and inconsistent.

## What to Build
A budget intelligence platform that ingests time entries from Clio/PracticePanther, classifies each entry to a litigation phase using a fine-tuned language model trained on legal billing narratives, and compares cumulative phase-level spend against budgets. A gradient-boosted model trained on completed matter data predicts total cost at completion based on current spend trajectory, case characteristics (case type, jurisdiction, opposing counsel, judge), and phase timing. The dashboard shows: current spend vs. budget by phase, projected total cost with confidence interval, burn rate alerts (flagging cases where discovery costs are tracking 2x the historical average), and staffing efficiency metrics (associate hours vs. partner hours by phase). The managing partner sees a single screen showing which of their 20 active cases need attention — before the client calls to complain about the bill.

## Target Customer
Managing partners at 3-10 attorney litigation firms billing $1M-10M annually, particularly those handling insurance defense or corporate litigation where clients impose outside counsel billing guidelines and phase-based budgets.

## Impact If Built
Prevents budget overruns that currently cost small litigation firms 10-20% of revenue through write-offs and client disputes. For a $3M firm, that's $300K-600K in preserved revenue. Equally important: budget transparency strengthens client relationships and competitive positioning against larger firms that already have enterprise budget tracking tools.
