# Non-Specialist Test Result Interpretation

**Niche:** [[niches/home-inspection/ancillary-services-specialty/profile|Ancillary Services & Specialty]]
**Industry:** [[industries/home-inspection|Home Inspection]]
**Type:** Fix (Pain Point)
**One-liner:** Home inspectors offer radon, mold, and sewer scope testing as revenue add-ons but many lack the specialist training to interpret results beyond pass/fail thresholds — leading to either over-alarming buyers with findings that are within normal ranges or under-communicating results that warrant action.
**Tags:** #gradient-boosting #worker-facing #compliance #quick-win

## The Problem
An inspector places a radon monitor, collects air samples for mold, and runs a sewer scope camera — then receives results that require specialist knowledge to interpret. Radon: the EPA action level is 4.0 pCi/L, but a reading of 3.8 in a basement with a sump pit is functionally different from 3.8 in a slab-on-grade home — the sump pit reading will fluctuate seasonally and likely exceed 4.0 in winter. Mold: a lab report showing 1,200 spores/m3 of Cladosporium is normal outdoor mold present in every home, while 200 spores/m3 of Stachybotrys (black mold) is a significant finding — but many inspectors don't know the significance by species and treat all elevated counts the same. Sewer scope: a minor root intrusion at a joint requires monitoring while a bellied section with standing water requires repair — but both look like "something wrong in the pipe" to a non-specialist. The result: inspectors either provide no interpretation beyond the raw data (unhelpful to buyers) or misinterpret findings (creating unnecessary alarm or missing real issues).

## Why It's Still Broken
Ancillary testing spans multiple scientific disciplines — radon physics, mycology, plumbing engineering — that no single home inspector is trained in. Certification courses (NRPP for radon, ACAC for mold, NASSCO for sewer) teach the mechanics of testing but often don't develop deep interpretive skill. The interpretation challenge is contextual: the same test result means different things depending on building characteristics, geographic location, season, and other inspection findings. No tool provides contextual interpretation guidance — radon monitors display a number, mold labs display spore counts, and sewer cameras display video.

## What a Fix Looks Like
An interpretation assistant embedded in the inspector's workflow where test results are processed with property context: (1) Radon: input the measured level, foundation type, presence of sump/drain tile, and season — output a contextual interpretation ("3.8 pCi/L with open sump in February suggests probable exceedance in winter months; recommend mitigation system evaluation even though current reading is below 4.0 action level"); (2) Mold: input spore counts by species from lab report plus observed moisture conditions — output significance assessment by species with reference to outdoor baseline and moisture source identification ("Stachybotrys at 200 spores/m3 is a marker for chronic water intrusion; correlate with the moisture staining observed at the south basement wall"); (3) Sewer: input defect observations with pipe material and age — output severity classification and recommended action by defect type and context. The system produces customer-facing interpretation language the inspector can include in their report.

## Who Feels the Pain
Inspectors who offer ancillary services but feel insecure about their interpretation accuracy — they know enough to run the test but not enough to confidently explain the results. Buyers who receive raw data without meaningful interpretation. Agents who ask the inspector "so what does this radon number mean?" and get an uncertain answer.

## Impact If Fixed
Transforms ancillary services from a "test-and-forward" revenue stream into a value-added consultation that justifies premium pricing. Increases inspector confidence in offering ancillary services, growing attachment rates by 15-25%. Reduces misinterpretation-related liability by providing evidence-based, contextual interpretation guidance. Enables inspectors to add $50-100 per ancillary service for "interpretation and recommendation" versus raw data delivery.
