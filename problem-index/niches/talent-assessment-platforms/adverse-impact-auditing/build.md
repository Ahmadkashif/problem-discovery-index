# Build: Continuous, Segmented Impact Monitoring With Honest Inference

**Niche:** [[niches/talent-assessment-platforms/adverse-impact-auditing/profile|Adverse Impact Auditing]]
**Industry:** [[industries/talent-assessment-platforms|Talent Assessment Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Monitor pass rates by group continuously and by segment, with intervals, so a real disparity is detected where it happens instead of averaged into an annual figure.
**Tags:** #hypothesis-testing #confidence-intervals #bayesian-inference #descriptive-statistics #evaluation-metrics #change-point-detection #compliance #automation
**Contested on:** Whether disparities can be detected reliably at the requisition and role level where sample sizes are small.

## The Problem

Bias auditing has become a legal requirement in some jurisdictions and is generally conducted once a year on aggregate pass rates, which is the least informative form it could take.

Aggregation across roles hides the pattern. An instrument balanced overall can produce a substantial disparity in one job family and the opposite in another, and the aggregate reports neither. Aggregation across time hides drift — an instrument fair in January can be unfair by September as the applicant population shifts, and an annual audit finds out eleven months late.

And the reporting convention makes inference impossible. Impact ratios are presented as point estimates, so a ratio computed from nineteen candidates in one group is reported with the same apparent authority as one from nineteen thousand, and both noise and real disparities are misread.

## Why Nobody Has Built This

The regulation specifies an annual audit on defined categories, and the market has built to that specification exactly. Doing more is a cost with no compliance benefit and a risk: a granular continuous monitor will find disparities that an annual aggregate would not, and having found them the employer has to act.

The small-sample inference problem is also genuinely awkward. Requisition-level analysis produces wide intervals and a lot of uncertainty, which is harder to report than a clean ratio and invites the objection that the analysis is inconclusive — which it frequently is, and saying so is more honest than the point estimate.

## What to Build

A continuous, segmented monitor with inference reported properly.

**Compute at every level and report the hierarchy.** Overall, by job family, by role, by location, by requisition, over time. The aggregate stays for compliance and the segments are where problems live.

**Report intervals, always.** An impact ratio from a small sample needs a confidence interval or it is not a finding. Bayesian estimation with shrinkage toward the aggregate handles the many-small-segments structure well and prevents both false alarms and false reassurance.

**Detect drift.** Pass-rate ratios as a time series per segment, with change-point detection. An instrument whose impact changes needs to be investigated when it changes, not at the next annual audit.

**Analyse intersectionally where samples permit.** Single-axis analysis can show balance on each dimension separately while a specific intersection is substantially disadvantaged. Sample sizes limit how far this can go and saying where it runs out is part of the analysis.

**Handle missing demographic data honestly.** Self-reported demographics are incomplete and non-response is not random. Sensitivity analysis over plausible assumptions about the missing, rather than analysis on complete cases as though they were the population.

**Trace the disparity to its source.** Which items, which subscales, which stages of a multi-stage process. An employer told their assessment has a disparity can do little; one told it arises in one subscale used for one role family has something to fix.

**Attach an action framework.** Threshold crossed, investigation triggered, remedy considered, decision recorded. An audit without a defined response is a document, and the regulatory regimes are moving toward asking what was done.

## Target Customer

Large employers with multi-jurisdiction exposure, for whom the annual minimum is already insufficient and who would rather find a problem themselves than have it found. Also the bias audit providers, for whom continuous segmented monitoring is the product beyond a compliance artefact, and vendors differentiating on it.

## Impact If Built

Disparities get detected where they occur — in a role, in a subscale, in a quarter — rather than averaged into an annual number. Small-sample findings get reported with the uncertainty they carry. And the employer finds their own problems before a regulator, a plaintiff or a journalist does.
