# A Channel With No Memory

**Niche:** [[niches/internal-developer-platforms/platform-engineer-support/profile|The Platform Engineer]]
**Industry:** [[industries/internal-developer-platforms|Internal Developer Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The same question is answered in the platform channel for the fortieth time, and the thirty-nine previous answers are in the same channel and are unfindable.
**Tags:** #bert #word-embeddings #k-means-clustering #descriptive-statistics #evaluation-metrics #confidence-intervals #quick-win #worker-facing
**Contested on:** Every serious competitor that takes this seriously is fighting to stop a platform team being the help desk for its own abstractions — and whoever does that takes the platform function, because that support load is what prevents the platform improving.

## The Problem
A developer asks how to grant a service access to a shared resource. The answer has been given thirty-nine times in that channel over two years, in slightly different words, in threads that are technically searchable and practically not — because the question is phrased differently each time, the answers are scattered across threads with other content, and chat search matches words rather than meaning. The engineer answering does not know it has been asked before either. The knowledge exists, is in one place, and is inaccessible.

## Why It's Still Broken
Chat is designed for conversation rather than for retrieval, and its search is lexical. Nobody owns converting answers into documentation, and the individual answer never feels worth documenting because it takes thirty seconds to give. The documentation that exists was written in advance by people guessing at what would be needed rather than derived from what has been asked. And the repetition is invisible because nobody counts.

## What a Fix Looks Like
Give the channel a memory. Index the channel history semantically, so a new question retrieves the prior answers regardless of phrasing, which is straightforward and immediately makes two years of accumulated answers accessible. Surface the prior answer to the asker before anybody responds, in the channel, which deflects the repeat without requiring anybody to change how they ask. Surface it to the answerer too, since an engineer who knows this is the fortieth time will answer differently — by fixing the documentation or the abstraction rather than the instance. Generate documentation from the recurring answers, which is the corpus the documentation should have been derived from and is sitting there. Detect and report repetition, since the count is the argument for fixing the underlying confusion and nobody has it. Mark authoritative answers, because a channel contains corrections and superseded advice and retrieving the wrong one is worse than nothing. And keep it current, since platform answers go stale and a confidently retrieved stale answer is the failure mode to avoid.

## Who Feels the Pain
Engineers answering the same question repeatedly; developers searching a channel that cannot find what is in it; and platform teams whose accumulated knowledge is inaccessible in the place it was created.

## Impact If Fixed
Semantic indexing over the channel history makes two years of answers retrievable and is an afternoon's work. Showing the answerer that this is the fortieth time is the change that converts an answer into a fix.
