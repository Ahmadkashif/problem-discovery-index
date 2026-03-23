# Work Authorization Tracking and Eligibility Engine

**Niche:** [[niches/staffing-agencies/refugee-immigrant-placement/profile|Refugee & Immigrant Workforce Placement]]
**Industry:** [[industries/staffing-agencies|Staffing Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No staffing tool understands the 30+ categories of employment authorization documents, their expiration rules, renewal timelines, and the immigration status changes that affect work eligibility.
**Tags:** #automation #compliance #workflow-orchestration #data-integration

## The Problem
Work authorization for refugees and immigrants involves a complex matrix of document types: Employment Authorization Documents (EADs) with category codes (C09, C10, C33, etc.) that determine eligibility and expiration rules, refugee travel documents, TPS designations with country-specific validity periods, asylum pending status with different work authorization timelines, and permanent resident cards with conditional vs. unconditional status. A placement coordinator must verify that each worker has valid authorization, track expiration dates that vary by document type and immigration status, initiate renewals at the correct lead time (EAD renewals should be filed 6 months before expiration), and re-verify when a worker's immigration status changes (asylum approval, green card receipt). All of this is tracked in spreadsheets or paper files.

## Why Nobody Has Built This
Immigration work authorization rules are governed by USCIS regulations that change frequently, involve 30+ document categories with different rules, and require nuanced interpretation (an EAD with a pending renewal is automatically extended for some categories but not others). Building a compliance engine requires encoding this regulatory logic and keeping it current as USCIS issues policy updates. The market — community organizations and small staffing operations serving immigrant populations — is small and budget-constrained, making it unattractive for mainstream software vendors.

## What to Build
A work authorization management system that: captures and classifies employment authorization documents (EAD category, expiration date, underlying immigration status), applies USCIS rules to determine current work eligibility and automatic extension applicability, generates a renewal timeline with filing deadlines and required documentation, alerts coordinators when authorization is approaching expiration, tracks immigration status changes that affect work eligibility, and produces I-9 compliant records for employer partners. The system must be updated when USCIS issues policy changes affecting authorization categories.

## Target Customer
Workforce coordinators at refugee resettlement agencies, immigrant services organizations, and staffing firms specializing in authorized immigrant workforce placement, managing 50-500 workers with diverse immigration statuses.

## Impact If Built
Prevents work authorization lapses that disrupt placements and expose employers to I-9 penalties ($252-$2,507 per violation), reduces compliance tracking time from 30-60 minutes per worker per month to 5 minutes, and enables proactive renewal management that keeps workers continuously employed.
