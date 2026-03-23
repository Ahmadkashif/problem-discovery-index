# Integrated WAP Intake-Audit-Production Workflow

**Niche:** [[niches/energy-auditors/low-income-community-programs/profile|Low-Income Community Programs]]
**Industry:** [[industries/energy-auditors|Energy Auditors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No platform connects WAP client intake (income verification, priority scoring) to energy audit (NEAT/MHEA) to production tracking (installation, inspection) to state reporting in a single system.
**Tags:** #workflow-orchestration #automation #data-integration #compliance

## The Problem
A community action agency processing a WAP client moves through 6 disconnected steps: (1) client application intake with income and eligibility documentation, (2) DOE priority scoring (elderly, disabled, children under 6, high energy burden), (3) scheduling and completing the energy audit (NEAT/MHEA), (4) developing the work scope from audit results, (5) tracking installation by weatherization crews, and (6) reporting production metrics to the state energy office. Each step uses a different system — eligibility determination in a custom database or spreadsheet, NEAT/MHEA on a desktop computer, work scope in a separate spreadsheet, production tracking in yet another database, and state reporting through a state portal. Client data (address, household composition, utility account numbers) is entered 3-5 times across these systems.

## Why Nobody Has Built This
WAP is funded through a single federal program administered by 50+ state energy offices, each with different reporting requirements and portal interfaces. The mandated use of NEAT/MHEA limits flexibility — any new system must either replace NEAT/MHEA (requiring DOE approval) or integrate with their data formats. The 800 CAAs are nonprofit agencies with minimal technology budgets ($0-$5,000/year for software), making the revenue opportunity unattractive for commercial software vendors. DOE has not funded a comprehensive modernization of the WAP technology stack.

## What to Build
A cloud-based WAP workflow platform that unifies: client intake with eligibility verification and priority scoring, NEAT/MHEA-compatible energy audit data collection (feeding into the existing audit engines or a modern alternative), work scope development with DOE-approved measure lists and cost estimation, production tracking with crew scheduling and inspection management, and state reporting with auto-populated submission forms. Client data enters once and flows through the entire pipeline. The platform must support offline field data collection (many WAP homes are in rural/low-connectivity areas).

## Target Customer
Community action agencies administering WAP programs that process 100-1,000 units per year and currently spend 40-50% of staff time on administrative data management.

## Impact If Built
Reduces per-unit administrative processing time by 50-60%, enabling CAAs to weatherize 30-40% more homes with existing staff — directly addressing the 12-24 month wait lists caused by administrative bottlenecks rather than funding shortages. For a CAA spending its $500K annual WAP allocation, this could mean 30-50 additional homes weatherized per year.
