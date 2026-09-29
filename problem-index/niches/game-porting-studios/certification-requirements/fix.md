# Failed Certification on a Requirement That Changed

**Niche:** [[niches/game-porting-studios/certification-requirements/profile|Certification & Platform Requirements]]
**Industry:** [[industries/game-porting-studios|Game Porting Studios]]
**Type:** Fix (Pain Point)
**One-liner:** The submission failed on a requirement that was worded differently in the previous document version, and nobody had compared them.
**Tags:** #quick-win #compliance #automation #workflow-orchestration #evaluation-metrics #descriptive-statistics #data-integration #sets-and-logic
**Contested on:** Every serious competitor in this niche is fighting to satisfy several platforms' certification regimes from requirement documents written in prose, where a late failure costs a release window — and whoever makes compliance checkable takes the account.

## The Problem
Certification requirement documents are revised between submissions. A requirement is added, tightened or reworded, and the studio working from the version it downloaded at project start does not notice. The submission fails, the resubmission cycle costs weeks, and a release window can be lost. The change was published; nobody diffed the documents, because diffing a large prose PDF by hand is not a thing anyone does.

## Why It's Still Broken
The documents are prose and nobody compares versions — a requirement set delivered as a PDF has no change notification, so an update is only discovered when it fails you. Change notices are terse or absent. The specialist is working from a spreadsheet built at project start. And the failure surfaces at the worst possible moment.

## What a Fix Looks Like
Diff the documents and re-check what moved. Diff each new requirement document against the version the project was built against, which is the fix and is straightforward text comparison once anyone does it. Maintain a per-project record of which document version was used, which most studios do not keep and which is the prerequisite. Check for new document versions on a schedule rather than at submission. Re-verify only the requirements that changed, which makes responding cheap. Subscribe to platform change notices and log them against projects. Flag requirements historically associated with failures for extra attention, since the distribution is not uniform. Verify against the current version before submission as a standing gate. Share findings across concurrent projects on the same platform, which is free within a studio and rarely happens. Keep a record of every failed certification and its cause, as the pattern is informative and nobody tabulates it. And build the diff into the project's standard milestones rather than treating it as a pre-submission scramble.

## Who Feels the Pain
Studios losing weeks to resubmission; publishers missing a release window; certification specialists blamed for a document they were never told changed; and the client relationship afterwards.

## Impact If Fixed
A requirement set delivered as a PDF has no change notification, so an update is only discovered when it fails you. Diffing against the version the project was built on is text comparison that saves a release window.
