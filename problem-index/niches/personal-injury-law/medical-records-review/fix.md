# Pre-Existing Condition Detection

**Niche:** [[niches/personal-injury-law/medical-records-review/profile|Medical Records Review]]
**Industry:** [[industries/personal-injury-law|Personal Injury Law]]
**Type:** Fix (Pain Point)
**One-liner:** PI attorneys stop being blindsided at deposition when the defense attorney reveals a pre-existing condition buried on page 847 of the medical records — automated detection surfaces every mention of prior injuries, chronic conditions, and contradictory patient statements before the demand goes out.
**Tags:** #bert #transformers #large-language-models #gradient-boosting #feature-engineering #evaluation-metrics #tacit-knowledge-ml #compliance

## The Problem
The single most damaging moment in a PI case is when the defense discovers a pre-existing condition the plaintiff's attorney didn't know about. The client told the ER doctor they had "no prior back problems," but a family physician's note from 18 months earlier mentions "chronic lumbar pain, prescribed meloxicam." This contradiction — buried in hundreds of pages of records — destroys the client's credibility and can reduce case value by 40-70%. Experienced medical records paralegals develop a sixth sense for these landmines — they know to look for "PMH" (past medical history) sections, medication lists that suggest chronic conditions, and intake questionnaires where patients often disclose conditions they later deny. Junior paralegals miss these entries because they're reading for the injury narrative, not scanning for defensive ammunition.

## Why It's Still Broken
Pre-existing condition detection requires understanding medical causation and relevance — not every prior medical mention is a "pre-existing condition" in the legal sense. A 2019 note about "occasional knee discomfort after running" may or may not be relevant to a 2024 knee injury from a car accident. The relevance determination requires both clinical knowledge (is this the same anatomical structure? Could the prior condition affect current symptoms?) and legal knowledge (will the defense use this to argue the injury was pre-existing? Does the "eggshell plaintiff" doctrine protect the client?). Current keyword searches ("back pain," "prior injury") generate massive false positive rates because medical records are full of references to historical conditions in review-of-systems sections that have no relevance to the current claim. The signal-to-noise ratio makes keyword searching almost useless at scale.

## What a Fix Looks Like
A pre-existing condition detection engine that goes beyond keyword matching. The model processes the full medical record set and: (1) identifies all mentions of prior conditions, injuries, and treatments in PMH sections, medication lists, intake questionnaires, and incidental mentions in clinical notes, (2) classifies each mention by relevance to the claimed injury (same body region, same condition type, related anatomy), (3) detects patient statement inconsistencies (client told Provider A "no prior back problems" but told Provider B about "chronic back pain" two years earlier), (4) assigns risk scores — high risk for directly contradictory statements and same-body-part prior conditions, medium risk for related-anatomy conditions, low risk for unrelated mentions. Output: a pre-existing condition report card that the attorney reviews before drafting the demand, with page citations to every flagged mention and an assessment of how the defense is likely to use each one.

## Who Feels the Pain
Attorneys who get ambushed at deposition or mediation with pre-existing condition evidence they should have known about. Medical records paralegals who are expected to catch every relevant prior mention across thousands of pages and feel the pressure of knowing that a single miss can tank the case.

## Impact If Fixed
Prevents the "deposition ambush" that reduces case value by 40-70% when a pre-existing condition is discovered by the defense first. Allows the attorney to proactively address pre-existing conditions in the demand letter (the "eggshell plaintiff" argument), turning a defensive weakness into a narrative strength. Reduces paralegal anxiety about missing critical details in voluminous records — the system catches what human review inevitably overlooks at page 847 of 1,200.
