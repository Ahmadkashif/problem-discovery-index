# A Surface Built to Help a Stranger Discover

**Niche:** [[niches/b2b-commerce-platforms/b2b-storefront-experience/profile|B2B Storefront Experience]]
**Industry:** [[industries/b2b-commerce-platforms|B2B Commerce Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** B2B storefronts inherited an architecture built to help a stranger discover a product, and both of their actual buyers — the repeat reorderer and the part searcher — need something else entirely.
**Tags:** #worker-facing #evaluation-metrics #data-integration #workflow-orchestration #automation #descriptive-statistics #graph-theory #revenue-impact
**Contested on:** Not terminal — the contest differs by whether the buyer already knows what they want, and the decomposition is recorded in the profile.

## The Problem
A maintenance buyer opens the storefront to reorder eleven items they buy monthly. They are shown a homepage with featured categories, a promotional banner and a recommendation carousel. Their order history is three clicks away, their requisition list is in a menu, and the search box is optimised for relevance ranking over a catalogue where they need one exact part. Meanwhile a technician searching for a cross-reference to a competitor's part number gets keyword matches on the description. The surface is organised around discovery for a visitor who does not exist in this business, and both of the buyers who do exist work around it.

## Why Nobody Has Built This
The platforms are consumer commerce products with business capability added, and the information architecture came with them. Merchandising features are what platform vendors build because that is their product tradition. The buyers who work around it place orders anyway, through the rep or the procurement system, so the revenue arrives and the surface's failure is invisible. And nobody has segmented the traffic by buyer intent to see how little of it is discovery.

## What to Build
Build the shared foundations and let the two experiences diverge. What genuinely serves both is the account context — who this buyer is, which entity they buy for, their entitlement, their approval rules, their delivery locations, their purchase history — carried into every surface, which the consumer architecture treats as a profile and which here is the primary key to everything. Make the entry point the buyer's own context rather than a merchandised homepage, since neither buyer is browsing and both start from something they already know. Model the buying organisation properly — multiple entities, locations, cost centres, approvers, budgets — since a consumer account model cannot express it and every B2B implementation extends it awkwardly. Carry approval workflow as a first-class part of the purchase rather than as a bolt-on, because an order that needs approval is the normal case and not an exception. Segment traffic by intent and report it, so the organisation can see how much of their storefront's design serves an audience that is not there. Support the buyer's own identifiers — their part numbers, their cost centres, their requisition references — since they order in their vocabulary and the platform insists on its own. Remove the merchandising that serves neither, which the fix note develops. And design both experiences from observation of the two buyers rather than from consumer patterns.

## Target Customer
Distributors and manufacturers running B2B storefronts, platform vendors, and the buyers working around the surface.

## Impact If Built
The surface is organised around a discovering visitor who does not exist in this business, and both real buyers work around it. Account context as the primary key rather than as a profile, and the buyer's own identifiers rather than the platform's, are the foundations both experiences need.
