# Storage Cost Nobody Puts in the Comparison

**Niche:** [[niches/agtech-platforms/grain-marketing-risk-tools/profile|Grain Marketing & Risk Tools]]
**Industry:** [[industries/agtech-platforms|Agtech Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The decision to store grain rather than sell it at harvest is made by comparing the current price to a hoped-for later one, with the interest, shrink, quality risk and bin cost of carrying it left out of the comparison entirely.
**Tags:** #descriptive-statistics #time-series-forecasting #confidence-intervals #evaluation-metrics #revenue-impact #hypothesis-testing #quick-win #automation
**Contested on:** Every serious competitor in grower-side grain marketing is fighting to show a grower their own position — bushels priced, basis exposure, storage and interest cost, against production risk — in one place, and whoever makes the grower's position legible takes the account.

## The Problem
Harvest price is disappointing, so the grain goes in the bin to wait for a better market. Carrying it costs interest on the value of the unsold crop, shrink from moisture loss, the risk of quality deterioration or a storage failure, and the opportunity cost of bin space and of not paying down an operating line. None of those enters the comparison, which is made between today's price and a hoped-for spring price. The grower frequently does capture a better price and frequently does not clear the carrying cost, and in either case does not know, because the carry was never computed.

## Why It's Still Broken
The carrying costs are diffuse and mostly non-cash: interest is on an operating line that is a single number, shrink is a small percentage nobody measures per bin, and bin cost is a capital asset already owned. Each individually feels negligible and the sum is not. There is also a behavioural element that anyone in the industry will recognise: storing feels like retaining an option and selling at a disappointing price feels like accepting a loss, which is a well-documented pattern and a poor basis for a six-figure decision.

## What a Fix Looks Like
Put the carry in the comparison, explicitly and per bushel. Interest at the operation's own borrowing rate on the value stored, shrink at measured rather than assumed rates, quality risk expressed as an expected discount from the operation's own history of what it has delivered out of storage, and a bin opportunity cost where bins are a constraint. Express the result as the break-even price — the price in March that makes storing equivalent to selling in October — which is a single number a grower can hold against the market and is currently never computed. Show the market's own carry from the futures spread alongside it, since the market is explicitly paying or not paying for storage and that signal is public and largely unused by growers. Record the outcome each year: what was stored, what it was ultimately sold for, and whether it beat the break-even — which over a few seasons tells the operation something true about its own storage decisions that no amount of general advice will.

## Who Feels the Pain
Growers comparing prices without carry; lenders financing stored inventory whose economics nobody computed; and the operation's cash position, which is tightest precisely when grain is sitting in bins.

## Impact If Fixed
The break-even storage price is arithmetic and is the single most useful number a grower can have at harvest, and almost none of them have it. Recording outcomes against it builds, over a few years, an honest picture of whether this operation's storage decisions have paid — which is a question the industry discusses endlessly and answers anecdotally.
