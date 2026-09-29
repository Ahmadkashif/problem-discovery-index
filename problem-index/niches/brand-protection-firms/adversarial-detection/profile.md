# Adversarial Detection

**Parent Industry:** [[industries/brand-protection-firms|Brand Protection Firms]]
**Category:** Contested Sub-Niche
**Contested on:** Whether detection finds the listings of operators who have learned exactly what it matches on, or only the ones who have not.

## Profile

**Market Size:** ~$640M
**Share of Parent Industry:** ~16%
**Digital Adoption:** High — and the opponent adapts faster
**Target Buyer:** Detection engineering, brand protection leadership
**Automation Potential:** Very high — it is a modelling contest

## What Makes This a Distinct Niche

This is the recall half, and it is an arms race. Detection matches images against brand asset libraries, keywords against brand names and their misspellings, and account signals against known patterns. The operators who matter know all of it.

So they alter images enough to defeat perceptual matching while remaining visually convincing to a buyer. They avoid the brand name in the title and place it in an image, a description or a reply to a question. They photograph their own goods rather than copying brand photography. They vary account characteristics. They test a listing, observe whether it survives, and adapt.

The result is a detection population skewed toward the naive. The seller who copies a brand photograph and puts the name in the title is found immediately. The operation running four hundred accounts with original photography and deliberate keyword avoidance is substantially under-detected.

That adversarial character is what separates it from its sibling. [[niches/brand-protection-firms/infringement-determination/profile|🎯 Infringement Determination]] is a legal judgement problem that no amount of detection improvement solves — and improving detection makes it harder, because a better matcher surfaces more borderline cases. This half is a modelling contest with a measurable objective, testable against held-out evasive listings, and better is always better.

## Current Tools & Gaps

Perceptual image hashing and embedding-based visual similarity. Keyword and misspelling matching with variant generation. Marketplace and social crawling at scale. Price anomaly detection. Seller profile heuristics. Some machine-assisted classification of listing text.

The gaps follow the adversary. Matching is largely static, so the features sellers perturb remain the features being matched. Evasion is not modelled — nobody trains against the perturbations operators actually use, despite the firm's own history containing thousands of examples. Cross-surface signals are unused, so an operator's listings on one marketplace do not inform detection on another. Detection is per-listing rather than per-account or per-operator, so the strongest available signal is discarded. And recall is unmeasured — nobody knows what fraction of infringing listings is found, because there is no ground truth for what was missed.

## Problems

- [[niches/brand-protection-firms/adversarial-detection/build|🔨 Build: Detection That Assumes an Opponent]]
- [[niches/brand-protection-firms/adversarial-detection/buy|🛒 Buy: Adversarial Robustness From Fraud and Abuse]]
- [[niches/brand-protection-firms/adversarial-detection/fix|🔧 Fix: Nobody Knows What Is Being Missed]]
