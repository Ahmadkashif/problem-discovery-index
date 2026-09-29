# Retrieval Quality Is Unmeasured in Production

**Industry:** [[vector-search-vendors|Vector Search Vendors]]
**Type:** High Impact
**One-liner:** The category reports recall against brute-force search, which measures the index and says nothing about whether the retrieved documents answer the question — and nobody measures that on the real query distribution.
**Tags:** #evaluation-metrics #hypothesis-testing #confidence-intervals #contrastive-learning #word-embeddings #bert #large-language-models #transformers #revenue-impact

## The Problem
Vector databases report recall as the fraction of true nearest neighbours the approximate index returns. It is a real number and it measures the index against its own brute-force baseline. It has almost nothing to do with whether the application works.

An application retrieving the ten closest vectors to a query embedding may be retrieving ten documents that are semantically adjacent and none that contain the answer. The index performed perfectly. The retrieval failed. The distinction is invisible to every metric the category reports.

Real retrieval quality is determined by things sitting on either side of the database. The embedding model and how it represents the domain. The chunking strategy — chunks too small lose context, too large dilute the signal, and boundaries placed badly split the answer across two chunks that each look irrelevant. The query itself, which in production is a user's real question rather than a well-formed search string. And the corpus, including whether the answer is in it at all.

Application teams discover failures anecdotally. Someone notices the assistant gave a wrong answer, traces it, and finds the right document was ranked twelfth. They adjust chunk size, or the number of results, or add a reranker, and check whether the anecdote improved. There is no measurement, so there is no way to know whether the change helped generally or fixed one case and broke others.

## Why It's Unsolved
Ground truth is genuinely expensive. Measuring retrieval quality means knowing, for a set of real queries, which documents in the corpus should have been returned — and that requires human judgement over a corpus that may contain millions of documents.

The vendors have also drawn their product boundary deliberately short of it. Owning retrieval quality means having opinions about embedding models and chunking strategies, which means competing with customers' own choices and with the embedding providers. Staying at the infrastructure layer is commercially safer and is why the category competes on cost per vector.

The embedding dependency is a real constraint. The vendor does not control the model that produces the vectors, that model is updated by a third party, and a change to it silently changes retrieval behaviour across the entire corpus without any signal in the database's own metrics.

And the failure mode is quiet. A retrieval-augmented application with mediocre retrieval still produces fluent answers, so there is no error, no exception, no obvious symptom — just answers that are worse than they should be.

## What a Solution Looks Like
Quality measurement on the production query distribution, built from labels the application already generates. Downstream signals — whether the user rephrased, whether they clicked through to a source, whether a generated answer cited the retrieved chunk, whether a support conversation escalated — are weak individually and usable in aggregate, and they are free.

A small human-labelled evaluation set drawn from real queries, refreshed periodically, as the anchor. This is the expensive part and it is bounded: a few hundred queries with judged relevance is enough to detect regression and to compare configurations.

Configuration comparison as a product feature. Chunk size, overlap, retrieval depth, hybrid weighting and reranking are a small parameter space, and evaluating them against a fixed query set is exactly what the vendor is positioned to automate and the customer is not.

Embedding drift detection. When the embedding provider updates a model, the vendor can detect the distributional shift immediately and warn — which is a failure mode customers currently discover through degraded answers weeks later.

Query-level failure attribution: was the answer absent from the corpus, present but chunked badly, present but ranked below the cut, or retrieved and ignored by the generation step. Each has a different fix and they are currently indistinguishable.

## Impact If Solved
Retrieval quality determines whether a retrieval-augmented application works, and it is currently tuned by anecdote in a category that measures index performance instead. Owning the quality question moves these vendors from commoditising infrastructure to the layer where the customer's actual outcome is decided.
