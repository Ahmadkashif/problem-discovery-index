# Scanning & Analysis

**Parent Industry:** [[industries/software-supply-chain-security|Software Supply Chain Security]]
**Category:** High Market Share
**Contested on:** Every serious competitor here is fighting to say something about an artefact that the commoditised scan cannot — and that contest is a program analysis problem in one market and an attestation problem in the other, which is why this niche is not terminal and is decomposed below.

## Profile
**Market Size:** ~$1.1B US composition analysis, artefact scanning and integrity tooling
**Share of Parent Industry:** ~37% of category revenue
**Digital Adoption:** Very High — scanning is universal
**Target Buyer:** Application security; separately, platform and compliance functions
**Automation Potential:** High, and the differentiating analysis is where the remaining work is

## What Makes This a Distinct Niche
Scanning is the category's largest commercial block and its most commoditised capability. Identifying which components are present and matching them against a vulnerability database is solved, available from several vendors and from the code hosting platforms at no additional cost, and nobody wins a deal on it. The competition has therefore moved above it, in two directions that have nothing to do with each other.

The filter fails here. "Scanning and analysis" names a mature capability rather than a contest. Reachability and exploitability is a program analysis problem: does this vulnerability actually apply to this application, given its code and configuration — bought by application security to reduce a queue, contested against other analysis vendors. Artefact provenance and integrity is an attestation problem: is what is running what was built from what was reviewed — bought by platform and compliance functions under regulatory pressure, contested against a different set of vendors and against open signing infrastructure. Decomposed below.

## Current Tools & Gaps
Composition analysis from several vendors and from the hosting platforms, container image scanning, reachability analysis of varying rigour, and signing and attestation infrastructure. The gaps: the commodity layer is still the basis of most pricing, which prices the thing nobody competes on; the vulnerability database's known limitations — incomplete coverage, inconsistent metadata, version range imprecision — are widely acknowledged and universally inherited; findings are regenerated nightly with no memory of prior assessment; and the two contests above the commodity layer are served by one product with a shared interface, which fits neither well.

## Problems
- [[niches/software-supply-chain-security/scanning-and-analysis/build|🔨 Build: Commoditised Below, Contested Above]]
- [[niches/software-supply-chain-security/scanning-and-analysis/buy|🛒 Buy: The Vulnerability Database Everyone Inherits]]
- [[niches/software-supply-chain-security/scanning-and-analysis/fix|🔧 Fix: A Scan With No Memory]]
