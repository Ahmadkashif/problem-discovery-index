# Delivering Data and Finding Data Are Different Businesses

**Niche:** [[niches/data-marketplace-brokers/data-distribution-platforms/profile|Data Distribution Platforms]]
**Industry:** [[industries/data-marketplace-brokers|Data Marketplace Brokers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Cloud platforms compete on how cleanly data arrives and specialist brokers compete on whether the right data can be found at all, and each is weak at the other's problem.
**Tags:** #data-integration #graph-theory #evaluation-metrics #compliance #workflow-orchestration #automation #descriptive-statistics #revenue-impact
**Contested on:** Not terminal — the contest differs by whether the platform is delivering data or finding it, and the decomposition is recorded in the profile.

## The Problem
A buyer needs commercial property transaction data for three specific metropolitan areas with a particular field they are not sure anybody collects. Their cloud platform's marketplace shows four listings, none matching, because the providers who hold that data are regional firms with no cloud presence. Meanwhile a specialist broker finds two suitable suppliers in a week and then spends a month on delivery, because moving the data into the buyer's environment with the right entitlements is work the broker does by hand every time. Each party is excellent at exactly the half of the problem the other has solved.

## Why Nobody Has Built This
Cloud platforms' advantage is their own ecosystem, and extending to providers outside it undermines the gravity that makes the marketplace strategic. Brokers are relationship and knowledge businesses whose economics do not support building delivery infrastructure. The two sides sell to different buyers through different motions. And the obvious combination — a broker's supply coverage with a platform's delivery — requires a partnership neither side's incentives favour.

## What to Build
Build the connective layer both sides lack. The genuinely common requirement is a description of a dataset rich enough to search on and precise enough to contract on: entity types, attribute definitions, coverage claims, freshness, provenance and permitted use, in a structured form rather than a marketing paragraph — which is the missing artefact in both businesses and the reason discovery is bad everywhere. Standardise it and make it machine-readable, so a requirement can be matched against supply automatically rather than by a person reading listings. Make delivery pluggable across platforms and out to providers with no cloud presence, since the supply that matters is frequently outside any ecosystem and the buyer's platform preference is not the provider's problem to solve. Carry entitlement and permitted-use terms as structured data through the delivery path, which the licence enforcement niche develops and which neither side does. Support trial and evaluation flows as first-class, since the evaluation problem is the market's largest and neither business is built to accommodate it. Attach outcome tracking to each transaction, which the outcome intelligence niche develops. And be explicit about which business a given platform is in, because a cloud marketplace pretending to be a broker and a broker pretending to be infrastructure both disappoint.

## Target Customer
Cloud data platforms, specialist brokers, and the buyers currently choosing between good delivery and good discovery.

## Impact If Built
A structured, contractable dataset description is the artefact both businesses lack and is why discovery is poor everywhere. Delivery that reaches providers with no cloud presence is what connects the supply that matters to the buyers who cannot currently find it.
