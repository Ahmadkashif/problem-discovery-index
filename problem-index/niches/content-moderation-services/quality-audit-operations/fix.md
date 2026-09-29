# Fix: Nobody Audits the Auditors

**Niche:** Quality Audit Operations
**Industry:** [[industries/content-moderation-services|Content Moderation Services]]
**Type:** Fix (Pain Point)
**One-liner:** Auditor severity varies substantially between individuals and drifts over time, and every bit of that variance is recorded as the accuracy of the reviewers they happened to grade.
**Tags:** #evaluation-metrics #hypothesis-testing #confidence-intervals #change-point-detection #worker-facing #compliance
**Contested on:** Whether audit effort is spent where it would change a judgement, or spread uniformly across a sample drawn at a rate the contract specified.

## The Problem

A reviewer's accuracy score is the output of two people: the reviewer who decided, and the auditor who graded. It is recorded and used as a measure of the first one only.

Auditors differ. Some are systematically stricter on borderline cases than others — the same well-understood severity effect that appears in every rater-mediated assessment system ever studied. Auditors also drift over time, individually and as a group, as they see more material and form their own readings of ambiguous policy language. And auditors are assigned to reviewers by whatever scheduling convenience dictates, which means a reviewer's monthly score depends in part on which auditor drew their sample.

In most operations none of this is measured. Calibration sessions exist and are a discussion: auditors review contested items together, talk through the reasoning and agree on an approach. Whether that discussion actually reduced severity variance is not tested afterwards, because there is no measurement either side of it.

So a reviewer coached for a drop in accuracy may have had a normal month and a strict auditor. A site that appears to be underperforming may have an auditor pool that reads one category more literally than the pool at the site it is being compared to. And the whole structure — coaching, performance plans, in some operations pay — sits on a number with an unmeasured second source of variance in it.

## Why It's Still Broken

**Measuring it requires double-auditing.** Establishing auditor severity means having multiple auditors grade the same items, which consumes audit capacity that is already fully allocated to meeting the contractual sampling rate. It is a real cost and the benefit is diffuse.

**The finding is uncomfortable in every direction.** Quantified auditor variance implicates past decisions about reviewers, raises questions about reported accuracy figures the client has been receiving, and tells individual auditors something about themselves. There is no group that wants the number.

**Calibration sessions feel like the solution.** They are visible, well-intentioned, and everybody does them, which creates a strong impression that alignment is being managed. Nobody checks whether they work, so nobody discovers that discussion-based alignment decays within weeks.

**Auditors are the quality function, and quality functions rarely turn the instrument on themselves.** The people who would have to design and run the measurement are the people it is about.

**The client audits separately and does not reconcile.** Where platform audits reach different conclusions from vendor audits on the same reviewers, the difference is usually managed as a commercial disagreement rather than investigated as evidence about both audit programmes.

**Turnover in the auditor pool.** Auditors are typically experienced reviewers, and this industry loses experienced reviewers steadily, so the pool is continuously changing and any calibration achieved is continuously eroded.

## What a Fix Looks Like

**Inject double-audited items routinely.** A modest fraction of items graded independently by two or more auditors, blind to each other, on a continuous basis. From that, severity and drift per auditor are directly estimable using statistics that have existed for decades. The cost is a small percentage of audit capacity and it is the single change that makes everything else in this section possible.

**Adjust reviewer scores for auditor severity.** Once severity is estimated, correct for it. A reviewer graded by a strict auditor should not be penalised for the assignment. This is standard practice in rater-mediated assessment everywhere else and would immediately make individual accuracy figures fairer and more comparable across sites.

**Use gold-standard items.** A maintained set of items with adjudicated correct answers, seeded into auditor workload. Auditor performance against known answers gives a direct calibration signal, catches drift quickly, and provides the objective reference the current system lacks entirely. Annotation platforms have done this for years.

**Measure calibration sessions.** Severity variance before and after. If the session did not reduce it, the session did not work, and that is worth knowing given how much time the industry spends on them. Expect to find that effects decay and that the sessions need to be far more frequent and far more specific than they are.

**Reconcile with the client's audit.** Where vendor and platform audits disagree on the same reviewers, treat it as a joint calibration problem with shared items and shared adjudication, rather than as a dispute. Both programmes have the same unmeasured variance and neither can see it alone.

**Count auditor exposure.** Auditors are re-reviewing the worst material in the queue, selected for difficulty, all day. They are frequently omitted from exposure programmes entirely because they are classified as quality staff rather than reviewers, which is an oversight that should be corrected wherever [[niches/content-moderation-services/exposure-management/profile|🟠 Reviewer Exposure Management]] is implemented.

## Who Feels the Pain

The reviewer, managed on a number containing a second person's variance that nobody has measured, and coached for a decline that may not have been theirs.

The auditor, who has no feedback on their own consistency, no objective reference, and no way to know whether they have drifted — and who is asked to be the standard without ever being measured against one.

The platform, receiving accuracy reports with an unquantified variance component, used to compare vendors and sites that may differ mainly in their auditor pools.

And the vendor's own improvement efforts, which are being aimed by a signal that is noisier than anyone believes.

## Impact If Fixed

Double-auditing a small fraction of items costs little and reveals a variance component that currently contaminates every accuracy figure in the industry. It is the cheapest high-value change available in this niche.

Severity-adjusted scores would make individual performance management substantially fairer, in a workforce where those numbers carry real consequences.

And gold-standard items would give auditors the thing they currently lack entirely: an objective reference, rather than being treated as the reference themselves.
