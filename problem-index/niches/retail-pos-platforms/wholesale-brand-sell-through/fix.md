# The Reorder Conversation Timed by Nobody

**Niche:** [[niches/retail-pos-platforms/wholesale-brand-sell-through/profile|Wholesale Brand Sell-Through]]
**Industry:** [[industries/retail-pos-platforms|Retail POS Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A store sells out of a brand's best item and neither the store nor the brand notices for six weeks, because the reorder conversation happens when a sales rep next calls rather than when the stock runs out.
**Tags:** #time-series-forecasting #descriptive-statistics #evaluation-metrics #confidence-intervals #workflow-orchestration #automation #revenue-impact #quick-win
**Contested on:** Every serious competitor serving independent brands is fighting to tell a wholesaler what actually sold at retail, store by store, in time to act on it — and whoever delivers sell-through from independent retail takes the brand.

## The Problem
A boutique's best-selling item from a small brand sells out in week five of a season. The owner, managing several hundred SKUs from forty vendors, does not notice. The brand, who would gladly ship more, does not know. The item is absent from the shelf for the remaining nine weeks of the season, the store loses the sales, the brand loses the sales, and both conclude the item performed moderately. Neither is wrong about what they observed and both are wrong about what happened.

## Why It's Still Broken
Reordering from small vendors is a manual, relationship-driven process with no replenishment logic behind it, and the store's attention is finite across many vendors. The brand has no visibility, as this niche describes. And the wholesale platforms that intermediate the order have historically been order-taking rather than replenishment-managing, so nothing triggers on a stockout. The result is that the most profitable moment in a wholesale relationship — an item selling out early — is the one both parties reliably miss.

## What a Fix Looks Like
Trigger on the stockout rather than on the calendar. Where a retailer shares sell-through, a sold-out or nearly sold-out item generates a restock prompt to the retailer with the sell-down rate, the remaining weeks of season and the vendor's lead time — which is the calculation the owner would do if they had time. The same event notifies the brand, who can confirm availability immediately, so the conversation starts with both parties informed. Even without full sharing, a retailer's own system can generate the prompt from its own data, which is a fix available today and unimplemented in most small-retail POS products for items from small vendors. Track reorder outcomes so both sides learn which items justify a mid-season reorder and which do not, which is a distinction currently made by instinct.

## Who Feels the Pain
Store owners losing weeks of sales on their best items; brands whose best performers go out of stock at retail invisibly; and customers who came for a thing the store used to have.

## Impact If Fixed
A mid-season stockout on a top item is the most expensive and most preventable inventory event in independent retail, and the trigger is a threshold on data the store already holds. It is also the clearest demonstration of the value of sharing, which makes it the right first capability to build in this niche.
