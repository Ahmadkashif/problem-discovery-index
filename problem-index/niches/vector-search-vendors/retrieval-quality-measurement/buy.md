# Information Retrieval Evaluation Methodology

**Niche:** [[niches/vector-search-vendors/retrieval-quality-measurement/profile|Retrieval Quality Measurement]]
**Industry:** [[industries/vector-search-vendors|Vector Search Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Information retrieval spent fifty years building relevance judgement methodology, pooled assessment and graded metrics, and the vector database category reimported none of it.
**Tags:** #evaluation-metrics #hypothesis-testing #confidence-intervals #descriptive-statistics #k-nearest-neighbors #probability-distributions #cross-validation #monte-carlo-methods
**Contested on:** Every serious competitor in this niche is fighting to tell a customer whether the documents they retrieved would actually answer the question asked — and whoever does that takes the account, because it is the only question the buyer has and the category answers a different one.

## The Problem
Measuring whether a retrieval system returns the right documents is the founding problem of information retrieval, and the field built an entire apparatus for it: graded relevance judgements, pooled assessment to make judging feasible on large corpora, rank-aware metrics, significance testing on query sets, and decades of published evaluation campaigns. The vector database category emerged from distributed systems, adopted recall against brute force, and left all of it behind.

## What Already Exists
Graded relevance judgement methodology with assessor guidelines and agreement measurement; pooled assessment for building judgements on large corpora affordably; rank-aware evaluation metrics including discounted cumulative gain and rank-biased precision; query set design with significance testing; evaluation campaign infrastructure; and click and implicit feedback models for inferring relevance from behaviour.

## The Customization Gap
The adaptation is to a live production system whose consumer is a language model. It requires: (1) relevance defined as supporting the generation rather than as topical aboutness, since a document can be on-topic and useless to the model and the classical definition does not capture that — this is the key conceptual adaptation; (2) pooled assessment with a model assessor calibrated against humans, which makes the classical method affordable continuously rather than once per campaign; (3) set-level rather than purely rank-level metrics, because the consumer reads the top few documents together and complementarity between them matters in a way rank metrics do not model; (4) implicit feedback models adapted to generation acceptance signals rather than clicks, where the click model literature transfers directly and nobody has applied it; and (5) evaluation on the customer's live query distribution rather than a fixed benchmark set, which is where this departs most from the campaign tradition and where the value is.

## Target Customer
Vector search vendors, application teams, and the information retrieval research community whose methodology has a large unserved commercial application here.

## Impact If Solved
Fifty years of relevance evaluation exists one field over and was left behind. Redefining relevance as supporting the generation, and adapting click models to acceptance signals, are the two transfers that would matter most.
