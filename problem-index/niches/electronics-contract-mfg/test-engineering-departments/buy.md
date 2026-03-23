# Test Program Lifecycle Management System

**Niche:** [[niches/electronics-contract-mfg/test-engineering-departments/profile|Test Engineering Departments]]
**Industry:** [[industries/electronics-contract-mfg|Electronics Contract Manufacturing]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Test programs, fixtures, and test limits are managed in engineer-specific directories on shared drives with no version control, no change history, and no linkage between the test program and the BOM revision it validates — creating a configuration management nightmare when BOMs change and test programs must be updated.
**Tags:** #workflow-orchestration #data-integration #compliance

## The Problem
Each customer program has an ICT test program (test vectors, component values, limits), an FCT test program (functional test sequences), and physical test fixtures — all of which must be updated when the customer revises their BOM (new components, value changes, layout modifications). Test programs are stored on the test system's local drive or a shared network folder, with version control ranging from "filename with date" to none at all. When a BOM revision arrives, the test engineer must manually identify which test program changes are needed, update the program, validate the changes, and document the update. If the wrong test program version is loaded (because the latest version was not clearly identified), boards are tested against incorrect limits — either passing defective boards or failing good ones.

## What Already Exists
PLM/PDM systems (Siemens Teamcenter, PTC Windchill) manage design data lifecycle with version control, change management, and release workflows. Test system vendors (Teradyne, Keysight) provide test program editors but no lifecycle management. Document control in QMS (MasterControl, Veeva) could technically manage test programs as controlled documents but lacks the test-specific metadata (which BOM revision, which fixture, which test system hardware configuration).

## The Customization Gap
A test program lifecycle system must: (1) link each test program version to a specific BOM revision and fixture revision, (2) trigger test program review when a BOM change notification is received, (3) manage test limit changes with approval workflow (limit changes affect product quality decisions), (4) track fixture maintenance and calibration status, and (5) ensure the correct test program version is loaded on the test system for each production run. This requires integration with the PLM/ERP (BOM revision notifications), the test system (program loading), and the QMS (change control workflow).

## Target Customer
Test engineering managers and quality managers at EMS providers with 3+ test platforms and 30+ active test programs. Approximately 200-300 US EMS facilities.

## Impact If Solved
Wrong-version test program loading events decrease by 90%+. BOM revision-to-test-program update cycle drops from 1-2 weeks to 2-3 days. Test program change control documentation (often an audit finding) becomes automated rather than manual.
