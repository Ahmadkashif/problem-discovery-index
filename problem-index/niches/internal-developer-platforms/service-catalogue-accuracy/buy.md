# Data Quality Practice for an Inventory

**Niche:** [[niches/internal-developer-platforms/service-catalogue-accuracy/profile|Service Catalogue Accuracy]]
**Industry:** [[industries/internal-developer-platforms|Internal Developer Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Data quality has a developed practice — completeness, accuracy, freshness, consistency, with monitoring and remediation — and the service catalogue has none of it applied to it.
**Tags:** #descriptive-statistics #change-point-detection #logistic-regression #evaluation-metrics #confidence-intervals #hypothesis-testing #data-integration #compliance
**Contested on:** Every serious competitor here is fighting to keep a service inventory correct without anybody maintaining it — and whoever does that takes the foundation of the category, because everything else depends on the catalogue and the catalogue depends on metadata nobody updates.

## The Problem
Data quality management is a mature discipline with defined dimensions — completeness, accuracy, timeliness, consistency, validity — monitoring frameworks, and remediation workflows. It is applied to customer records, product data and financial data as a matter of routine. The service catalogue, which is a dataset with all the same problems and more consumers than most master data, has no quality measurement of any kind.

## What Already Exists
Data quality frameworks with defined dimensions and measurement methodology; data observability products that monitor freshness, volume and distribution; master data management practice, including the survivorship rules for reconciling conflicting sources; expectation-based validation frameworks; and reconciliation methodology.

## The Customization Gap
The adaptation is to an inventory whose ground truth is a running system. It requires: (1) reconciliation against observed reality as the accuracy measure, since unlike customer data there is an authoritative external check — the services that are actually running — and accuracy can therefore be measured rather than estimated; (2) per-field freshness with different expectations, because ownership changes often and purpose rarely, and a single staleness threshold is wrong for both; (3) survivorship rules across derived and declared sources, since a derived owner and a declared owner will conflict and the resolution must be principled and visible rather than arbitrary; (4) consumer-specific quality reporting, because security cares about data classification completeness and incident response cares about ownership accuracy, and a single quality score serves neither; and (5) remediation routed to whoever can actually fix it, which for derived fields is a systems integration and for declared fields is a person, and conflating the two produces requests nobody can action.

## Target Customer
Catalogue and portal vendors, platform engineering teams, and the data quality and observability vendors for whom this is an adjacent dataset.

## Impact If Solved
A mature quality discipline is unapplied to a dataset with more consumers than most master data. The availability of an authoritative external check makes accuracy measurable here in a way it rarely is elsewhere, which is an unusual advantage nobody uses.
