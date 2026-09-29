# A Query That Cannot Be Typed

**Niche:** [[niches/digital-goods-marketplaces/aesthetic-and-style-search/profile|Aesthetic & Style Search]]
**Industry:** [[industries/digital-goods-marketplaces|Digital Goods Marketplaces]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The buyer knows a template is wrong in half a second and cannot say what right looks like, and every search system in use requires them to state the query.
**Tags:** #contrastive-learning #dimensionality-reduction #transformers #manifold-learning #evaluation-metrics #confidence-intervals #transfer-learning #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to match a buyer to a feeling they cannot put into words — and whoever builds the interaction that extracts an aesthetic intent wins the searches that keyword and similarity search both fail.

## The Problem
The buyer wants something restrained, editorial, not corporate, not startup-cheerful, with generous spacing and a serif that is not fussy. They type minimal. The system returns things tagged minimal, which is a word applied to half the catalogue by creators who each meant something different by it. The buyer rejects forty results in ninety seconds — clearly, decisively, on a basis they could not have articulated — and the system learns nothing from any of the rejections, because it was built to accept a query and return matches rather than to converge on a target through feedback.

## Why Nobody Has Built This
Retrieval assumes a stated query, which is the foundational assumption and the one that fails here. Style has no labels, so supervised approaches have nothing to train on and the field defaults to general embeddings that entangle style with subject. Interactive refinement costs more requests per session, which looks like worse efficiency on standard search metrics. And the failure is a long session ending in a mediocre purchase, which registers as a conversion.

## What to Build
Learn a style space and search it by feedback. Separate style from subject in the representation, training on signals that exist without labels — a creator's own catalogue is a strong style-consistency signal, as are curated collections and buyers' saved sets — which is the key move and it makes the problem tractable without an annotation project. Build the search as a convergence loop rather than a query: show a diverse spread, learn from what is rejected, narrow, repeat, since rejection is the abundant and reliable signal and acceptance is rare. Treat each rejection as information about a direction rather than about an item, which is what makes the loop converge in a handful of rounds instead of hundreds. Support starting from anything the buyer has — a brand, an existing document, a screenshot, a mood board — because most buyers have some artefact and none have a query. Let the buyer steer along interpretable directions, since more restrained or warmer or denser are adjustments people can express even when the destination is not, and exposing those axes is the interface that works. Model the buyer's persistent taste across sessions, as it is stable and currently re-elicited every time. Diversify results deliberately, because twenty near-identical results waste the round and collapse the loop. Learn a house style per buyer organisation, which is what agencies and in-house teams actually need. Evaluate on time to a satisfying result rather than on relevance judgements, which cannot be collected for a query that was never stated. And show creators where their work sits in the style space, which tells them something about positioning nothing else can.

## Target Customer
Digital goods and creative asset marketplaces, stock and template platforms, and the design teams whose search sessions run to forty minutes.

## Impact If Built
Retrieval assumes a stated query and this buyer has none, only instant recognition of wrong. Learning style from creator catalogues and curated sets avoids an annotation project, and treating rejections as directions is what makes the loop converge in a few rounds.
