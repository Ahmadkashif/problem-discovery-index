# ADV Amendment Auto-Population from Firm Systems

**Niche:** [[niches/wealth-management-rias/ria-compliance-operations/profile|RIA Compliance & Regulatory Operations]]
**Industry:** [[industries/wealth-management-rias|Wealth Management RIAs]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** ADV filing tools exist (IARD, RIA in a Box) but require manual data entry of AUM, employee counts, fee schedules, and business descriptions that already exist in the firm's portfolio management and HR systems.
**Tags:** #data-integration #automation #compliance #quick-win

## The Problem
SEC-registered RIAs must file annual ADV amendments within 90 days of fiscal year-end, plus interim amendments within 30 days of material changes. Each filing requires updating AUM calculations, employee/advisor counts, disciplinary disclosures, fee schedule changes, custody disclosures, and business description text — data that already exists in the firm's portfolio management system, HRIS, and fee billing platform. The CCO manually copies these figures into the IARD filing system or a compliance tool, a process that takes 8-20 hours per annual amendment and creates data entry error risk.

## What Already Exists
The SEC's IARD system provides the filing interface. RIA in a Box and SmartRIA offer guided ADV filing workflows with templates and change-tracking. These tools reduce the complexity of understanding what needs to be disclosed but do not automatically pull the underlying data from firm systems.

## The Customization Gap
An integration layer that connects the ADV filing workflow to the firm's data sources: (1) pulls current AUM from Orion/Black Diamond via API and maps it to the ADV's Item 5 AUM reporting format; (2) pulls employee/advisor counts from HRIS or payroll systems; (3) extracts current fee schedules from the billing platform; (4) flags changes since the last filing that require narrative disclosure updates; and (5) generates a draft ADV amendment with pre-populated data fields for CCO review rather than blank-form data entry.

## Target Customer
CCOs and compliance consultants at RIAs with $500M+ AUM who file annual and interim ADV amendments and currently spend 8-20 hours per filing on manual data gathering and entry.

## Impact If Solved
Reduces ADV amendment preparation from 8-20 hours to 2-4 hours per filing, eliminates data entry errors that trigger SEC deficiency letters, and enables CCOs to focus on the substantive disclosure decisions rather than the data assembly process.
