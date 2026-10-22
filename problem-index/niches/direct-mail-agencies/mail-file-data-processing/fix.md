# Net-Name Counts Nobody Can Reproduce

**Niche:** [[niches/direct-mail-agencies/mail-file-data-processing/profile|Mail File Data Processing]]
**Industry:** [[industries/direct-mail-agencies|Direct Mail Agencies]]
**Type:** Fix (Pain Point)
**One-liner:** A list owner questions the net-name count on an invoice three months after the drop, and the processor cannot rebuild the run that produced it.
**Tags:** #descriptive-statistics #evaluation-metrics #data-integration #compliance #quick-win
**Contested on:** Every serious competitor in this niche is fighting to build a deduplicated, suppressed, Move-Update-compliant mail file from a dozen sources by the list due date, with every surviving name traced to its source for net-name billing — and whoever does it fastest with counts the list owners never dispute takes the account.

## The Problem
Rented lists are billed on the names that survive merge/purge, usually with a contractual floor. The count depends on the priority order, the match rules, the suppressions applied and any late changes — all of which may have been adjusted between runs. When a list manager disputes the count, the agency's only evidence is the final report.

## Why It's Still Broken
Merge/purge jobs are run, output, and overwritten; the exact inputs, rule settings and reruns are not versioned together. Disputes are settled by negotiation rather than evidence.

## What a Fix Looks Like
Version every job run as a package — input files with checksums, rule settings, priority order, suppression files and output — and generate the net-name report from that package, so any count can be reproduced and explained name by name.

## Who Feels the Pain
Data processors asked to defend a number from months ago; list managers chasing revenue; agencies writing off disputed invoices.

## Impact If Fixed
Reproducible counts end most disputes quickly and make the agency a list manager's preferred customer.
