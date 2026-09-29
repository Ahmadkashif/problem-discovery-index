# The Diagnostic Script Run After the State Is Gone

**Niche:** [[niches/database-platform-vendors/database-support-engineer/profile|The Database Support Engineer]]
**Industry:** [[industries/database-platform-vendors|Database Platform Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** Support asks the customer to run a diagnostic script, which collects the current state of a database that recovered an hour ago, and reports that everything is fine.
**Tags:** #descriptive-statistics #evaluation-metrics #confidence-intervals #hypothesis-testing #k-means-clustering #quick-win #worker-facing #automation
**Contested on:** Every serious competitor that takes this seriously is fighting to capture the state that explains an incident while the incident is happening — and whoever does that takes the support organisation, because reconstruction after the fact is most of what database support does.

## The Problem
A ticket is opened after an incident. Support's first response is the standard diagnostic collection request: run this script and attach the output. The customer runs it the following morning. It collects the current session list, the current lock state, current statistics and the configuration — a complete picture of a database that is working perfectly. The genuinely useful parts are the configuration and the version. The exercise takes the customer half an hour, adds a day to the ticket, and answers nothing, and it is the first step of essentially every database support interaction.

## Why It's Still Broken
The diagnostic script was designed for the case where the problem is ongoing, which is a minority of tickets, and has been applied uniformly because it is the established first step. Nobody has separated the state that is only useful live from the configuration and history that are useful any time. Customers do not know to capture anything during an incident, because nobody told them and the incident is not the moment to read documentation. And the script's output is consumed by a human who knows which parts to ignore, which hides the inefficiency from the process.

## What a Fix Looks Like
Split the collection by when it is useful and prepare in advance. Separate the script into a live-only portion and an any-time portion, and stop requesting the former after the fact — which alone removes a day and a wasted half hour from most tickets. Give customers a one-command live capture to run during an incident, documented in advance and installed at onboarding rather than mentioned when it is too late, since a customer who has it ready will use it and one who is sent a link mid-incident will not. Enable the triggered capture described in the build note by default, so that the live state exists without anybody having to act. Collect history rather than current state where the engine retains it — the statistics snapshots, the log, the query history — and ask for it specifically. Include the version, configuration and recent change history automatically, since those are always relevant and are always requested. And measure round trips per ticket, since this single exchange accounts for a large share of them and no support organisation tracks it.

## Who Feels the Pain
Support engineers reading a snapshot of a healthy database; customers spending half an hour producing something useless; and both parties adding a day to every ticket before the investigation begins.

## Impact If Fixed
Separating the live-only collection from the any-time collection removes a wasted exchange from the majority of tickets and requires only that somebody classify the script's contents. A pre-installed live capture command turns the customer's most useful possible action into one they can actually take.
