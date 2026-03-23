# Apprenticeship Progress Tracker

**Niche:** [[niches/trade-associations/construction-trade-groups/profile|Construction Trade Groups]]
**Industry:** [[industries/trade-associations|Trade Associations]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool today gives apprenticeship coordinators, employers, and apprentices themselves a unified view of progress toward journey-level completion — tracking on-the-job hours by task category, classroom attendance, competency assessments, and mentor evaluations in one system.
**Tags:** #data-integration #workflow-orchestration #automation #compliance

## The Problem
A construction apprenticeship (electrician, plumber, ironworker) runs 4-8 years with requirements across three dimensions: on-the-job hours (8,000-10,000 total, with minimums in specific task categories), related instruction (144-216 classroom hours per year), and competency assessments. Tracking progress requires combining employer-submitted timesheets (with task category breakdowns), classroom attendance records, and assessment results. Apprenticeship coordinators at trade associations manage 50-500 active apprentices using Access databases, Excel spreadsheets, and paper files. An apprentice who asks "How many hours do I need in conduit bending to qualify for my 3rd-year raise?" waits days for an answer because the coordinator must manually tally timesheets.

## Why Nobody Has Built This
State apprenticeship systems (RAPIDS, state DOL databases) track registration and completion but not granular progress. The task categories for on-the-job hours vary by trade, state, and sponsoring organization — there is no universal schema. Employers submit hours in different formats (paper timesheets, QuickBooks exports, Excel files). Building a unified tracker requires standardizing task categories by trade, ingesting hours from multiple formats, and syncing with state systems — a domain-specific integration challenge that generic education or workforce tools don't address.

## What to Build
A cloud-based apprenticeship management platform where: employers submit monthly OJT hours with task category breakdowns (mobile-first for field supervisors), classroom instructors record attendance and grades, the system automatically calculates progress toward journey-level requirements (total hours, hours by category, classroom completion, assessment scores), and apprentices see their own progress dashboard on a phone app. The system alerts coordinators when apprentices are behind pace, qualify for raises, or are approaching competency assessment deadlines.

## Target Customer
Apprenticeship coordinators at construction trade associations managing 100-500 active apprentices, currently spending 15-20 hours/week on manual progress tracking.

## Impact If Built
Reduces apprenticeship tracking from 20 hours/week to 4 hours/week per coordinator, enables apprentices to self-serve progress inquiries (eliminating 50+ monthly phone/email requests), and prevents the 5-10% of apprentices who fall behind without anyone noticing until it's too late to catch up.
