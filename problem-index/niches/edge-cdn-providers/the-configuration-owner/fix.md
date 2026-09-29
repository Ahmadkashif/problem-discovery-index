# Rules Nothing Ever Matches

**Niche:** [[niches/edge-cdn-providers/the-configuration-owner/profile|The Configuration Owner]]
**Industry:** [[industries/edge-cdn-providers|Edge & CDN Providers]]
**Type:** Fix (Pain Point)
**One-liner:** A rule set of several hundred entries contains rules that have never matched a single request, and no provider reports per-rule match counts.
**Tags:** #descriptive-statistics #graph-theory #evaluation-metrics #confidence-intervals #hypothesis-testing #quick-win #automation #worker-facing
**Contested on:** Every serious competitor that takes this seriously is fighting to let the person who owns the rule set know whether a change helped — and whoever does that takes them, because without it the rule set only ever grows and nobody dares remove a line.

## The Problem
The configuration has three hundred rules. Nobody knows which ones ever match. Among them are rules for paths that no longer exist, rules for a campaign that ended in 2021, rules shadowed by an earlier rule that always matches first, and duplicates added by two people who did not know about each other's. The owner suspects all of this and can prove none of it, so the whole set stays and is evaluated on every request. The edge evaluates each rule against every request and records nothing about which matched.

## Why It's Still Broken
Rule evaluation is on the hot path and counting matches was presumably considered an unnecessary cost, although the counter is trivial relative to the evaluation. The telemetry that exists is about requests and responses rather than about the configuration that produced them. And nobody has asked, because the customers who would benefit are the individual configuration owners rather than the accounts' buyers.

## What a Fix Looks Like
Count the matches and report the set's health. Per-rule match counts and last-matched timestamps, which is a counter on the hot path and is the whole unlock — a rule that has never matched in a year is safely removable and a rule owner cannot currently identify one. Static detection of shadowed and unreachable rules, which follows from the rule set alone without any traffic and is a straightforward analysis over an ordered rule list. Duplicate and overlap detection, since these accumulate when several people maintain one set. Evaluation cost per rule and in total, so the owner knows what the rule set costs on every request and whether pruning is worth anything beyond clarity. Age and authorship, so a rule added four years ago by someone who left is distinguishable from one added last month. Archival rather than deletion with a reversion path, which is what makes the decision safe enough to take. And a periodic report rather than a tool to invoke, because the owner is doing this alongside their actual job and will not run an audit.

## Who Feels the Pain
Configuration owners maintaining rules nobody understands; every request paying the evaluation cost of rules that never match; and organisations whose delivery behaviour is determined by an artefact no living person can read.

## Impact If Fixed
A match counter on the hot path is cheap and immediately identifies the removable population, which is usually large. Static shadowing detection requires no traffic at all and finds rules that could never have worked since the day they were added.
