# Service Catalogue Accuracy

**Parent Industry:** [[industries/internal-developer-platforms|Internal Developer Platforms]]
**Category:** Low Digitized
**Contested on:** Every serious competitor here is fighting to keep a service inventory correct without anybody maintaining it — and whoever does that takes the foundation of the category, because everything else depends on the catalogue and the catalogue depends on metadata nobody updates.

## Profile
**Market Size:** ~$340M US attributable to service inventory and metadata management
**Share of Parent Industry:** ~17% of category revenue
**Digital Adoption:** Low — populated by request and stale on the second day
**Target Buyer:** Platform and architecture functions, and increasingly security and compliance
**Automation Potential:** Very High — everything the catalogue records is observable elsewhere

## What Makes This a Distinct Niche
The service catalogue is the foundation everything else depends on, and it is populated by asking teams to fill in metadata files that are accurate on the day they are written and never again. The dependency is total: scorecards, ownership routing, dependency mapping, incident response, compliance evidence and the portal itself are all computed from it, so its inaccuracy propagates everywhere, silently, as confidently wrong answers. The failure is structurally identical to tagging in cloud cost management and to approved-component lists in open-source procurement — declared inventories maintained by people who get no benefit from maintaining them — and it has the same remedy. What makes it distinct here is that the catalogue's consumers now extend well beyond the platform team: security wants it for their asset inventory, compliance wants it for evidence, and incident response depends on it at the worst moment.

## Current Tools & Gaps
Metadata files in repositories, catalogue import mechanisms, and manual curation. The gaps: freshness is not tracked, so no field carries any indication of whether it is current; there is no reconciliation against reality, so services that exist and are absent from the catalogue are structurally invisible; the schema grows as consumers add fields, which increases the maintenance burden and therefore the decay; ownership and dependency, the two most consulted facts, are the two most volatile; and nobody measures the catalogue's own accuracy, so its reliability is assumed rather than known.

## Problems
- [[niches/internal-developer-platforms/service-catalogue-accuracy/build|🔨 Build: Accurate on the Day It Was Written]]
- [[niches/internal-developer-platforms/service-catalogue-accuracy/buy|🛒 Buy: Data Quality Practice for an Inventory]]
- [[niches/internal-developer-platforms/service-catalogue-accuracy/fix|🔧 Fix: The Schema That Grows Until Nobody Fills It In]]
