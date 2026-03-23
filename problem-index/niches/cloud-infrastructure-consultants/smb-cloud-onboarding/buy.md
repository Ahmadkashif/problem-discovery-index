# Templated Migration Playbooks

**Niche:** [[niches/cloud-infrastructure-consultants/smb-cloud-onboarding/profile|SMB Cloud Onboarding]]
**Industry:** [[industries/cloud-infrastructure-consultants|Cloud Infrastructure Consultants]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Project management tools like Monday.com and Asana can track migration tasks but lack pre-built SMB migration playbooks with step-by-step instructions tailored to common small-business infrastructure patterns.
**Tags:** #workflow-orchestration #automation #quick-win

## The Problem
SMB cloud consultants run the same 5-8 migration patterns repeatedly: Exchange-to-M365, file-server-to-SharePoint, on-prem-QuickBooks-to-cloud, basic-AD-to-Entra-ID. Despite this repeatability, each consultant builds their own task lists from scratch in generic project tools, missing steps and re-learning lessons from previous engagements. There is no shared playbook library tuned to SMB-scale migrations.

## What Already Exists
Monday.com, Asana, and ClickUp offer project templates, and BitTitan provides email-specific migration automation. Microsoft FastTrack has deployment guides but they are written for IT professionals, not for SMB consultants managing 10 migrations per month with junior technicians.

## The Customization Gap
The missing layer is a library of SMB-specific migration playbooks — pre-built task sequences with estimated durations, prerequisite checks, common failure modes, and rollback procedures. These playbooks need to be parameterized by SMB profile (e.g., "10-user office with Exchange 2016 and a Synology NAS") and connected to the actual migration tooling (BitTitan, ShareGate) so tasks auto-complete when tools finish their work.

## Target Customer
SMB-focused MSPs and cloud consultants running 5-20 small migrations per month who want to standardize delivery and delegate to junior staff.

## Impact If Solved
Reduces per-migration delivery time by 35% (from 20 hours to 13 hours), allows junior technicians to execute migrations previously requiring senior staff, and cuts missed-step incidents by 60%.
