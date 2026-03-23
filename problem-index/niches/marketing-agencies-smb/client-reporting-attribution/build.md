# Narrative Performance Report Generator with Business Context

**Niche:** [[niches/marketing-agencies-smb/client-reporting-attribution/profile|Client Reporting and ROI Attribution]]
**Industry:** [[industries/marketing-agencies-smb|SMB Marketing Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No reporting tool generates the narrative commentary that transforms a data dashboard into a strategic report — explaining not just what happened but why, and what the agency recommends next.
**Tags:** #llm #text-generation #nlp #automation #revenue-impact

## The Problem
A client receives a monthly report showing impressions up 20%, clicks up 15%, but conversions down 5%. The data is correct but unhelpful without context: "Impressions and clicks increased because we expanded the keyword set to include long-tail queries, which drove more traffic but at a higher funnel stage. Conversions dipped because 3 of the new keywords are informational rather than transactional — we recommend creating landing pages for these keywords to capture leads earlier in the funnel." This narrative takes the account manager 30-45 minutes to write for each client, drawing on their memory of what changes were made that month, their understanding of the client's business, and their interpretation of the data trends. It is the part of the report that justifies the agency's retainer — without it, the client could read a dashboard themselves.

## Why Nobody Has Built This
Generating meaningful narrative requires three inputs that no tool combines: (1) the performance data itself (available from reporting APIs), (2) the actions taken during the period (campaign changes, creative swaps, landing page updates — which live in the account manager's notes, not in a structured format), and (3) the client's business context (seasonality, competitor actions, business changes — which live in the account manager's head). An LLM can generate narrative from data, but it produces generic commentary unless it has access to the action log and business context that make the narrative specific and valuable.

## What to Build
A report generation system that combines three data sources: performance data pulled from platform APIs (Google Ads, Meta, GA4, email), a structured action log maintained by the account manager during the month (what changes were made, when, and why), and client context profiles (business type, seasonality, goals, competitive landscape). The system generates a draft narrative for each section of the report: what happened, why it happened (linking metrics to logged actions), and what the agency recommends next (based on data trends and the client's stated goals). The account manager reviews and edits the draft in 10-15 minutes rather than writing from scratch in 30-45 minutes.

## Target Customer
Account managers at agencies with 20-60 clients who spend 40-80 hours per month writing narrative report commentary.

## Impact If Built
Reduces report creation time from 2-4 hours per client to 30-45 minutes (including review), recovering 1-2 FTEs of account manager capacity. Improves report quality consistency across the team and enables agencies to deliver reports weekly instead of monthly — increasing client engagement without increasing labor.
