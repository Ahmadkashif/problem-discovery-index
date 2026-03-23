# Program-Specific QA Pre-Check

**Niche:** [[niches/energy-auditors/utility-weatherization-programs/profile|Utility Weatherization Programs]]
**Industry:** [[industries/energy-auditors|Energy Auditors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** QA validation tools exist for energy models, but none enforce the specific submission requirements of individual utility programs — catching errors weeks later instead of at data entry.
**Tags:** #gradient-boosting #anomaly-detection #tabular-ml #compliance #quick-win

## The Problem
Each utility weatherization program has specific QA requirements beyond the energy model itself: photo documentation standards (minimum 15 photos covering specific building components), data consistency rules (insulation depth must match the installed R-value in the measure list), combustion safety test results within acceptable ranges, and savings thresholds that trigger additional review. Auditors submit projects and discover QA failures 2-4 weeks later — "photo of attic insulation depth ruler not included," "blower door reading inconsistent with reported air sealing measures," "projected savings exceed program ceiling, requiring engineering review." Each QA failure delays the project by 2-4 weeks and delays the auditor's payment by the same amount.

## What Already Exists
Energy modeling software (TREAT, Ekotrope, REM/Rate) validates inputs against building science rules (e.g., R-value cannot be negative). BPI and RESNET standards define audit quality benchmarks. Some utility program portals perform basic field validation on submission (required fields, value ranges). None of these enforce the complete set of program-specific QA criteria that the program's QA reviewer will apply.

## The Customization Gap
Auditors need a pre-submission QA layer that applies the specific program's review criteria to their completed audit before submission: checking photo inventory against the program's required photo list, validating data consistency across related fields, flagging values that fall outside the program's historical distribution (anomaly detection on savings claims), and generating a QA readiness score. The tool must be configurable per program, as each utility has different requirements. When a pre-check fails, the tool identifies the specific issue and the corrective action.

## Target Customer
Energy auditors submitting to programs with 15-20% QA rejection rates who lose 2-4 weeks per rejection waiting for re-review, and utility program managers seeking to reduce QA review workload by catching obvious errors before submission.

## Impact If Solved
Reduces QA rejection rates from 15-20% to under 5%, accelerating auditor payment cycles by 2-4 weeks per project. For an auditor submitting 100 projects per year, this prevents 10-15 rejections, each costing $500-$1,000 in delayed payment and rework time.
