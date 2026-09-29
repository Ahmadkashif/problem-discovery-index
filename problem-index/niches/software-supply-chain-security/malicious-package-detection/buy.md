# Behavioural Malware Analysis, Applied to Packages

**Niche:** [[niches/software-supply-chain-security/malicious-package-detection/profile|Malicious Package Detection]]
**Industry:** [[industries/software-supply-chain-security|Software Supply Chain Security]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Malware analysis has decades of sandboxing, behavioural detection and adversarial adaptation practice, and package ecosystems are defended by name similarity checks.
**Tags:** #gradient-boosting #contrastive-learning #k-means-clustering #change-point-detection #evaluation-metrics #confidence-intervals #compliance #cross-validation
**Contested on:** Every serious competitor here is fighting an adversary who publishes deliberately poisoned packages and adapts within days — and whoever detects the adaptation across the whole registry takes the market, because signature matching loses this contest structurally.

## The Problem
Malware analysis is a mature discipline: sandboxed dynamic execution, behavioural signatures, family clustering, evasion detection, and an institutional understanding of how adversaries adapt to defences. Package ecosystems face a malware problem with an unusually favourable property — the code is published openly and can be analysed before anybody installs it — and are defended largely by name similarity heuristics and manual reports.

## What Already Exists
Sandboxed dynamic analysis platforms; behavioural detection and family clustering from the malware research community; static analysis for obfuscation and suspicious construct detection; the adversarial adaptation literature; and several open package-scanning projects applying parts of this.

## The Customization Gap
The adaptation is to source-available code published openly before use. It requires: (1) exploiting the pre-publication analysis opportunity, since unlike binary malware the code is available and can be analysed before any user installs it — which is a defender's advantage the discipline has never had and is under-used; (2) install-time execution as the primary behaviour to observe, because the attack's mechanism in several ecosystems is code that runs during installation, and sandboxing that specific phase catches the dominant pattern; (3) differential analysis against the previous version, since the interesting signal is what changed in this release rather than what the package does in general, and a maintainer-compromise attack is visible as an anomalous diff; (4) very low false positive tolerance, because flagging a legitimate popular package disrupts an enormous number of builds and the ecosystem's tolerance for that is near zero — which constrains the aggressiveness far more than in endpoint malware; and (5) speed, since the window between publication and installation is short and an analysis that completes in a day has already missed the pipelines that pulled it overnight.

## Target Customer
Package registries, supply chain security vendors, and the malware analysis vendors for whom package ecosystems are an adjacent and under-defended domain.

## Impact If Solved
A mature discipline exists and the defended surface is unusually favourable, since the code is published before it is used. Differential analysis against the previous version is the adaptation that catches maintainer compromise, which is the case reputation signals get wrong.
