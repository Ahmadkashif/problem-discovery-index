# Module-Aware Skill Matching for ERP Staffing

**Niche:** [[niches/it-staffing-firms/sap-erp-staffing/profile|SAP/ERP Implementation Staffing]]
**Industry:** [[industries/it-staffing-firms|IT Staffing Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Bullhorn and JobDiva parse resumes for keywords like "SAP" but cannot distinguish SAP FI/CO blueprint experience from SAP SD cutover experience — the distinction that determines placement success.
**Tags:** #named-entity-recognition #nlp #data-integration #automation

## The Problem
ERP staffing requires matching across four dimensions simultaneously: ERP platform and version (SAP ECC 6.0 vs. S/4HANA), module (FI/CO, MM, SD, PP, etc.), project phase (blueprint, realization, testing, cutover, hypercare), and industry vertical. Generic ATS platforms flatten this into keyword matching, returning candidates who mention "SAP" anywhere in their resume regardless of relevance. A recruiter searching for "SAP MM consultant with S/4HANA greenfield experience in CPG" gets hundreds of results that require manual review because the ATS cannot parse the dimensional structure.

## What Already Exists
Bullhorn, JobDiva, and Ceipal all offer AI-powered resume matching, but their models are trained on general IT job descriptions, not ERP-specific taxonomies. Hirebridge and some niche staffing platforms have attempted "skill ontologies" but these treat SAP as a single skill rather than a family of 50+ modules with version-specific expertise. TechFetch has an ERP-focused job board but no matching intelligence.

## The Customization Gap
The adaptation requires building a structured ERP taxonomy layer that sits on top of the existing ATS. This taxonomy must model: platform hierarchies (SAP > S/4HANA > version), module trees (FI > FI-GL, FI-AP, FI-AR), phase progression (a consultant who has done blueprint and build but not cutover), and cross-module competency (a consultant who bridges FI/CO and MM integration points). Resume parsing must extract these structured dimensions rather than treating them as flat keywords.

## Target Customer
ERP staffing firms using Bullhorn or JobDiva who process 50+ ERP consultant requisitions per quarter and rely on senior recruiters' mental models to filter candidates.

## Impact If Solved
Reduces recruiter screening time per requisition from 4-6 hours to 30 minutes by surfacing dimensionally matched candidates. Improves placement success rate by 25-35% through more precise module-phase-industry matching.
