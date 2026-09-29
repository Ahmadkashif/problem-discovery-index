# Fix: A Sortable Column of Bare Numbers

**Niche:** [[niches/talent-assessment-platforms/ats-integration/profile|ATS Integration & Score Plumbing]]
**Industry:** [[industries/talent-assessment-platforms|Talent Assessment Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The integration writes one number into one field, the applicant tracking system renders it as a sortable column, and the decision gets made from that.
**Tags:** #descriptive-statistics #evaluation-metrics #confidence-intervals #data-integration #workflow-orchestration #compliance #quick-win #worker-facing
**Contested on:** Whether the score will be displayed in a form that invites the distinctions the instrument can support.

## The Problem

A recruiter opens their candidate list. There is a column headed with the assessment name and a number in each row. They sort descending and work down the list.

That interface is the assessment's entire presence in the decision. Whatever the assessment platform's own report says about intervals, bands, constructs and appropriate use, the recruiter does not open it — they are working in the applicant tracking system, where the score is a number in a column.

The sorting is the specific harm. It invites exactly the fine-grained ranking the instrument cannot support, at the scale of a whole requisition, with a single click.

## Why It's Still Broken

The integration writes what the ATS has a field for, and the ATS has a numeric field, so a number is what arrives. Neither vendor considered that the rendering is the decision interface.

Recruiters also want to sort, reasonably — they have four hundred applicants and need an order. The instrument just cannot support the order they are creating.

And nobody owns the seam. The assessment vendor owns their report, the ATS vendor owns the list view, and the interpretation happens in the gap.

## What a Fix Looks Like

Change what arrives and how it renders. Both are modest.

Send the band, not the score, as the primary value. If the instrument supports three or four meaningful groups, that is what should populate the field. A column of "Recommended / Possible / Not recommended" cannot be over-sorted the way a percentile can.

Keep the score available in a detail view for the cases that need it, with the interval shown.

Add the warnings as visible flags in the list: out of validated range, administration compromised, near a band boundary. These should be seen without opening anything.

Group rather than sort. Where the ATS allows, present candidates grouped by band with an arbitrary order within the band, which is the honest rendering of what the instrument supports and prevents the false precision entirely.

Link to the full report from the row, so the recruiter who wants the detail is one click away rather than in another system.

And carry the instrument version and date in the record, silently, so that a later validation can interpret what it finds — the cheapest field in the payload and the one with the longest life.

## Who Feels the Pain

Candidates ranked by distinctions the instrument cannot make, at scale, by a single click. Recruiters, given an interface that invites a misuse nobody warned them about. Employers, whose selection decisions rest on a rendering choice nobody made deliberately. And assessment vendors, whose careful score report is bypassed by the integration they built.

## Impact If Fixed

The decision interface starts reflecting what the instrument supports — bands rather than a sortable percentile, with warnings visible. The false precision that a numeric column invites disappears. And the instrument version, the field nobody thought to send, makes every future validation interpretable.
