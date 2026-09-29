# The Wash Sale in the Other Account

**Niche:** [[niches/robo-advisors/tax-loss-harvesting/profile|Tax-Loss Harvesting]]
**Industry:** [[industries/robo-advisors|Robo-Advisors]]
**Type:** Fix (Pain Point)
**One-liner:** The platform avoids wash sales perfectly inside its own accounts and the client's workplace plan buys the same fund every payday.
**Tags:** #compliance #quick-win #data-integration #automation #evaluation-metrics #descriptive-statistics #workflow-orchestration #confidence-intervals
**Contested on:** Every serious competitor in this niche is fighting to prove what harvesting actually delivered for this specific client after wash-sale exposure they cannot see — and whoever can state a per-client realised number replaces an industry-wide average that applies to almost nobody.

## The Problem
The platform harvests a loss on a broad market fund and buys a substitute. Meanwhile the client's 401(k) contribution buys the same index fund every two weeks, their spouse's IRA holds it, and their brokerage account rebalanced into it last month. Any of those can trigger a wash sale that disallows the loss. The platform cannot see them, does not ask about them in a usable way, and reports the harvested loss as though it were secured.

## Why It's Still Broken
Wash-sale avoidance was scoped to the accounts the platform controls, which is the boundary the engineering naturally took — and the client's other accounts were treated as their problem because the platform has no line of sight. Asking about external holdings is friction at onboarding. The exposure usually surfaces at tax time if at all. And nobody measures how often it happens.

## What a Fix Looks Like
Ask, warn, and avoid the obvious cases. Ask the client which funds they hold elsewhere and in what accounts, which is the fix and is a short question that prevents the most common failure. Warn explicitly about workplace plan contributions, since automatic biweekly purchases of a broad index fund are the single most frequent trigger and almost no client knows it. Choose substitutes that avoid the funds the client has disclosed, because the avoidance is easy once the exposure is known. Explain the risk in plain terms at the point it matters, as clients are not told at all and would act if they were. Flag the harvested losses that are at risk rather than reporting them as clean, which is an accuracy fix as much as a client service one. Use aggregation where the client connects accounts, since that closes the loop entirely and connects to held-away assets. Re-ask periodically, because plans and holdings change. Report how many harvests are potentially exposed, which is a number nobody has and which will justify the work. Give the client a document their preparer can use, since the reconciliation currently falls on them. And handle the spouse case explicitly, as it is common, counterintuitive and never mentioned.

## Who Feels the Pain
Clients whose harvested losses are disallowed; tax preparers discovering it in April; platforms reporting benefits that may not exist; and the credibility of the category's headline feature.

## Impact If Fixed
Avoidance was scoped to the accounts the platform controls and everything outside was treated as the client's problem. A short disclosure question plus a warning about workplace plan contributions removes the most common exposure entirely.
