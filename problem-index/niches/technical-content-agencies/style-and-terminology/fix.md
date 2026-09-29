# Three Names for the Same Thing

**Niche:** [[niches/technical-content-agencies/style-and-terminology/profile|Style & Terminology Consistency]]
**Industry:** [[industries/technical-content-agencies|Technical Content Agencies]]
**Type:** Fix (Pain Point)
**One-liner:** The product renamed a feature and the old name is still used in a third of the corpus.
**Tags:** #quick-win #automation #data-integration #evaluation-metrics #descriptive-statistics #compliance #word-embeddings #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to keep one term meaning one thing across a corpus written by many people over many years, and whoever enforces that mechanically takes the account.

## The Problem
A product renames something. The announcement goes out, new content uses the new name, and the existing corpus keeps the old one. Readers encounter both, cannot tell whether they are the same thing, and searches for one miss content about the other. The rename was a decision somebody made in an afternoon and its propagation through the documentation is a task nobody scheduled.

## Why It's Still Broken
Renames are announced rather than propagated — a decision to change a name is communicated as news and never executed as a change across the corpus, so the corpus holds both names indefinitely. Nobody owns the propagation. A find-and-replace is risky without review. And the old name still appears in the product's own history.

## What a Fix Looks Like
Treat a rename as a corpus change with an owner. Run a corpus-wide replacement for every rename, reviewed rather than applied blindly, which is the fix and is a morning's work per rename. Keep a terminology change log so renames are tracked rather than remembered. Add the old name as a search alias so readers using it still find the content, which is necessary regardless of the replacement. Handle references to historical versions deliberately, since those legitimately keep the old name and a blanket replacement breaks them. Check the corpus for the old term periodically rather than assuming the replacement was complete. Enforce the new term at authoring so it cannot reappear. Coordinate with the product's own release communication, so the rename and the propagation happen together. Cover the reference material, which is generated and may have its own naming. Tell support, who field the resulting confusion first. And make propagation part of the rename decision rather than a consequence of it.

## Who Feels the Pain
Readers who cannot tell whether two names mean one thing; search, which splits the content; support teams answering the confusion; and writers who inherit a corpus with several vocabularies in it.

## Impact If Fixed
A decision to change a name is communicated as news and never executed as a change across the corpus, so both names persist indefinitely. A reviewed corpus-wide replacement is a morning per rename.
