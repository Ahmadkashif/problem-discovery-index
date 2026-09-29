# The New Menu Item With No History

**Niche:** [[niches/restaurant-tech-platforms/independent-fsr-forecasting/profile|Independent Restaurant — Forecasting on a Thin History]]
**Industry:** [[industries/restaurant-tech-platforms|Restaurant Tech Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Restaurants change menus constantly and every new item is prepped by guess for its first month, with the over-prep thrown away and the under-prep costing a sold-out dish on a Saturday, and nobody has ever measured which way the guess goes.
**Tags:** #k-nearest-neighbors #gradient-boosting #descriptive-statistics #evaluation-metrics #confidence-intervals #feature-engineering #automation #quick-win
**Contested on:** Every serious competitor selling forecasting to independent restaurants is fighting to make a useful prediction for a location with two years of history and a menu that changes monthly — and whoever borrows most effectively from comparable locations takes the account.

## The Problem
A chef adds four items to the menu. For the first several weeks nobody knows how they will sell, so prep quantities are guesses. Some items are over-prepped and the excess is discarded nightly; others sell out early and disappoint guests who ordered from a menu that offered them. After a month the guesses converge on reality through trial and waste, and then the menu changes again. In a business where menu churn is constant, the restaurant is permanently in the guessing phase for some part of its offering, and the cost is invisible because waste is recorded, if at all, as a lump.

## Why It's Still Broken
An item with no history has no history, and every forecasting product in the segment is built on item history, so the new-item case falls outside the product and is handed back to the operator. Nobody has treated it as the predictable problem it is: a new item is not unprecedented, it is similar to items this restaurant has sold before and to the same item at comparable restaurants. Waste measurement is also weak enough that the cost of guessing wrong is not visible, which keeps the problem from having a size.

## What a Fix Looks Like
Predict a new item from its attributes and its neighbours. Within the restaurant, an item's category, price relative to the menu, position on the menu, protein and preparation, and what it replaced are all informative — an entrée replacing another entrée at a similar price captures a predictable share of it. Across the corpus, the same dish appears at hundreds of comparable restaurants with known demand curves, including the shape of the early-weeks novelty effect that operators consistently misjudge. Combine both into a prep recommendation with an interval, and update aggressively in the first two weeks as real data arrives, since a new item's first ten days are highly informative. Measure the outcome honestly: track over- and under-prep on new items specifically, which no restaurant currently does and which is the number that shows whether any of this works.

## Who Feels the Pain
Kitchen managers throwing away a guess every night; chefs whose new dish sold out at eight; and owners whose food cost includes a churn penalty nobody has ever quantified.

## Impact If Fixed
New-item prep guidance shortens the guessing phase from a month to a few days, which in a restaurant with frequent menu changes is a permanent reduction in waste rather than a one-off. Measuring new-item prep error is the first step and typically reveals a systematic bias in one direction, which is correctable the moment it is visible.
