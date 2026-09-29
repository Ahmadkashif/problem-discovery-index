# Recall Against Brute Force Measures the Index

**Niche:** [[niches/vector-search-vendors/retrieval-quality-measurement/profile|Retrieval Quality Measurement]]
**Industry:** [[industries/vector-search-vendors|Vector Search Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The category reports recall against brute-force search, which measures the index and says nothing about whether the retrieved documents answer the question — and nobody measures that on the real query distribution.
**Tags:** #evaluation-metrics #k-nearest-neighbors #large-language-models #hypothesis-testing #confidence-intervals #norms-and-inner-products #descriptive-statistics #cross-validation
**Contested on:** Every serious competitor in this niche is fighting to tell a customer whether the documents they retrieved would actually answer the question asked — and whoever does that takes the account, because it is the only question the buyer has and the category answers a different one.

## The Problem
A support assistant retrieves five documents per question and generates an answer. Users report it is wrong about a third of the time. The dashboard shows 98 percent recall and a 12 millisecond p99, both excellent. Those numbers say the index returned the same documents brute-force search would have. They do not say whether those documents contain the answer, and in this case they frequently do not — because the chunking split procedures across boundaries, and because the users phrase questions in operational language while the documents are written in product language. The vendor's instruments are all green and the product does not work.

## Why Nobody Has Built This
Measuring whether a document answers a question requires an opinion about relevance, which requires opinions about embeddings and chunking that the vendors have deliberately avoided having — neutrality on those choices is a positioning decision, and it precludes the measurement. Relevance labels are expensive, and the category's engineering culture is distributed systems rather than information retrieval. And the current metrics are genuinely good ones for the thing they measure, which makes the substitution easy to overlook.

## What to Build
Measure retrieval on the customer's own queries. Sample production queries and grade the returned sets for whether they contain the answer, using a model grader calibrated against human labels on a few hundred items, which makes continuous relevance measurement affordable for the first time and is the core of this build. Attribute failures to a stage rather than reporting an aggregate: embedding representation, chunking, index approximation, query formulation, or corpus absence — since each has a different fix and the undifferentiated number tells an engineer nothing. Report the index's contribution honestly, because approximation loss is frequently the smallest term and saying so is more credible than implying otherwise. Use the downstream signal where the application is instrumented — whether the generated answer was accepted, retried, escalated or edited — which is a free relevance label most deployments already produce and discard. Compare against a brute-force and a lexical baseline on the same queries, so the customer sees what the approximation and the embedding are each costing them. Segment quality by query type, since aggregate quality conceals that one class of question fails consistently and that class is usually nameable. Report quality continuously rather than at onboarding, because corpora and query distributions both move. And be opinionated about chunking and embedding where the evidence supports it, since the neutrality that blocks this measurement is a choice rather than a constraint.

## Target Customer
Application teams building on retrieval, the platform teams buying vector infrastructure for them, and the vendors who currently compete on cost per vector.

## Impact If Built
The category's instruments are all green while the product fails, because they measure the index rather than the retrieval. Attributing failures to embedding, chunking, index or corpus is what turns a quality number into an action, and the downstream acceptance signal is a free relevance label most applications already discard.
