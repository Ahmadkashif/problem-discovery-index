# Detecting It Before the Penalty

**Niche:** [[niches/music-distribution-platforms/stream-manipulation-detection/profile|Stream Manipulation Detection]]
**Industry:** [[industries/music-distribution-platforms|Music Distribution Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The distributor learns its artist's streams were artificial when the penalty arrives, and the artist learns it from the distributor.
**Tags:** #gradient-boosting #graph-theory #change-point-detection #evaluation-metrics #confidence-intervals #compliance #automation #k-means-clustering
**Contested on:** Every serious competitor in this niche is fighting to identify artificial streams before the penalty lands and to tell a wrongly accused artist why — and whoever detects accurately and explains defensibly stops the enforcement falling on the innocent.

## The Problem
Detection happens at the streaming services, which see the listening behaviour. Enforcement lands on the distributor, which sees the stream counts in its reporting and has done no detection of its own. The artist, who may have paid a promotion service that quietly used bots, is told their release was removed or their royalties withheld, with a reason that amounts to a policy citation. Nobody in the chain has an incentive to explain, and the fraud itself is a transfer from every honest artist in the pool.

## Why Nobody Has Built This
Detection was assumed to belong upstream because that is where the listening data is, so distributors built nothing — a party that receives an enforcement decision does not naturally develop the capability to anticipate it. The reporting distributors receive is aggregated and lagged. Explaining a detection risks explaining how to evade it. And the artist's inability to contest is not anyone's problem.

## What to Build
Detect from what the distributor can see and make the decision contestable. Detect anomalous stream patterns from the reporting the distributor does receive — implausible growth, geographic concentration, playlist and daypart signatures, listener-to-stream ratios — which is the core and is enough to flag before a penalty arrives. Warn the artist early, since the most common case is a legitimate artist who bought a bad promotion service and can stop. Distinguish purchased promotion from deliberate operation, because they are treated identically and are morally and practically different. Track promotion services by the outcomes of artists who used them, as that is the actionable intelligence and no single artist can assemble it. Detect the coordinated network across artists, which is visible to a distributor and not to any individual. Give the artist a specific, evidence-backed explanation, as the current policy citation makes appeal impossible. Build an appeal that can succeed, since the innocent case is common and currently has no remedy. Report detection performance, because the balance between catching fraud and penalising the innocent is currently unmeasured. Share patterns with services where it helps, as the detection is genuinely collective. And publish guidance about promotion services, which is the cheapest prevention available.

## Target Customer
Trust and safety leadership, artists penalised without explanation, streaming services enforcing, and fraud detection vendors.

## Impact If Built
A party that receives an enforcement decision does not naturally develop the capability to anticipate it, so distributors detect nothing. The reporting they already receive supports enough detection to warn an artist before a penalty rather than after.
