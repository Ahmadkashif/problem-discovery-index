# Small-Line Allocation Learned From Stores That Sell It

**Niche:** [[niches/greeting-card-publishers/multicultural-faith-and-language-lines/profile|Multicultural, Faith & Spanish-Language Lines]]
**Industry:** [[industries/greeting-card-publishers|Greeting Card Publishers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Culturally specific card lines are allocated to stores by census tiers, when the stores already carrying them reveal, sale by sale, where they actually sell.
**Tags:** #bayesian-inference #k-nearest-neighbors #gaussian-processes #feature-engineering #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to match each store's card assortment to the languages, faiths and communities of the shoppers it actually serves, and whoever places the right Spanish-language, faith and culturally specific designs in the right stores sells them through instead of taking them back.

## The Problem
A publisher decides which stores get a Spanish-language block, a Mahogany-style section or a faith section from demographic shares around the store. Those shares are a weak proxy: shoppers travel, bilingual households buy in both languages, and faith-based buying does not map neatly to census fields. Stores that would sell the line never get it, and stores that will not are given it anyway.

## Why Nobody Has Built This
Each line sells a few units per pocket per week in the stores that carry it and nothing is observed where it is absent, so the data looks too thin for store-level modelling. The lines are a small slice of revenue and get little analytics attention.

## What to Build
A hierarchical model that estimates each store's demand for each line from the sales of stores that carry it, borrowing strength from similar stores (trade area, shopper mix, channel, sales of related everyday pockets), with spatial smoothing across neighbouring stores. It recommends where to add, grow, shrink or remove each line's pockets and runs controlled tests at resets to confirm.

## Target Customer
Directors of multicultural and faith lines and the category managers who allocate them.

## Impact If Built
Higher sell-through on the lines with the least room for error, more shoppers finding a card in their own language or faith, and fewer returns from stores that should never have had the block.
