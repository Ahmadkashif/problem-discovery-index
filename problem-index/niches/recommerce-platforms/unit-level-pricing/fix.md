# A Percentage of a Retail Price Nobody Paid

**Niche:** [[niches/recommerce-platforms/unit-level-pricing/profile|Unit-Level Pricing]]
**Industry:** [[industries/recommerce-platforms|Recommerce Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Resale prices are set as a percentage of an original retail price that is frequently unknown, often wrong, and in many cases was never what anybody actually paid.
**Tags:** #descriptive-statistics #evaluation-metrics #confidence-intervals #hypothesis-testing #gradient-boosting #revenue-impact #quick-win #k-nearest-neighbors
**Contested on:** Every serious competitor in this niche is fighting to price a one-of-a-kind unit correctly in seconds at a cost the item can bear — and whoever does that takes the economics, because the price decision determines whether a processed item makes money and it is made hundreds of times a shift.

## The Problem
The pricing rule anchors on original retail. For a mid-market fashion item that price was a list price discounted most of the year, so a percentage of it overprices systematically. For an item bought in an outlet the anchor is meaningless. For an older item the retail price is unknown and is guessed from a similar current product. For a brand whose resale demand exceeds its retail position the anchor underprices badly. The anchor is doing all the work in the pricing decision and it is an unreliable number that frequently bears no relationship to what the item is worth to a resale buyer.

## Why It's Still Broken
Original retail is the only universal reference available at intake without research, which makes it the natural anchor. The percentage rule is simple to operate and to explain to sellers in a consignment split. Nobody has measured how well the anchor predicts realised price, because the realised price is in another system. And when the price is wrong it is attributed to condition or demand rather than to the anchor.

## What a Fix Looks Like
Anchor on realised resale prices instead. Use the platform's own realised prices for comparable items as the reference, which is more predictive than retail by a wide margin and is available for almost every category the platform handles — this substitution is the fix and requires no modelling beyond a comparable lookup. Measure how well retail predicts realised price by category, which is a one-off analysis that will show the anchor is weak in most categories and strong in a few, and that alone should change the rule. Maintain a resale value index per brand and category, updated continuously, which is a durable asset and is what the anchor should be. Handle the categories where retail genuinely is predictive differently, since it is not uniformly useless and a blanket replacement would overcorrect. Report the anchor's error distribution so the pricing team can see where the rule is failing. Stop using retail in seller-facing communication where it sets an expectation the resale market will not meet, which is a common source of seller dissatisfaction. Detect items where the anchor and the comparable lookup disagree sharply, since those are the items worth a second look. And publish the index externally where it is useful, since a platform that defines what secondhand value is in a category holds a position competitors cannot take.

## Who Feels the Pain
Platforms systematically mispricing whole categories; sellers whose expectations were set by a retail anchor; and buyers paying above or below what the resale market supports.

## Impact If Fixed
Realised resale comparables predict far better than retail and are available for nearly every category, which makes the substitution a lookup rather than a model. Measuring the anchor's error by category is a one-off analysis that should change the rule by itself.
