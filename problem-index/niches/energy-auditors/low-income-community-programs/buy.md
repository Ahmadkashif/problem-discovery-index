# NEAT/MHEA Data Migration and Modern Interface

**Niche:** [[niches/energy-auditors/low-income-community-programs/profile|Low-Income Community Programs]]
**Industry:** [[industries/energy-auditors|Energy Auditors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** NEAT/MHEA audit tools have 1990s-era interfaces and desktop-only operation, but replacing them requires DOE approval — a modernized interface layer over the existing engines could bypass this constraint.
**Tags:** #automation #data-integration #worker-facing #quick-win

## The Problem
NEAT (National Energy Audit Tool) and MHEA (Manufactured Home Energy Audit) are the audit tools mandated by DOE for WAP-funded work. They run as desktop applications with interfaces designed in the 1990s — dozens of data entry screens with no field data collection capability, no mobile access, and no integration with modern tools. Auditors collect data on paper in the field, return to the office, and manually enter it into NEAT/MHEA — a process that takes 2-3 hours per audit. The software crashes frequently on modern operating systems, data files are stored locally (no cloud backup), and training new auditors on the non-intuitive interface takes weeks. Despite these limitations, CAAs cannot switch to alternatives without state energy office approval, and states are reluctant to approve tools that have not been validated against NEAT/MHEA outputs.

## What Already Exists
WxPROE was developed as a web-based WAP audit tool and has gained some state approvals, but adoption is limited and it does not yet replicate all NEAT/MHEA functionality. Ekotrope is DOE-approved for some programs but not universally accepted for WAP. Modern field data collection apps (Fulcrum, GoCanvas) can capture audit data on mobile devices but do not connect to NEAT/MHEA input formats.

## The Customization Gap
WAP auditors need a modern interface layer — mobile-first field data collection that maps directly to NEAT/MHEA input fields, with data exported in NEAT/MHEA-compatible format for analysis. This approach preserves the DOE-mandated audit engine (avoiding the approval barrier) while modernizing the data collection experience. The interface must: replicate every NEAT/MHEA data entry field in a mobile-friendly format, validate entries in real time against building science rules, capture photos linked to specific data points, and export data files that NEAT/MHEA can import without manual re-entry.

## Target Customer
Community action agencies with 3-10 WAP auditors who currently lose 2-3 hours per audit to paper-to-desktop data entry and experience frequent data loss from NEAT/MHEA crashes.

## Impact If Solved
Eliminates 2-3 hours of per-audit data re-entry (saving 200-600 hours annually per CAA), reduces data entry errors by 40-50% through real-time validation, and provides cloud backup for audit data that was previously stored only on local desktops vulnerable to crashes and hardware failures.
