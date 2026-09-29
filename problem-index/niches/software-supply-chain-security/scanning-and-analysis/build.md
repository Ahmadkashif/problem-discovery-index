# Commoditised Below, Contested Above

**Niche:** [[niches/software-supply-chain-security/scanning-and-analysis/profile|Scanning & Analysis]]
**Industry:** [[industries/software-supply-chain-security|Software Supply Chain Security]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Identifying components and matching them against a vulnerability database is free and universal, and most of the category's pricing still rests on it.
**Tags:** #graph-theory #bert #descriptive-statistics #evaluation-metrics #confidence-intervals #compliance #automation #data-integration
**Contested on:** Every serious competitor here is fighting to say something about an artefact that the commoditised scan cannot — and that contest is a program analysis problem in one market and an attestation problem in the other, which is why this niche is not terminal and is decomposed below.

## The Problem
An organisation evaluates three composition analysis products. All three enumerate the same dependencies from the same manifests, match against substantially the same database, and produce similar findings with similar severity ratings. The hosting platform does the same thing for nothing. The evaluation therefore turns on interface, integration and price, and the capability that would differentiate — telling this organisation which findings matter for their application, or attesting that what is running is what was built — is either a premium tier or a different product.

## Why Nobody Has Built This
The commodity layer was genuinely hard when the category formed and became the product, and pricing and packaging followed. The two capabilities above it require different investments — program analysis in one direction, cryptographic attestation and build system integration in the other — and vendors have added both to one product because the buyer relationship is shared, which produces a suite that is adequate at each and excellent at neither. And the free alternative from the hosting platforms has compressed the commodity layer's value faster than the vendors have repriced.

## What to Build
The shared foundation both sub-niches need, and honesty about what is commodity. Build the artefact model properly: a complete, accurate, version-precise inventory of what is in a build including transitive and vendored dependencies, which is the commodity layer done well and is more than the commodity layer done cheaply — the free tools are adequate on the common cases and miss vendored code, dynamically loaded components and multi-language builds. Correct for the database's known limitations rather than inheriting them, as the buy note describes. Retain assessment state across scans, which is the memory the fix note addresses and which every sub-niche needs. Establish identity for components across ecosystems and naming conventions, since the same library appears differently in different manifests and the mismatches produce both missed findings and false ones. Then build the two contested capabilities properly on that foundation rather than as features of a scanner, since they are different products serving different buyers. And price the commodity layer as commodity, because a customer paying premium rates for something available free will eventually notice.

## Target Customer
Composition analysis vendors facing a commoditised core, and the security and platform functions who would like to buy the capability above it rather than the one below.

## Impact If Built
The commodity layer is free and is still the basis of most pricing, which is a market repricing that has not happened. A precise artefact model, database correction and persistent assessment state are the shared foundation both live contests depend on.
