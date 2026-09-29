# Accurate on the Day It Was Written

**Niche:** [[niches/internal-developer-platforms/service-catalogue-accuracy/profile|Service Catalogue Accuracy]]
**Industry:** [[industries/internal-developer-platforms|Internal Developer Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The service catalogue is the foundation everything else depends on, and it is populated by asking teams to fill in metadata files that are accurate on the day they are written and never again.
**Tags:** #graph-theory #k-means-clustering #logistic-regression #descriptive-statistics #evaluation-metrics #confidence-intervals #data-integration #compliance
**Contested on:** Every serious competitor here is fighting to keep a service inventory correct without anybody maintaining it — and whoever does that takes the foundation of the category, because everything else depends on the catalogue and the catalogue depends on metadata nobody updates.

## The Problem
A security review asks which services process payment data. The catalogue has a field for it, populated when each service was registered. Several services have changed what they do since; two that now handle payment data were registered before they did and say otherwise; four services that exist are not in the catalogue at all because they were created by a team that never onboarded. The answer produced from the catalogue is confidently wrong in both directions, and the review proceeds on it because it is the only inventory that exists.

## Why Nobody Has Built This
The catalogue was designed as a declaration because that is the obvious design and because the alternative — deriving it — requires integrating with a dozen systems that vary per organisation. Maintenance has no benefit to the maintainer, which guarantees decay, and the decay is invisible because a stale entry renders identically to a current one. The schema also grows as each new consumer adds a field, which increases the burden and accelerates the decay, and nobody owns the trade-off. And no catalogue reports its own accuracy, so the problem has no metric.

## What to Build
Derive, reconcile and report freshness. Populate from the systems of record — repositories, deployment records, cloud inventories, identity, traffic — so that the volatile facts are computed rather than declared, which is the same inversion the portal sub-niche describes and is the structural fix. Reconcile against what is actually running to find the services the catalogue does not know about, which is the shadow inventory and is the finding security and compliance most need. Track freshness per field with its provenance, so every answer carries how it was obtained and when, which preserves trust in an imperfect catalogue and is the single cheapest improvement. Validate the declared fields that cannot be derived — data classification, criticality, purpose — by prompting the owner at moments when they are already engaged, such as a deployment or an incident, rather than by a periodic request nobody answers. Detect contradictions between declared and observed, since a service declaring it handles no personal data while its traffic suggests otherwise is a specific and important finding. Report the catalogue's accuracy as a metric, which is what lets a platform team manage it and what tells its consumers how much to rely on it. And expose the catalogue to its non-platform consumers deliberately, since security, compliance and incident response now depend on it and are not the audience it was designed for.

## Target Customer
Platform and architecture functions, security and compliance teams who depend on the inventory, and the catalogue and portal vendors.

## Impact If Built
Every capability in the category is computed from a catalogue that decays by construction, and the decay is invisible. Derivation for the volatile fields and freshness provenance on all of them together convert a confidently wrong inventory into one whose reliability is stated.
