# Hybrid Search Weighting

**Industry:** [[vector-search-vendors|Vector Search Vendors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every vendor supports combining lexical and dense retrieval because it reliably beats either alone, and the weighting between them is set to whatever the documentation example used.
**Tags:** #optimization-fundamentals #logistic-regression #bayesian-optimization #evaluation-metrics #hypothesis-testing #confidence-intervals #feature-engineering

## The Problem
Dense vector search finds semantically related content and misses exact matches — a product code, an error string, a surname, a rare technical term that the embedding model has effectively never seen. Lexical search finds those precisely and misses paraphrase. Combining them outperforms either, consistently, across essentially every published comparison.

Every vector database now supports hybrid search. The combination requires a weighting: how much to trust the dense score against the lexical score, or what parameters to use in a reciprocal rank fusion.

Almost nobody tunes it. The value in production is the one from the quickstart, because tuning requires an evaluation set the team does not have, and because the effect of the parameter is invisible without one.

Worse, the correct weighting is not a constant. A query that is an exact identifier should weight lexical heavily; a query that is a conceptual question should weight dense. A single global parameter is a compromise applied to a query distribution containing both.

## What Already Exists
Hybrid search is supported natively by Weaviate, Qdrant, Elasticsearch, OpenSearch, Vespa and most managed vector services. Reciprocal rank fusion is a standard, robust and parameter-light combination method. BM25 implementations are mature. Reranking models from Cohere, Voyage and open alternatives provide a strong second stage that partially compensates for a badly weighted first stage. The information retrieval literature on fusion is extensive and decades old.

## The Customisation Gap
The parameter exists and nothing helps set it. Tuning requires labelled queries, the customer has none, and the vendor has not offered a way to generate them — even though generating a plausible evaluation set from the corpus itself, by producing questions that a given chunk answers, is now straightforward and would make tuning possible for every customer.

Query-adaptive weighting is the larger unexploited gap. Classifying a query as identifier-like, keyword-like or conceptual is easy, and the appropriate weighting differs sharply between them. Fixed global weighting is leaving obvious performance on the table and no product does it.

Out-of-vocabulary detection is the specific case where dense retrieval fails hardest and predictably. A query containing tokens the embedding model handles poorly — rare identifiers, novel product names, code fragments — should route lexically, and this is detectable from the query before retrieval runs.

Reranking is treated as an always-on stage rather than a decision. It adds latency and cost, and whether it is worth it depends on how well the first stage did, which is estimable from score distributions in the candidate set.

## Impact If Solved
Hybrid weighting is a small parameter space with a large effect on results, left at its default value across most production deployments because tuning requires an evaluation set nobody built. Generating that set from the corpus and adapting the weighting per query are both tractable and would improve retrieval quality more than most architectural changes.
