# Network Path Attribution

**Industry:** [[game-hosting-providers|Game Hosting Providers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** A player reports lag, the provider shows healthy servers, the studio shows a clean client, the internet provider says nothing is wrong, and the player still cannot play.
**Tags:** #change-point-detection #graph-neural-networks #gradient-boosting #bayesian-inference #confidence-intervals #evaluation-metrics #data-integration #time-series-forecasting

## The Problem
A multiplayer connection crosses many components: the player's device and local network, their internet provider's access network, transit and peering between networks, the provider's edge and backbone, the allocated region, and the game server itself. A degradation anywhere produces the same experience — rubber-banding, hit registration failures, disconnections — and each party can demonstrate that its own component looks fine.

The evidence each party holds is partial and self-serving in structure rather than in intent. The hosting provider sees server-side metrics and its own network. The studio sees client telemetry. The internet provider sees its access network. Nobody sees the path, and the failures frequently live in the parts nobody sees — a congested peering point at a particular hour, a route change, a regional interconnect.

So problems that affect thousands of players in one city on one network at one time of day persist for weeks. They are individually reported as personal connection problems, none of the parties can see the pattern, and the player community documents it before any of the operators do.

## What Already Exists
Every layer has telemetry. Providers run network monitoring and have peering visibility. Studios collect client-side network metrics in most modern titles. Internet measurement platforms — RIPE Atlas, Measurement Lab, ThousandEyes — observe paths independently. Some studios publish server status pages. Game-specific network diagnostic tools exist for players and are generally unusable by the people who need them. Content delivery and edge providers have mature versions of this for web traffic that have not been adapted to interactive latency-sensitive workloads.

## The Customisation Gap
The data exists at every layer and is never joined, which is a data integration problem before it is a modelling one. Client-side telemetry correlated with server-side metrics, path measurements and network identity would localise a degradation to a component with real confidence — and the reason it is not done is that the layers belong to different companies with no established mechanism for sharing.

Population-level detection is the immediately achievable half. A provider hosting many titles sees client-reported quality across all of them, which means a degradation on one internet provider in one metropolitan area appears as a correlated anomaly across unrelated games — a signal no single studio can see and the provider is uniquely positioned to detect. That alone would turn a class of multi-week mysteries into same-day findings.

The interactive workload is what makes existing tooling inapplicable. Web performance monitoring optimises for throughput and page completion; interactive games care about jitter, tail latency and packet loss patterns at timescales those tools do not measure. The measurement design has to be built for this workload rather than borrowed.

And the output has to be usable by a support engineer and by a player. A confident statement that the problem is in a specific segment, with the evidence, is what ends the circular conversation — and where the answer is the player's own network, saying so clearly and specifically is more helpful than a denial.

## Impact If Solved
Connection quality problems are the most common and least resolvable complaints in multiplayer gaming, and they persist because the evidence is distributed across parties who each see only their own component. Cross-title population-level anomaly detection is achievable by a provider alone and would find regional degradations within a day rather than a month; full path attribution requires cooperation and is the version that ends the dispute.
