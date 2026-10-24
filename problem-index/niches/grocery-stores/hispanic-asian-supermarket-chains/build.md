# Festival-Aware Forecasts for Container Orders

**Niche:** [[niches/grocery-stores/hispanic-asian-supermarket-chains/profile|Hispanic & Asian Supermarket Chains]]
**Industry:** [[industries/grocery-stores|Grocery Stores]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Multicultural supermarket chains place container orders months ahead of festivals whose dates move every year, using last year's spreadsheet and the buyer's memory.
**Tags:** #time-series-forecasting #gradient-boosting #bayesian-inference #feature-engineering #tacit-knowledge-ml #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to size the direct-import and festival-season orders that drive these chains' sales, and whoever leaves the lowest unsold seasonal stock at an unchanged in-stock rate takes the account.

## The Problem
Lunar New Year can fall anywhere from late January to mid-February, Ramadan moves about eleven days earlier each year, and Diwali follows the lunisolar calendar. A buyer orders festival goods by container ~8–12 weeks ahead (estimate), adjusting last year's quantities by instinct for new stores, a shifted date and a change in the neighbourhood. Leftovers are marked down for months; shortfalls cannot be refilled.

## Why Nobody Has Built This
Forecasting vendors build for chains on the Gregorian retail calendar with weekly replenishment. These chains are mid-sized and few, and their data has thin item records. The buyer's knowledge of how each community shops before each festival is tacit.

## What to Build
A forecast keyed to moving festival dates, with features for days-to-festival, store community mix (from the store's own basket data), new-store ramp and import lead time. It produces a container-level order recommendation with an uncertainty band, a planned markdown path for leftovers, and a post-season review that records what the buyer changed and whether it worked.

## Target Customer
Heads of purchasing at Hispanic and Asian supermarket chains of 10 to 150 stores.

## Impact If Built
If festival goods are ~8% of a ~$500M chain's sales (estimate), cutting unsold seasonal stock by a quarter on a 10% leftover rate saves ~$1M a year in markdowns and write-offs.
