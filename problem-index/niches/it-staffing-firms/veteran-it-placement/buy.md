# Veteran-Aware Resume Parsing for ATS Platforms

**Niche:** [[niches/it-staffing-firms/veteran-it-placement/profile|Veteran IT Career Placement]]
**Industry:** [[industries/it-staffing-firms|IT Staffing Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Bullhorn and JobDiva parse military resumes into garbage — "SIPR network administration" maps to nothing, "DISA STIG compliance" is not recognized as security hardening, and rank/grade structures are ignored entirely.
**Tags:** #named-entity-recognition #nlp #data-integration #worker-facing

## The Problem
When a veteran submits a resume to an IT staffing firm, the ATS resume parser fails on multiple levels: military acronyms are not resolved (SIPR, NIPR, DISA, STIG, ATO), military rank does not map to experience level (an E-6 with 8 years is mid-senior but the ATS has no rank-to-level mapping), military training courses are not recognized as equivalent certifications (Army Cyber School coursework covers material equivalent to CompTIA Security+ but is not flagged), and military job titles do not match civilian search terms. The veteran's profile sits unsearchable in the ATS database.

## What Already Exists
Sovren (now Textkernel) and DaXtra offer resume parsing engines used by most ATS platforms. These parsers are trained on civilian resume formats and vocabulary. Some have added basic military MOS lookup, but this only maps the MOS code to a generic occupation title — it does not parse the body of the resume for military-specific terminology. Hire Heroes USA offers resume rewriting services, but this is a manual, one-time process that does not scale.

## The Customization Gap
The parser needs a military-to-civilian terminology layer that: (1) resolves military acronyms to their civilian equivalents in the parsed output, (2) maps military ranks to experience-level tags (E-4 = junior, E-6 = mid, O-3 = senior/management), (3) recognizes military training programs as certification equivalents, (4) extracts security clearance information as a structured field, and (5) maps military unit types to industry context (working in a medical battalion = healthcare IT experience). This layer must plug into existing ATS platforms via their parsing API extensions.

## Target Customer
IT staffing firms that have committed to veteran hiring programs but find that their existing ATS technology renders veteran candidates invisible in searches.

## Impact If Solved
Makes 80-90% of veteran IT candidates searchable in existing ATS databases, increasing veteran placement rates by 30-40%. For a firm with 500 veteran candidates in their database, this surfaces 100-200 previously unfindable qualified candidates.
