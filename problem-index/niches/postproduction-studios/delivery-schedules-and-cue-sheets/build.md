# A Delivery Schedule That Tracks Its Own Evidence

**Niche:** [[niches/postproduction-studios/delivery-schedules-and-cue-sheets/profile|Delivery Schedules, Cue Sheets & Paper Deliverables]]
**Industry:** [[industries/postproduction-studios|Postproduction Studios]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every distributor writes its delivery schedule differently, and every post team re-types it into a spreadsheet and tracks ~150 items (estimate) by hand.
**Tags:** #large-language-models #transformers #feature-engineering #evaluation-metrics #compliance #workflow-orchestration #data-integration
**Contested on:** Every serious competitor in this niche is fighting to close every item on a distributor's delivery schedule (cue sheet, licences, credits, chain of title, E&O certificate) before the payment holdback date, and whoever closes schedules with no item sent back takes the producer's next show.

## The Problem
A feature sold to three territories and a streamer carries four delivery schedules, each with its own numbering, wording and technical appendix. "Dialogue, continuity and spotting list", "as-broadcast script" and "combined continuity" can mean the same item or not. The deliverables team builds a master tracker by hand and chases items by email. Returned items are found when the distributor's delivery department writes back, weeks later. This is the delivering side of the schedule; the distributor's own servicing of its licensees is covered under [[industries/film-distributors|Film Distributors]].

## Why Nobody Has Built This
Each production's schedule set is unique and the documents come from a dozen parties (production legal, music supervisor, composer, insurer, sales agent). Post houses own only part of the list, and nobody owns the whole.

## What to Build
A schedule parser that reads each distributor's PDF into canonical items mapped to a shared taxonomy. Each item is linked to the file or document that satisfies it, with automated checks where possible: the cue sheet matches the final cut, the E&O certificate names the right entity and term, captions match the final runtime. Status rolls up per schedule, with owners and chase emails drafted for open items.

## Target Customer
Heads of deliverables at post facilities; independent producers and sales agents delivering to multiple territories.

## Impact If Built
Schedules close days or weeks sooner, the payment holdback releases faster, and each returned item gets traced to the step that produced it.
