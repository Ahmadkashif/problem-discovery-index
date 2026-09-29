# Relevance Against the Customer's Actual Estate

**Industry:** [[threat-intelligence-vendors|Threat Intelligence Vendors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** A feed of millions of indicators is delivered with sector tags, and the customer's analysts do the filtering with time they do not have.
**Tags:** #graph-neural-networks #gradient-boosting #bert #k-nearest-neighbors #confidence-intervals #dimensionality-reduction #evaluation-metrics #data-integration

## The Problem
Threat intelligence is delivered broadly because the vendor does not know the customer's environment. A feed covers adversaries, malware families, infrastructure and vulnerabilities across many sectors and technologies, tagged coarsely by industry and geography.

What determines relevance is specific. Whether the organisation runs the software a campaign targets, whether the exploited version is present, whether the affected component is exposed externally, whether the adversary's targeting pattern includes organisations of this size in this sector, and whether existing controls already mitigate it.

None of that is knowable to the vendor and all of it is knowable to the customer, so the filtering happens at the customer — performed by the scarcest people in the organisation, repeatedly, against a stream that never stops. Security teams describe intelligence as a source of work rather than a source of leverage, which is an indictment of the delivery model rather than of the content.

Vulnerability intelligence is the sharpest case. A stream of disclosures with severity scores means little without knowing whether the affected component is present, reachable and exploitable in this environment, and the difference between the raw severity and the contextual one is frequently the difference between an emergency and a routine patch.

## What Already Exists
Vendors provide sector and geography tagging and some profile-based tailoring. Threat intelligence platforms aggregate and deduplicate feeds and support filtering rules the customer writes. Attack surface management and asset inventory tools hold the environment data on the customer side. Vulnerability management vendors have moved toward exploit-likelihood scoring, which is a genuine improvement and is still environment-agnostic. Some intelligence vendors offer a managed service where their analysts do the filtering, which is the current answer for those who can afford it.

## The Customisation Gap
The two halves — the intelligence and the environment — sit in different systems at different companies, and joining them is the whole opportunity. A customer's asset inventory, software bill of materials, external attack surface and control configuration are exactly what determines relevance, and a vendor able to score against them would deliver a fraction of the volume with most of the value.

Exposure reasoning is what makes the score meaningful. Relevance is not presence of a technology; it is presence, in a reachable position, in a version affected, without a mitigating control. Reasoning over that chain is a graph problem with the data available, and it is the difference between a list of applicable threats and a list of real ones.

Targeting fit is the second dimension. Adversary targeting is patterned — sector, size, geography, function — and estimating whether a given campaign plausibly targets organisations like this one is learnable from the vendor's own historical victim data, which the incident-response-connected vendors hold and do not expose this way.

And the delivery should be a ranked short list with reasoning, not a filtered feed. A security team can act on five items with an explanation each; it cannot act on a filtered stream of eight hundred.

## Impact If Solved
Intelligence is currently consumed by the scarcest people in a security organisation doing filtering the vendor could do better. Joining the feed to the customer's own estate, reasoning over the exposure chain rather than matching technologies, and delivering a short ranked list with reasoning would convert a work-generating stream into the leverage the product was supposed to be — and would let vendors compete on relevance rather than on volume.
