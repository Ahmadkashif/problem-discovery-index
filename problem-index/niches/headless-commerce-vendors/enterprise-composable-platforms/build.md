# A Data Model Whose Limits Appear in Year Two

**Niche:** [[niches/headless-commerce-vendors/enterprise-composable-platforms/profile|Enterprise Composable Platforms]]
**Industry:** [[industries/headless-commerce-vendors|Headless Commerce Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A retailer selects a platform on a demonstration and a reference architecture, and discovers what its data model cannot express eighteen months into a replatform they cannot abandon.
**Tags:** #data-integration #graph-theory #evaluation-metrics #compliance #workflow-orchestration #confidence-intervals #descriptive-statistics #automation
**Contested on:** Every serious competitor in this sub-niche is fighting to be the commerce core a large retailer can build twelve business units and fifteen markets on for a decade — and whoever does that takes the licence, because the buyer is choosing what they will be unable to leave.

## The Problem
A retailer with trade and consumer channels, franchise partners, market-specific bundles and a loyalty scheme that predates the internet selects a platform after a six-month evaluation of demonstrations, reference architectures and analyst reports. Eighteen months into the programme they find that the platform's product model cannot represent a bundle whose components price differently by channel, and the workaround is a service that intercepts pricing. Three more such discoveries follow. The evaluation tested whether the platform could do the things everybody does and never tested the things this organisation specifically does, which are the only ones that matter.

## Why Nobody Has Built This
The evaluation is designed by procurement around feature comparison, which tests common capability. The genuinely hard requirements are known to the retailer's own architects and are not expressed in a form a vendor can be tested against. The vendor's answer to a hard requirement is that it is extensible, which is true and defers the discovery. And the discovery happens after the contract, when the cost of being wrong is highest and the willingness to admit it lowest.

## What to Build
Test the model against the organisation before the contract. Build a structured modelling exercise into the evaluation: the retailer's ten hardest real scenarios expressed against the platform's data model by the vendor's own architects, with the result inspected — which is a fortnight of work and replaces a demonstration with evidence, and is the change that would prevent most of the failures in this category. Publish the model's limits explicitly, since every model has them and a vendor who names them is trusted on everything else. Provide a migration mapping from the common legacy platforms, which is the buyer's largest unknown and which vendors leave to integrators. Model the multi-dimensional cases the enterprise buyer actually has — channel, market, brand, customer type, contract — as first-class rather than as attributes, since the workarounds always originate there. Report what existing customers extended and why, which the platform layer's fix note develops and which is the most honest possible answer to what the model cannot do. Design for a decade of change, since the requirement that breaks the model is usually one that did not exist at selection. Make exit possible and say so, because a buyer told they can leave trusts the vendor more and the commitment costs little to a vendor confident in their product. And measure implementations by how much extension they required, which is the outcome metric this business should be judged on.

## Target Customer
Architecture committees at large retailers, the integrators delivering the programmes, and the vendors whose evaluations do not test what matters.

## Impact If Built
The evaluation tests what everybody does and the failures come from what this organisation specifically does. A structured modelling exercise against the retailer's ten hardest scenarios is a fortnight of work that replaces a demonstration with evidence.
