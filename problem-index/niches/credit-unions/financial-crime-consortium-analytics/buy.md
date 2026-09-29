# Network Detection Adapted to Cross-Institution Typologies

**Niche:** [[niches/credit-unions/financial-crime-consortium-analytics/profile|Financial Crime Consortium Analytics]]
**Industry:** [[industries/credit-unions|Credit Unions]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Graph analytics platforms find dense subgraphs; a mule network is deliberately sparse, spread across twelve institutions, and structured specifically so that no single institution's graph looks unusual.
**Tags:** #graph-neural-networks #graph-theory #contrastive-learning #k-means-clustering #evaluation-metrics #feature-engineering #dbscan #compliance #data-integration #automation

## The Problem
The consortium's whole reason to exist is seeing what no member can see alone. A money mule network recruits across institutions precisely so that each institution observes a handful of ordinary-looking accounts, and elder fraud schemes replicate a pattern across a region rather than concentrating anywhere. Detecting these requires reasoning over a graph spanning institutions, with counterparties resolved across them, at a scale where the interesting structures are sparse and deliberately unremarkable. Current detection leans heavily on within-institution rules and typology signatures maintained by hand, which catch the patterns someone has already characterized and miss the ones being invented.

## What Already Exists
Graph analytics is a strong market. Neo4j, TigerGraph, and the cloud graph services handle large graphs with mature query and algorithm libraries; Quantexa and Palantir offer investigative graph platforms built for financial crime; community detection, centrality, and path-finding are commodity algorithms with good implementations.

## The Customization Gap
Those platforms and algorithms are tuned to find density and centrality — the fraud ring that clusters. Adversarial actors structure specifically to avoid that, so the signals that matter are behavioural and temporal rather than topological: accounts opened in a coordinated window across institutions, funds moving in characteristic timing patterns, shared weak identifiers that are individually unremarkable, and roles within a structure rather than positions in a cluster. The adaptation is detection built on typology structure rather than on generic graph anomaly — models trained to recognize the shape of a laundering or mule pattern across institutions, with counterparty resolution designed for the case where identifiers are deliberately fragmented. Privacy architecture is not an add-on: cross-institution linkage must work without exposing one member's customers to another, which constrains the design fundamentally and is why a general graph platform cannot simply be pointed at the problem. And alerting has to carry the network context an investigator needs to act, since a cross-institution finding that arrives as an unexplained score will be dispositioned as noise.

## Target Customer
Heads of detection science and product at consortium analytics vendors, and the financial crime investigators at member institutions who currently see one fragment of a structure and cannot know it is a fragment.

## Impact If Solved
Delivers the capability the consortium model promises and largely has not: detection of the patterns that exist only between institutions. That is also the one thing a single-institution competitor structurally cannot match, which makes it the right place for the vendor's differentiation to live.
