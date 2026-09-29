# Translating Four Thousand Reports

**Niche:** [[niches/data-platform-integrators/migration-scoping/profile|Migration Scoping]]
**Industry:** [[industries/data-platform-integrators|Data Platform Integrators]]
**Type:** Fix (Pain Point)
**One-liner:** The programme is translating every report in the estate and nobody has checked how many were opened last year.
**Tags:** #quick-win #data-integration #descriptive-statistics #evaluation-metrics #revenue-impact #optimization-fundamentals #automation #confidence-intervals
**Contested on:** Every serious competitor in this niche is fighting to establish which of a decade's warehouse logic and four thousand reports actually needs to move — and whoever scopes that honestly takes the account.

## The Problem
Migration programmes commit to translating the full report estate before anyone checks the access logs. The reporting tool records who opened what and when. Running that report would typically show that a large majority of the estate has not been opened in a year, and that the programme is committing years of effort to carrying it. The check takes an afternoon and happens after the scope has been agreed, if at all.

## Why It's Still Broken
The scope is set before anyone looks — an inventory count is available immediately and a usage count requires somebody to ask, so the programme is sized on the inventory. The reporting tool's access log is not part of anyone's scoping process. Clients want everything. And a smaller scope is a smaller programme.

## What a Fix Looks Like
Pull the access log before agreeing the scope. Report opens per report over the last twelve months from the reporting tool's own log, which is the fix and takes an afternoon. Include who opened it, since a report opened monthly by the chief executive is not the same as one opened monthly by its author. Rank by use and show the concentration, which is usually stark enough to change the conversation on its own. Exclude the untouched tail from the initial scope with the source kept available, which removes the risk objection. Estimate the effort and cost saved, which is the number that makes the case. Identify near-duplicate reports, since proliferation means many of the used ones overlap heavily. Migrate by usage rank so value lands early in the programme. Monitor the source for access after cutover to catch anything needed. Record what was excluded and whether anyone asked for it, which is evidence for every subsequent client. And run the same analysis on the transformation layer, where the same concentration holds.

## Who Feels the Pain
Programmes running years longer than necessary; clients paying to carry inventory onto a platform that charges to store it; engineers translating logic nobody reads; and the business case, built on an estate size rather than an estate.

## Impact If Fixed
An inventory count is available immediately and a usage count requires somebody to ask, so the programme is sized on the inventory. An afternoon with the reporting tool's access log resizes the whole programme.
