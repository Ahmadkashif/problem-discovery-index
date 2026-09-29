# Attribution With a Confidence

**Niche:** [[niches/crypto-exchanges/address-attribution/profile|Address Attribution & Taint Propagation]]
**Industry:** [[industries/crypto-exchanges|Crypto Exchanges]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An address label arrives as a fact when it is an inference, and no downstream decision knows how strong that inference was.
**Tags:** #graph-theory #graph-neural-networks #confidence-intervals #bayesian-inference #evaluation-metrics #k-means-clustering #compliance #gradient-boosting
**Contested on:** Every serious competitor in this niche is fighting to say who actually controls an address and how far illicit taint legitimately travels through a public ledger — and whoever attributes most accurately, with a confidence they can defend, owns the input every downstream decision consumes.

## The Problem
The exchange's screening consumes a categorical label: this address is associated with a mixer, a sanctioned entity, a darknet market. That label was produced by clustering heuristics and investigative work, with a confidence that ranges from near-certain to speculative and is not transmitted. A near-certain sanctions match and a weak behavioural inference arrive as the same kind of fact, and the threshold that acts on them cannot distinguish. The exchange, meanwhile, holds the strongest attribution evidence in existence — deposits and withdrawals joining verified identities to addresses — and sells it upstream for free by using the product.

## Why Nobody Has Built This
Attribution was purchased, so it was never modelled in-house — the make-or-buy decision was settled a decade ago and nobody revisited what the exchange's own data could produce. Vendors have no incentive to publish confidence, because a label with an admitted error rate is a weaker product. The clustering heuristics are genuinely difficult and adversarially targeted. And the exchange's own junction data has been treated as an operational record rather than as the category's most valuable training signal.

## What to Build
Model attribution and carry the uncertainty. Build attribution from the exchange's own junction evidence — the addresses its verified customers deposit from and withdraw to — which is the core and is the ground source most vendor labels ultimately derive from. Express every attribution as a probability with the evidence that produced it, since the downstream decision cannot be set sensibly on a categorical label of unknown strength. Model entity clustering explicitly rather than inheriting heuristics, because the heuristics are contested, adversarially targeted and change as the chains change. Combine vendor labels with own-evidence rather than replacing them, as the vendors' cross-exchange view is real and the exchange's identity join is complementary. Surface vendor disagreement as a signal, which is free information currently discarded. Model propagation as decay over hops and volume rather than as binary taint, since the substantive question is how much risk survives distance. Validate attribution against the resolved cases, using the same scarce labels the decision problem needs. Handle the chains' different structures properly, because a UTXO chain and an account chain support entirely different inferences. Publish the method internally so a freeze can be defended, since an inference nobody can explain cannot be adjudicated. And track attribution accuracy over time, because heuristics decay as the adversary adapts.

## Target Customer
Exchange compliance and data leadership, blockchain analytics vendors whose labels arrive without confidence, and law enforcement consuming attributions as facts.

## Impact If Built
The make-or-buy decision was settled a decade ago and never revisited. The exchange's own deposit and withdrawal junction is where most vendor labels originate, and using it directly with expressed confidence changes what every downstream decision can do.
