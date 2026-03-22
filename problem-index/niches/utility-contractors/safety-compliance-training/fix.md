# OSHA 1926 Trenching/Excavation Compliance Monitoring

**Niche:** [[niches/utility-contractors/safety-compliance-training/profile|Safety, Compliance & Training]]
**Industry:** [[industries/utility-contractors|Utility Contractors]]
**Type:** Fix (Pain Point)
**One-liner:** OSHA's trenching and excavation standard (1926 Subpart P) is the second-most-cited construction regulation — utility contractors average 2-5 trenching violations per OSHA inspection because field crews skip the daily competent person assessment, don't document soil classification, or use insufficient trench protection for the soil type, and the safety director has no visibility into field compliance until OSHA shows up.
**Tags:** #compliance #worker-facing #cnns #dbscan #gradient-boosting

## The Problem
Every trench over 5 feet deep (4 feet in some jurisdictions) requires: a competent person to assess soil conditions, classify the soil type (A, B, or C per OSHA), select appropriate trench protection (sloping/benching angles, shoring requirements, or trench box specifications), and document these decisions. Every day. On every trench. A utility contractor with 10 crews running 10 trenches produces 10 daily trench assessments — 50 per week, 2,500 per year. In practice, 30-50% of these assessments are not performed or not documented. The foreman "knows the soil is Type B" from experience and skips the formal classification. The crew "always uses a trench box" regardless of soil type and doesn't document the selection rationale. The safety director, located at the office, has no real-time visibility into whether today's trenches are compliant. OSHA investigators, who can arrive at any job site unannounced, request the daily assessment and find either no documentation or incomplete documentation — resulting in citations at $15,848+ per serious violation.

## Why It's Still Broken
Paper-based trench assessments are burdensome (the foreman is running a backhoe, managing traffic control, and coordinating with the utility — stopping to fill out a form is de-prioritized). Generic safety apps don't guide the foreman through the OSHA-required assessment logic: "What type of soil are you excavating in? Here's how to classify it. Based on Type B soil at 8 feet deep, you must slope at 1:1 or use a trench box rated for Type B at this depth." No tool verifies compliance visually — is the trench actually sloped to the required angle? Is the trench box properly sized?

## What a Fix Looks Like
A mobile trench compliance tool that: (1) guides the foreman through the OSHA competent person assessment in 2-3 minutes — soil classification (with visual/physical test guidance), depth measurement, trench protection selection based on soil type and depth (the system provides the correct protection requirement, eliminating guesswork); (2) captures a photo of the trench with protection in place, using a CNN-based analysis to verify that the visible slope angle approximates the required angle for the classified soil type, or that a trench box is visible and properly seated; (3) GPS-timestamps the assessment, creating an auditable compliance record; (4) sends real-time compliance status to the safety director's dashboard — showing which trenches have been assessed today and which have not, enabling proactive follow-up on missing assessments; and (5) alerts when conditions change — if the weather forecast shows rain that would reclassify soil from Type B to Type C (requiring steeper slopes or stronger protection), the system notifies affected crews.

## Who Feels the Pain
Field foremen who face personal OSHA citations ($15K+) for trenching violations they "should have documented." Safety directors who discover non-compliance only during OSHA inspections, when it's too late to correct. Utility contractors whose Experience Modification Rate (EMR) increases after trenching citations, raising workers' compensation insurance costs by 15-30%.

## Impact If Fixed
Increases daily trench assessment compliance from 50-70% to 90%+ through a guided 2-3 minute mobile workflow. Reduces OSHA trenching citations by 60-80% through documented, verifiable compliance records. Provides real-time compliance visibility to the safety director, enabling same-day correction of non-compliant trenches. Protects field foremen from personal OSHA liability through documented competent person assessments.
