# The Buyer Cannot Say What They Want

**Niche:** [[niches/digital-goods-marketplaces/asset-discovery/profile|Asset Discovery]]
**Industry:** [[industries/digital-goods-marketplaces|Digital Goods Marketplaces]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Visual embedding search is deployed and genuinely better than keyword matching, and buyers still cannot find the asset they want because what they want is a style, a mood and a compatibility requirement rather than a subject.
**Tags:** #contrastive-learning #transformers #word-embeddings #evaluation-metrics #revenue-impact #dimensionality-reduction #confidence-intervals #transfer-learning
**Contested on:** This niche is not terminal — matching an aesthetic intent and establishing technical fit are different contests with different winners, and they are stated separately in the sub-niches.

## The Problem
A designer needs a presentation template that feels restrained and editorial, for a client in finance, in their brand colours, editable in the software they own. They type minimal presentation template. They get four thousand results, sorted by sales, most of which are neither minimal nor restrained nor editable in their software. They scroll for forty minutes and buy something adequate. Meanwhile a creator who made exactly the right thing eight months ago has never been seen by anyone, because their tags said clean and modern rather than minimal, and the ranking rewards existing sales.

## Why Nobody Has Built This
Search infrastructure came from lexical retrieval and was upgraded to visual similarity, which solves the wrong half — similarity requires an example and the buyer's problem is that they have none. Aesthetic vocabulary is not standardised and creators tag inconsistently by necessity. Compatibility metadata requires structured data creators have no reason to supply. And discovery is judged on conversion, which a scrolling buyer eventually produces anyway.

## What to Build
Rebuild discovery around what the buyer is actually trying to express. Represent style separately from subject, since a buyer wanting a particular feel and a buyer wanting a particular object are asking different questions and one embedding cannot serve both — this is the structural insight the sub-niche develops. Let the buyer express intent by selection and refinement rather than by words, because the aesthetic query cannot be typed and interaction is the only route to it. Build compatibility as a first-class filter dimension, derived from the files rather than from creator claims, which is the other sub-niche and where the unambiguous wins are. Take the buyer's context — their project, their brand, their software, their licence needs — as part of the query, since it is stable across searches and currently re-entered or ignored every time. Surface adjacent and complementary assets, as buyers usually need a coherent set rather than one item and the platforms sell them one at a time. Give new work genuine exposure, because ranking by historical sales means a creator without sales never gets them, which quietly determines who has an income. Learn from what buyers rejected as well as what they bought, since forty minutes of scrolling is a strong signal and is discarded. Handle the collection query — assets that work together — which is what a buyer building something actually needs. Measure whether the buyer got what they came for rather than whether they bought something. And report discovery outcomes to creators, so they can act on why their work is not found.

## Target Customer
Digital goods marketplaces, the creators whose income depends on being found, and the buyers scrolling through four thousand results.

## Impact If Built
Visual similarity solves the half that requires an example the buyer does not have. Separating style from subject, and deriving compatibility from the files rather than from creator claims, are the two structural changes the sub-niches develop.
