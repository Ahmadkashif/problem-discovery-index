# Event Monitoring Adapted to Site-Level Attribution

**Niche:** [[niches/contract-manufacturing/supply-chain-risk-intelligence/profile|Multi-Tier Supply Chain Risk Intelligence]]
**Industry:** [[industries/contract-manufacturing|Contract Manufacturing]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** News and event monitoring products find the fire; deciding whether the burning building is the plant that makes a client's connector is the part nobody sells.
**Tags:** #bert #transformers #large-language-models #graph-neural-networks #word-embeddings #contrastive-learning #evaluation-metrics #transfer-learning #automation #data-integration

## The Problem
Disruption monitoring means watching an enormous stream — news in dozens of languages, regulatory actions, port and weather data, financial filings, labour disputes — for events that affect a client's specific supply chain. The stream is easy to acquire and nearly useless without attribution: an event matters only if it hits a site that makes something a client depends on, and establishing that requires resolving a place name in a local-language news report to a specific facility in the map, then tracing that facility's downstream path to a client part. Analysts do the attribution, which is why alert latency is measured in hours rather than minutes and why coverage thins outside major languages and regions.

## What Already Exists
Event and news monitoring is a crowded market. Dataminr, Factiva, and the OSINT platforms deliver real-time multilingual event detection with geolocation and entity extraction; the risk intelligence aggregators bundle weather, port, and geopolitical feeds. Named entity recognition and geocoding are commodity capabilities.

## The Customization Gap
All of these resolve events to companies and places. The operative entity here is a facility — a specific plant with a specific address making specific things — and company-level attribution is far too coarse, because a supplier with forty sites is unaffected by a fire at one of them unless that one makes the part in question. Local reporting rarely names the company at all; it names a district, an industrial park, or a landmark. So the adaptation is facility resolution: a site registry with addresses, coordinates, aliases in local scripts, and the parts and processes each site is known to perform, with events matched against it geospatially and linguistically rather than by company name. On top of that, propagation through the supply graph to determine which clients and which parts are actually exposed, with severity estimated from the site's role and available alternatives rather than from the drama of the headline. And confidence must be explicit, because a false alert that triggers a sourcing scramble costs a client real money and is the fastest way to lose their trust in the product.

## Target Customer
Heads of intelligence operations and product at supply chain risk vendors, and the risk managers at manufacturers who currently receive alerts they must themselves assess for relevance.

## Impact If Solved
Cuts alert latency and, more importantly, cuts false positives — which is what determines whether a client acts on alerts or learns to ignore them. Facility-level resolution also extends coverage into the regions and languages where local reporting is the only source, which is precisely where sub-tier suppliers concentrate.
