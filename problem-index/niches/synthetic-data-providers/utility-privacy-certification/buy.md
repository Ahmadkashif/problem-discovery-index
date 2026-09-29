# Privacy Auditing Methods That Exist

**Niche:** [[niches/synthetic-data-providers/utility-privacy-certification/profile|Utility–Privacy Certification]]
**Industry:** [[industries/synthetic-data-providers|Synthetic Data Providers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Empirical privacy auditing has developed real methods for measuring what a released model or dataset actually leaks, and the category reports a theoretical parameter instead.
**Tags:** #monte-carlo-methods #hypothesis-testing #confidence-intervals #evaluation-metrics #bayesian-inference #cross-validation #compliance #gradient-boosting
**Contested on:** Every serious competitor in this niche is fighting to certify that a synthetic dataset is simultaneously safe to release and useful to train on — and whoever issues that claim credibly takes the category, because it is the only claim customers are actually buying.

## The Problem
The privacy research community has developed empirical auditing: rather than relying on a theoretical bound, measure what an adversary can actually recover, using membership inference, attribute inference, reconstruction attacks and canary insertion — and derive an empirical lower bound on the leakage. The methods are published with implementations, and they answer the question the theoretical parameter only bounds. The category reports the parameter, sometimes runs one attack, and presents the result as due diligence.

## What Already Exists
Membership inference attack methodology with a substantial literature and known strength characteristics; attribute inference and reconstruction attacks; canary insertion for measuring memorisation directly; empirical privacy auditing frameworks that derive lower bounds from attack success; and the differential privacy accounting machinery that produces the upper bound.

## The Customization Gap
The adaptation is to synthetic tabular and sensor data rather than to models. It requires: (1) attacks appropriate to a released dataset rather than a queryable model, since most of the literature assumes model access and the threat here is somebody holding the synthetic records — which changes the attack surface and the relevant methods; (2) a realistic adversary model, since attack success depends enormously on auxiliary information and the honest question is what an adversary with plausible side information can recover, which requires stating the assumption rather than choosing the weakest attack; (3) attacks run adversarially rather than by the generating vendor, because the vendor's incentive is to run a weak attack and the field's credibility problem originates there; (4) reporting a lower bound alongside the theoretical upper bound, since the two together bracket the truth and either alone is misleading in a known direction; and (5) outlier-specific evaluation, since aggregate attack success conceals that the individuals most at risk are the unusual records, and those are precisely the people a privacy guarantee exists to protect.

## Target Customer
Generation vendors, privacy and compliance functions evaluating their claims, independent assurance providers, and the privacy research community.

## Impact If Solved
Empirical auditing answers what the theoretical parameter only bounds and the category reports the bound. Outlier-specific evaluation is the part most likely to be skipped and most consequential, since aggregate success rates conceal the risk to exactly the individuals the guarantee is for.
