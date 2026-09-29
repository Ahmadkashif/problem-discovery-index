# The Item That Went Back in the Box

**Niche:** [[niches/live-commerce-platforms/seller-inventory-and-listing/profile|Seller Inventory & Listing]]
**Industry:** [[industries/live-commerce-platforms|Live Commerce Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Whatever does not sell during the show goes back in the box, is never recorded as unsold, and is rediscovered by accident eighteen months later.
**Tags:** #workflow-orchestration #automation #evaluation-metrics #revenue-impact #descriptive-statistics #quick-win #worker-facing #time-series-forecasting
**Contested on:** Every serious competitor in this niche is fighting to get a seller's stock into the platform without the seller typing it in — and whoever removes that step decides how much inventory the format can carry.

## The Problem
A host shows sixty items in an hour. Forty sell. The other twenty go back in the box. There is no record that they were shown, no record that they did not sell, no note of what was asked for them and no reason they will ever be shown again except chance. Sellers routinely carry thousands of dollars of stock they have forgotten they own, bought with money they needed, while sourcing more. The platform saw every one of those items on camera and recorded nothing, because its data model only has room for things that sold.

## Why It's Still Broken
The order is the only object the platform creates, so an item that did not become an order leaves no trace — this is a data model gap rather than a feature gap. Nobody has asked sellers to track unsold stock because nobody tracks it. Sourcing is more exciting than reworking old inventory. And the loss is unrealised revenue, which never appears in any report.

## What a Fix Looks Like
Make the shown-and-unsold item a first-class record. Create an item record when it is shown rather than when it sells, which is the whole of the fix and follows directly from capturing the frame and description at show time. Record the asking price and the room's response, since an item shown three times at twelve dollars is telling the seller something specific about its price. Queue unsold items for a later show automatically, with an interval and a suggested price adjustment, so rework becomes a default rather than an initiative. Prioritise the queue by carrying cost and by demand signal — an item matching a viewer's declared want should come back next show, which links the pool to discovery. Report aged inventory with money tied up, which is the number that changes sourcing behaviour and which no seller currently has. Suggest bundling for items repeatedly unsold individually, since that is what experienced sellers do by instinct. Offer a fixed-price listing as a fallback, so an item that does not work live is not simply stuck. Track sell-through by source lot, which tells the seller which suppliers and which pallets are actually worth buying — the highest-leverage decision they make and currently made on feel. And show the pool's value on the seller dashboard, because unsold stock that is never displayed is never worked.

## Who Feels the Pain
Sellers with capital locked in forgotten boxes; viewers who wanted an item that has been sitting unshown; and platforms whose supply is smaller than the inventory actually present.

## Impact If Fixed
The platform's data model only has room for things that sold, so a shown-and-unsold item leaves no trace at all. Creating the record at show time turns rework into a default, and sell-through by source lot informs the highest-leverage decision a seller makes.
