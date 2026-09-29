# Buy: Recommendation Practice for Indicator Selection

**Niche:** Indicator Feeds
**Industry:** [[industries/threat-intelligence-vendors|Threat Intelligence Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Recommendation systems learned to select a small relevant set from a vast catalogue using behavioural signals from similar users, and threat intelligence ships the catalogue.
**Tags:** #gradient-boosting #k-nearest-neighbors #k-means-clustering #evaluation-metrics #confidence-intervals #dimensionality-reduction #data-integration
**Contested on:** Whether a feed delivers what a particular customer should act on, or everything the vendor collected with the filtering left to the buyer.

## The Problem

Selecting a small relevant subset from a very large catalogue, for a specific user, using signals from similar users, is a solved commercial problem. Recommendation systems do it at enormous scale with well-understood techniques: collaborative filtering from behavioural similarity, content-based matching on item attributes, hybrid approaches combining both, and careful handling of the cold start.

Threat intelligence has the same structure. The catalogue is millions of indicators. The user is an organisation with attributes — stack, sector, geography, exposure. The behavioural signal is which indicators matched at which organisations. And the task is selecting the subset this organisation should act on.

The category does not attempt it. Indicators are tagged with coarse sector labels and shipped in full, with the selection pushed onto the customer. The techniques that would do this properly are commodity, well documented and deployed everywhere else.

## What Already Exists

Recommendation systems: collaborative filtering, matrix factorisation, content-based and hybrid recommenders, with mature open-source implementations and extensive practical literature on cold start, popularity bias and evaluation.

Search and ranking: learning to rank, relevance modelling and the whole apparatus of ordering a large candidate set for a specific query and user.

Anomaly and rarity scoring: techniques for identifying which items in a large set are unusual for a particular context, which maps closely onto identifying indicators unusual for a given organisation.

Security-adjacent: vulnerability prioritisation products that rank findings by exploitability and environmental relevance — the closest existing application of this thinking in security, and applied to vulnerabilities rather than to indicators.

Threat intelligence platforms: scoring and filtering features, mostly rule-based on coarse attributes.

## The Customization Gap

**The behavioural signal exists and is not used.** Which indicators matched at which organisations is exactly the interaction matrix a collaborative filter needs. Vendors with telemetry have it and none uses it for selection.

**The cost asymmetry inverts the usual objective.** A recommender optimises engagement and a missed recommendation is cheap. Here a withheld indicator that would have mattered is expensive, so the selection must be recall-oriented with transparency about what was withheld — a different operating point from any consumer system.

**Cold start is severe.** A new customer has no match history. Content-based matching on organisational attributes is the answer, and it needs those attributes to be captured properly rather than as a sector dropdown.

**Popularity bias would be actively harmful.** A recommender that favours widely-matched indicators would systematically deprioritise the singleton match that indicates targeting — which is the most valuable indicator in the feed. This needs deliberate handling and would be the default failure of a naive implementation.

**Evaluation requires the quality measurement.** Recommender quality is assessed against held-out interactions. Here that means match data, which is the measurement the category does not publish — so selection cannot be evaluated until quality measurement exists.

**Vulnerability prioritisation is the proof of concept.** The same thinking applied to vulnerabilities is commercially established and accepted. Applying it to indicators is a shorter step than it appears and nobody has taken it.

## Target Customer

Vendors with installed-base telemetry, for whom the interaction matrix already exists and the technique is commodity.

Threat intelligence platform vendors, who sit across multiple feeds and could offer selection as a layer above all of them — arguably a better position than any single feed vendor.

Security operations leadership as the buyer, where the argument is analyst capacity rather than feed features.

## Impact If Solved

Commodity recommendation technique reaches a selection problem that is currently solved by coarse tags and customer effort.

The cross-organisation match matrix is a genuine asset that vendors hold and use for nothing, and it is precisely the signal that would make selection work.

And handling the popularity-bias problem deliberately would preserve the singleton matches that indicate targeted activity — which is both the hardest part of the adaptation and the part that makes it worth doing.
