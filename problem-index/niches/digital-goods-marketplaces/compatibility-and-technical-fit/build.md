# Bought It, Cannot Open It

**Niche:** [[niches/digital-goods-marketplaces/compatibility-and-technical-fit/profile|Compatibility & Technical Fit]]
**Industry:** [[industries/digital-goods-marketplaces|Digital Goods Marketplaces]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Whether an asset works in the buyer's project is fully determined by the file and the buyer's environment, and no marketplace answers it before the money changes hands.
**Tags:** #feature-engineering #graph-theory #automation #evaluation-metrics #workflow-orchestration #data-integration #revenue-impact #compliance
**Contested on:** Every serious competitor in this niche is fighting to tell a buyer whether an asset will actually work in their project before they pay for it — and whoever answers that reliably removes the largest cause of refunds and abandoned purchases in the category.

## The Problem
The buyer purchases a plugin. It requires an engine version they are not on, because their project is mid-development and upgrading would break everything. Or a template that opens only in the subscription tier they do not have. Or a font missing the accented characters their client's name needs. Or an asset that depends on three other assets, unmentioned. In every case the information was present in the file and the buyer's environment was knowable, and the marketplace let the transaction complete and then processed a refund. The category treats this as an unavoidable friction of selling files, and it is a question with a computable answer.

## Why Nobody Has Built This
Compatibility is asked of creators as a form field, which makes it a claim rather than a fact, and claims decay as software versions move. Extracting requirements means parsing dozens of proprietary formats, which is unglamorous work no platform has prioritised. Knowing the buyer's environment requires asking or integrating, neither of which anyone has done. And refunds are absorbed as a cost of the category.

## What to Build
Derive compatibility from the files and check it against the buyer. Parse uploaded assets to extract their real requirements — format versions, software minimums, dependencies, character coverage, resolution, colour space, engine APIs — which is the foundation and replaces a declaration with a fact. Model the buyer's environment once, from a stated profile or a tool integration, and reuse it across every search and purchase, since it is stable and currently re-established never. Answer compatibility before purchase, plainly, per asset, which is the product and is what converts the browsing experience from a gamble into a decision. Resolve dependencies and show the full set needed, because the hidden dependency is the most common and most infuriating failure and the buyer discovers it only after paying. Verify licence fit against the buyer's stated use in the same check, connecting this to the licensing work, since an incompatible licence is as disqualifying as an incompatible format. Re-verify continuously as software versions release, so the catalogue does not silently rot — this is the fix note's subject. Warn existing owners when an asset they bought stops working with their updated toolchain, which no platform does and which is the difference between a purchase and a relationship. Let buyers filter on their own environment as a default rather than as an advanced option, which is what makes the whole capability reach people. Tell creators exactly which compatibility gaps cost them sales, which is actionable in a way sales figures are not. And report pre-purchase compatibility coverage as a catalogue health metric.

## Target Customer
Digital goods and creative asset marketplaces, game asset and plugin stores, and the buyers refunding assets they could not open.

## Impact If Built
The answer is in the file and the environment is knowable, and the platform lets the transaction complete and refunds it. Deriving requirements by parsing the asset replaces a decaying creator claim with a fact, and hidden dependencies stop being discovered after payment.
