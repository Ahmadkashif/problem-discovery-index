# The Example That Stopped Compiling

**Niche:** [[niches/technical-content-agencies/content-drift/profile|Content Drift]]
**Industry:** [[industries/technical-content-agencies|Technical Content Agencies]]
**Type:** Fix (Pain Point)
**One-liner:** The first code sample a new developer copies has not compiled for four months.
**Tags:** #quick-win #automation #workflow-orchestration #evaluation-metrics #compliance #data-integration #descriptive-statistics #change-point-detection
**Contested on:** Every serious competitor in this niche is fighting to keep prose true about software that ships weekly, and whoever detects the drift automatically takes the account.

## The Problem
Code examples are the most used and least verified part of any documentation corpus. A developer copies the quickstart example, it does not compile, and their first experience of the product is that its documentation is wrong. The example broke when a parameter was renamed months ago. Nobody ran it, because running documentation examples is not part of anybody's pipeline, and the readers who hit it mostly leave rather than report it.

## Why It's Still Broken
Examples are prose to the build system — a code block inside a document is text as far as every pipeline is concerned, so nothing ever attempts to run it. Documentation and code are in different repositories or different processes. Readers do not report. And the failure is discovered by the people the product most wants to impress.

## What a Fix Looks Like
Run the examples, which is the single highest-value check available here. Extract and compile every code example in continuous integration, which is the fix and is a well-trodden pattern in several documentation toolchains. Run the examples that can be run, not only compile them, since compiling proves less than it appears to. Start with the quickstart and getting-started examples, as those carry the first impression and are disproportionately damaging. Fail the build on a broken example rather than reporting it, which is what keeps them working. Pin the examples to a tested version so a passing example is meaningful. Alert the team that made the breaking change, since they can fix it fastest. Track how long examples stay broken, which is the metric that shows whether the check is working. Test examples in every language the documentation offers, as the secondary languages are usually the stale ones. Make the examples themselves the test fixtures where possible, so they cannot diverge. And treat a broken quickstart as an incident, because for a new developer it is one.

## Who Feels the Pain
Developers whose first experience is a failing example; support teams receiving the resulting questions; product teams losing evaluations for a documentation defect; and writers blamed for a code change they never saw.

## Impact If Fixed
A code block inside a document is text as far as every pipeline is concerned, so nothing ever attempts to run it. Compiling and running examples in continuous integration is the highest-value check in the whole corpus.
