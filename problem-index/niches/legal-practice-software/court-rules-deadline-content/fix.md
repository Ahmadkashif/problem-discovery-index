# Nobody Publishes How Stale the Rules Are

**Niche:** [[niches/legal-practice-software/court-rules-deadline-content/profile|Court Rules & Deadline Content]]
**Industry:** [[industries/legal-practice-software|Legal Practice Software]]
**Type:** Fix (Pain Point)
**One-liner:** Deadline calculators present every computed date with identical confidence regardless of whether the underlying rule was verified last week or in 2021, and no provider publishes coverage or freshness, so firms cannot tell where the product is guessing.
**Tags:** #descriptive-statistics #evaluation-metrics #hypothesis-testing #confidence-intervals #compliance #automation #quick-win #worker-facing
**Contested on:** Every serious competitor in court rules content is fighting to detect a rule, standing order or judge-specific practice change before a deadline is computed wrongly from it — and whoever holds detection latency lowest takes the account.

## The Problem
A lawyer computes a response deadline in a state trial court division. The calculator returns a date, formatted identically to the date it returns for a federal district where the rules are checked weekly. The lawyer has no way to know that the rule behind this particular date was last verified eighteen months ago, or that the judge's standing order was never incorporated at all. The interface's uniform presentation communicates a uniform confidence that the underlying content does not have, and the lawyer relies on it, which is what the product is for.

## Why It's Still Broken
Displaying staleness is commercially unattractive: a provider that shows "last verified 14 months ago" on a fifth of its courts has published its own weakness, and no competitor does it, so the first mover is punished. Internally the data often does not exist in usable form either — rule sets are maintained without per-rule verification timestamps, because nobody ever needed one. And the buyer has never asked, because coverage and freshness are not part of how this content is compared.

## What a Fix Looks Like
Record a verification timestamp and a source against every rule, which is a schema change and a discipline rather than a project. Surface it at the point of use: a computed date carries its rule's verification age and a link to the source, and a rule below a freshness threshold is shown as provisional with the lawyer prompted to confirm. Publish coverage honestly — which courts, divisions and judges are covered, and which are not, because a silent gap is worse than a stated one. For the uncovered and the stale, route to the docketing safety net rather than presenting a confident date. The same timestamps give the content team a work queue ordered by risk instead of by rotation, which improves the content as a side effect of being honest about it.

## Who Feels the Pain
Lawyers relying uniformly on content of non-uniform quality; docketing staff who suspect certain courts are unreliable and cannot prove it; and malpractice carriers, who price this risk without any visibility into it.

## Impact If Fixed
Per-rule freshness is the measurement this niche has never had, and it turns both the product and the purchase decision honest — a firm can finally compare providers on the dimension that matters. It also gives the content team a risk-ordered queue, which is the single cheapest improvement to content quality available and requires no new technology whatsoever.
