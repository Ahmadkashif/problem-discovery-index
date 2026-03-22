# Medical Record Gap Identification

**Niche:** [[niches/personal-injury-law/underserved-rural-claimants/profile|Underserved Rural Claimants]]
**Industry:** [[industries/personal-injury-law|Personal Injury Law]]
**Type:** Fix (Pain Point)
**One-liner:** Rural PI attorneys stop discovering at settlement time that their client's medical record is too thin to support the claim — automated gap analysis identifies missing treatment documentation early enough to refer the client for supplementary evaluations.
**Tags:** #gradient-boosting #decision-trees #feature-engineering #evaluation-metrics #cross-validation #tacit-knowledge-ml #revenue-impact

## The Problem
PI case value depends on documented medical treatment: diagnosis, treatment plan, follow-up visits, specialist referrals, and functional impairment assessments. Rural clients have access to fewer providers — they see the ER once, their family doctor twice, and maybe a physical therapist 20 miles away for a few sessions. The resulting medical record is thin compared to an urban client with the same injury who sees an orthopedist, a pain management specialist, gets an MRI, and completes 12 weeks of PT. The insurance adjuster uses this documentation gap to undervalue the rural client's claim: "If the injury were really that bad, why did the client only see a doctor three times?" An experienced PI attorney recognizes this gap early and refers the client for supplementary evaluations. A less experienced attorney discovers the gap when the adjuster points it out, by which time it's too late to backfill treatment credibly.

## Why It's Still Broken
No PI case management tool analyzes the medical record for completeness relative to the claimed injuries. The "gap detection" skill is tacit knowledge — an experienced attorney looks at a cervical strain claim with only two ER visits and no imaging and knows the record won't support a demand over $15K. They've seen hundreds of cases and internalized the pattern: this injury type, with this severity, should have this treatment profile. Without that pattern recognition, the case proceeds to demand with inadequate documentation, and the settlement is 30-50% below what properly documented treatment would support.

## What a Fix Looks Like
A medical record completeness analyzer that compares the client's treatment profile against benchmarks for the claimed injury type. Input: diagnosis codes, treatment dates, provider types, and procedures from the medical record chronology. The model compares this profile against historical benchmarks: for a cervical strain with reported moderate symptoms, the expected treatment profile includes X imaging studies, Y specialist visits, and Z PT sessions over W months. Output: a gap report identifying missing elements — "No imaging study documented for cervical injury; consider referring for MRI" or "Only 3 PT sessions documented; comparable cases average 12-16 sessions." The attorney receives this gap report within 30 days of case opening, while there's still time to refer the client for supplementary evaluation. The model is trained on thousands of prior PI cases with known outcomes, learning the relationship between treatment documentation completeness and settlement value.

## Who Feels the Pain
Rural PI attorneys and their paralegals who discover at the demand stage that the medical record doesn't support the case value — by which point the credibility of additional treatment is diminished. Clients who receive lower settlements because their rural healthcare access produced thinner records than their injuries warranted.

## Impact If Fixed
Identifies treatment documentation gaps within 30 days of case opening instead of 6-12 months later at demand time. Enables timely supplementary referrals that can increase case value by 30-50% for underdocumented cases. Reduces the urban-rural settlement gap — rural clients with properly documented injuries should receive comparable settlements to urban clients with the same conditions.
