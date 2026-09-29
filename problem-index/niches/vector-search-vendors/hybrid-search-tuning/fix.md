# Scores That Are Not on the Same Scale

**Niche:** [[niches/vector-search-vendors/hybrid-search-tuning/profile|Hybrid Search Tuning]]
**Industry:** [[industries/vector-search-vendors|Vector Search Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** Lexical and dense scores live on incomparable scales that vary per query, and combining them with a weighted sum means the weight is doing something different for every query.
**Tags:** #descriptive-statistics #probability-distributions #evaluation-metrics #hypothesis-testing #norms-and-inner-products #confidence-intervals #quick-win #monte-carlo-methods
**Contested on:** Every serious competitor in this niche is fighting to set the balance between lexical and dense retrieval from the customer's own evidence rather than from a documentation default — and whoever does that takes the account, because the setting is free to change and nobody knows what theirs should be.

## The Problem
A lexical score depends on term frequencies and document lengths and can range widely between queries. A cosine similarity is bounded but its useful range is narrow and query-dependent, since some queries sit in a dense region of the space where everything scores high. Adding them with a fixed weight means that for one query the lexical side dominates the sum and for the next it is negligible — not because that is desirable but because the scales happened to differ. The configured weight describes an intention that the arithmetic does not deliver, and per-query behaviour is effectively arbitrary.

## Why It's Still Broken
The weighted sum is the obvious combination and its scale problem is subtle enough to be missed by anyone not from the retrieval field. Normalisation requires knowing the score distribution, which varies per query and requires retrieving a larger candidate set to estimate. Rank-based fusion avoids the problem and discards score magnitude, which is a real loss and is treated as settling the matter. And the symptom is inconsistent quality across queries, which is attributed to embeddings rather than to arithmetic.

## What a Fix Looks Like
Put the scores on a comparable scale before combining. Normalise each mode's scores within the query's own candidate set, which is the minimum correct step, costs almost nothing, and fixes the grossest version of the problem immediately. Calibrate each score to a probability of relevance using a small labelled set, which makes the combination principled rather than heuristic and is what turns the weight into a meaningful quantity. Offer rank fusion and calibrated score fusion as explicit alternatives with guidance on when each is better, since rank fusion is genuinely more robust with poor calibration and genuinely worse with good calibration, and presenting it as the universal answer is what has stalled progress here. Report the per-query contribution of each mode so the inconsistency is visible rather than inferred. Detect queries where one mode's scores are degenerate — everything scoring nearly the same — which is where the combination breaks worst and is easy to identify. Retrieve a wider candidate set from each mode before fusing, since fusing two short lists loses documents that either mode ranked just outside its cut. And document the scale behaviour, because the current silence leaves every customer to rediscover it.

## Who Feels the Pain
Teams whose hybrid search works well for some queries and badly for others with no apparent pattern; engineers blaming embeddings for an arithmetic problem; and vendors whose hybrid feature underdelivers against its own documented claim.

## Impact If Fixed
Per-query normalisation costs nothing and fixes the grossest version immediately. Calibrating both scores to a relevance probability is what makes the configured weight mean what the customer thinks it means.
