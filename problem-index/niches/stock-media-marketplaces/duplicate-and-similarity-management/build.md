# Knowing How Big the Library Actually Is

**Niche:** [[niches/stock-media-marketplaces/duplicate-and-similarity-management/profile|Duplicate & Similarity Management]]
**Industry:** [[industries/stock-media-marketplaces|Stock Media Marketplaces]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The catalogue is counted in hundreds of millions of assets and covers a far smaller number of distinct things.
**Tags:** #contrastive-learning #k-means-clustering #dimensionality-reduction #evaluation-metrics #confidence-intervals #automation #revenue-impact #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to stop a catalogue of hundreds of millions of assets being mostly the same few million pictures — and whoever measures redundancy honestly knows what their library is actually worth.

## The Problem
Asset count is the number everyone quotes and it measures the wrong thing. A library of three hundred million assets in which a hundred thousand are photographs of a handshake in an office is not three hundred million distinct offerings. The redundancy costs money in review, storage and search quality, dilutes what each contributor earns, and means nobody — not the marketplace, not the buyer, not a model developer valuing the corpus — knows how much distinct content actually exists.

## Why Nobody Has Built This
Asset count is the competitive metric, so nothing that would reduce it gets measured — a business that markets on a number will not compute the number that shrinks it. Similarity detection was built for policy enforcement and stops at obvious duplicates. Contributors are rewarded for volume. And redundancy's costs are spread across several budgets and attributed to none.

## What to Build
Measure coverage rather than count. Cluster the catalogue by visual and semantic similarity and report effective distinct coverage, which is the core and is the honest measure of what the library contains. Report saturation per concept, since it identifies both where contribution is wasted and where the gaps are, connecting directly to commissioning. Quantify the cost of redundancy in review, storage and search quality, as those are real and currently unattributed. Adjust contributor incentives so volume is not the reward, because the redundancy is a rational response to the current rules. Use clustering in search to diversify results, in review to batch near-identical submissions and in valuation to price the corpus honestly. Show contributors their own internal redundancy, as many upload thirty frames when three would earn the same and would rather know. Distinguish redundancy from legitimate variation, since aspect ratios, orientations and small differences genuinely matter to buyers and over-collapsing is a real harm. Report effective coverage to buyers, which is a differentiator for a marketplace whose catalogue is genuinely varied. Use it in the corpus valuation, because a model developer paying for scale should be paying for distinct coverage. And publish the measure, since being the marketplace that reports coverage rather than count is a defensible position.

## Target Customer
Catalogue operations and executive leadership, contributors, buyers, and model developers valuing corpora by size.

## Impact If Built
A business that markets on a number will not compute the number that shrinks it, so redundancy goes unmeasured. Clustering the catalogue produces the honest coverage figure and feeds search diversity, review batching and corpus valuation at once.
