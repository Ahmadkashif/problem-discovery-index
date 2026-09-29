# The Same Custom Interface, Built Repeatedly

**Niche:** [[niches/data-labeling-services/annotation-tooling/profile|Annotation Tooling]]
**Industry:** [[industries/data-labeling-services|Data Labeling Services]]
**Type:** Fix (Pain Point)
**One-liner:** A vendor's solutions engineers have built the same comparison interface eleven times for eleven customers, each as a separate project, and none of them knows about the others.
**Tags:** #k-means-clustering #bert #descriptive-statistics #evaluation-metrics #confidence-intervals #quick-win #automation #worker-facing
**Contested on:** Every serious competitor in annotation tooling is fighting to support a genuinely new task type without a solutions engineer building an interface first — and whoever does that takes the in-house teams, because the bespoke build is the delay before any data exists.

## The Problem
Eleven customers have asked for a pairwise comparison task with a rationale field and a tie option. Eleven bespoke interfaces exist, built by different solutions engineers over three years, each in a customer's own project, differing in trivial ways. None was promoted into the product. The twelfth request will be quoted as three weeks. The vendor has, in effect, a library of common task types accumulated at considerable cost and stored as eleven separate one-off builds nobody can find.

## Why It's Still Broken
Solutions engineering work lives in the customer's project and there is no mechanism or incentive to promote it into the product — the engineer is measured on delivering the project, and the product team does not see what was built. The builds are also each slightly customised, which makes them look more different than they are and discourages generalisation. And the bespoke build is billed, which means the repetition is revenue rather than obviously waste.

## What a Fix Looks Like
Inventory the bespoke builds and promote the recurring ones. Catalogue what solutions engineering has built across customers, which is a straightforward exercise nobody has performed and which will reveal a small number of recurring shapes. Cluster them by task structure rather than by customer, which separates the genuinely novel from the near-identical and shows that most are variants of a handful of types. Promote the recurring shapes into the product as configurable task types, which converts three weeks into an afternoon for every subsequent customer. Establish a path from a bespoke build to the product, with somebody responsible, since its absence is the actual cause. Measure the bespoke build rate and its trend, since a rising one indicates the product is falling further behind the demand and is currently invisible as a metric. Let customers share task definitions with each other where they are willing, since the same evaluation task shapes recur across the industry and nobody benefits from eleven private versions. And report the time-to-first-label improvement from each promotion, which is the evidence that makes the next one happen.

## Who Feels the Pain
Customers quoted three weeks for something built ten times before; solutions engineers rebuilding the same interface; and vendors whose product falls further behind the demand while their services organisation absorbs the difference.

## Impact If Fixed
Cataloguing and clustering the bespoke builds is an afternoon's work and reveals that most are variants of a few shapes. Promoting those into the product converts the vendor's most common quoted delay into a configuration.
