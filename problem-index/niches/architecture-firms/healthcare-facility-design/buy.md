# Room Data Platforms With Regulatory Logic

**Niche:** [[niches/architecture-firms/healthcare-facility-design/profile|Healthcare Facility Design]]
**Industry:** [[industries/architecture-firms|Architecture Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Room data platforms already hold every room's requirements; they don't know which ones the regulation sets and the reviewer enforces.
**Tags:** #feature-engineering #large-language-models #evaluation-metrics #compliance #data-integration
**Contested on:** Every serious competitor in this niche is fighting to deliver clinical planning that passes FGI Guidelines-based state review (HCAI in California) on the first submission and matches the health system's operating model, and whoever holds that clinical and regulatory record wins the system's next project.

## The Problem
Healthcare firms track room requirements in a room data system or spreadsheet and synchronise them with Revit. The requirements mix the owner's standards, the clinical users' requests and the regulatory minimums with nothing distinguishing which is which, so a user request that drops below the regulatory minimum looks like any other change.

## What Already Exists
dRofus and similar room data and briefing platforms, with Revit synchronisation; medical equipment planning databases.

## The Customization Gap
The adaptation needs: a regulatory source attached to each requirement (FGI section, ASHRAE 170 table, state amendment); automatic alerts when a design change breaks a regulatory minimum rather than a preference; edition tracking, since a project is reviewed under the edition in force at submission; and export of a conformance matrix in the state reviewer's format.

## Target Customer
Healthcare planners and project architects at firms already licensing a room data platform.

## Impact If Solved
Regulatory conformance becomes visible during design rather than at agency review, using a platform the firm already owns.
