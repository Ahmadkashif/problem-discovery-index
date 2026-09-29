# A Portal Built on a Stale Catalogue

**Niche:** [[niches/internal-developer-platforms/build-vs-buy-portals/profile|Portals & Catalogues]]
**Industry:** [[industries/internal-developer-platforms|Internal Developer Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The portal is only as good as the catalogue underneath it, the catalogue is populated by asking people to maintain metadata files, and developers stop trusting a portal that shows them wrong answers twice.
**Tags:** #graph-theory #k-means-clustering #descriptive-statistics #logistic-regression #evaluation-metrics #confidence-intervals #data-integration #automation
**Contested on:** Every serious competitor here is fighting to give an organisation a portal and catalogue that stays accurate without a team operating it — and whoever does that takes the decision, because operational cost and catalogue accuracy are the two reasons these deployments fail.

## The Problem
A developer opens the portal to find who owns a service they need to change. The owner field names a team that was reorganised a year ago. They try another service and the documentation link is dead. They stop using the portal and ask in a chat channel instead, which is what everybody else does, and the portal — which took two engineers a year to stand up and takes one to operate — becomes an artefact that exists and is not consulted. The catalogue's staleness caused this and was inevitable, because it depends on several hundred developers maintaining metadata files about things they are not thinking about.

## Why Nobody Has Built This
The declaration model was the obvious design — ask each team to describe their services — and it fails for the same structural reason tagging fails in cloud cost management: the people who must maintain it get no benefit from maintaining it, and the decay is invisible until somebody relies on it. Deriving the catalogue from evidence requires integrating with the systems that actually know — deployment records, repositories, identity, infrastructure — which is per-organisation integration work that a framework prefers to leave as a plugin. And a stale catalogue still renders, which means the failure is silent.

## What to Build
Derive the catalogue rather than collecting it. Populate from the systems that know: repositories for code ownership, deployment records for what is running, cloud inventories for infrastructure, identity for team structure, and traffic for dependencies — which produces a catalogue that is accurate by construction and does not depend on anybody remembering. Resolve ownership by inference with confidence, as the cloud attribution niche describes, and route only the ambiguous minority to a human. Detect staleness actively: an owner who has left, a team that no longer exists, a documentation link that returns an error, a service that has not deployed in a year — each of which is checkable and none of which is checked. Show freshness on every field, since a portal that says how old its information is retains trust when it is wrong and loses it entirely when it is silent. Reconcile against what is actually running to find the services missing from the catalogue, which is the shadow inventory and is typically substantial. Let declaration override inference rather than replace it, so a team can correct the derived answer without being responsible for producing it. And measure portal usage, since a portal nobody opens is the outcome and nobody currently measures it.

## Target Customer
Platform teams operating or evaluating a portal, the portal framework and commercial vendors, and the architecture functions who need an accurate service inventory for their own reasons.

## Impact If Built
Catalogue staleness is the mechanism by which portals lose trust, and the declaration model guarantees it. Derivation from the systems that already know makes accuracy structural, and freshness indicators preserve trust in the residue that remains wrong.
