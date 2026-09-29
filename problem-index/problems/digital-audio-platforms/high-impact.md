# The Pool Pays by Share of Total Streams, Not by Who Anybody Listened To

**Industry:** [[digital-audio-platforms|Digital Audio Platforms]]
**Type:** High Impact
**One-liner:** A subscriber's fee is pooled and divided by overall stream share, which means the money does not follow the listening, fraud pays because it redistributes from a fixed pot, and nobody can audit any of it.
**Tags:** #causal-inference #graph-neural-networks #monte-carlo-methods #bayesian-inference #confidence-intervals #hypothesis-testing #evaluation-metrics #compliance

## The Problem
Under the pro-rata model, all subscription revenue for a market is pooled and each rights holder receives a share proportional to their share of total streams. A subscriber who listens exclusively to one niche artist all month contributes a fee that is distributed mostly to artists they have never played. This is the standard settlement across the industry and it has three consequences that compound.

The first is the redistribution itself. Dedicated audiences for niche work subsidise high-volume mainstream listening, and the artists with the most committed listeners capture the least value from that commitment. The user-centric alternative — dividing each subscriber's fee according to what they actually played — has been analysed, piloted in a few markets and never broadly adopted, partly because the transition redistributes money away from parties with the most influence over the licensing negotiation.

The second is fraud. Because the pool is fixed, artificially inflating streams for one catalogue does not generate new money; it takes money from every legitimate rights holder. That gives fraud an unusually direct victim and makes detection an economic necessity rather than a hygiene measure. The techniques are adversarial and evolving — distributed accounts, low-volume-per-account patterns designed to stay under thresholds, uploaded noise catalogues — and platforms disclose little about their detection rates, so no rights holder can assess how much of their share is being taken.

The third is auditability. An artist receives a statement showing streams and a payment, with no way to verify the pool, the deductions, the share calculation or the fraud adjustments. The intermediate layers — distributor, label, publisher, collecting society — each apply their own accounting. The result is an industry where the people generating the value cannot check the arithmetic, which is the underlying reason every royalty controversy of the last decade has been conducted in the absence of evidence.

Recent policy changes have made the stakes explicit. Minimum annual stream thresholds before a track earns anything, and minimum play durations for functional audio, moved real money between categories of rights holder — decisions taken unilaterally, with the affected parties learning the consequences from their next statement.

## Why It's Unsolved
The allocation model is the product of licensing negotiations between platforms and major rights holders, and the parties with the most leverage benefit most from the current arrangement. This is a distributional conflict, not a technical gap, and it is resolved by contract rather than by analysis.

The complexity argument is offered and is partly genuine. Per-subscriber allocation requires per-subscriber accounting across a catalogue of tens of millions of recordings and dozens of intermediaries, with different rights split across master and publishing, across territories, and across time as ownership changes. That is real engineering. It is not beyond an industry that computes personalised recommendations for hundreds of millions of people in real time.

Fraud detection is genuinely hard and genuinely adversarial. Distinguishing a coordinated campaign from a passionate fanbase that streams an album repeatedly on release day is a real classification problem with high costs on both sides: failing to detect steals from everyone, and a false positive withholds an artist's income on the basis of an algorithm they cannot see or contest.

And auditability is resisted for a straightforward reason: publishing the arithmetic invites disputes about the arithmetic. Every layer in the chain has some incentive to keep its own deductions unexamined.

## What a Solution Looks Like
Compute the counterfactual and publish it. The platform has every subscriber's complete listening record; calculating what each rights holder would have earned under user-centric allocation, per market and per period, is a tractable computation against data already held. Publishing that alongside the actual pro-rata figure does not require changing any contract and would, for the first time, put a number on the argument the industry has been having without one.

Treat fraud as a shared-loss problem with due process. Detection should be relational — coordinated account behaviour, shared infrastructure, catalogue-level patterns — rather than threshold-based, because thresholds are what fraudulent operations are designed around. Equally important is what happens after detection: an artist whose income is withheld needs to see the evidence and have a route to contest it, and the absence of that process is currently a serious and under-discussed harm to legitimate artists caught by imperfect classifiers.

Make the statement auditable. A rights holder should be able to see the pool, the deductions, their stream count by market, the fraud adjustment applied, and the arithmetic connecting those to the payment — with enough detail to check it. Most of this is a reporting problem rather than a modelling one, and its absence is a choice.

Instrument policy changes before they ship. A minimum stream threshold or a play-duration rule is a policy with a computable distributional effect, and running it as a simulation across the catalogue before adoption — and publishing who gains and who loses — is the difference between a negotiated change and an announced one.

## Impact If Solved
This determines how roughly $18B a year reaches the people who made the music, and the mechanism is currently unauditable to almost everyone it pays. Publishing the user-centric counterfactual would settle the industry's longest-running economic argument with evidence rather than advocacy. Relational fraud detection with a contestable process protects the pool and the artists wrongly caught by it. And an auditable statement removes the informational asymmetry that has made every royalty dispute of the last decade unresolvable.
