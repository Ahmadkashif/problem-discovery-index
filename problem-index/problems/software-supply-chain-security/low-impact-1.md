# Malicious Package Detection

**Industry:** [[software-supply-chain-security|Software Supply Chain Security]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every registry and scanner now checks for malicious packages, and the attack has moved from exploiting vulnerable dependencies to publishing poisoned ones — which is an adversarial problem that signature matching loses.
**Tags:** #gradient-boosting #graph-neural-networks #bert #dbscan #change-point-detection #confidence-intervals #evaluation-metrics #compliance

## The Problem
The supply chain attack has changed shape. Rather than waiting for a vulnerability in a legitimate dependency, attackers publish malicious code directly: typosquatted package names, dependency confusion against internal package names, compromised maintainer accounts pushing a poisoned version of a trusted library, or a legitimate package acquired and then weaponised.

Detection is genuinely adversarial. Malicious code is deliberately obfuscated, frequently executes only in specific conditions, and often lives in install scripts rather than in the library's own code. Attackers test against public scanners before publishing.

The behaviours that indicate malice are recognisable in principle — network calls during installation, reading credential files and environment variables, obfuscated payloads, code that activates only outside a test environment — and are also present in some legitimate packages, which makes the false positive cost real: blocking a widely used package breaks builds across an ecosystem.

The most dangerous case is the compromised legitimate package, because it carries reputation, download history and existing trust, and it is precisely where reputation-based signals fail.

## What Already Exists
Registries have added scanning and takedown processes and respond faster than they used to. Vendors (Socket, Phylum, and the incumbents) analyse package behaviour rather than only known vulnerabilities. Sigstore provides signing and provenance attestation where adopted. Dependency confusion is mitigated by registry scoping where configured correctly. Typosquatting detection by name similarity is standard. Security researchers publish attack analyses quickly.

## The Customisation Gap
Behavioural analysis at publication is stronger than name matching and remains shallow — most implementations look for a set of known-bad patterns, which is exactly what an attacker tests against.

Maintainer compromise detection is the most valuable gap and the least served. A legitimate package's publishing behaviour is stable over years — same maintainer, same release cadence, same build environment, consistent code style — and a compromise produces a discontinuity in several of those simultaneously. That is change detection on a well-observed series and it is what would catch the attacks that reputation cannot.

Relational modelling across the ecosystem is the second gap. Attack campaigns publish many packages sharing infrastructure, timing, code fragments and account characteristics, and modelling the graph catches what per-package analysis misses.

Update timing is a practical mitigation nobody productises: most malicious packages are removed within days, so a policy of delaying adoption of brand-new versions for non-urgent dependencies eliminates a large share of exposure at almost no cost.

## Impact If Solved
Malicious packages are the fastest-growing supply chain attack vector and reach production through the same trusted channel as everything else. Publishing-behaviour discontinuity detection is the specific capability that would catch maintainer compromise, which is both the most dangerous case and the one that defeats every reputation-based defence.
