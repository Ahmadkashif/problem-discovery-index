# The Endpoint Nobody Knew Was There

**Niche:** [[niches/api-infrastructure-providers/api-security-shadow-endpoints/profile|API Security & Shadow Endpoints]]
**Industry:** [[industries/api-infrastructure-providers|API Infrastructure Providers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every API security control protects the endpoints the organisation knows about, and the incidents keep happening on the ones it does not.
**Tags:** #graph-theory #k-means-clustering #bert #logistic-regression #evaluation-metrics #confidence-intervals #compliance #data-integration
**Contested on:** Every serious competitor here is fighting to produce a complete inventory of an organisation's exposed endpoints and what each one does with sensitive data — and whoever does that takes the security account, because nobody can currently produce the list.

## The Problem
A security team maintains a register of ninety APIs with their owners, data classifications and controls. The actual number of reachable endpoints is several hundred: an internal service exposed through a load balancer rule added during an incident two years ago, three versions of a customer API that were superseded and not removed, an acquired company's estate that was network-joined and never inventoried, and a debugging endpoint on a service whose author has left. The register is accurate about the ninety. The next incident will involve one of the others, which is what the published record of API breaches consistently shows.

## Why Nobody Has Built This
Discovery products mostly observe traffic at the gateway, which by construction cannot see endpoints that do not pass through it — and those are precisely the ones at risk. Complete discovery requires correlating several vantage points: network observation, load balancer and DNS configuration, cloud resource inventory, code and specification analysis, and external scanning. Nobody owns the correlation. And an honest inventory produces a large number of newly discovered exposures, which creates work for the team that commissioned it, so the incentive to look hard is weaker than it should be.

## What to Build
Discovery from several vantage points, reconciled. Observe traffic wherever it can be observed — gateway, mesh, load balancer, network flow logs — and combine with configuration evidence: routing rules, DNS records, cloud resource inventory, certificate transparency for external names. Analyse code and specifications to find routes that exist and are undocumented, since the gap between what is defined and what is registered is a large part of the answer. Scan externally to establish what is reachable from outside, which is the definitive test for the exposure that matters most. Reconcile all of it into one inventory with provenance per endpoint, so the security team can see which evidence found it and which sources missed it — the misses being informative in themselves. Classify each endpoint by the data it handles, inferred from observed payload structure rather than from a declaration, since data classification is the question compliance actually asks and declarations are unreliable. Then diff continuously and alert on new exposure, because the inventory's value is in staying current rather than in being produced once.

## Target Customer
Security functions and platform engineering at organisations with large or acquired estates, API security vendors, and attack surface management vendors for whom this is the layer below their current product.

## Impact If Built
Every control depends on an inventory nobody can produce, and the endpoints outside it are where the incidents happen. Multi-vantage reconciliation is what makes the inventory complete rather than merely large, and payload-derived data classification answers the compliance question directly.
