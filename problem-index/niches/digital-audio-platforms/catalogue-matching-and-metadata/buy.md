# Master Data and Entity Resolution

**Niche:** [[niches/digital-audio-platforms/catalogue-matching-and-metadata/profile|Catalogue Matching & Metadata]]
**Industry:** [[industries/digital-audio-platforms|Digital Audio Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Entity resolution expresses match confidence and reviews the uncertain, and rights matching returns matched or unmatched.
**Tags:** #graph-theory #word-embeddings #evaluation-metrics #confidence-intervals #data-integration #k-nearest-neighbors #automation #contrastive-learning
**Contested on:** Every serious competitor in this niche is fighting to match a recording to a rights record cleanly enough that its money reaches an owner — and whoever resolves the unmatched pool releases a real sum to people who do not know it exists.

## The Problem
Entity resolution and master data management have well-developed answers for exactly this: probabilistic matching with confidence scores, blocking to make large-scale comparison tractable, stewardship review of uncertain matches, and quality measurement of the matching process itself. Rights matching at streaming scale is a binary lookup with a manual claims process behind it, which is the architecture entity resolution abandoned decades ago.

## What Already Exists
Probabilistic record linkage with match scores; blocking and candidate generation at scale; stewardship review workflows; golden record construction; and match quality measurement.

## The Customization Gap
The adaptation is to records with a strong non-textual signal and a financial consequence. It requires: (1) audio as a matching feature, which no entity resolution framework contemplates and which is the strongest evidence available here — this is the substantive addition; (2) a many-to-many structure across recordings, compositions and rights holders, more complex than the usual duplicate-detection shape; (3) a wrong match paying the wrong person, which sets the confidence threshold far higher than a merged customer record would; (4) a hundred thousand daily arrivals, so review capacity is the binding constraint; and (5) claimants outside the system who cannot participate in stewardship.

## Target Customer
Rights operations leadership, rights holders, societies and distributors, and entity resolution vendors.

## Impact If Solved
Entity resolution moved past binary matching decades ago and rights matching has not. Adding audio as a matching feature is the substantive extension, and the financial consequence of a wrong match is what sets the review threshold.
