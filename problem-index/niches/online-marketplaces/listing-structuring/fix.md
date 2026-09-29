# A Category Tree Built for the Wrong People

**Niche:** [[niches/online-marketplaces/listing-structuring/profile|Listing Structuring]]
**Industry:** [[industries/online-marketplaces|Online Marketplaces]]
**Type:** Fix (Pain Point)
**One-liner:** The taxonomy is designed by category managers for reporting and merchandising, sellers file against it badly because it does not match how they think, and buyers navigate it badly for the same reason.
**Tags:** #k-means-clustering #word-embeddings #evaluation-metrics #graph-theory #descriptive-statistics #automation #quick-win #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to turn an amateur's photograph and paragraph into the structured attributes everything downstream depends on — and whoever does that takes the account, because search, pricing, matching and recommendation all rest on structure the seller never provided.

## The Problem
The category tree was built for reporting lines and merchandising campaigns. A seller looking for where to put a handmade ceramic bowl finds three plausible categories and picks one; three other sellers pick the other two. A buyer browsing for the same thing goes to a fourth. The tree is internally coherent and matches neither how sellers describe nor how buyers search, and since it determines filtering, browse navigation and frequently ranking, that mismatch propagates into every part of the experience. It is also nearly impossible to change, because reporting depends on it.

## Why It's Still Broken
Taxonomies are owned by category management and serve their reporting needs first, which is a legitimate requirement badly conflated with a navigation one. Restructuring a tree breaks historical reporting, which makes any change expensive. The evidence that would settle how buyers actually think — search queries and browse paths — sits with the search team. And the misfiling is absorbed as a seller error.

## What a Fix Looks Like
Separate the reporting tree from the navigation structure. Keep the reporting taxonomy stable and derive a separate navigational structure from behaviour, mapping between them, which resolves the conflation that makes the tree unchangeable and is the fix. Derive the navigational structure from query and browse data — what buyers actually search, what they click together, what they compare — rather than from merchandising logic. Let items sit in multiple places, since a handmade ceramic bowl is legitimately tableware and pottery and a gift, and forcing one choice loses two audiences. Measure misfiling rates per category from extraction and from search behaviour, which identifies the places the tree is confusing rather than the sellers being careless. Merge and split categories on evidence, since a category nobody browses and one with thousands of items are both failures. Support the seller with a suggestion rather than a tree, because nobody navigates a taxonomy willingly. Map to buyer vocabulary explicitly, so the words buyers use route to the right place regardless of what the category is called internally. And review the structure on a cadence with the behavioural evidence, since categories drift with fashion and a tree fixed five years ago describes a different market.

## Who Feels the Pain
Sellers guessing between three plausible categories; buyers browsing a structure that does not match how they think; and search teams compensating for a taxonomy they do not own.

## Impact If Fixed
Separating the reporting tree from the navigational structure resolves the conflation that makes the taxonomy unchangeable. Deriving navigation from query and browse behaviour, and allowing multiple placement, addresses both the seller's guess and the buyer's path at once.
