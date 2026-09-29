# Liquidity for Unique Inventory

**Industry:** [[online-marketplaces|Online Marketplaces]]
**Type:** High Impact
**One-liner:** Matching works when a thousand sellers offer the same product and breaks when every listing is one of a kind — which is precisely the inventory marketplaces exist to serve.
**Tags:** #contrastive-learning #cnns #bert #word-embeddings #gradient-boosting #evaluation-metrics #dimensionality-reduction #k-nearest-neighbors #revenue-impact

## The Problem
A marketplace succeeds when listings sell and buyers find things. For commodity inventory this is a solved ranking problem: many identical items, abundant behavioural data per product, price as the main differentiator.

The marketplaces that matter are not like that. A vintage jacket, a used guitar, a piece of handmade furniture, a wholesale line from an independent brand — each listing is a single unit, described by a seller in their own words, photographed in their own way, and it exists once. When it sells it is gone, taking its behavioural data with it.

This breaks the machinery. Collaborative filtering needs repeated interactions with the same item and there are none. Query-to-product matching needs consistent product identity and there is none. Price signals need comparables and there is one of these.

So buyers search and find nothing suitable, sellers list and get no views, and both conclude the marketplace does not have what they need. The listing expires, the seller lists somewhere else, and the marketplace loses supply — which loses demand, which loses more supply.

The failure is invisible in the metrics that matter to most teams. Conversion is measured on the transactions that happened. Searches that returned nothing worth buying, and listings that never found a buyer, are recorded as absence.

## Why It's Unsolved
The cold start is total. Every listing is a cold start with no behavioural history, ever, and the standard remedy of falling back to content signals depends on content that amateurs produced — a title typed on a phone, four photographs in poor light, a description that assumes knowledge the buyer does not have.

Buyer intent is equally underspecified. Someone searching for a vintage denim jacket has constraints about size, condition, era, cut and price that they will recognise when they see it and cannot express in a query. The marketplace has no way to elicit them.

Attribute extraction from amateur content is genuinely hard, and it is the foundation everything else needs. Without knowing that this listing is a size medium 1970s piece in good condition, matching is guesswork.

And the temporal problem is unusual: supply is transient. A listing that would have been perfect for a buyer who searched last week appears today, and nothing connects them, because saved searches are opt-in and rarely used.

## What a Solution Looks Like
Attribute extraction as the foundation. Deriving structured attributes from listing photographs and text — category, brand, size, condition, material, era, style — turns unique items into positions in an attribute space where similarity is computable even without behavioural data. Images carry more signal than amateur titles and are systematically underused.

Similarity learned from behaviour rather than declared by taxonomy. Items that the same buyers considered are similar in the way that matters commercially, and that signal survives even when the items themselves do not repeat.

Unmet demand as a primary metric. Searches with no acceptable result, and browse sessions ending without engagement, are a direct measurement of what the marketplace is missing, and they should drive supply acquisition rather than sitting unanalysed.

Temporal matching. A buyer who searched and left should be reconnected when matching supply appears, automatically, without requiring them to have set up an alert.

Listing quality feedback to sellers at the point of listing, since a poorly described unique item is unfindable and the seller does not know why it did not sell.

## Impact If Solved
Liquidity is the whole business. A marketplace that improves the probability that a unique listing finds its buyer improves seller retention, which improves supply, which improves buyer experience — the flywheel every marketplace claims and few sustain. And it rests on data these platforms already hold and mostly treat as absence.
