# Inspector-to-Inspector Variation on Boundary Conditions

**Niche:** [[niches/contract-manufacturing/quality-inspection-automation/profile|Quality Inspection Automation]]
**Industry:** [[industries/contract-manufacturing|Contract Manufacturing]]
**Type:** Fix (Pain Point)
**One-liner:** Two inspectors looking at the same borderline surface condition will disagree 10-25% of the time — creating unpredictable quality outcomes where the same part is accepted on day shift and rejected on night shift depending on who is inspecting.
**Tags:** #cnns #evaluation-metrics #tacit-knowledge-ml #worker-facing #compliance

## The Problem
Visual inspection standards describe acceptance criteria in language that requires human interpretation: "surface porosity is acceptable if individual pits do not exceed 0.3mm and total affected area does not exceed 2% of the surface." At the boundaries of these criteria — is that pit 0.25mm or 0.35mm? Is the affected area 1.8% or 2.2%? — experienced inspectors make judgment calls that vary by individual, shift, fatigue level, and even the inspection batch (after rejecting 5 borderline parts in a row, the inspector's threshold unconsciously shifts toward acceptance). Studies in manufacturing quality literature consistently find 10-25% disagreement between inspectors on the same boundary-condition samples. This variation creates two problems: quality escapes (defective parts passed by lenient inspectors) and over-rejection (acceptable parts scrapped by strict inspectors).

## Why It's Still Broken
Gauge R&R studies (measurement system analysis for inspection) document the variation but don't fix it — they quantify the problem in a report that management reviews annually but doesn't act on daily. Inspector calibration training helps but the effect fades within weeks as individual habits reassert. The fundamental issue is that human visual perception varies — two people literally see the same surface differently — and no amount of training eliminates this biological variability at the boundary conditions where standards are ambiguous.

## What a Fix Looks Like
A vision-assisted inspection system for boundary conditions: when the primary inspection model classifies a part as borderline (confidence between 40-60%), it presents the inspector with the flagged condition alongside reference images of the nearest accept and reject examples from the calibration set. The inspector makes the final call, but with visual calibration context that anchors their judgment to the standard rather than to their individual perception. All borderline dispositions are logged with images and inspector ID, enabling R&R analysis at the individual level — identifying which inspectors consistently deviate from consensus on specific defect types.

## Who Feels the Pain
Quality managers who discover inspector variation through customer complaints (quality escapes) or yield reports (unexplained rejection rate differences between shifts), and inspectors who are uncertain about borderline calls and feel pressure from production to accept marginal parts.

## Impact If Fixed
Reduces inspector-to-inspector variation from 10-25% disagreement to under 5% on boundary conditions. Decreases quality escapes by 30-50% — the highest-cost quality failure mode. Reduces over-rejection by 15-25%, recovering scrap that is actually acceptable product. For a CM with $10M annual production and 2% over-rejection rate, reducing by half saves $100,000 annually in unnecessary scrap.
