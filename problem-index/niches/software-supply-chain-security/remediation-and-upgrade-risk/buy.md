# API Diffing and Breaking Change Detection

**Niche:** [[niches/software-supply-chain-security/remediation-and-upgrade-risk/profile|Remediation & Upgrade Risk]]
**Industry:** [[industries/software-supply-chain-security|Software Supply Chain Security]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Tools that compare two versions of a library and report the breaking changes exist for most major ecosystems, and no security tool uses one.
**Tags:** #graph-theory #bert #gradient-boosting #evaluation-metrics #confidence-intervals #cross-validation #transfer-learning #automation
**Contested on:** Every serious competitor here is fighting to tell a team what an upgrade will break before they attempt it — and whoever does that takes the remediation rate, because uncertainty about breakage is why findings age rather than unwillingness to fix them.

## The Problem
Interface comparison tools exist for most major ecosystems: given two versions of a library, they report removed, changed and added public surface, and several are used by library maintainers to check their own compatibility claims. Consumers facing an upgrade do not use them, security tools do not invoke them, and the developer reads release notes instead — which are written by the maintainer about what they did rather than about what it breaks.

## What Already Exists
Interface comparison tools for the major ecosystems; semantic versioning checkers used by maintainers; codemod and migration tooling for several widely-used frameworks; the research on breaking change detection and its empirical findings about how often versioning conventions are violated; and static call analysis to determine consumer usage.

## The Customization Gap
The adaptation is to the consumer's perspective rather than the maintainer's. It requires: (1) intersecting the library's changes with the consumer's usage, since the maintainer's question is what they broke and the consumer's is what breaks them, and the second is a far shorter list — this intersection is the whole value and is performed by nobody; (2) behavioural change detection beyond the interface, because a library that changes a default, an error condition or a serialisation format breaks consumers without touching a signature, and interface diffing misses all of it — which is where the public upgrade corpus supplies the evidence; (3) transitive interface effects, since an upgrade can change a library's own dependencies and break the consumer indirectly; (4) ecosystem coverage, because the tools exist unevenly and the ecosystems with the weakest tooling are frequently the ones with the least reliable versioning; and (5) effort rather than a change list, since the developer's question is how long this will take and a list of forty affected call sites is an input to that.

## Target Customer
Supply chain security vendors, dependency update tooling projects, and the platform teams performing upgrades at estate scale.

## Impact If Solved
Interface comparison tools exist and are used by maintainers rather than consumers, and the intersection with the consumer's usage — which is the short and useful list — is computed by nobody. Behavioural change is the half interface diffing misses and is where the public corpus is most informative.
