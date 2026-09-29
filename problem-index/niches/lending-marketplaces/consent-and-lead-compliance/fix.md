# The Page Nobody Kept a Copy Of

**Niche:** [[niches/lending-marketplaces/consent-and-lead-compliance/profile|Consent & Lead Compliance]]
**Industry:** [[industries/lending-marketplaces|Lending Marketplaces]]
**Type:** Fix (Pain Point)
**One-liner:** Defending a contact means proving what the consumer saw, and the page has been redesigned four times since.
**Tags:** #compliance #quick-win #automation #data-integration #evaluation-metrics #workflow-orchestration #descriptive-statistics #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to prove that every contact made to every consumer was covered by a consent that survives a courtroom — and whoever makes that provable at lead level removes the largest litigation exposure in the business.

## The Problem
A complaint arrives about a call made eighteen months ago. The defence requires showing the exact page the consumer submitted, including the disclosure language, the list of named parties, and the position of the consent checkbox. The page has been through four redesigns, two copy changes and a partner list update. What exists is the current page, a database row saying consent was true, and whatever a marketing team member can remember. The record that matters was never preserved.

## Why It's Still Broken
Pages are treated as marketing assets and deployed continuously, so no versioning discipline was ever applied — and the consent record was designed as a database field rather than as evidence about a moment. Preserving rendered pages was not part of the deployment process. Disputes arrive long after the fact. And nobody has tested whether a typical lead's evidence would actually stand up.

## What a Fix Looks Like
Preserve the artefact at the moment of submission. Snapshot the rendered page with every lead, which is the fix, is cheap to store, and converts an unanswerable question into a retrieval. Version every disclosure change with a timestamp, so the page a given lead saw is identifiable even without a snapshot. Record the named partner list as it stood at submission, since the list changes constantly and it is the part most often disputed. Store the interaction detail — what was clicked, in what order, how long the page was open — because it is captured by analytics anyway and is directly probative. Run a retrieval test on a sample of historical leads, as that exercise will show immediately how many could not be defended. Keep the evidence for the full limitation period, which is longer than most retention schedules assume. Make retrieval a self-service query rather than an engineering request, since disputes arrive regularly and each currently costs days. Include the consent artefact when a lead is sold, so the buyer inherits evidence rather than an assertion. Train the marketing team that disclosure pages are governed assets, which is a process change more than a technical one. And report evidence completeness as a compliance metric, because the exposure is currently unquantified.

## Who Feels the Pain
Legal teams defending contacts with no record; compliance staff reconstructing pages from memory; lead buyers inheriting undocumented permissions; and the whole business, since this is its largest concentrated exposure.

## Impact If Fixed
Pages are marketing assets deployed continuously and the consent record was built as a database field rather than as evidence about a moment. Snapshotting the rendered page with each lead is cheap and turns an unanswerable question into a lookup.
