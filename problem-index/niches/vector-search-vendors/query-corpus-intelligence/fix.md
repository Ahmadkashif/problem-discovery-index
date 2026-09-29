# Chunking Advice From a Blog Post

**Niche:** [[niches/vector-search-vendors/query-corpus-intelligence/profile|Query & Corpus Intelligence]]
**Industry:** [[industries/vector-search-vendors|Vector Search Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** Chunking is the most common cause of retrieval failure and the field's collective guidance is a handful of round numbers from blog posts, repeated until they became defaults.
**Tags:** #evaluation-metrics #descriptive-statistics #hypothesis-testing #confidence-intervals #k-means-clustering #large-language-models #quick-win #cross-validation
**Contested on:** Every serious competitor in this niche is fighting to turn what they see across every deployment — queries, returned sets, corpora, outcomes — into empirical answers about chunking, embedding and configuration, and whoever does that stops competing on cost per vector.

## The Problem
Every team building retrieval chooses a chunk size and an overlap. The numbers in circulation — a few hundred tokens, some overlap — trace back to early examples rather than to evidence, and they are wrong for many document types: a legal contract's meaning spans clauses, a technical manual's procedure spans steps, a chat transcript's context spans turns, and a reference table is destroyed by any fixed-size split. Teams discover this months in, after attributing the symptoms to the embedding model. The advice is not merely absent, it is confidently present and unfounded.

## Why It's Still Broken
Chunking sits outside every vendor's product boundary, so it belongs to nobody. Evaluating it properly requires measuring retrieval quality, which the category also does not do, so the two gaps sustain each other. The round numbers are easy to repeat and appear in every tutorial, which gives them the authority of ubiquity. And the failure presents as poor retrieval quality generally, which sends teams to the embedding model first.

## What a Fix Looks Like
Replace the folklore with evidence. Publish measured chunking guidance by document type, derived from deployments where quality is instrumented, which is the artefact the field lacks and which any vendor with a corpus could produce — it is the single highest-value publication available in this category. Recommend a strategy from the customer's own corpus characteristics — structural markers, length distribution, whether meaning spans natural boundaries — rather than from a default, since the document type is knowable automatically. Support structure-aware chunking natively, splitting on sections, clauses, steps and turns rather than on token counts, which is what most corpora need and what almost no pipeline does. Detect chunking failures directly: relevant content split across a boundary, chunks that are mostly boilerplate, chunks with no self-contained meaning — all identifiable from the corpus without any queries. Support multiple granularities with parent retrieval, so a precise small chunk can return its surrounding context, which resolves most of the trade-off and is underused. Report chunking's contribution to retrieval failures per deployment, which is what redirects teams away from blaming the embedding model. And stop shipping a round number as a default without saying what it is based on.

## Who Feels the Pain
Teams whose retrieval underperforms for a reason nothing points at; engineers evaluating embedding models to fix a chunking problem; and every newcomer inheriting numbers whose provenance is a tutorial.

## Impact If Fixed
Published chunking guidance by document type is the field's largest missing artefact and any vendor with an instrumented corpus could produce it. Structure-aware splitting and parent retrieval resolve most of the trade-off and are largely unused.
