# The Join the Industry Loses Money On

**Niche:** [[niches/music-distribution-platforms/rights-matching-and-metadata/profile|Rights Matching & Metadata]]
**Industry:** [[industries/music-distribution-platforms|Music Distribution Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Hundreds of millions of dollars fail to reach their owners because two rights systems do not share a key, and the data that would join them sits with the distributors.
**Tags:** #graph-theory #word-embeddings #evaluation-metrics #confidence-intervals #data-integration #compliance #bert #k-nearest-neighbors
**Contested on:** Every serious competitor in this niche is fighting to make the money from a stream reach the people who own the recording and wrote the song — and the contest splits cleanly enough that it is not terminal.

## The Problem
The recording side and the composition side are administered separately, with different identifiers, by different organisations. The link between them is metadata: who wrote this, what are the splits, which publishers administer them. It is supplied at upload by an artist who may not know what a publisher is. When it is absent or wrong, the composition royalty has no payee, the money accumulates in an unmatched pool, and its eventual distribution by market share sends it to parties who had nothing to do with the songs.

## Why Nobody Has Built This
No participant is paid for money that reaches someone else, which is the structural reason — an industry-level matching failure has no owner because fixing it benefits parties other than the fixer. Distributors hold the corpora and use them to validate their own uploads. The identifier systems predate streaming and were not designed to join. And the unmatched pool's eventual distribution benefits the largest participants, who are therefore not urgent about it.

## What to Build
Match across the corpora and fix the capture. Match recordings to compositions using the distributor's own corpus of recordings with known writers and splits, which is one half and is the largest training set for this problem in existence. Capture the rights data correctly at upload from artists who do not know the terminology, which is the other half and prevents the problem rather than repairing it. Use audio fingerprinting alongside metadata, since the same composition recorded twice is identifiable acoustically and by lyric even when the text fields disagree. Trace unmatched money back to its cause, because attributing the failure to a missing field, a misspelt writer or an unregistered work is what makes it fixable. Express match confidence, as a wrong match sends money to the wrong person and is worse than no match. Feed the matches back to the registries rather than keeping them, which is the industry-level fix and is where the collective benefit sits. Build the commercial model deliberately, since the obstacle is that nobody is paid for this and a claiming or success-fee structure changes that. Report the distributor's own unmatched rate, which is a number that does not currently exist and would be competitive information. Handle the contested case, because two parties claiming the same composition is common and needs adjudication rather than a match. And measure money recovered, which is the only metric that matters here.

## Target Customer
Data and rights leadership, artists and writers whose money does not arrive, collecting and licensing organisations, and music data vendors.

## Impact If Built
An industry-level matching failure has no owner because fixing it benefits parties other than the fixer. Distributors hold the largest corpus of recordings matched to compositions in existence and use it to validate their own uploads.
