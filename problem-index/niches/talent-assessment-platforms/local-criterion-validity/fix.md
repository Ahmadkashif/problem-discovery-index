# Fix: The Scores Are Never Joined to What Happened Next

**Niche:** [[niches/talent-assessment-platforms/local-criterion-validity/profile|Local Criterion Validity]]
**Industry:** [[industries/talent-assessment-platforms|Talent Assessment Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The assessment score and the person's subsequent performance sit in two systems that never exchange a key, so the question cannot be asked at all.
**Tags:** #data-integration #descriptive-statistics #evaluation-metrics #confidence-intervals #workflow-orchestration #compliance #quick-win #hypothesis-testing
**Contested on:** Whether the assessment score will be written into the employee record at hire.

## The Problem

A candidate is assessed, scored, hired, and becomes an employee. The assessment score lives in the vendor's platform or an applicant tracking field. The employee record is created fresh in the HRIS. Nothing carries the score across.

So even an employer who wants to validate cannot, without a retrospective data project to match candidates to employees across two systems with no shared key — matching on names and dates, with the attendant errors, across several years of records.

The fix is a field. Writing the assessment score onto the employee record at the point of hire, as a retained attribute, makes every future validation a query instead of a project.

## Why It's Still Broken

The integration was scoped to move candidates into the HRIS, and the assessment score was not on anyone's list of fields to carry because nobody downstream had asked for it.

There is also a reflexive privacy caution: an assessment score is sensitive candidate data, and retaining it on an employee record feels like it needs justification. It does need a stated purpose, a retention period and access controls — which is a policy to write, not a reason to discard the field.

And nobody owns the question. The recruiting team's job ends at hire, the HR analytics team does not know the field could exist, and the assessment vendor has no interest in making validation easy.

## What a Fix Looks Like

Carry the field, with a governance wrapper.

Write the assessment score, the instrument version, the date and the requisition onto the employee record at hire, as part of the existing ATS-to-HRIS integration. This is a mapping change and it is the whole fix.

Define the governance properly: purpose limited to validation and fairness monitoring, restricted access, a defined retention period, and exclusion from any operational use in performance management or promotion. That last point matters enormously — an assessment score visible to a manager becomes a self-fulfilling prophecy and contaminates the criterion the validation depends on. Write it down and enforce it in access control.

Retain scores for non-hires too, under a separate, shorter retention and with appropriate consent, because the unselected distribution is what makes range restriction correction possible. Without it, every future validation is weaker.

Record the instrument version and configuration, since instruments change and a validation on a mixed-version sample is uninterpretable.

And backfill where a match is feasible, acknowledging the error rate. Even an imperfect retrospective join gives an employer a first look and tells them whether the proper analysis is worth commissioning.

## Who Feels the Pain

Employers who cannot answer whether their assessment works because the data was never linked, and who therefore keep using it on faith. Analytics teams asked the question and forced into a matching project. Candidates screened by an instrument whose local performance is unknowable by construction. And regulators or plaintiffs asking for evidence that cannot be produced.

## Impact If Fixed

The question becomes askable. A field written at hire converts every future validation from a data project into a query, which is the difference between an analysis that happens and one that is always proposed and never scheduled. And retaining the unselected distribution makes the correction that matters possible at all.
