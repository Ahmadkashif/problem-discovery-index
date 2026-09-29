# Every Query Seen, Nothing Concluded

**Niche:** [[niches/vector-search-vendors/query-corpus-intelligence/profile|Query & Corpus Intelligence]]
**Industry:** [[industries/vector-search-vendors|Vector Search Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** These vendors sit at the exact point where retrieval quality is determined and have defined their product boundary just short of it, so they see everything and conclude nothing.
**Tags:** #gradient-boosting #bayesian-optimization #transfer-learning #evaluation-metrics #k-means-clustering #hypothesis-testing #confidence-intervals #dimensionality-reduction
**Contested on:** Every serious competitor in this niche is fighting to turn what they see across every deployment — queries, returned sets, corpora, outcomes — into empirical answers about chunking, embedding and configuration, and whoever does that stops competing on cost per vector.

## The Problem
A new customer indexes a corpus of technical manuals and asks what chunk size to use, which embedding model suits their vocabulary, and how to weight hybrid search. The vendor has thousands of deployments including dozens with technical manuals, complete records of their configurations, their query distributions and — for the instrumented ones — how well retrieval performed. The answer is computable. The customer is pointed at a documentation example and a blog post, spends a month experimenting, and arrives somewhere the corpus could have put them on day one.

## Why Nobody Has Built This
Crossing the boundary means having opinions about embedding and chunking, which the category avoided deliberately to stay neutral and appealing to every model provider. Cross-customer analysis is contractually awkward and nobody has asked the narrow version of the question. The engineering organisations are distributed systems teams whose instinct is index performance. And the findings would show that configuration matters more than the index choice that customers are buying on, which complicates the sales story.

## What to Build
Cross the boundary. Start with chunking, because it is the most common cause of retrieval failure, the corpus supports an empirical answer by document type, and no credible guidance exists anywhere — publishing it would be immediately valuable and immediately cited. Build a corpus-profile to configuration recommender, characterising a new corpus by computable properties — document length distribution, vocabulary overlap with general text, structural regularity, query length and type mix — and returning a configuration derived from similar deployments, so a customer starts near a good answer rather than at a template. Benchmark embedding models on domain-specific corpora rather than general benchmarks, since the published leaderboards are on general text and a customer with specialised vocabulary is choosing on evidence that does not apply to them. Feed the aggregate back into each deployment as a recommendation with its evidence, at the moment a configuration decision is being made. Establish an aggregation basis that is narrow and inspectable, since the contractual objection is to open-ended use and is solvable by asking specifically. Offer each customer their own analysis first, which needs no permission and demonstrates the value. And publish the findings, because a category that supplies the field's empirical answers about retrieval is no longer selling cost per vector.

## Target Customer
Vector search vendors, their customers as beneficiaries, and the retrieval community that has no empirical account of practice at this scale.

## Impact If Built
The vendors see everything that determines retrieval quality and have drawn their boundary just short of it. Empirical chunking guidance by document type would be cited immediately and exists nowhere, and a corpus-profile recommender puts a customer on day one where a month of experimentation lands them.
