# Malicious Package Detection

**Parent Industry:** [[industries/software-supply-chain-security|Software Supply Chain Security]]
**Category:** Low Digitized
**Contested on:** Every serious competitor here is fighting an adversary who publishes deliberately poisoned packages and adapts within days — and whoever detects the adaptation across the whole registry takes the market, because signature matching loses this contest structurally.

## Profile
**Market Size:** ~$420M US malicious package and dependency abuse detection
**Share of Parent Industry:** ~14% of category revenue
**Digital Adoption:** Low in substance — everyone checks and the adversary adapts
**Target Buyer:** Security functions, package registries and platform teams
**Automation Potential:** Very High — the publication corpus is public and the behaviours are observable

## What Makes This a Distinct Niche
The attack has moved from exploiting vulnerable dependencies to publishing poisoned ones, which is a different problem with a different structure. Typosquatting, dependency confusion, maintainer account compromise and deliberately malicious first releases have all been used at scale, and they are adversarial in the way vulnerability scanning is not: an attacker publishes, observes whether it is caught, and adjusts. Signature matching loses that contest by construction, because a signature describes what was caught and the attacker's next attempt is designed around it. The defender's structural advantage is the registry-wide view — a new publication pattern appears across many packages and a single consumer sees only their own dependencies — and it is under-exploited. This is also the failure mode with the worst consequence in the category, since a malicious package executes on a developer's machine and in a build system with credentials.

## Current Tools & Gaps
Registry-side scanning, behavioural analysis of install scripts, typosquatting detection by name similarity, and reputation signals. The gaps: detection is largely signature and heuristic based against an adaptive adversary; the registry-wide publication corpus is the strongest available signal and is used by the registries rather than by the consumers; maintainer account compromise produces a malicious version of a trusted package, which reputation signals rate as safe; the response time between publication and detection is the window that matters and is not reported; and the install-time execution model, which is the reason this attack works, is a design property of several ecosystems rather than a bug.

## Problems
- [[niches/software-supply-chain-security/malicious-package-detection/build|🔨 Build: An Adversary Who Adapts Within Days]]
- [[niches/software-supply-chain-security/malicious-package-detection/buy|🛒 Buy: Behavioural Malware Analysis, Applied to Packages]]
- [[niches/software-supply-chain-security/malicious-package-detection/fix|🔧 Fix: A Trusted Package With a Compromised Maintainer]]
