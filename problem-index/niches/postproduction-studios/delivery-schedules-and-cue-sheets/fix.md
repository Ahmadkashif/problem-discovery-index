# The Cue Sheet Rebuilt After Every Re-Cut

**Niche:** [[niches/postproduction-studios/delivery-schedules-and-cue-sheets/profile|Delivery Schedules, Cue Sheets & Paper Deliverables]]
**Industry:** [[industries/postproduction-studios|Postproduction Studios]]
**Type:** Fix (Pain Point)
**One-liner:** A music cue sheet is built from the final cut, and every version (broadcast, streaming, international, airline) needs its own, rebuilt by hand.
**Tags:** #cnns #feature-engineering #large-language-models #evaluation-metrics #compliance #quick-win
**Contested on:** Every serious competitor in this niche is fighting to close every item on a distributor's delivery schedule (cue sheet, licences, credits, chain of title, E&O certificate) before the payment holdback date, and whoever closes schedules with no item sent back takes the producer's next show.

## The Problem
The music editor or coordinator lists every cue with timecodes, duration, usage type, writers, publishers and PRO affiliations. A broadcast cut with act breaks, a streaming cut, an edited-for-airline version and a territory version with a replaced song each change the timings. The cue sheet is rebuilt for each, from the session or by scrubbing.

## Why It's Still Broken
The cue sheet is treated as a document produced once at the end, not data derived from the timeline. Fingerprinting services identify commercial tracks but not edited score fragments, and the version-to-version differences are reconciled by eye.

## What a Fix Looks Like
Derive the cue sheet from the locked AAF or EDL and music stems for the master version. For each derived version, diff the timeline against the master and update only the changed cues, flagging any usage that falls outside the licence for that version's media.

## Who Feels the Pain
Music editors and post coordinators; composers whose royalties depend on accurate cue sheets; deliverables teams waiting on the last item.

## Impact If Fixed
Each additional version's cue sheet becomes a review of a generated diff, and errors that delay composers' performance royalties stop recurring.
