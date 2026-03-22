# Service Authorization Utilization Tracking

**Niche:** [[niches/home-health-agencies/medicaid-waiver-personal-care/profile|Medicaid Waiver Personal Care Programs]]
**Industry:** [[industries/home-health-agencies|Home Health Agencies]]
**Type:** Fix (Pain Point)
**One-liner:** Agencies lose revenue by under-utilizing Medicaid service authorizations they can't track — each patient has an authorized number of hours per week/month, but no system monitors utilization against authorization in real time.
**Tags:** #automation #data-integration #compliance #revenue-impact #quick-win

## The Problem
Every Medicaid waiver patient has a service authorization specifying the number of hours per week or month they're approved to receive. These authorizations have start/end dates and must be renewed before expiration. Agencies are reimbursed only for services delivered within the authorized amount, but they're also leaving money on the table when they under-utilize authorizations — delivering 15 hours when 20 are authorized because no one tracked the gap. Conversely, delivering services beyond the authorized amount results in unpaid work. Tracking utilization against authorization across hundreds of patients, each with different authorization periods and hour limits, is a spreadsheet exercise that breaks constantly.

## Why It's Still Broken
Authorization data lives in the state Medicaid system or managed care organization portal. Service delivery data lives in the scheduling/EVV platform. These two systems don't talk to each other automatically. Program coordinators manually check authorization balances by logging into state portals patient-by-patient, then comparing against their scheduling records. Renewal requests must be submitted weeks before expiration, but tracking which authorizations are expiring requires a manual calendar system. The problem compounds in states with multiple managed care organizations, each with its own authorization portal and process.

## What a Fix Looks Like
A dashboard that integrates authorization data (hours authorized, period dates, renewal deadlines) with scheduling/EVV data (hours delivered, hours scheduled) to show: (1) real-time utilization percentage for each patient, (2) patients with under-utilized authorizations ranked by revenue gap, (3) authorizations approaching expiration with auto-generated renewal request workflows, (4) alerts when scheduled services would exceed authorization limits. The system pulls authorization data from state portals via API where available, or from uploaded authorization letters via document extraction where APIs don't exist.

## Who Feels the Pain
Program coordinators who spend 10-15 hours/week manually checking authorizations across state portals. Agency directors who discover at month-end that they under-utilized 15-20% of their authorized hours — leaving $50K-$200K per year in unrealized revenue.

## Impact If Fixed
Increasing authorization utilization from 80% to 95% would capture $150K-$500K in additional annual revenue for a mid-size Medicaid personal care agency. Automating renewal tracking would prevent the 5-8% of authorizations that lapse due to missed renewal deadlines, each representing a gap in care and revenue.
