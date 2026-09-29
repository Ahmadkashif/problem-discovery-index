# The Missing Attribute Nobody Filters Past

**Niche:** [[niches/recommerce-platforms/catalogue-attribute-automation/profile|Catalogue & Attribute Automation]]
**Industry:** [[industries/recommerce-platforms|Recommerce Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** An item with a blank size or material field is excluded from every search that filters on it, which is most searches, and the listing looks complete because the fields are optional.
**Tags:** #evaluation-metrics #descriptive-statistics #data-integration #automation #confidence-intervals #revenue-impact #quick-win #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to turn a photograph into a complete, findable listing without a person typing — and whoever does that takes the cost out, because listing labour is a fixed cost on every item regardless of what it is worth.

## The Problem
A coat is listed without a size, because the label was faded and the processor moved on. Every buyer browsing coats filters by size, so the item is invisible to all of them. It receives almost no views, is discounted on schedule, and is eventually disposed of. The listing passed validation because size is an optional field. The same happens with material, colour when unusual, and any attribute that a category's buyers filter on — and the items affected are invisible in a way that looks like low demand rather than like a catalogue defect.

## Why It's Still Broken
Fields are optional because making them mandatory would block listings the processor cannot complete, which is a real operational constraint. The connection between a blank field and invisibility is not reported anywhere, so the cost is unknown. Which attributes buyers actually filter on is known to the search team and not to catalogue operations. And an incomplete listing looks the same as a complete one in the system.

## What a Fix Looks Like
Measure findability rather than completeness. Identify which attributes buyers filter on per category from the search logs, which is a query the platform can run today and which is the list that actually matters — completeness against every field is the wrong target and completeness against the filtered ones is the right one. Score every listing on findability against that list and report the distribution, which reveals a population of effectively invisible inventory. Infer the missing attributes from the photographs rather than leaving them blank, since size is frequently determinable from measurements, material from texture, and both are better estimated than absent. Estimate with a stated confidence and say so in the listing, since an approximate size shown as approximate is far better for the buyer than no size at all. Route genuinely undeterminable items for a measurement rather than listing them incomplete, which for high-value items is obviously worth doing. Alert when an item has been live with low impressions and a missing filtered attribute, which is the combination that identifies the invisible population. Report the sales impact of missing attributes, which is measurable by comparison and is the evidence for any of this. And stop treating field completeness as the metric, because the fields nobody filters on are not worth the labour.

## Who Feels the Pain
Sellers whose items were invisible for a blank field; buyers who never saw something they would have bought; and platforms disposing of inventory that failed on a catalogue defect rather than on demand.

## Impact If Fixed
Which attributes buyers filter on is a query the platform can run today, and completeness against that short list is the target rather than completeness against every field. Inferring an approximate size and labelling it as approximate is far better for the buyer than a blank that makes the item invisible.
