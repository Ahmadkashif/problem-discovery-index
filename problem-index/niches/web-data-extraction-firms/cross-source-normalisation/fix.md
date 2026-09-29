# The Same Field Name Meaning Different Things

**Niche:** [[niches/web-data-extraction-firms/cross-source-normalisation/profile|Cross-Source Normalisation]]
**Industry:** [[industries/web-data-extraction-firms|Web Data Extraction Firms]]
**Type:** Fix (Pain Point)
**One-liner:** Two sites both have a price field, one includes tax and delivery and the other does not, and the delivered dataset presents them in the same column with no indication that they are not comparable.
**Tags:** #data-integration #evaluation-metrics #descriptive-statistics #hypothesis-testing #compliance #quick-win #automation #confidence-intervals
**Contested on:** Every serious competitor in this niche is fighting to turn a thousand sites' worth of the same entity into one coherent dataset — and whoever does that takes the account, because that reconciliation is the work customers assume they are buying.

## The Problem
A price comparison consumes two hundred sources. In one country prices are quoted inclusive of tax by convention; in another they are not. Some sites include delivery in the displayed price and some add it later. Some show a member price to logged-out visitors and some do not. All of it arrives in a column called price. The analysis concludes that one market is systematically cheaper than another, and a meaningful part of that finding is a tax convention. The semantic difference was visible on the page, known to whoever wrote the extractor, and recorded nowhere.

## Why It's Still Broken
The field name is the same, so the mismatch is invisible in the schema and only appears in the values, where it looks like real variation. Recording semantics requires the extractor author to write down what they observed, which is unbilled and unprompted. Customers assume comparability because the column name implies it. And the error is systematic rather than random, which means it survives every sanity check that looks for outliers.

## What a Fix Looks Like
Record the semantics with the field. Capture per-source field semantics at extraction time — tax treatment, inclusions, currency, the visitor state the page was fetched in, the unit — as structured metadata, which is a few fields the extractor author already knows and is the whole fix. Deliver semantics with the data so a customer can normalise or segment rather than assuming comparability. Normalise to a stated convention where possible and say which, rather than silently mixing. Detect semantic inconsistency automatically from value distributions, since a systematic offset between two sources selling identical products is detectable and is a strong hint that their conventions differ. Flag fields where sources disagree systematically, which tells a customer exactly where not to aggregate. Record the page state — logged out, no location set, no currency selected — because the same page shows different prices under different states and this is never captured. Document known convention differences per market as a reference, which is a durable artefact the firm is uniquely placed to build. And warn when a query aggregates across sources with incompatible semantics, which is the point of use and the last chance to catch it.

## Who Feels the Pain
Analysts drawing conclusions from a column that mixes two definitions; customers whose systematic error survives every outlier check; and the extraction engineers who noticed the difference and had nowhere to record it.

## Impact If Fixed
The semantic difference is visible on the page, known to whoever wrote the extractor, and recorded nowhere. A few structured metadata fields captured at extraction time let a customer normalise deliberately instead of aggregating two definitions into one column.
