# The Last-Sale Price That Was One Trade

**Niche:** [[niches/virtual-economy-operators/price-discovery-and-market-data/profile|Price Discovery & Market Data]]
**Industry:** [[industries/virtual-economy-operators|Virtual Economy Operators]]
**Type:** Fix (Pain Point)
**One-liner:** The displayed price is whatever the most recent transaction was, and the most recent transaction was two accounts doing each other a favour.
**Tags:** #quick-win #descriptive-statistics #evaluation-metrics #confidence-intervals #automation #change-point-detection #data-integration #compliance
**Contested on:** Every serious competitor in this niche is fighting to publish a reference price people can rely on for goods they buy with real money — and whoever publishes it credibly takes the account.

## The Problem
Where a price is shown at all, it is usually the last sale. For a thin item that is a single trade, and a single trade is trivially manufactured. Someone buys from themselves at a high price, the platform displays it as the market price, and other participants transact against it. The display is doing active harm: it presents one arbitrary number with the authority of the platform behind it.

## Why It's Still Broken
Last sale is the easiest thing to display — a price that requires no computation will be the price that gets displayed, and the platform's authority then attaches to whatever the last trade happened to be. Nobody specified what the number should mean. Thin markets are the majority. And the harm falls on whoever transacts against it.

## What a Fix Looks Like
Replace one trade with a window and say how thin it is. Display a median or volume-weighted price over a window rather than the last sale, which is the fix and removes the single-trade attack immediately. Show the number of trades behind the figure, since a price from three trades and a price from three thousand should not look identical. Mark items as thinly traded rather than showing a confident price, which is honest and immediately useful. Exclude trades between linked accounts where they can be identified, as those are the manufactured ones. Show a price range rather than a point for illiquid items. Display the trade history so participants can judge for themselves, which costs nothing and is currently hidden. Suppress the price entirely below a minimum trade count rather than publishing a meaningless one. State what the displayed number means in one line, which is what turns a figure into information. Apply the same treatment wherever the price is surfaced, including in trade interfaces. And publish the change, since participants have built expectations around the current number.

## Who Feels the Pain
Participants who paid a manufactured price; anyone valuing an inventory from these figures; third-party trackers repeating them; and the operator, whose authority is attached to a number it never computed.

## Impact If Fixed
A price that requires no computation will be the price that gets displayed, and the platform's authority then attaches to whatever the last trade happened to be. A windowed median with a trade count removes the single-trade attack outright.
