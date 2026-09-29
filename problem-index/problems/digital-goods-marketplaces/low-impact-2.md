# Discovery for Creative Assets

**Industry:** [[digital-goods-marketplaces|Digital Goods Marketplaces]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Visual embedding search is deployed and genuinely better than keyword matching, and buyers still cannot find the asset they want because what they want is a style, a mood and a compatibility requirement rather than a subject.
**Tags:** #contrastive-learning #cnns #transformers #word-embeddings #dimensionality-reduction #k-nearest-neighbors #evaluation-metrics #gradient-boosting

## The Problem
A buyer needs a font that feels like a specific era but is not a cliché, a template that fits their brand and works in the tool they use, a plugin compatible with their engine version, a preset that produces a look they can describe only by pointing at an example.

They search with words. The words are inadequate — aesthetic qualities do not have agreed vocabulary — so they browse, which is slow, or they leave.

Creators tag their own work, which produces the predictable problems: inconsistent vocabulary, aspirational tagging, keyword stuffing toward whatever is trending. The taxonomy fits some categories and not others.

Technical compatibility is a hard filter that is frequently soft in practice. A plugin that requires a specific version, a template that needs a particular application, a font that lacks a language's glyphs — buying the wrong one produces a refund and a poor review, and the compatibility information is frequently in the description rather than in a filterable field.

The consequence lands on creators. Work that is not found earns nothing, and new creators are least findable at exactly the point when they are deciding whether the platform is worth their time.

## What Already Exists
Visual similarity search using learned embeddings is deployed at the larger marketplaces and works well for images. Reverse image search is available. Faceted filtering exists where attributes are populated. Recommendation based on purchase history is standard. Some platforms extract dominant colours and basic style attributes automatically. Text search with synonym handling is mature.

## The Customisation Gap
Similarity search answers "more like this" and buyers frequently arrive without a starting example, which is the harder and more common case. Bridging a natural language description of a feeling to a region of asset space is a different problem from image-to-image matching.

Style vocabulary is undefined. There is no shared language for aesthetic qualities, and inducing one from how buyers actually search and what they subsequently purchase is a genuine opportunity — the marketplace sees millions of query-to-purchase pairs that encode exactly this mapping.

Compatibility should be a hard filter extracted from files rather than from descriptions. Engine versions, application requirements, glyph coverage and format support are readable from the assets themselves and are currently transcribed by creators if at all.

Bundle and workflow context is the fourth gap. Buyers frequently need assets that work together, and coherence across a set is a different objective from individual relevance.

## Impact If Solved
Discovery determines which creators earn, and the queries buyers actually have are aesthetic and compatibility-based rather than lexical. Inducing a style vocabulary from query-to-purchase behaviour and extracting compatibility from files addresses both halves, and the query-purchase corpus that makes the first possible exists only inside these marketplaces.
