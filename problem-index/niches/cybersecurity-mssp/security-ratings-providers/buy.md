# Asset Attribution Adapted to Contested Ownership

**Niche:** [[niches/cybersecurity-mssp/security-ratings-providers/profile|Security Ratings Providers]]
**Industry:** [[industries/cybersecurity-mssp|Cybersecurity MSSPs]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Attack surface discovery tools find internet assets; the rating depends on deciding which organization is responsible for each one, and that is a question the internet does not answer.
**Tags:** #graph-neural-networks #graph-theory #contrastive-learning #random-forests #bert #evaluation-metrics #probability-distributions #confidence-intervals #automation #data-integration

## The Problem
Every rating rests on attributing observed internet assets to a rated organization, and attribution errors flow directly into the score. A subsidiary acquired last year, a domain retained after divestiture, shared hosting where a neighbour's misconfiguration is visible, a cloud range reassigned between tenants, a partner's infrastructure operating under the client's brand — each of these produces a rating that reflects someone else's posture. Rated organizations dispute attributions constantly, and each dispute is handled as a support case. Attribution is maintained by a combination of registry data, certificate observation, and analyst research, and its accuracy is not measured.

## What Already Exists
Attack surface management is a crowded category. Censys, Shodan, and the ASM vendors handle internet-scale scanning, certificate transparency ingestion, DNS enumeration, and basic organizational attribution well. Corporate hierarchy data is available commercially. Graph platforms handle the relationship modelling.

## The Customization Gap
Available attribution is inference from registration and certificate data, which works where organizations register assets in their own name and fails in exactly the cases that produce disputes — shared and ephemeral infrastructure, corporate change, and delegated operation. The adaptation is attribution as a probabilistic assignment with responsibility modelled rather than assumed: an asset can be operated by one party, owned by another, and reasonably the responsibility of a third, and the rating should be explicit about which relationship it is scoring. Corporate structure needs a temporal dimension, since an acquisition or divestiture changes responsibility on a date and the rating history should reflect that rather than being retroactively rewritten. Confidence must be per-asset and surfaced, so a rating built substantially on uncertain attributions is visibly different from one built on certain ones. And the dispute history is the natural training signal — every resolved dispute is a labelled attribution error, and it is currently discarded into a support ticketing system.

## Target Customer
Heads of data science and attribution at ratings providers, and the vendor risk and insurance teams who act on ratings whose asset basis they cannot inspect.

## Impact If Solved
Removes the largest source of rating error and the largest source of customer dispute simultaneously, since they are the same problem. Surfacing attribution confidence also addresses the fairness objection the segment faces most sharply — that organizations are scored on infrastructure they do not control and cannot see.
