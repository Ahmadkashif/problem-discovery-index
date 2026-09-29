# The New Licence Design Nobody Knew About

**Niche:** [[niches/identity-verification-vendors/document-and-geography-coverage/profile|Document & Geography Coverage]]
**Industry:** [[industries/identity-verification-vendors|Identity Verification Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** A state redesigned its licence, the failure rate for that state tripled, and it took five weeks to work out why.
**Tags:** #change-point-detection #quick-win #evaluation-metrics #automation #descriptive-statistics #confidence-intervals #data-integration #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to support thousands of document types across hundreds of jurisdictions, each with its own layout, security features and revision history — and whoever stops maintaining that library by hand supports the documents everyone else declines.

## The Problem
An issuing authority releases a new document design. Holders start presenting it. The system does not recognise the layout, reads fields incorrectly or fails classification, and rejects them. Nobody is watching failure rates by jurisdiction and revision, so the problem surfaces as a customer complaint weeks later, is diagnosed over another week, and a template is authored in a third. During that time every holder of the new document is rejected.

## Why It's Still Broken
Coverage is managed as a roadmap of planned additions, so new revisions are discovered reactively — a plan for what to add next has no mechanism for noticing what just changed. Issuing authorities do not notify verification vendors. Failure monitoring is aggregate rather than segmented. And the affected population is small enough per customer to look like noise.

## What a Fix Looks Like
Watch for the change in the failure data. Monitor failure rates segmented by issuing jurisdiction and document type, which is the fix and would have caught this in days rather than weeks. Alert on a change point rather than a threshold, since a tripling from a low base is the signal and an absolute threshold will miss it. Cluster the failing images, because a new design produces a tight, obvious cluster that is visually identifiable in minutes. Track issuing authority announcements where published, as many are and nobody watches them. Pool the signal across customers, since the vendor sees the change long before any single customer's volume makes it visible. Route unrecognised documents to review rather than rejecting them, so the affected people are not excluded during the gap. Shorten the template authoring path with a fast lane for detected revisions. Report time from first appearance to support, which is the metric for this whole function and does not exist. Keep older revisions supported, because they remain valid and their holders are a distinct population. And tell customers when a jurisdiction's failure rate moves, since they are fielding the complaints.

## Who Feels the Pain
Holders of newly issued documents rejected for being current; customers losing applicants in a region; support teams diagnosing a pattern nobody surfaced; and coverage teams working reactively.

## Impact If Fixed
A roadmap for what to add next has no mechanism for noticing what just changed, so revisions are discovered through complaints. Change-point monitoring by jurisdiction and document type catches the shift in days and routes affected people to review instead of rejection.
