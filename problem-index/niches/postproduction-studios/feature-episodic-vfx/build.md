# Shot Identity That Survives the Re-Cut

**Niche:** [[niches/postproduction-studios/feature-episodic-vfx/profile|Feature & Episodic VFX]]
**Industry:** [[industries/postproduction-studios|Postproduction Studios]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A VFX shot changes name, length and sometimes number every time editorial re-cuts, so the bid line, the versions, the notes and the invoice stop pointing at the same thing.
**Tags:** #feature-engineering #graph-theory #large-language-models #evaluation-metrics #data-integration #revenue-impact
**Contested on:** *Not terminal as stated.* The honest partial sentence is "every serious competitor is fighting to price shot packages on fixed bids accurately enough to win the award and still make money," but the winners differ: tentpole feature packages are won by whoever can commit hundreds of artists under a trusted supervisor in the richest incentive jurisdiction, while episodic and invisible-effects work is won by whoever turns around high shot counts at a known cost per shot inside a weekly schedule. Decomposed into contested sub-niches below.

## The Problem
A shot is bid as line 214 of a breakdown, turned over as ABC_0420, split into two shots after a re-cut, extended by 30 frames in the next turnover, and invoiced as two lines that match neither the bid nor the tracker. Multiply that by 1,000 shots and five turnovers and the vendor loses the thread: it cannot say which shots grew, which were omitted after work began, or which bid lines turned into which delivered shots. The bid-accuracy question every vendor needs answered is unanswerable because the join key is broken.

## Why Nobody Has Built This
Production trackers treat the shot as a record that editorial renames; editorial tools treat clips as timeline events; bid templates are spreadsheets. Each assumes the others will keep IDs stable, and none of them does. The lineage is reconstructed by coordinators in email when an invoice is disputed.

## What to Build
A shot lineage graph that ingests every turnover (EDL, AAF, pull lists), every bid version and every tracker export, and links them by source clip, timecode overlap and frame range. Splits, merges, extensions and omits become explicit edges with dates. Every delivered shot then has a path back to the bid line and every bid line has a path forward to what it became, with frames added and work done before omission attached.

## Target Customer
VFX executive producers and heads of production at vendors with 100 or more artists working on episodic and feature packages.

## Impact If Built
Change orders backed by lineage evidence, recovered omit-after-start work, and for the first time a clean bid-versus-actual dataset. On a 1,000-shot show, recovering even 3–5% of the package value in uncaptured scope changes would pay for the system many times over (estimate).
