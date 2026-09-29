# Judging a Stranger at the Door

**Niche:** [[niches/neobanks/onboarding-identity-decisioning/profile|Onboarding & Identity Decisioning]]
**Industry:** [[industries/neobanks|Neobanks]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The institution decides whether a stranger can have a bank account from third-party data, a device fingerprint and a photograph, against an adversary who buys the same data and tests the defences.
**Tags:** #gradient-boosting #logistic-regression #graph-theory #evaluation-metrics #confidence-intervals #compliance #hypothesis-testing #object-detection
**Contested on:** Every serious competitor in this niche is fighting to judge a stranger from third-party data and a document against an organised adversary — and whoever does that well decides who can open a bank account at all.

## The Problem
An application arrives. The institution checks identity vendors, examines a device fingerprint, runs a document and selfie check, and applies rules. It has no history with this person. An organised fraud operation submitting applications at scale has access to breached identity data that will pass the vendor checks, device farms that defeat naive fingerprinting, and enough attempts to learn where the thresholds are. Meanwhile a legitimate applicant with a thin file — recently arrived, young, previously unbanked — looks statistically similar to a synthetic identity and is refused. Both errors are consequential and only one of them is counted.

## Why Nobody Has Built This
The capability is bought from vendors and each institution's configuration is a set of purchased scores with thresholds, which means nobody owns the end-to-end performance — the assembly is the product and the assembly is unevaluated. Declines produce no feedback, so the false positive rate is structurally invisible. Fraud losses are counted precisely, which biases every trade-off toward refusing. And the thin-file applicant has no way to appeal and no voice.

## What to Build
Evaluate and combine rather than accumulate. Score the vendors against this institution's own confirmed outcomes rather than accepting their general performance, which is the highest-return step and frequently reorders which vendors are worth paying for. Combine signals in a model rather than stacking thresholds, since a set of independent vendor cut-offs discards the joint information and is the crudest possible use of expensive data. Use the graph — shared devices, addresses, funding sources, contact details across applications — which is where organised fraud is visible and individual scores are not. Detect the adversary's testing behaviour, since a fraud operation probing thresholds leaves a recognisable pattern and catching the probe is more valuable than catching any single application. Measure the false decline rate deliberately, through approving a random sample near the threshold and observing outcomes, which is the only way to see the invisible error and is affordable at small volumes. Build a path for thin files rather than refusing them, which is the fix note's subject and is where growth and fairness coincide. Handle document fraud with current techniques, since the known defeats are documented and many implementations still fail them. Feed confirmed outcomes back continuously, connecting to the measurement niche. Monitor for adversarial adaptation rather than for drift, since the distribution changes because someone is changing it. And report both error rates to leadership, because an institution optimising one of them is not managing risk, it is managing one number.

## Target Customer
Risk and growth leadership at digital banks, identity and fraud vendors whose scores are unevaluated in situ, and the applicants refused bank accounts by a threshold.

## Impact If Built
The assembly of purchased scores is the product and nobody evaluates it end to end, while declines produce no feedback and make the false positive rate structurally invisible. Approving a random sample near the threshold buys visibility of the invisible error at small cost.
