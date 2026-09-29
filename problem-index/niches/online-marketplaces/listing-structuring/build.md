# Amateur Text Against Somebody Else's Taxonomy

**Niche:** [[niches/online-marketplaces/listing-structuring/profile|Listing Structuring]]
**Industry:** [[industries/online-marketplaces|Online Marketplaces]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Search infrastructure and learned ranking are mature commodities, and marketplace search still fails because the inventory is described by amateurs against a taxonomy designed by someone else.
**Tags:** #large-language-models #cnns #object-detection #word-embeddings #evaluation-metrics #automation #transfer-learning #k-means-clustering
**Contested on:** Every serious competitor in this niche is fighting to turn an amateur's photograph and paragraph into the structured attributes everything downstream depends on — and whoever does that takes the account, because search, pricing, matching and recommendation all rest on structure the seller never provided.

## The Problem
A seller lists a chair. The title says "lovely old chair, great condition". The description says where they bought it and that it would suit a hallway. The category is furniture, one level up from where it belongs. Material, period, style, dimensions, maker and condition are all blank, and all six are visible in the photograph or inferable from the prose. Search cannot filter it, the valuation model cannot price it, the recommender cannot place it, and the buyer looking for exactly this chair will never find it. Every one of the six was extractable at listing time by a capability that is now ordinary.

## Why Nobody Has Built This
Attribute fields were designed as a form for the seller to fill, and the response to low completion was to require more fields, which sellers route around. Extraction from images was expensive until recently and the assumption of difficulty persists. Extraction from free text against a specific taxonomy was genuinely hard before language models and is now not. And the five downstream systems that would each benefit are owned by five teams, none of whom owns the input.

## What to Build
Extract the structure instead of asking for it. Read attributes from the photographs and the description automatically and populate the fields, with the seller confirming rather than authoring, which turns a form nobody completes into a review that takes seconds and is the whole build. Run extraction over the existing inventory, not just new listings, since the back catalogue is where most of the unstructured inventory lives and a one-time pass improves every downstream system immediately. Report an inventory structure score per category, so it is visible which parts of the catalogue are unfilterable and unrankable — a number nobody currently has. Extract into the buyer's vocabulary as well as the taxonomy's, since buyers and category managers use different words and indexing only the latter is why search fails. Attach confidence per extracted attribute, and use the uncertain ones to ask the seller a single targeted question rather than presenting a blank form. Detect category misplacement and correct it, which is mechanical and is a large share of why items are not found. Feed the extraction into pricing, matching, search and recommendation as a shared service, since the leverage comes from one extraction serving five systems. And measure downstream lift per system, because that is what justifies the investment and is currently nobody's number.

## Target Customer
Search, catalogue and category teams, the marketplace's downstream systems, and the sellers whose items are invisible for reasons they could not have known.

## Impact If Built
Six attributes are visible in the photograph and blank in the record, and extracting them is now ordinary. One extraction improves search, pricing, matching, recommendation and filtering at once, which makes it the highest-leverage automation in the category.
