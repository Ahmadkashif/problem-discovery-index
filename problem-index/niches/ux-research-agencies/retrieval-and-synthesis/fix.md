# Four Hundred Results and No Answer

**Niche:** [[niches/ux-research-agencies/retrieval-and-synthesis/profile|Retrieval & Synthesis]]
**Industry:** [[industries/ux-research-agencies|UX Research Agencies]]
**Type:** Fix (Pain Point)
**One-liner:** The search matched the word in four hundred transcripts and the person asking needed one sentence.
**Tags:** #quick-win #word-embeddings #evaluation-metrics #descriptive-statistics #data-integration #automation #workflow-orchestration #confidence-intervals
**Contested on:** Every serious competitor in this niche is fighting to get a usable answer out of years of transcripts and tagged findings when the question is a design question rather than a keyword — and whoever answers it takes the account.

## The Problem
Repository search returns transcripts. A person with a specific question gets hundreds of matches on a common word, or no matches because the previous researcher used a different term, and in both cases abandons the search. The repository is judged useless, when what failed was a keyword match against conversational speech — a task keyword matching has never been good at.

## Why It's Still Broken
The index is over raw transcripts — matching a word in conversational speech returns everything and nothing, because people say ordinary words constantly and name the same concept differently. Findings are not indexed separately from transcripts. Nobody measures failed searches. And the conclusion drawn is that repositories do not work.

## What a Fix Looks Like
Index the findings rather than the transcripts, and mine the failures. Index findings and summaries as a separate layer above the raw material, which is the fix and changes what search returns immediately. Write a one-line answerable claim per finding, since that is the unit people are searching for. Log failed and abandoned searches, which names the vocabulary gaps rather than leaving them to guesswork. Build a synonym map from those logs plus the corpus's own language. Return the study rather than the transcript, with a summary a person can scan. Rank by recency and sample size rather than by match count, which orders results the way the question needs. Show what the study covered so relevance can be judged in a glance. Add a one-line study summary retrospectively for the last two years, which is a day's work and disproportionately useful. Measure whether searches lead to an answer, which nobody currently tracks. And tell people when nothing relevant exists rather than returning weak matches.

## Who Feels the Pain
Researchers who searched and gave up; product teams commissioning studies unnecessarily; research operations defending a repository nobody uses; and the years of material sitting unread.

## Impact If Fixed
Matching a word in conversational speech returns everything and nothing, because people say ordinary words constantly and name the same concept differently. Indexing findings rather than transcripts changes what comes back.
