# Estimate-to-Actual Feedback Loop Gap

**Niche:** [[niches/software-dev-agencies/project-estimation-scoping/profile|Project Estimation & Scoping]]
**Industry:** [[industries/software-dev-agencies|Software Dev Agencies]]
**Type:** Fix (Pain Point)
**One-liner:** Agencies estimate projects, deliver projects, and never systematically compare the estimate to actuals at the feature level — so the same estimation mistakes repeat indefinitely.
**Tags:** #data-integration #workflow-orchestration #quick-win

## The Problem
An agency completes 30 projects per year. Each project has an estimate (in the proposal) and actuals (in the time tracking system). But estimates live in Google Docs or PandaDoc proposals as unstructured text, while actuals live in Harvest or Toggl as time entries tagged by project — not by feature. Comparing "we estimated 120 hours for user authentication" to "we spent 180 hours on authentication" requires manually cross-referencing two systems with incompatible data structures. Nobody does this. The agency learns nothing from its estimation history. The same architect who underestimates API integrations by 40% continues to underestimate them on the next project.

## Why It's Still Broken
Estimation and time tracking are owned by different people (solutions architect vs. project manager) using different tools at different points in the project lifecycle. Connecting them requires: (1) standardized feature categories used in both estimates and time tracking, (2) time entries tagged at the feature level (not just the project level), and (3) a post-project review process that compares estimate to actual by feature. None of these exist in standard agency workflows. Post-project retrospectives focus on delivery process, not estimation accuracy. The feedback loop is never closed.

## What a Fix Looks Like
A workflow integration that: (1) exports feature categories from the approved estimate into the time tracking system as time entry tags, (2) prompts developers to tag time entries against estimated features (not just the project), (3) auto-generates an estimate vs. actual comparison report at project completion, (4) aggregates variance data across projects to identify systematic estimation patterns ("API integrations consistently take 1.8x estimated hours"), and (5) presents these patterns to the estimator before they begin the next estimate. The fix requires minimal behavior change — just adding a feature tag to time entries.

## Who Feels the Pain
Agency principals who know they mis-estimate but cannot identify specific patterns, and project managers who see budget overruns but cannot trace them back to estimation errors vs. scope changes vs. execution issues.

## Impact If Fixed
Closes the estimation feedback loop within 2-3 project cycles, enabling 10-15% improvement in estimation accuracy per quarter. Identifies the top 3 feature categories where the agency consistently underestimates, allowing targeted estimation calibration. For a $3M agency, improving estimation accuracy by 10% recovers $150K-$300K in margin annually.
