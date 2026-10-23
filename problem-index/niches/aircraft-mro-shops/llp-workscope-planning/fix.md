# Used Parts Priced Without a Remaining-Life Comparison

**Niche:** [[niches/aircraft-mro-shops/llp-workscope-planning/profile|LLP & Workscope Planning]]
**Industry:** [[industries/aircraft-mro-shops|Aircraft MRO & FBO Shops]]
**Type:** Fix (Pain Point)
**One-liner:** A shop picks between a new LLP, a repaired one and three used offers on price per part, when the number that matters is price per remaining cycle with a clean trace.
**Tags:** #feature-engineering #linear-regression #evaluation-metrics #revenue-impact #quick-win
**Contested on:** Every serious competitor in this niche is fighting to build each engine to the cheapest workscope that still delivers the on-wing life the owner needs, with every life-limited part proven back to birth, and whoever predicts module findings and remaining part lives most accurately at induction takes the account.

## The Problem
With OEM parts supply running 10–20% short of demand (Bain, 2024), shops lean on used serviceable material to hold costs and dates. Offers arrive by email from distributors and part-out sellers, each with a price, a cycles-remaining figure and a trace package of uneven quality. Buyers and engineers compare them in a spreadsheet, often on headline price.

## Why It's Still Broken
Remaining cycles depend on the engine's thrust rating and the build's target interval, and trace quality is judged only after the documents are read. Neither fits a purchasing workflow built for consumables, so the comparison stays manual and inconsistent from one buyer to the next.

## What a Fix Looks Like
A comparison sheet generated for every LLP decision: each option's price per usable cycle for this engine's rating and target interval, the trace status from a quick document read (complete, gaps named, not yet reviewed), lead time, and the effect on the workscope's cost per flight hour. The engineer chooses; the sheet records why.

## Who Feels the Pain
Shop buyers and powerplant engineers making dozens of LLP calls per month; owners who later find a cheap part forced an early removal; records analysts asked to vet trace packages at the last minute.

## Impact If Fixed
Choosing on cost per usable cycle rather than headline price could save ~5–10% of LLP spend on visits that use used material (estimate). That is ~$150,000–$500,000 on a full CFM56- or LEAP-class LLP stack.
