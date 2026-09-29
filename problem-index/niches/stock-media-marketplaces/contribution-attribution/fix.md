# Counting Downloads as a Proxy

**Niche:** [[niches/stock-media-marketplaces/contribution-attribution/profile|Contribution Attribution]]
**Industry:** [[industries/stock-media-marketplaces|Stock Media Marketplaces]]
**Type:** Fix (Pain Point)
**One-liner:** The formula pays on historical downloads, which measures how well an asset sold and not what it taught a model.
**Tags:** #quick-win #descriptive-statistics #evaluation-metrics #confidence-intervals #revenue-impact #hypothesis-testing #compliance #causal-inference
**Contested on:** Every serious competitor in this niche is fighting to measure what an individual asset contributed to a trained model's behaviour and output — and whoever demonstrates an attribution that survives technical scrutiny gives the whole licensing question a basis it currently lacks.

## The Problem
Compensation formulas lean on download history because it is the number that exists. But a heavily downloaded generic image is one of tens of thousands of near-identical assets and may have contributed almost nothing distinctive; a rarely downloaded photograph of an unusual subject may be the only example of its kind in the corpus and therefore far more informative to a model. The proxy is not merely imprecise — for this purpose it is plausibly backwards, and it is being used because it was available.

## Why It's Still Broken
The formula needed an input that existed on day one, so the sales metric was used for a training question — a proxy chosen for availability rather than for validity becomes the basis of a distribution nobody can defend. Uniqueness is not computed. Nobody tested whether downloads correlate with anything relevant. And arguing about the formula's basis is unwelcome once payments are out.

## What a Fix Looks Like
Add the dimensions that are computable today. Compute a uniqueness or rarity measure per asset from the corpus itself, which is the fix and is a straightforward embedding and clustering exercise on data already held. Report the corpus's redundancy, since a large share of assets are near-duplicates of each other and that fact alone reframes the formula. Weight by coverage of a concept rather than by volume within one, as the model gains from breadth and the formula rewards depth. Use the query record to identify assets that satisfied demand nothing else could, which is revealed-value evidence and is not a download count. Test whether downloads correlate with any plausible contribution measure, because the assumption has never been checked and may be refutable quickly. Publish the alternative dimensions even before changing the formula, as transparency about the basis is separable from changing the payments. Handle the exclusive and commissioned asset differently, since they are categorically distinct in provenance and in scarcity. Show contributors where their assets sit on these dimensions, which is more informative than a payment. Commit to revising the basis as measurement improves, so the formula is provisional rather than settled. And say plainly that downloads are a proxy, because presenting it as a contribution measure is the part that is indefensible.

## Who Feels the Pain
Contributors of rare work paid as though it were generic; contributors of generic work receiving a share nobody can justify; marketplaces defending a basis they know is weak; and the credibility of licensed corpora generally.

## Impact If Fixed
A proxy chosen for availability rather than validity becomes the basis of a distribution nobody can defend. Uniqueness and coverage are computable from the corpus today and are plausibly closer to what a model actually gained.
