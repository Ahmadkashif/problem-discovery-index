# Streaming Manipulation Detection and Penalties

**Industry:** [[music-distribution-platforms|Music Distribution Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Artificial streams draw from a fixed royalty pool, so fraud transfers money from every legitimate artist — and the enforcement against it now falls on distributors and artists who often cannot tell what triggered it.
**Tags:** #graph-neural-networks #gradient-boosting #k-means-clustering #change-point-detection #autoencoders #evaluation-metrics #compliance #feature-engineering

## The Problem
Streaming royalties are paid from a pool divided by share of total streams. An artificial stream therefore does not create money; it moves money from everyone else. At scale this is a material transfer, and the services have moved from treating it as a nuisance to treating it as a serious problem, introducing minimum stream thresholds and financial penalties for tracks flagged as artificially streamed from 2024.

Those penalties are charged to the distributor, who charges them to the artist. The artist may have bought promotion from a service that delivered bot streams, may have been targeted maliciously by someone else, or may have done nothing at all.

Detection belongs to the streaming service and is opaque by necessity — publishing the method would defeat it. So an artist receives a penalty, a takedown or a payout withheld, with a description that does not permit them to understand or contest it.

Distributors are caught between. They are liable for penalties, they have no visibility into the detection, and they must decide whether to pass on a charge to an artist who may be genuinely innocent.

Malicious streaming is the case that most clearly breaks the current arrangement: buying artificial streams for a competitor's track is cheap and produces penalties against the victim. Any enforcement regime without an appeal path converts this into an effective attack.

And distributors do hold signals of their own — release patterns, upload behaviour, catalogue characteristics, payout destinations, account relationships — which are relevant and largely unused.

## What Already Exists
Streaming services run detection internally and do not disclose it. Industry bodies have published definitions of artificial streaming. Distributors perform some screening at upload and monitor payout anomalies. Fraud detection in adjacent domains is mature. Content identification handles infringement separately.

## The Customisation Gap
Distributors do not model their own data. Account creation patterns, upload cadence, catalogue composition, cross-account relationships, payout destination clustering and the correlation between promotional service usage and subsequent flags are all observable at the distributor and are rarely modelled.

Pre-emptive warning does not exist. A distributor able to tell an artist that their stream pattern resembles cases that were later penalised — before the penalty — would prevent the harm rather than pass on the cost.

Malicious targeting is not distinguished from participation, and the distinction determines whether a penalty is just. A track whose artificial streams originate from accounts with no relationship to the artist's own promotion history is a different case from one whose owner bought them, and the distributor holds some of the evidence.

Appeal is unsupported. An artist contesting a penalty has no structured way to present evidence, and the distributor has no structured way to evaluate it.

And nothing closes the loop. Which artists were penalised, what preceded it, and whether the penalty was later reversed is a labelled dataset every distributor accumulates and none uses.

## Impact If Solved
Artificial streaming takes money from every legitimate artist and the enforcement against it currently falls on people who frequently cannot tell what happened or contest it. A distributor modelling its own signals could warn before the penalty, distinguish targeting from participation, and support an appeal — which protects both the royalty pool and the artists the current regime treats as collateral.
