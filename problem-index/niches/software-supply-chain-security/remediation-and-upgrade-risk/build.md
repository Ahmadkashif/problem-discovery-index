# What Will This Upgrade Break

**Niche:** [[niches/software-supply-chain-security/remediation-and-upgrade-risk/profile|Remediation & Upgrade Risk]]
**Industry:** [[industries/software-supply-chain-security|Software Supply Chain Security]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The question that determines whether a vulnerability gets fixed is what the fix will break, and no tool in the category answers it despite the evidence existing in thousands of public upgrades.
**Tags:** #graph-theory #gradient-boosting #bert #survival-analysis #evaluation-metrics #confidence-intervals #automation #transfer-learning
**Contested on:** Every serious competitor here is fighting to tell a team what an upgrade will break before they attempt it — and whoever does that takes the remediation rate, because uncertainty about breakage is why findings age rather than unwillingness to fix them.

## The Problem
A team must upgrade a framework two major versions to resolve a vulnerability. The release notes span hundreds of entries. They do not know which of the breaking changes affect their code, how long the upgrade took other teams, what usually goes wrong, or whether anybody has published a migration path. They estimate three weeks, which is a guess weighted by caution, and it is not scheduled. The finding ages. Meanwhile several thousand public projects have performed this exact upgrade, their commits are visible, the changes they had to make are in the diffs, and the time it took them is in the timestamps.

## Why Nobody Has Built This
The scanner's responsibility ends at the finding and the update tool's ends at opening a pull request, so the risk question falls between them and belongs to nobody. Assessing it requires relating the library's changes to the consumer's usage, which is static analysis nobody has packaged for this purpose. The public upgrade corpus is abundant and scattered across millions of repositories, and assembling it is real work with no obvious owner. And the security function, whose interest is highest, is not the party that would build it.

## What to Build
Assess the upgrade before it is attempted. Diff the library's public interface between the current and target versions, which identifies what actually changed rather than what the release notes mention. Determine which of those changes the consuming application uses, by static analysis of the application's calls into the library, which reduces hundreds of breaking changes to the three that affect this codebase — and is the single most valuable output. Mine the public upgrade corpus: how many projects have made this upgrade, what changes they had to make, how long it took, what they reverted — which is abundant, public and unassembled, and turns an estimate into an observation. Detect behavioural change beyond the interface, since a library can break a consumer without changing a signature and the release notes are frequently silent, which is where the corpus evidence is most valuable. Produce an effort estimate with its basis, so a team can schedule rather than defer. Surface any published migration guide or codemod, and generate the mechanical changes where possible. And report the risk alongside the finding, since the remediation decision is a trade-off between the vulnerability and the upgrade and currently only one side is quantified.

## Target Customer
Application and platform engineering teams, supply chain security vendors whose findings age, and the dependency update tooling projects.

## Impact If Built
Upgrade risk is the question that determines remediation and is answered by nobody, while the evidence sits in thousands of public upgrades. Relating the library's interface changes to the application's own usage collapses hundreds of breaking changes to the few that matter here.
