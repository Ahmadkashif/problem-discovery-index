# ATS Status Events That Stop at "In Progress"

**Niche:** [[niches/investigation-and-screening-firms/high-volume-hourly-screening/profile|High-Volume Hourly & Gig Screening]]
**Industry:** [[industries/investigation-and-screening-firms|Investigation & Background Screening Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Applicant tracking integrations pass the screener's report status as one field, so a recruiter with 200 open offers cannot tell which applicants will clear today and which are stuck in one county.
**Tags:** #survival-analysis #gradient-boosting #evaluation-metrics #workflow-orchestration #data-integration #automation
**Contested on:** Every serious competitor in this niche is fighting to clear an hourly or gig applicant before that applicant accepts another offer, and whoever returns the largest share of complete, accurate reports within one business day takes the account.

## The Problem
Recruiters at a distribution centre hiring for peak season watch a column of "background check in progress". They call the screener's support line, which looks up each order. Applicants who could start tomorrow wait for news; applicants stuck for a week drift away without anyone deciding whether to hold the job or move on.

## What Already Exists
Workday, iCIMS, UKG and SAP SuccessFactors offer screening integrations with order, status and result events, and screeners expose component status through their own dashboards and APIs.

## The Customization Gap
The volume recruiter needs component-level status in the tracking system they live in, a predicted completion time per applicant with a confidence range, the reason for any hold in plain language (county court backlog, verification pending, applicant action needed), and prompts for the applicant when they are the blocker. That needs the screener's per-county latency history exposed as a prediction, not an average, and an event schema richer than "in progress" and "complete".

## Target Customer
Talent acquisition operations leaders at retail, logistics and staffing employers hiring tens of thousands a year.

## Impact If Solved
Recruiters spend their time on the few applicants who are actually stuck, applicants get honest timelines, and fewer offers are lost to silence.
