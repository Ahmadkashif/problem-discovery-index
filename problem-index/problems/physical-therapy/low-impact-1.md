# Home Exercise Program Compliance Tracking

**Industry:** [[physical-therapy|Physical Therapy]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Home exercise apps exist by the hundreds, but none close the loop between what the PT prescribes, what the patient actually does at home, and how that adherence connects to clinical progress in the EMR.
**Tags:** #time-series-forecasting #linear-regression #evaluation-metrics #descriptive-statistics #worker-facing #data-integration

## The Problem
Physical therapists prescribe home exercise programs (HEPs) at every visit — typically 4-8 exercises with specific sets, reps, and frequency. Patient adherence is estimated at 30-50%, but PTs have no reliable data on actual compliance. At the next visit, the PT asks "did you do your exercises?" and the patient says "mostly" — and the PT adjusts the treatment plan based on this unreliable self-report. Poor HEP adherence is the #1 reason patients plateau, and PTs can't differentiate between "the program isn't working" and "the patient isn't doing the program."

## What Already Exists
HEP platforms like MedBridge, PhysiTrack, PT Wired, and HEP2go let PTs create exercise programs with videos and send them to patients via app or email. Some include basic adherence tracking (patient self-reports completing exercises).

## The Customisation Gap
The gap is bidirectional data flow: the HEP platform needs to feed actual adherence data back into the PT's clinical workflow — not as a separate app the PT checks, but integrated into the visit note workflow. When a patient's PHQ-9 equivalent for PT (a functional outcome measure) isn't improving, the system should surface whether adherence is the likely culprit. The exercise prescription also needs to update automatically when the PT modifies the treatment plan in the EMR, rather than requiring manual re-creation in the HEP app.

## Impact If Solved
Gives PTs actionable adherence data for clinical decision-making. Estimated 15-20% improvement in patient outcomes when PTs can address non-adherence directly. Saves 5 minutes per visit currently spent asking about and documenting HEP compliance.
