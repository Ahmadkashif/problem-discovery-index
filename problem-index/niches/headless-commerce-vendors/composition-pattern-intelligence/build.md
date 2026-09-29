# Hundreds of Implementations, No Learning

**Niche:** [[niches/headless-commerce-vendors/composition-pattern-intelligence/profile|Composition Pattern Intelligence]]
**Industry:** [[industries/headless-commerce-vendors|Headless Commerce Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A vendor sees hundreds of compositions of their platform with the resulting performance, incidents, extension footprint and upgrade behaviour, and publishes a reference architecture written from opinion.
**Tags:** #graph-theory #gradient-boosting #evaluation-metrics #confidence-intervals #causal-inference #descriptive-statistics #k-means-clustering #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to turn hundreds of implementations into an empirical account of which compositions work — and whoever does that advises better than anybody, because every architect in the category is currently designing from anecdote.

## The Problem
An architect asks whether putting personalisation in the critical path of the product page is a good idea. The vendor's answer is a reference architecture and an opinion. The actual answer is in the vendor's own telemetry: of the implementations that did it, what happened to page latency, conversion and incident rate compared to those that did not. The same applies to where inventory state lives, whether search should own the catalogue, how promotions should be evaluated, and every other composition decision. Hundreds of natural experiments have been run and the results are distributed across account teams as impressions.

## Why Nobody Has Built This
Characterising an implementation's composition in a comparable form requires deliberate capture that nobody set up. Outcomes live in support systems, account records and the customer's own analytics. Vendors are reluctant to publish findings that reflect on partner or complementary vendor components. And the knowledge is held by solutions architects who move between firms, which makes it feel like individual expertise rather than a company asset.

## What to Build
Characterise the implementations and analyse the outcomes. Record each implementation's composition in a structured form — which services, which boundaries, where state lives, which extensions, which consistency choices — which is a capture exercise at onboarding and review time and is the precondition for everything. Join it to outcomes: page performance, incident rate and type, extension footprint, upgrade currency, time to go live, and retention. Analyse which composition choices predict which outcomes, controlling for retailer size and complexity, which is an observational study on an unusually clean set of natural experiments and is the build. Derive the reference architecture from the evidence rather than from opinion, which the fix note develops. Publish findings that are safely publishable, since a vendor whose guidance is evidenced becomes the category's reference. Feed the analysis into the architect's sandbox and the pattern library, so the evidence reaches the design decision. Feed it into the roadmap, since a composition pattern that reliably causes incidents is frequently a product gap. Share aggregate findings with customers, which is genuinely useful to them and is a differentiator. And keep the analysis current, since the service landscape changes and a finding from three years ago describes a different set of vendors.

## Target Customer
Platform vendors, systems integrators, architecture functions at retailers, and the architects designing the next composition from anecdote.

## Impact If Built
Hundreds of natural experiments have been run and the results are distributed across account teams as impressions. Structured composition capture joined to outcomes turns a reference architecture from opinion into evidence, and it is a position no competitor can occupy without the same implementations.
