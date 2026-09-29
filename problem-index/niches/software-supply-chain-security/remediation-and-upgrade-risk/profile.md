# Remediation & Upgrade Risk

**Parent Industry:** [[industries/software-supply-chain-security|Software Supply Chain Security]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor here is fighting to tell a team what an upgrade will break before they attempt it — and whoever does that takes the remediation rate, because uncertainty about breakage is why findings age rather than unwillingness to fix them.

## Profile
**Market Size:** ~$340M US attributable to remediation and upgrade risk assessment
**Share of Parent Industry:** ~11% of category revenue
**Digital Adoption:** Low — the fix is proposed and its consequences are unstated
**Target Buyer:** Platform and application engineering
**Automation Potential:** Very High — the corpus of how upgrades actually went exists across the fleet

## What Makes This a Distinct Niche
Every finding raises three questions: does it matter, how do I fix it, and what will the fix break. The third determines whether the fix happens, and nothing in the category addresses it. A developer facing an upgrade from one major version to another has no information about what changed behaviourally, whether their usage is affected, or how the upgrade went for the thousands of other projects that have already attempted it. They estimate conservatively, defer, and the finding ages — which is read by the security function as unwillingness and is in fact rational uncertainty. This is a distinct contested surface because the evidence exists in abundance: the upgrade has been performed by many other projects, publicly, with the outcome visible in their repositories, and nobody has assembled it.

## Current Tools & Gaps
Automated update pull requests with test results, semantic versioning as a declared compatibility signal, and release notes. The gaps: semantic versioning is a convention that is frequently violated, so a patch release can and does break things; release notes describe what changed rather than what breaks and are written by the maintainer for themselves; the public record of how an upgrade went for other projects is abundant and unassembled; whether the consuming application uses the changed interface is determinable statically and is not determined; and the test suite's result on the update pull request is the only evidence offered, which is worth exactly as much as the suite is.

## Problems
- [[niches/software-supply-chain-security/remediation-and-upgrade-risk/build|🔨 Build: What Will This Upgrade Break]]
- [[niches/software-supply-chain-security/remediation-and-upgrade-risk/buy|🛒 Buy: API Diffing and Breaking Change Detection]]
- [[niches/software-supply-chain-security/remediation-and-upgrade-risk/fix|🔧 Fix: Semantic Versioning Treated as a Guarantee]]
