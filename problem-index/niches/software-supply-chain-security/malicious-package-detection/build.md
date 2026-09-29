# An Adversary Who Adapts Within Days

**Niche:** [[niches/software-supply-chain-security/malicious-package-detection/profile|Malicious Package Detection]]
**Industry:** [[industries/software-supply-chain-security|Software Supply Chain Security]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every registry and scanner now checks for malicious packages, and the attack has moved from exploiting vulnerable dependencies to publishing poisoned ones — which is an adversarial problem that signature matching loses.
**Tags:** #gradient-boosting #contrastive-learning #change-point-detection #k-means-clustering #evaluation-metrics #confidence-intervals #compliance #automation
**Contested on:** Every serious competitor here is fighting an adversary who publishes deliberately poisoned packages and adapts within days — and whoever detects the adaptation across the whole registry takes the market, because signature matching loses this contest structurally.

## The Problem
An attacker publishes a package whose name differs from a popular one by a transposed character. It is caught by name-similarity detection within a day. The next attempt uses a plausible alternative name rather than a near-miss, obfuscates the payload, delays execution until after install, and exfiltrates only on a machine that looks like a build system. It is not caught for three weeks, during which it is installed by build pipelines with credentials. The detection that caught the first attempt described the first attempt, and the attacker read the detection as feedback — which is the structure of every adversarial contest and is why a signature-based defence is permanently a step behind.

## Why Nobody Has Built This
Detection was built on the attacks that had been seen, which is the natural way to build it and produces a defence shaped like the past. The registry-wide publication corpus — every package, every version, every maintainer action — is the strongest available signal and sits with the registries, whose incentives around policing their own ecosystem are mixed and whose resources are frequently modest. Consumers see only their own dependencies, which makes cross-package pattern detection impossible for them. And the install-time execution model that makes the attack effective is a design property of several ecosystems, which means the most effective mitigation is a change nobody can make unilaterally.

## What to Build
Detect the publication pattern rather than the payload. Analyse the publication event rather than only the code: a new maintainer publishing to an established package, a version published outside the project's usual cadence, a release with no corresponding source commit, a first-time publisher with a name close to something popular, a dependency added that the project has no reason to need — these are behavioural signals about the act of publishing and they generalise across payload changes in a way signatures do not. Use the registry-wide view as the primary detector, since a campaign appears as a correlated pattern across many packages and is unmistakable in aggregate — this is the structural advantage and it must be exercised at the registry or by a party with registry-wide visibility. Analyse behaviour dynamically in a sandbox, since the payload is code and executing it under observation is the definitive test, and it is done inconsistently. Separate the account compromise case explicitly, which the fix note addresses and which reputation signals actively get wrong. Measure the window from publication to detection, which is the metric that describes the defence's actual performance and is not reported by anybody. And publish the detections and the reasoning, since the ecosystem's defence improves collectively and hoarding signatures loses to an adversary who reads them anyway.

## Target Customer
Package registries, supply chain security vendors, platform teams operating internal registries, and the security functions whose build systems are the target.

## Impact If Built
The contest is adversarial and the defence is signature-shaped, which guarantees a permanent lag. Publication-behaviour signals generalise across payload changes, and the registry-wide correlated view is the only advantage the defender structurally has.
