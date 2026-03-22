# Real-Time OASIS Validation During Assessment

**Niche:** [[niches/home-health-agencies/oasis-documentation/profile|OASIS Assessment & Clinical Documentation]]
**Industry:** [[industries/home-health-agencies|Home Health Agencies]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** OASIS scrubber tools (SHP, OASIS Answers) catch errors after the assessment is complete — but the real need is real-time validation during the assessment, preventing errors instead of generating rework.
**Tags:** #decision-trees #gradient-boosting #feature-engineering #evaluation-metrics #compliance #automation #quick-win

## The Problem
OASIS scrubbers are a $200M+ market segment that reviews completed assessments for clinical inconsistencies, coding errors, and skip pattern violations. An agency submits an OASIS, the scrubber flags 8-12 issues, and a quality reviewer sends it back to the clinician for corrections. This cycle takes 2-5 days and requires the clinician to re-open an assessment they completed days ago, recall the patient encounter, and make corrections under time pressure. The clinician experiences this as punitive ("my assessment was rejected again") rather than educational. The errors that scrubbers catch are largely preventable: inconsistent responses, missed skip patterns, and clinically implausible combinations that a real-time check would flag in the moment.

## What Already Exists
SHP (Strategic Healthcare Programs), OASIS Answers, and similar tools provide post-completion OASIS review. These products are well-established with 5,000+ agency customers. WellSky and HCHB have basic field-level validation (required fields, value ranges) but no clinical consistency checking. The scrubber vendors have the clinical rules but apply them after completion; the EMR vendors have the point-of-entry interface but don't apply clinical rules.

## The Customization Gap
Moving OASIS validation from post-completion to real-time requires embedding the scrubber's clinical rule engine into the EMR's assessment workflow. The customization needs: (1) clinical consistency rules that fire as the clinician enters each response, not after submission (e.g., flagging immediately when a cognitive score contradicts a medication management response), (2) skip pattern enforcement that hides irrelevant questions rather than flagging them as errors later, (3) gentle in-context guidance ("Based on your wound measurement, did you intend to select 'not healing'?") rather than rejection-style error reports, (4) the ability to override with clinical justification (the clinician may be correct and the rule wrong), and (5) learning from override patterns to refine rules over time.

## Target Customer
Medicare-certified home health agencies currently paying $15K-$40K/year for OASIS scrubber services who want to reduce the scrubber rejection rate from 40-60% to under 15% by preventing errors at the point of entry.

## Impact If Solved
Shifting validation to real-time would reduce OASIS correction cycles from 2-5 days to zero for 80% of assessments, reclaiming 5-10 quality reviewer hours per week. Clinician satisfaction would improve as the assessment experience shifts from "submit and get rejected" to "guided completion with real-time support." Scrubber costs could be reduced by 50-70% as fewer assessments require post-completion review.
