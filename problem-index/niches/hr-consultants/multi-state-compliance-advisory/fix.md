# State Employment Law Threshold Tracking Per Client

**Niche:** [[niches/hr-consultants/multi-state-compliance-advisory/profile|Multi-State Compliance Advisory]]
**Industry:** [[industries/hr-consultants|HR Consultants]]
**Type:** Fix (Pain Point)
**One-liner:** Many employment laws trigger at specific headcount thresholds (15 employees for ADA, 20 for ADEA, 50 for FMLA, state-specific thresholds for paid leave) — when a client hires across that threshold, new obligations activate, but nobody tracks headcount against thresholds in real time.
**Tags:** #automation #compliance #data-integration #worker-facing

## The Problem
Employment law obligations are often threshold-dependent: the ADA applies at 15 employees, ADEA at 20, FMLA at 50, ACA employer mandate at 50 FTEs, and dozens of state laws at various thresholds (California's CFRA at 5 employees, New York's PFML at 1 employee, Illinois' BIPA at any size). When a client grows from 49 to 51 employees, they suddenly have FMLA obligations — but the consultant typically learns about headcount changes months later during a quarterly review. In the interim, an employee who should have received FMLA protections was denied leave, creating both a legal violation and a potential lawsuit. Tracking headcount against these thresholds requires real-time payroll/HRIS data that the consultant rarely has access to.

## Why It's Still Broken
Headcount data lives in the client's payroll system (Gusto, ADP, Paychex, QuickBooks Payroll), which the consultant may or may not have access to. Even with access, the consultant must manually check each client's headcount against a list of threshold-dependent laws for each state where the client has employees — a matrix that grows exponentially with multi-state clients. Payroll systems don't flag legal threshold crossings because they are payroll tools, not compliance tools. The consultant relies on the client self-reporting headcount changes, which happens inconsistently.

## What a Fix Looks Like
An automated threshold monitor that: (1) connects to the client's payroll/HRIS system via API (Gusto, ADP, Paychex, Rippling all offer APIs), (2) maintains a database of employment law thresholds by jurisdiction (federal, state, local), (3) monitors headcount per state in real time, and (4) alerts the consultant when any client crosses a threshold: "Client X now has 51 employees in California — CFRA obligations are now active (5+ threshold was crossed earlier, FMLA threshold now crossed). Required actions: update leave policies, train managers on FMLA administration, post required notices." The alert includes the specific compliance actions required.

## Who Feels the Pain
HR consultants who discover threshold crossings months late during quarterly reviews, and clients who unknowingly violate employment laws they didn't know applied to them.

## Impact If Fixed
Eliminates the 30-90 day gap between a threshold crossing and the consultant's awareness. Prevents violations of threshold-dependent laws that currently affect 10-15% of growing SMB clients each year. Each prevented violation saves $5,000-50,000 in potential penalties and litigation exposure.
