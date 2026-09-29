# The Answer Was Never in the Corpus

**Niche:** [[niches/vector-search-vendors/retrieval-quality-measurement/profile|Retrieval Quality Measurement]]
**Industry:** [[industries/vector-search-vendors|Vector Search Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** A large share of retrieval failures are not retrieval failures — the corpus simply does not contain the answer — and nothing distinguishes that case, so teams spend months tuning a pipeline that was working.
**Tags:** #evaluation-metrics #descriptive-statistics #k-means-clustering #dbscan #hypothesis-testing #large-language-models #quick-win #automation
**Contested on:** Every serious competitor in this niche is fighting to tell a customer whether the documents they retrieved would actually answer the question asked — and whoever does that takes the account, because it is the only question the buyer has and the category answers a different one.

## The Problem
Users ask the assistant about a policy that was never documented, a product edge case covered only in a support agent's head, or a procedure written down in a system that was never indexed. The retriever returns the five closest documents, because it always returns five, and the model generates a confident answer from irrelevant material. The team sees a wrong answer, assumes retrieval failed, and spends a quarter adjusting chunk sizes and embedding models. The pipeline was working correctly the whole time and the corpus has a hole, which nobody has ever looked for.

## Why It's Still Broken
The retriever always returns its top results regardless of how poor they are, so there is no signal distinguishing a good match from the best of a bad set. Similarity scores are not comparable across queries, which makes a naive threshold useless and has discouraged the whole approach. Corpus coverage is nobody's job — it sits between the content owners and the engineering team. And the diagnosis is unwelcome, because it implies a content problem rather than a tuning problem.

## What a Fix Looks Like
Detect the hole and say so. Calibrate a confidence signal from the retrieval scores so that a query with nothing genuinely relevant is identified, using score distribution shape and the gap between top results rather than an absolute threshold — this is the technical core and it is what makes abstention possible. Let the application abstain, because saying the documentation does not cover this is a better product behaviour than confidently answering from irrelevant material, and the retrieval layer is where the evidence for it exists. Cluster the unanswerable queries and report them as a content gap report, which is the single most valuable artefact this build produces — it tells the content owners exactly what to write next, ranked by demand, and no team currently has that. Distinguish an absent answer from a present but unfindable one by checking with a lexical search and a wider sweep, since the fixes are completely different. Track the share of queries the corpus cannot answer as a standing metric, since it is usually much larger than anyone expects and it reframes the entire improvement effort. Route unanswerable queries to a human channel where one exists. And feed answered escalations back into the corpus, which closes the loop and is how the hole gets filled rather than merely measured.

## Who Feels the Pain
Engineering teams tuning a working pipeline for months; users receiving confident answers assembled from irrelevant documents; and the content owners who would happily write the missing material if anyone told them what it was.

## Impact If Fixed
A large share of apparent retrieval failures are content gaps, and nothing distinguishes them. Clustering unanswerable queries into a demand-ranked content gap report is the highest-value artefact available here and no team currently has one.
