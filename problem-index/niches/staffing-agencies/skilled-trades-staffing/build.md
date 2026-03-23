# Structured Skill Taxonomy and Certification Matching Engine

**Niche:** [[niches/staffing-agencies/skilled-trades-staffing/profile|Skilled Trades Staffing]]
**Industry:** [[industries/staffing-agencies|Staffing Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No ATS understands that an AWS D1.1 6G certified welder with FCAW-G on carbon steel is qualified for a job requiring D1.1 3G SMAW but not one requiring D1.8 seismic work — the certification hierarchy is invisible to keyword search.
**Tags:** #transformer #ranking #nlp #graph-ml #tacit-knowledge-ml #revenue-impact

## The Problem
Skilled trades job orders specify multi-dimensional requirements that form a hierarchy: welding process (SMAW/GMAW/FCAW/GTAW), base metal (carbon steel/stainless/aluminum), position (1G through 6G), code (AWS D1.1/D1.5/ASME IX/API 1104), and site-specific safety certifications (OSHA 10/30, TWIC, MSHA, confined space). An experienced recruiter mentally maps candidate qualifications against these requirements — knowing that a 6G certification implies competency in all lower positions, that D1.1 structural steel does not qualify for D1.5 bridge work, and that a petrochemical site requires both TWIC and site-specific safety orientation. This matching logic lives in the recruiter's head. When that recruiter leaves, the agency loses the ability to make qualified matches.

## Why Nobody Has Built This
The certification hierarchies are trade-specific and complex: welding alone has 50+ distinct qualification combinations. Adding electrical (journeyman vs. master, state-specific licenses, NEC code cycle), pipefitting (ASME B31.1 vs. B31.3, material-specific qualifications), and machining (CNC program-specific, tolerance-level certifications) creates a multi-trade taxonomy that no ATS vendor has invested in building. The staffing industry's approach has been to let recruiters handle this complexity manually, which works until the recruiter leaves.

## What to Build
A structured skill and certification knowledge graph that encodes the hierarchical relationships between trade qualifications. The matching engine takes a job order's requirements, parses them into the taxonomy (process + metal + position + code + safety), identifies all candidates whose qualifications meet or exceed each requirement dimension, and ranks by overall fit. The system understands implication rules (6G implies 1G-5G, journeyman implies apprentice-level work) and exclusion rules (D1.1 does not satisfy D1.5). Candidate certifications are extracted from uploaded certificates and verified against issuing body databases where APIs exist.

## Target Customer
Branch managers and recruiters at skilled trades staffing firms with 500-5,000 candidate records and 10-50 active job orders requiring specific trade certifications.

## Impact If Built
Eliminates 60-70% of recruiter search time for skilled trades positions, prevents unqualified placements that create safety liability ($50K-$500K per incident), and makes the firm's matching capability independent of individual recruiter knowledge.
