# Semantic Versioning Treated as a Guarantee

**Niche:** [[niches/software-supply-chain-security/remediation-and-upgrade-risk/profile|Remediation & Upgrade Risk]]
**Industry:** [[industries/software-supply-chain-security|Software Supply Chain Security]]
**Type:** Fix (Pain Point)
**One-liner:** Automated updates apply patch and minor releases on the assumption that they are compatible, the convention is violated regularly, and the resulting breakages teach teams to disable automatic updates entirely.
**Tags:** #descriptive-statistics #logistic-regression #hypothesis-testing #confidence-intervals #evaluation-metrics #quick-win #automation #cross-validation
**Contested on:** Every serious competitor here is fighting to tell a team what an upgrade will break before they attempt it — and whoever does that takes the remediation rate, because uncertainty about breakage is why findings age rather than unwillingness to fix them.

## The Problem
A team enables automatic patch and minor updates on the reasonable basis that the versioning convention promises compatibility. A patch release changes a default and breaks their service in production. They disable automatic updates, which means the next security patch arrives by ticket and takes six weeks instead of a day, and their overall exposure increases substantially because of one violated convention. The convention's actual reliability is measurable — the upgrade corpus contains every project that broke on that release — and is treated as a guarantee rather than as a probability.

## Why It's Still Broken
Semantic versioning is a social convention presented as a technical contract, and the tooling treats the declared version increment as authoritative because it has nothing better. Violation rates are measurable per library and per maintainer from public evidence and are measured by nobody. The consequence of one bad experience is disproportionate — teams disable the whole mechanism — which is rational given that they have no way to distinguish a reliable library from an unreliable one.

## What a Fix Looks Like
Treat the convention as evidence rather than as a promise. Measure per-library versioning reliability from the public record: how often a patch or minor release from this library has broken consumers, which is observable from the upgrade corpus and from the library's own issue history, and is the number that should govern automatic update policy. Set automatic update policy per library from that reliability rather than uniformly, so a library with an excellent record updates automatically and one with a poor record requires review — which is the policy teams would set if they had the data. Verify the increment against the interface diff, since a patch release that removes public surface is a detectable violation and can be flagged before it is applied. Delay automatic application briefly for widely-used libraries, so a release that breaks many consumers is identified by somebody else first — which is the cooling period the malicious package niche also recommends and serves both purposes. Report the reliability publicly, since it is a public good and creates a reputational incentive for maintainers to honour the convention. And measure the cost of disabling automatic updates in exposure terms, so a team's reaction to one breakage is weighed against the security consequence rather than taken reflexively.

## Who Feels the Pain
Teams broken by a release that promised compatibility; organisations whose security exposure rose after they disabled automation; and maintainers who honour the convention and receive no credit for it.

## Impact If Fixed
Versioning reliability is measurable per library from public evidence and is treated as a uniform guarantee, which is why one violation disables the whole mechanism. Per-library policy derived from the measured record is what lets automation stay on where it is safe.
