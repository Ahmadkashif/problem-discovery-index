# Channel Plans Changed by Trial and Error at Midnight

**Niche:** [[niches/wireless-carriers/wisp-sector-qoe/profile|WISP Sector Congestion & Subscriber Experience]]
**Industry:** [[industries/wireless-carriers|Wireless Carriers]]
**Type:** Fix (Pain Point)
**One-liner:** When interference hits an unlicensed sector, the engineer tries channels one at a time late at night and records nothing about what worked.
**Tags:** #bayesian-optimization #feature-engineering #worker-facing #quick-win #automation
**Contested on:** Every serious competitor in this niche (subscriber-experience platforms, radio controllers and traffic shapers) is fighting to find first which sector, link or interferer is pushing which homes below plan at evening peak and what to change, and whoever diagnoses and fixes that fastest takes the account.

## The Problem
Interference in unlicensed bands changes as neighbours install gear. The fix is a channel or width change, but each change briefly disconnects customers, so engineers do it after midnight, one try at a time, judging by feel.

## Why It's Still Broken
Spectrum scans exist on many radios but aren't combined across sectors, and changes aren't logged with before-and-after results.

## What a Fix Looks Like
Collect scans from all radios on a tower, propose a channel plan that minimises self- and external interference, and log each change with its measured effect so the next proposal is better.

## Who Feels the Pain
WISP engineers working nights, and customers on the affected sector.

## Impact If Fixed
Fewer late nights and faster, documented recovery from interference.
