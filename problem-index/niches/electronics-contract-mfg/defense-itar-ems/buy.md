# ITAR-Aware MES Access Control Layer

**Niche:** [[niches/electronics-contract-mfg/defense-itar-ems/profile|Defense & ITAR-Compliant EMS]]
**Industry:** [[industries/electronics-contract-mfg|Electronics Contract Manufacturing]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Standard MES platforms grant system access based on job role, but ITAR requires access control based on citizenship status, program assignment, and data classification level — three dimensions that no commercial MES models natively, forcing manual access management that is error-prone and audit-sensitive.
**Tags:** #compliance #automation #data-integration

## The Problem
ITAR requires that only US persons (citizens and permanent residents) access controlled technical data. In an EMS environment, controlled technical data includes Gerber files, BOMs, test programs, and assembly instructions for ITAR-controlled programs. A standard MES grants access by role (operator, engineer, manager) without regard to citizenship or program classification. The Facility Security Officer must manually maintain an access control list mapping each employee to each program they are authorized to access, update it when employees are hired/terminated or programs are added/reclassified, and audit it quarterly. When an MES is used for both ITAR and commercial programs on the same production floor, the access control complexity multiplies.

## What Already Exists
MES platforms (Aegis, Cogiscan, Plex) provide role-based access control. Identity management platforms (Okta, Azure AD) manage user authentication. ITAR compliance tools provide training tracking and classification guidance. None integrate citizenship-based access control with program-level data classification in the MES environment.

## The Customization Gap
The ITAR-aware layer must: (1) classify each program in the MES as ITAR-controlled or commercial, (2) maintain employee authorization attributes (citizenship status verified by FSO, program-specific access authorization), (3) enforce access control at the program level (an operator can view work instructions for Program A but not Program B based on their ITAR authorization), (4) log all access to controlled data for audit trail, and (5) alert the FSO when access control anomalies occur (unauthorized access attempt, authorization expiration, new employee needing program access). This must integrate with the existing MES without replacing it.

## Target Customer
Facility Security Officers and IT Managers at ITAR-registered EMS providers running commercial MES platforms for mixed ITAR/commercial production. Approximately 150-200 US facilities.

## Impact If Solved
Manual access control list maintenance drops from 5-10 hours per week to automated enforcement. ITAR access control audit findings (a common DDTC compliance concern) decrease by 80-90%. Risk of inadvertent ITAR violation from incorrect access authorization is virtually eliminated.
