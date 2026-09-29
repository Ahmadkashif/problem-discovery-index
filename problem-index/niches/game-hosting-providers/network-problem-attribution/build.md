# Finding the Layer That Is Actually Broken

**Niche:** [[niches/game-hosting-providers/network-problem-attribution/profile|Network Problem Attribution]]
**Industry:** [[industries/game-hosting-providers|Game Hosting Providers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Four parties can each prove their own component is healthy and the player still cannot play.
**Tags:** #causal-inference #graph-theory #change-point-detection #evaluation-metrics #confidence-intervals #data-integration #automation #k-means-clustering
**Contested on:** Every serious competitor in this niche is fighting to establish which layer is responsible when a player says the game is lagging, across four parties who can each prove their own component is fine — and whoever can attribute it takes the account.

## The Problem
The path between a player and a game server crosses their local network, their access provider, one or more transit and peering relationships, and the hosting provider's own infrastructure. Each party instruments its own segment. When the experience is bad, every party's dashboard is green, because the failure is frequently at a boundary or in aggregate across segments that are individually within tolerance. Nobody measures the path end to end, so nobody can attribute.

## Why Nobody Has Built This
No single party owns the whole path and none has an incentive to fund measurement that might implicate them. Client-side measurement requires cooperation from the game. Cross-party data sharing has no framework. And the current equilibrium — everyone proving their own innocence — is stable and cheap for each participant individually.

## What to Build
Measure the whole path and use the population to locate the fault. Instrument the end-to-end path from client to server with per-hop timing and loss, which is the core — a fault at a boundary is invisible to every party measuring only its own segment. Correlate across players sharing an access provider, region or route, since a problem affecting many players on one path is diagnosable and a single report is not. Compare each player's session against their own history rather than an absolute threshold, because what constitutes degradation is individual. Classify the likely responsible layer with a stated confidence rather than asserting a cause. Detect peering and transit degradation from population patterns, as that class is the commonest unowned failure. Produce evidence in a format the access provider will accept, which is what turns a diagnosis into a resolution. Distinguish jitter and loss from raw latency, since players describe all three as lag and the remedies differ entirely. Feed confirmed route problems into server allocation so players are steered around them, which is the fix the provider can actually apply unilaterally. Give the player a plain explanation of what is wrong, which changes the support experience even when nothing can be fixed. And share the diagnosis with the studio rather than only defending the infrastructure.

## Target Customer
Game hosting providers, studios operating multiplayer titles, internet service providers and transit operators, and network monitoring vendors.

## Impact If Built
A fault at a boundary is invisible to every party measuring only its own segment, which is why every dashboard is green. End-to-end path measurement correlated across a population locates the layer and produces evidence somebody will accept.
