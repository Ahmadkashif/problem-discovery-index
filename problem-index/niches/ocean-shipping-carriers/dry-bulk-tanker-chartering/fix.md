# The Voyage Estimate Never Compared With the Voyage

**Niche:** [[niches/ocean-shipping-carriers/dry-bulk-tanker-chartering/profile|Dry Bulk & Tanker Chartering]]
**Industry:** [[industries/ocean-shipping-carriers|Ocean Shipping Carriers]]
**Type:** Fix (Pain Point)
**One-liner:** The estimate that justified a fixture is overwritten as the voyage runs, so nobody learns which assumptions were wrong.
**Tags:** #evaluation-metrics #feature-engineering #quick-win #revenue-impact #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to fix each open ship on the cargo that earns the most once port time, bunkers and laytime are counted, and whoever fixes the fleet at the highest time-charter equivalent against the Baltic route average takes the account.

## The Problem
A chartering manager fixes a ship on an estimate of 4.5 port days, 13 knots and modest demurrage. The ship waits eight days at anchor, burns more fuel than planned and the laytime claim is disputed. The estimate is edited as the voyage progresses, so by the time the accounts close there is no frozen record of what was assumed.

## Why It's Still Broken
Freezing estimates takes discipline nobody enforces, and post-voyage reviews are done only for disasters.

## What a Fix Looks Like
Snapshot every estimate at the moment of fixing. When the voyage closes, compare each assumption with the outcome — port days, speed, consumption, laytime result, bunker price — and keep a running record of each desk's and each port's systematic bias. Feed the corrected port times back into the next estimate.

## Who Feels the Pain
Chartering managers whose estimates are wrong the same way every time, operators blamed for port delays, and owners who cannot tell skill from market luck.

## Impact If Fixed
Correcting a systematic one-day underestimate of port time on a Supramax hired at ~$15,000 a day (estimate) is worth ~$15,000 per voyage, or ~$150,000 a year per ship at ten voyages (estimate).
