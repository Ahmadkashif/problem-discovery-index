# 90-Day Milestone Timeline Manager

**Niche:** [[niches/nonprofits-social-services/refugee-resettlement-agencies/profile|Refugee Resettlement Agencies]]
**Industry:** [[industries/nonprofits-social-services|Nonprofits Social Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool today can manage the 30+ mandatory milestones a refugee family must complete within 90 days of arrival, tracking dependencies, scheduling appointments, and alerting case managers when milestones are at risk of being missed.
**Tags:** #workflow-orchestration #automation #compliance #ai-agent

## The Problem
Within 90 days of a refugee family's arrival, the case manager must complete housing setup, Social Security applications, school enrollment for children, health screening, benefits enrollment (SNAP, Medicaid, cash assistance), cultural orientation, employment services, and English language assessment. Each milestone has dependencies (can't apply for SNAP without Social Security Number), variable processing times (SSN takes 2-6 weeks), and appointment scheduling constraints. Case managers with caseloads of 15-25 families track all of this on paper calendars and mental notes, regularly missing milestones that result in ORR compliance findings.

## Why Nobody Has Built This
The 90-day resettlement workflow is hyper-specific to the nine national resettlement agencies, and the rules differ by state (each state has different benefit enrollment processes). The total addressable market is only about 350 local affiliate offices nationwide — too small for generic SaaS companies to target. National agencies build their own systems but focus on ORR reporting rather than operational workflow management for frontline case managers.

## What to Build
A milestone management platform that generates a personalized 90-day timeline for each arriving family based on family composition (single adult, family with children, elderly member), state of residence, and arrival date. The system schedules milestones with dependency logic, sends case manager reminders for upcoming deadlines, flags at-risk milestones (SSN hasn't arrived and SNAP application is due in 5 days), and provides a portfolio-level view showing which families across the caseload need attention today.

## Target Customer
Case managers and program directors at the 350 local resettlement affiliate offices, each managing 100-500 new arrivals per year.

## Impact If Built
Reduces missed milestone rate from 15% to 3%, prevents $200K-$500K in ORR compliance penalties per agency, and allows case managers to manage 30% larger caseloads without increasing missed-milestone risk.
