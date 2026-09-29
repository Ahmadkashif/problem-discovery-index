# Federated Matching Practice

**Niche:** [[niches/programmatic-ad-platforms/deterministic-identity-resolution/profile|Deterministic Identity Resolution]]
**Industry:** [[industries/programmatic-ad-platforms|Programmatic Ad Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Banks, health systems and statistical agencies match records across organisations without pooling them, using protocols designed for exactly that, and adtech uses a shared vendor and trust.
**Tags:** #compliance #graph-theory #evaluation-metrics #confidence-intervals #data-integration #bayesian-inference #hypothesis-testing #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to assemble the largest graph of real people that both buyers and publishers will actually adopt and regulators will accept — and whoever does that sets the addressable currency of the market.

## The Problem
Matching people across organisations that cannot share their underlying data is a solved problem with real deployments. Privacy-preserving record linkage is used between health systems, financial institutions and national statistical offices, with protocols that compute a match without either side learning the other's records, plus governance, audit and legal frameworks around them. Adtech's version of the same operation runs by sending hashed identifiers to a shared third party and hoping the arrangement holds up.

## What Already Exists
Privacy-preserving record linkage protocols; private set intersection and secure computation; data clean rooms with controlled query surfaces; differential privacy for aggregate release; and federated governance frameworks with audit.

## The Customization Gap
The adaptation is from a periodic batch linkage between a few institutions to continuous matching across thousands of parties at auction scale. It requires: (1) throughput and latency that the cryptographic protocols cannot currently meet at bid time, which forces a split between precomputed bridging and real-time lookup — this architecture question is the substantive engineering work; (2) many-party rather than two-party matching, since the chain runs buyer to platform to exchange to publisher and the pairwise protocols compose poorly; (3) commercial incentives that are adversarial rather than cooperative, unlike the health and statistics deployments where all parties want the match to be correct — here at least one party benefits from an inflated match rate; (4) consent granularity per use rather than per study, since a single record may be usable for measurement and not for targeting; and (5) economics that work at fractions of a cent per impression, where the existing deployments tolerate substantial per-match cost.

## Target Customer
Identity providers, clean room vendors, publishers and platforms, and privacy technology vendors for whom real-time advertising matching is unserved.

## Impact If Solved
The protocols exist and are deployed where all parties want a correct match; here at least one benefits from inflating it. Splitting precomputed bridging from bid-time lookup is what makes cryptographic matching viable at auction economics.
