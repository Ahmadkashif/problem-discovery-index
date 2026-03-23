# Employee Work Location Tracking for Tax and Compliance Purposes

**Niche:** [[niches/hr-consultants/remote-workforce-compliance/profile|Remote Workforce Compliance]]
**Industry:** [[industries/hr-consultants|HR Consultants]]
**Type:** Fix (Pain Point)
**One-liner:** Remote employees move between states without telling HR — an employee working from their partner's apartment in New York for 3 months triggers nexus, tax withholding obligations, and employment law compliance that nobody knows about until the state sends a notice.
**Tags:** #compliance #automation #data-integration #worker-facing

## The Problem
Remote employees work from wherever they want — and many change locations without notifying their employer. An employee whose address is registered in Texas spends January-March working from their partner's apartment in California. The employer now has California income tax withholding obligations, California employment law compliance requirements, and potentially a California corporate tax nexus — all triggered by an employee working from a couch they never reported to HR. The HR consultant advising the company has no visibility into where employees are actually working. Payroll systems withhold taxes based on the employee's registered address, not their actual work location. When California sends a notice 18 months later asking why income taxes weren't withheld, the company owes back taxes, penalties, and interest.

## Why It's Still Broken
Employers are reluctant to track employee locations because it feels invasive — the whole point of remote work is flexibility. Current HRIS systems don't prompt employees to report location changes, and there's no easy way for employees to self-report ("I'll be working from Oregon for the next 6 weeks while my mom recovers from surgery"). Tax compliance rules for remote workers vary by state (some have de minimis thresholds — 15-30 days before triggering obligations; others trigger on day 1), and no standard framework exists. The HR consultant advises clients to require location reporting but has no tool to implement and enforce it.

## What a Fix Looks Like
A lightweight location reporting tool integrated with the HRIS that: (1) prompts employees monthly to confirm their primary work location, (2) accepts temporary location reports ("working from Oregon 3/1-4/15"), (3) applies state-specific de minimis threshold rules to determine whether a temporary location triggers compliance obligations (e.g., "employee has worked 12 days in New York — threshold is 14 days before withholding obligation triggers — alert at 10 days"), (4) notifies the HR consultant and payroll when a threshold is crossed, and (5) maintains a location history audit trail for state tax inquiries. Employee experience is minimal — a monthly 10-second confirmation and a travel reporting button. Compliance impact is immediate.

## Who Feels the Pain
HR consultants who discover state tax and compliance obligations months after they were triggered by unreported employee relocations, and company CFOs who receive state tax notices with back withholding, penalties, and interest.

## Impact If Fixed
Prevents the state tax notices that currently surprise 20-30% of distributed companies each year, each costing $5,000-50,000 in back taxes, penalties, and consultant remediation fees. Gives the HR consultant proactive visibility into compliance obligations instead of reactive damage control.
