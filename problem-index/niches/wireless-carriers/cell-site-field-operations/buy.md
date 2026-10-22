# Field Service Platforms That Understand a Cell Site

**Niche:** [[niches/wireless-carriers/cell-site-field-operations/profile|Cell Site Field Operations & Fault Diagnosis]]
**Industry:** [[industries/wireless-carriers|Wireless Carriers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Carriers already run enterprise field service platforms, built for appliance repairs and meter reads, not for sites with landlords, tower owners and FCC outage clocks.
**Tags:** #large-language-models #feature-engineering #workflow-orchestration #data-integration #worker-facing #compliance
**Contested on:** Every serious competitor in this niche is fighting to resolve a site fault on the first visit or without one, and whoever turns alarms and site history into the right part, person and decision before the truck leaves takes the field operations contract.

## The Problem
A cell site visit has constraints a generic work order ignores: landlord notice periods, rooftop escort rules, tower-owner approval before any climb, generator fuel levels, and an outage clock if enough users are affected to require an FCC NORS report.

## What Already Exists
ServiceNow Field Service Management, Salesforce Field Service and IBM Maximo, with scheduling, mobile apps, inventory and asset records.

## The Customization Gap
The adaptation needs a site object with access rules, landlord and tower-owner contacts and notice periods; a link from alarms and outage scope to the NORS reporting clock; parts kits per alarm pattern; storm mode that routes generator fuel runs by telemetry; tower-crew dispatch and climb approvals as dependent tasks; and capture of each visit's findings in structured form, drafted from the technician's voice notes and photos.

## Target Customer
Field operations and IT leaders at carriers already licensing one of these platforms.

## Impact If Solved
The carrier's existing platform starts running cell site work as it is actually done, with fewer blocked visits and on-time outage reporting.
