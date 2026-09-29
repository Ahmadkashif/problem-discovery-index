# Pricing a Person the System Cannot Recognise

**Niche:** [[niches/programmatic-ad-platforms/identity-and-addressability/profile|Identity & Addressability]]
**Industry:** [[industries/programmatic-ad-platforms|Programmatic Ad Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every model in the stack is defined in terms of a person, and the industry can no longer reliably tell whether two impressions reached the same one.
**Tags:** #graph-theory #bayesian-inference #confidence-intervals #evaluation-metrics #compliance #dimensionality-reduction #revenue-impact #transfer-learning
**Contested on:** This niche is not terminal — assembling a legitimate deterministic graph and performing well with no identifier at all are different contests with different winners, and they are stated separately in the sub-niches.

## The Problem
Frequency capping assumes you can recognise a person. So do reach measurement, audience targeting, suppression lists, sequential messaging, incrementality holdouts and every attribution model in use. The identifier that made all of it work is disappearing across browsers and platforms, and what replaced it is a set of partially overlapping, partially adopted, mutually incompatible alternatives with no shared coverage. The models were not rewritten. They still assume a person, they are fed something that is sometimes a person and sometimes a device and sometimes a household and sometimes nothing, and the numbers they produce are presented without qualification.

## Why Nobody Has Built This
The industry treated deprecation as a replacement problem — find a new identifier and continue — rather than as a modelling problem, which is why the effort went into competing identifiers instead of into systems that degrade honestly. Every alternative graph is a commercial asset whose owner has no reason to make it interoperable. Reporting coverage honestly makes a platform look worse than one that does not. And the assumption is buried so deeply in the stack that removing it is a rewrite rather than a feature.

## What to Build
Build a stack that works with partial identity and says so. Represent identity as a probabilistic assertion with a confidence and a provenance, rather than as a key, which is the foundational change — every downstream problem follows from treating an uncertain match as a certainty. Carry consent and permitted-use with the identifier, since an identifier that cannot state what it may be used for is a liability in a regulated market and this is where the partnership contest is actually decided. Make the models degrade explicitly: frequency, reach and suppression should all report what they know and what they are inferring, which is the sub-niches' shared requirement. Bridge across graphs rather than betting on one, because no single identifier will reach majority adoption and the interoperability layer is the durable position. Estimate reach and frequency statistically where identity is partial, which is a measurement discipline with a real literature and is the honest replacement for a count. Treat the no-identifier case as a first-class regime rather than a fallback, since it is the majority of inventory and is the second sub-niche's contest. Price the difference between addressable and unaddressable inventory properly, which the market currently does by reflex rather than by evidence. Handle household and shared-device ambiguity, which connected television has made central and which device-level thinking handles badly. Report addressable coverage to advertisers plainly, because an unqualified reach number over partial identity is not a measurement. And evaluate on outcomes rather than on match rates, since match rate has become a vanity metric optimised directly.

## Target Customer
Demand and supply-side platforms, identity providers and publishers, and advertisers whose reach and frequency numbers no longer mean what they say.

## Impact If Built
The stack assumes a person it can no longer recognise, and deprecation was treated as a replacement problem rather than a modelling one. Representing identity as a probabilistic assertion with consent and provenance attached is the change every other fix in the niche depends on.
