# The Connection That Broke in March

**Niche:** [[niches/robo-advisors/held-away-assets/profile|Held-Away Assets]]
**Industry:** [[industries/robo-advisors|Robo-Advisors]]
**Type:** Fix (Pain Point)
**One-liner:** The client linked their other accounts once, the credential expired months ago, and the net worth screen has been quietly wrong ever since.
**Tags:** #data-integration #quick-win #automation #change-point-detection #evaluation-metrics #descriptive-statistics #worker-facing #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to advise on the client's whole financial position when most of it is custodied somewhere else — and whoever makes the complete picture usable turns advice from account management into planning.

## The Problem
Account aggregation links break constantly — a password change, an institution's authentication update, a multi-factor prompt, an expired token. The client linked their 401(k) eighteen months ago and has not thought about it since. The connection failed in March. The screen still shows the last known balance, undated, as though it were current. Any advice, any net worth figure and any planning output built on it has been silently wrong for months.

## Why It's Still Broken
Aggregation is a background integration, so breakage was treated as an operational error rate rather than as a client-facing failure — the feed either works or does not and nobody owned the difference. Telling clients to re-authenticate is friction. Stale data looks identical to fresh data in the interface. And nobody reports the share of connections that are stale.

## What a Fix Looks Like
Date the data and chase the breakage. Show the as-of date on every aggregated balance, which is the fix and turns an invisible failure into an obvious one. Report the proportion of connections currently stale, since it is one query and the number will be far higher than anyone assumes. Prompt the client to reconnect with a clear reason, because clients reconnect readily when they understand what is broken and are almost never asked. Suppress or caveat any advice built on stale data, as advice from a year-old balance is worse than advice that declines to be given. Detect breakage immediately rather than letting it age, since the fix rate falls sharply with time. Prioritise chasing by account size, because the workplace plan matters more than the store card. Batch reconnection prompts sensibly so clients are not nagged weekly. Support manual update as a fallback, since some institutions will never aggregate reliably. Track reconnection rates by prompt design, which is a straightforward optimisation nobody runs. And make connection health a reported metric, so the whole aggregated picture has a known quality.

## Who Feels the Pain
Clients viewing a net worth figure that is months out of date; service associates discussing balances that no longer exist; advice engines optimising against stale inputs; and platforms whose planning outputs rest on broken feeds.

## Impact If Fixed
Breakage was treated as an integration error rate rather than a client-facing failure, and stale data looks identical to fresh data. Dating every balance and reporting the stale share makes an invisible problem impossible to ignore.
