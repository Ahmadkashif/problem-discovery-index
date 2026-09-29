# Assessments & Documentation

**Parent Industry:** [[industries/privacy-tech-vendors|Privacy Tech Vendors]]
**Category:** Highly Automatable
**Contested on:** Whether an impact assessment changes what gets built, or documents a decision already taken in a form a regulator will accept.

## Profile

**Market Size:** ~$700M
**Share of Parent Industry:** ~10%
**Digital Adoption:** Moderate — templates and workflow
**Target Buyer:** Privacy programme managers, privacy counsel
**Automation Potential:** Very high — assembly, routing and review are mechanical

## What Makes This a Distinct Niche

Data protection impact assessments, transfer impact assessments, legitimate interests assessments and records of processing are the documentary layer of a privacy programme. Each has a defined structure, a triggering condition and a regulatory audience.

The mechanics are well served. Templates exist, workflow routes them for review, approvals are tracked and the artefacts are stored. It is the most automatable part of the category.

The contest is about timing and consequence. An assessment performed before a decision can change what gets built — narrowing collection, adding a safeguard, choosing a different vendor. An assessment performed after the decision documents it. The overwhelming majority are performed after, as a step before launch, which makes them a compliance artefact rather than a design instrument. And because assessments are filed rather than tracked, the mitigations they specify are frequently never implemented and nobody checks.

## Current Tools & Gaps

Assessment templates by type and jurisdiction, questionnaire-driven intake, risk scoring, routing for review and approval, storage with version history, and record-of-processing generation from the same inputs. Threshold logic determining when an assessment is required.

The gaps are about effect. Assessments are triggered by someone initiating them, so processing that nobody flagged is never assessed. They are performed late, when the design is fixed. Mitigations are recorded as commitments and not tracked to implementation, so an assessment can conclude that a risk is acceptable given a safeguard that was never built. Nothing reassesses when the processing changes. Risk scoring is a questionnaire output with no relationship to observed outcomes. And the same assessment is rewritten for each framework because nothing reuses the analysis.

## Problems

- [[niches/privacy-tech-vendors/assessments-and-documentation/build|🔨 Build: Assessments That Track Their Own Mitigations]]
- [[niches/privacy-tech-vendors/assessments-and-documentation/buy|🛒 Buy: Environmental and Safety Assessment Practice]]
- [[niches/privacy-tech-vendors/assessments-and-documentation/fix|🔧 Fix: The Assessment Happens After the Decision]]
