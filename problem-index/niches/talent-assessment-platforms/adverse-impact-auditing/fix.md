# Fix: An Annual Aggregate Ratio With No Interval

**Niche:** [[niches/talent-assessment-platforms/adverse-impact-auditing/profile|Adverse Impact Auditing]]
**Industry:** [[industries/talent-assessment-platforms|Talent Assessment Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The audit reports one number per group per year, with no breakdown and no uncertainty, which is simultaneously unable to find a real problem and able to manufacture a false one.
**Tags:** #descriptive-statistics #hypothesis-testing #confidence-intervals #evaluation-metrics #compliance #quick-win #automation #workflow-orchestration
**Contested on:** Whether the audit will be computed in a form capable of detecting what it exists to detect.

## The Problem

The bias audit produces impact ratios: pass rate for one group divided by pass rate for the reference group, computed over a year, aggregated across every role the instrument was used for.

Two failures follow from that construction. It cannot find a disparity confined to one role family or one location, because the aggregate dilutes it — and role-specific disparity is the common case, since an instrument's fit to a job varies. And it reports point estimates from samples that are sometimes tiny, so a ratio of 0.74 from thirty candidates is presented identically to one from thirty thousand, producing both false alarms and false reassurance.

Everything needed to fix this is in the same dataset the audit already uses.

## Why It's Still Broken

The regulation asks for an annual audit and the market supplies exactly that. Additional granularity costs money, produces findings that require action, and earns no compliance credit.

Reporting intervals is also uncomfortable in a compliance context: a ratio with a wide interval reads as inconclusive, and a compliance document wants to conclude. That preference produces a worse analysis presented more confidently.

And the segmentation is straightforward, which means its absence is a choice rather than a limitation.

## What a Fix Looks Like

Segment it and report the uncertainty. Both are queries over data the auditor already has.

Break the ratio down by job family, role, location and time period, and report the distribution rather than only the aggregate. Where the segments disagree with the aggregate, that is the finding.

Report confidence intervals on every ratio, and state clearly where the sample is too small to conclude anything. "Insufficient data to assess" is an honest and useful output; a point estimate from twenty-eight candidates is not.

Shrink small segments toward the aggregate rather than reporting them raw. This is standard, it prevents the noisiest segments from dominating attention, and it is what makes segmented reporting usable rather than alarming.

Compute quarterly, not annually. Same analysis, four times, which catches drift within months and costs almost nothing once the pipeline exists.

Trace a detected disparity to a stage or a subscale. A multi-stage process or a multi-scale instrument has components, and knowing which one produces the disparity is the difference between a finding and an action.

And report intersectionally where the samples support it, saying explicitly where they do not.

## Who Feels the Pain

Candidates disadvantaged by a disparity confined to the role they applied for, which the aggregate audit reports as balance. Employers reassured by an audit incapable of finding their actual problem, and separately alarmed by noise from small samples. Auditors, whose professional judgement is constrained by a reporting convention that rewards a clean number. And the regulatory regime itself, whose purpose is defeated by the minimum-compliant implementation.

## Impact If Fixed

The audit becomes capable of detecting the disparities it exists to detect, by segmenting data it already has. Small-sample noise stops being reported as a finding, and genuine role-specific disparities stop being averaged away. And quarterly computation catches drift within months rather than within a year.
