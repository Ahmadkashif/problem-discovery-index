# Entity Resolution and Graph Inference

**Niche:** [[niches/crypto-exchanges/address-attribution/profile|Address Attribution & Taint Propagation]]
**Industry:** [[industries/crypto-exchanges|Crypto Exchanges]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Entity resolution is a mature discipline with probabilistic matching and expressed uncertainty, and blockchain attribution reinvented it as categorical labels.
**Tags:** #graph-theory #bayesian-inference #confidence-intervals #graph-neural-networks #evaluation-metrics #k-means-clustering #data-integration #gradient-boosting
**Contested on:** Every serious competitor in this niche is fighting to say who actually controls an address and how far illicit taint legitimately travels through a public ledger — and whoever attributes most accurately, with a confidence they can defend, owns the input every downstream decision consumes.

## The Problem
Deciding that two records refer to the same real-world entity is a well-developed field: probabilistic record linkage, blocking strategies, clustering with transitivity constraints, match scores with thresholds chosen against measured error rates, and active learning to acquire labels where they matter most. Blockchain attribution is exactly this problem on a graph, and it is practised as a proprietary label feed with no match score, no error rate and no documented method.

## What Already Exists
Probabilistic record linkage and entity resolution frameworks; graph-based clustering with constraints; match scoring with threshold selection against measured precision; active learning for label acquisition; and provenance tracking on derived entities.

## The Customization Gap
The adaptation is to an adversarial graph with a strong identity junction at one point. It requires: (1) an adversary actively defeating the linkage, which record linkage literature does not contemplate and which makes heuristic decay a first-class concern — this is the substantive adaptation; (2) one high-quality identity anchor at the exchange rather than attributes on both sides, inverting the usual matching structure; (3) transitive risk propagation after resolution, since knowing the entity is only half the question; (4) chain-specific structure, where UTXO and account models support different inferences from the same technique; and (5) consequences at the individual level, since a false match freezes a person's money rather than merging two customer records.

## Target Customer
Exchange data and compliance teams, analytics vendors whose method is undocumented, and entity resolution vendors for whom adversarial graph linkage is an unentered adjacency.

## Impact If Solved
Entity resolution has fifty years of method for expressing match confidence and measuring error. Attribution discarded all of it for a categorical feed, and reintroducing match scores is what lets the downstream threshold be set on evidence.
