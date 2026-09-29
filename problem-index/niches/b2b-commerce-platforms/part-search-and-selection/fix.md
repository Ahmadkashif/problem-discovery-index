# The Competitor Part Number That Returns Nothing

**Niche:** [[niches/b2b-commerce-platforms/part-search-and-selection/profile|Part Search & Selection]]
**Industry:** [[industries/b2b-commerce-platforms|B2B Commerce Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The most common industrial search is a part number from another manufacturer, and the storefront returns no results because it only indexes its own numbers.
**Tags:** #k-nearest-neighbors #data-integration #evaluation-metrics #graph-theory #descriptive-statistics #automation #quick-win #revenue-impact
**Contested on:** Every serious competitor in this sub-niche is fighting to identify the one correct item in three hundred thousand from whatever the buyer happens to have — and whoever does that takes the account, because the alternative is calling a specialist and the wrong part stops a machine.

## The Problem
A buyer types the number printed on the failed component. It is a competitor's number, or an original equipment manufacturer number, or a legacy number from before a rebranding. The storefront searches its own part numbers and descriptions, finds nothing, and shows an empty result. The distributor sells an exact equivalent and has done for years. The buyer concludes the distributor does not stock it and calls somebody — possibly the competitor whose number they typed. The single most common way an industrial buyer identifies a part is the one the search does not support, and the equivalence is frequently known to the distributor's own staff.

## Why It's Still Broken
Cross-reference data is expensive to assemble and maintain, is not supplied by manufacturers who have no interest in helping competitors, and is treated as a catalogue enhancement rather than as the primary access path. Search indexes the distributor's own identifiers because that is what the product data contains. The lost search produces no event anybody reviews. And the resulting call is handled as normal business.

## What a Fix Looks Like
Index the numbers buyers actually use. Build and index a cross-reference set covering competitor, original equipment and legacy numbers, which is the highest-return catalogue investment in technical distribution and is where the searches are — assembling it from published interchange data, the distributor's own quote history and reps' knowledge is the practical route. Mine failed searches for the numbers people type, which is a free and continuously updating list of exactly what the cross-reference set is missing and is reviewed nowhere. Capture the resolution when a specialist answers a call, since every such call is a cross-reference the business just established and currently discards. Show the equivalence explicitly with its basis, since a buyer asked to fit an equivalent needs to know why it is equivalent. Handle partial and fuzzy number matches, since numbers are transcribed with errors and a near match is frequently the answer. Report the share of searches returning nothing and the revenue behind them, which is a direct measure of the gap and is not computed. Publish the cross-reference set, since a distributor whose site answers a competitor's part number acquires the search traffic for it. And treat cross-reference coverage as a catalogue completeness metric alongside attributes.

## Who Feels the Pain
Buyers who conclude the distributor does not stock a part it does; specialists answering cross-reference calls all day; and distributors losing searches to competitors whose numbers they do not index.

## Impact If Fixed
The most common access path is the one the search does not support, and the equivalence is frequently known to staff. Failed searches are a free, continuously updating list of exactly what the cross-reference set is missing and nobody reviews them.
