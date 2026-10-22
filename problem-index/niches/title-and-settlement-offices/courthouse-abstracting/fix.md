# The Misindexed Instrument

**Niche:** [[niches/title-and-settlement-offices/courthouse-abstracting/profile|Courthouse Abstracting in Non-Plant Counties]]
**Industry:** [[industries/title-and-settlement-offices|Title & Settlement Offices]]
**Type:** Fix (Pain Point)
**One-liner:** A judgment or mortgage indexed under a misspelled name is invisible to a name search, and is found only when it becomes a claim.
**Tags:** #k-nearest-neighbors #large-language-models #evaluation-metrics #compliance #quick-win
**Contested on:** Every serious competitor in this niche is fighting to return a complete, correctly indexed search from a county with no title plant and no reliable online index inside the agent's turn time, and whoever knows each courthouse's indexing quirks and gaps takes that county's orders.

## The Problem
Grantor-grantee indexes depend on clerks typing names correctly. "McDonald" filed as "MacDonald", a married name instead of a maiden name, or a transposed initial hides the instrument from an exact search. Experienced searchers run variants by habit; newer ones do not.

## Why It's Still Broken
County index software does exact or prefix matching, and abstractors' variant lists live in their heads.

## What a Fix Looks Like
Fuzzy and phonetic name matching across index entries, nickname and maiden-name variants drawn from the chain itself, and a search log showing which variants were run, attached to every delivered search.

## Who Feels the Pain
Abstractors whose searches miss instruments; examiners relying on incomplete searches; underwriters paying the claims.

## Impact If Fixed
Variant searching becomes standard and documented rather than dependent on the searcher's memory.
