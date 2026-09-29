# Downstream Impact Tracing

**Parent Industry:** [[industries/customer-data-platforms|Customer Data Platforms]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in this niche is fighting to say what breaks when something changes, before it changes — and whoever builds that lineage across the customer data stack makes every other failure in the category preventable.

## Profile
**Market Size:** ~$500M US
**Share of Parent Industry:** ~10% of category revenue
**Digital Adoption:** Low — nobody traces past the warehouse
**Target Buyer:** Data platform and analytics leadership
**Automation Potential:** Very High — lineage is derivable from definitions

## What Makes This a Distinct Niche
Almost every failure in this category shares a shape: something upstream changed, and nobody knew what depended on it. An event renamed, a field's meaning drifted, a warehouse model refactored, a segment edited, a threshold moved — in each case the consequences were discovered downstream, weeks later, by someone looking at a number. The dependency information exists in the definitions the platform stores, and nobody assembles it into a graph that spans from an event to a campaign. This is a single automatable capability that makes the other failures preventable, which is what makes it a niche rather than a feature.

## Current Tools & Gaps
Warehouse lineage tools that stop at the analytics layer, platform-internal dependency views of varying completeness, and manual investigation. The gaps: lineage that does not span the customer data stack; activations and campaigns outside every dependency graph; no impact preview before a change; no ownership attached to a dependency; and investigation after the fact as the only mode.

## Problems
- [[niches/customer-data-platforms/downstream-impact-tracing/build|🔨 Build: Nobody Knew What Depended on It]]
- [[niches/customer-data-platforms/downstream-impact-tracing/buy|🛒 Buy: Data Lineage Practice]]
- [[niches/customer-data-platforms/downstream-impact-tracing/fix|🔧 Fix: The Change Nobody Could Assess]]
