# Third-Party Inspection Quality Scoring

**Niche:** [[niches/real-estate-appraisers/desktop-and-hybrid-appraisers/profile|Desktop & Hybrid Appraisers]]
**Industry:** [[industries/real-estate-appraisers|Real Estate Appraisers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** AMCs send third-party inspection reports (photos, measurements, condition notes) to appraisers for hybrid appraisals, but the quality varies wildly — some inspectors provide 50 clear photos with accurate measurements, others submit 10 blurry photos with estimated square footage — and no tool scores inspection quality to help the appraiser decide whether the data supports a credible valuation.
**Tags:** #cnns #gradient-boosting #automation #compliance

## The Problem
In a hybrid appraisal, the appraiser relies on a third-party inspector's data instead of personal inspection. The inspector may be a licensed real estate agent, a home inspector, or a trained data collector — their skill level varies dramatically. The appraiser receives the inspection package and must assess: are the photos clear enough to determine condition? Are the measurements accurate (or do they look estimated)? Are all required photos present (front, rear, street scene, kitchen, all bathrooms, all bedrooms)? Is the condition description consistent with the photos? If the inspection data is insufficient, the appraiser must reject the order or request re-inspection — adding delay and friction.

## What Already Exists
AMC platforms (Clear Capital, CoreLogic) that dispatch inspectors provide basic photo upload requirements. Fannie Mae's Property Data Collector app guides inspectors through required photos and measurements. Neither platform provides quality scoring of the completed inspection — the appraiser manually reviews every photo and measurement for adequacy.

## The Customization Gap
An inspection quality scoring tool needs to: (1) assess photo quality (blur detection, lighting adequacy, completeness of required angles); (2) verify measurement consistency (do the exterior dimensions match the reported GLA? Is the GLA plausible for the property type?); (3) check photo-to-description consistency (does the "C4 Good" condition rating match photos showing deferred maintenance?); (4) generate a quality score with specific deficiency flags ("missing rear exterior photo, bedroom 3 photo is too blurry for condition assessment, GLA differs from tax records by >10%").

## Target Customer
Appraisers receiving hybrid inspection packages and AMCs managing inspector quality — approximately 15,000-20,000 appraisers and 200+ AMCs nationally.

## Impact If Solved
Appraisers identify insufficient inspection data immediately instead of discovering problems mid-report (saving 1-2 hours per rejected order). AMCs improve inspector quality through feedback loops. Re-inspection rates drop from 15-20% to 5-8%, reducing cycle time and cost.
