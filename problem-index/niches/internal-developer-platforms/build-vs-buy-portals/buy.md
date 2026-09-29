# Discovery Instead of Declaration

**Niche:** [[niches/internal-developer-platforms/build-vs-buy-portals/profile|Portals & Catalogues]]
**Industry:** [[industries/internal-developer-platforms|Internal Developer Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Configuration management databases learned decades ago that declared inventories decay and discovery-based ones do not, and the service catalogue was designed as a declared inventory.
**Tags:** #graph-theory #k-means-clustering #logistic-regression #descriptive-statistics #evaluation-metrics #confidence-intervals #data-integration #compliance
**Contested on:** Every serious competitor here is fighting to give an organisation a portal and catalogue that stays accurate without a team operating it — and whoever does that takes the decision, because operational cost and catalogue accuracy are the two reasons these deployments fail.

## The Problem
The configuration management database has a long history and a well-documented lesson: an inventory maintained by people declaring things decays immediately, and one populated by discovery stays current. The discipline responded by building discovery tooling, and the resulting products are mature. The service catalogue was designed a decade later as a declared inventory maintained in metadata files, and is decaying for the reason that was established before it was built.

## What Already Exists
Configuration management and discovery tooling with decades of development; network and cloud resource discovery; service dependency extraction from traffic, which is documented in the API infrastructure industry in this vault; code ownership mechanisms in repositories; identity directories; and reconciliation methodology for comparing discovered against declared.

## The Customization Gap
The adaptation is to services rather than to infrastructure assets. It requires: (1) the service as the unit rather than the host or the container, which means grouping discovered artefacts — repositories, deployments, running instances, endpoints — into the logical service a developer thinks about, and is the central modelling problem; (2) ownership inference from several weak signals, since no system authoritatively records which team owns a service and the answer is assembled from commit history, deployment identity, on-call rotation and directory structure; (3) reconciliation rather than replacement, because the declared catalogue contains genuine knowledge — intent, criticality, documentation — that discovery cannot produce, and the right design keeps both with provenance; (4) continuous operation, since the failure being fixed is decay and a discovery run performed once reproduces it; and (5) low integration burden, because the reason frameworks leave this as a plugin is that each organisation's systems differ, and a product requiring six bespoke integrations before it is useful will not be adopted.

## Target Customer
Portal and catalogue vendors, platform engineering teams, and the configuration management vendors for whom the service catalogue is an adjacent and younger market.

## Impact If Solved
The declared-inventory lesson was learned decades ago in an adjacent discipline and the service catalogue was designed without it. Grouping discovered artefacts into logical services is the modelling work, and keeping declaration alongside discovery with provenance is what preserves the knowledge discovery cannot produce.
