# Unidentified Usage Resolved Before It Becomes Non-Distributable

**Niche:** [[niches/music-publishers/collecting-societies-distribution/profile|Performing Rights Organisations & Collecting Societies]]
**Industry:** [[industries/music-publishers|Music Publishers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Societies work unidentified usage lines largely in arrival order, although a small share of lines holds most of the money and the oldest are about to be lost to members.
**Tags:** #k-nearest-neighbors #gradient-boosting #large-language-models #evaluation-metrics #compliance #data-integration #revenue-impact
**Contested on:** Every serious competitor in this pocket is fighting to identify every use of every work and pay the right share to the right member inside the distribution window, before unidentified money becomes non-distributable, and whoever does that most accurately and fastest keeps the writers and publishers whose repertoire makes its licence worth buying.

## The Problem
Every distribution leaves usage the society could not match to a registered work or a complete set of shares. Examples are a broadcast cue with no identifier, a streamed track whose composition was never registered, or a local title variant. The money is held while staff and members try to resolve it. In the EU, what is still unidentified three years after the collection year becomes non-distributable. The lines vary enormously in value, yet they are worked through as queues and monthly claim lists.

## Why Nobody Has Built This
Matching engines were built to process the easy majority at volume. The hard residue needs evidence from many places: audio, member claim histories, other societies' registrations, publishers' catalogues. The society's archive of past manual resolutions, the best training data it has, sits in case notes rather than in a model.

## What to Build
A resolution system trained on the society's own history of resolved lines. It ranks unidentified usage by value and by how close each line is to the non-distributable date. For each line it proposes candidate works and share holders using metadata, audio fingerprints, lyrics, member claim patterns and other societies' data received under reciprocal agreements, with calibrated confidence. High-confidence matches go out to members to confirm, and the rest are routed to analysts with the evidence attached.

## Target Customer
Chief distribution officers at mid-size and large societies in Europe and elsewhere, and data leaders at the US societies.

## Impact If Built
More money reaches identified members inside the statutory window. That improves the distribution accuracy members choose societies on, and leaves less to be shared out by proxy.
