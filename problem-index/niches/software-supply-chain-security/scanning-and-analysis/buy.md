# The Vulnerability Database Everyone Inherits

**Niche:** [[niches/software-supply-chain-security/scanning-and-analysis/profile|Scanning & Analysis]]
**Industry:** [[industries/software-supply-chain-security|Software Supply Chain Security]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** The whole category rests on a shared public vulnerability database whose limitations are widely acknowledged, and almost nobody corrects for them.
**Tags:** #bert #large-language-models #graph-theory #descriptive-statistics #evaluation-metrics #confidence-intervals #compliance #cross-validation
**Contested on:** Every serious competitor here is fighting to say something about an artefact that the commoditised scan cannot — and that contest is a program analysis problem in one market and an attestation problem in the other, which is why this niche is not terminal and is decomposed below.

## The Problem
The national vulnerability database is the substrate the category is built on, and its limitations are widely acknowledged: incomplete coverage of some ecosystems, inconsistent and sometimes wrong affected-version ranges, metadata that lags the advisory, and entries whose descriptions do not clearly identify what is affected. Every tool inherits these, which means the false positives and false negatives every organisation experiences originate partly in a shared dataset nobody corrects.

## What Already Exists
The public vulnerability database and its ecosystem-specific counterparts; the open advisory databases maintained by several package ecosystems, which are frequently more precise; language models capable of reading an advisory and extracting affected versions and conditions; commit-level fix identification from linked patches; and the vulnerability research community's own corrections, published informally.

## The Customization Gap
The adaptation is to correcting a shared substrate rather than consuming it. It requires: (1) version range verification against the actual fix commit, since the most consequential error class is an imprecise affected range and the patch identifies the truth — which is mechanical where the fix is linked and is the highest-value correction available; (2) reconciliation across sources, because the ecosystem-specific advisory databases frequently disagree with the general one and the disagreement is informative; (3) reading the advisory text for conditions, since many advisories state that the vulnerability applies only under a particular configuration and that condition is in prose and not in the structured metadata — which is precisely what the tools ignore and is a large share of false positives; (4) contributing corrections back, since a vendor correcting privately improves their product and leaves the substrate wrong for everybody, and the reputational position of contributing is worth more than the differentiation of hoarding; and (5) transparency about which findings rest on corrected data, because a customer acting on a correction should know its provenance.

## Target Customer
Composition analysis vendors, the vulnerability database maintainers, the ecosystem advisory database projects, and the security functions inheriting the errors.

## Impact If Solved
A shared substrate with acknowledged limitations produces false positives and negatives across the entire category simultaneously, and correcting it is mechanical for the most consequential error class. Extracting applicability conditions from advisory prose addresses a large share of the noise that makes the category's output ignorable.
