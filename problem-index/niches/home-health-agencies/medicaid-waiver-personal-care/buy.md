# Cross-State EVV Reconciliation with Medicaid Billing

**Niche:** [[niches/home-health-agencies/medicaid-waiver-personal-care/profile|Medicaid Waiver Personal Care Programs]]
**Industry:** [[industries/home-health-agencies|Home Health Agencies]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** EVV systems exist per state mandate, but none reconcile visit verification data with Medicaid billing across state-specific formats or handle the self-directed care model where the patient is the employer.
**Tags:** #decision-trees #feature-engineering #automation #compliance #data-integration #workflow-orchestration #quick-win

## The Problem
The 21st Century Cures Act mandated EVV for Medicaid-funded personal care services, but implementation was delegated to states. Some states use Sandata, others use HHAeXchange, others built proprietary systems. Each state requires different data elements, different submission formats, and different reconciliation timelines. An agency operating in three states must maintain three separate EVV workflows and manually reconcile each state's EVV data with its billing system. In self-directed care models (CDPAP, IHSS), the patient/family member who is the "employer" must interact with the EVV system — adding a consumer-facing usability challenge that enterprise EVV platforms were never designed for.

## What Already Exists
HHAeXchange is the leading Medicaid home care EVV and billing platform, operating in 30+ states. Sandata provides EVV aggregation in several states. State-built EVV systems exist in a handful of states. Each solution handles one state well but none provide a unified cross-state view or handle the billing reconciliation step end-to-end.

## The Customization Gap
The gap is a translation and reconciliation layer that sits between state-specific EVV systems and the agency's billing platform. This layer would: (1) normalize EVV data from different state formats into a common schema, (2) auto-reconcile verified visits against Medicaid service authorizations, (3) generate state-specific billing files from reconciled data, (4) flag discrepancies (visit verified but not authorized, authorized but no visit recorded) before claim submission, and (5) provide a simplified EVV interface for self-directed care participants who are patients or family caregivers, not healthcare professionals.

## Target Customer
Medicaid personal care agencies operating in 2+ states or managing 500+ self-directed care participants who struggle with EVV compliance and Medicaid billing reconciliation.

## Impact If Solved
Automating EVV-to-billing reconciliation would eliminate 15-20 hours/week of manual reconciliation work per state. Reducing EVV-related claim rejections by 40-60% would recover $100K-$300K annually. For self-directed care programs, a usable consumer-facing EVV interface would reduce the 10-15% of visits that go unverified due to participant technology barriers.
