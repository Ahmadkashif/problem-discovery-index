# OASIS Assessment & Clinical Documentation

**Parent Industry:** [[industries/home-health-agencies|Home Health Agencies]]
**Category:** Highly Automatable

## Profile
**Market Size:** $5-7B (embedded across all Medicare home health)
**Share of Parent Industry:** Touches all Medicare-certified agencies
**Digital Adoption:** Medium — All agencies use digital OASIS forms, but the tools are electronic paper; no intelligent guidance, auto-population, or real-time validation exists
**Target Buyer:** Clinical quality director / Director of Nursing
**Automation Potential:** Very High — OASIS has deterministic skip patterns, predictable response carry-forward, and quantifiable consistency rules that are ideal for rule-engine and ML automation

## What Makes This a Distinct Niche
OASIS is the federally mandated assessment instrument for Medicare home health. Its 89 data elements drive everything: PDGM payment classification, quality Star Ratings, patient outcome measurement, and CMS survey readiness. Despite its centrality, the OASIS workflow is brutal — 45-90 minutes per assessment at admission, every 60-day recertification, and discharge. Complex skip patterns lead clinicians to answer irrelevant questions or skip critical ones. Errors cascade: an incorrect functional status response changes the PDGM payment group, an inconsistent wound assessment triggers a claim denial, and a missed assessment window makes the entire episode unbillable.

## Current Tools & Gaps
WellSky, HCHB, and Axxess all have OASIS modules that present the 89-element form digitally. Post-completion scrubber tools (SHP, OASIS Answers, Strategic Healthcare Programs) review submitted assessments for errors and suggest corrections. The gap is timing: all quality checking happens after the clinician has spent 60+ minutes completing the assessment, generating corrections and rework rather than preventing errors during entry. No tool auto-populates stable responses from prior assessments, enforces skip patterns dynamically, validates clinical consistency in real-time, or shows PDGM payment implications as the clinician enters responses.

## Problems
- [[niches/home-health-agencies/oasis-documentation/build|🔨 Build: AI-Guided OASIS Assessment with Auto-Population]]
- [[niches/home-health-agencies/oasis-documentation/buy|🛒 Buy: Real-Time OASIS Validation During Assessment]]
- [[niches/home-health-agencies/oasis-documentation/fix|🔧 Fix: OASIS Timing Compliance and Window Tracking]]
