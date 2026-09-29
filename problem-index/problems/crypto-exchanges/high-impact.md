# Deposit Screening Without Ground Truth

**Industry:** [[crypto-exchanges|Crypto Exchanges]]
**Type:** High Impact
**One-liner:** Exchanges freeze deposits on a vendor's address risk score, almost never learn whether the funds were actually criminal, and have therefore never measured the precision of the control their entire compliance posture rests on.
**Tags:** #graph-neural-networks #graph-theory #gradient-boosting #causal-inference #confidence-intervals #evaluation-metrics #feature-engineering #compliance

## The Problem
A customer deposits. The exchange looks up the sending address with Chainalysis, TRM or Elliptic, which returns an attribution — this address belongs to a cluster associated with a darknet market, a sanctioned entity, a mixer, a ransomware payment, a gambling site, or nothing known — together with an indirect exposure measure computed across the address's transaction history.

Above a threshold, the deposit is held. The customer is asked for source-of-funds documentation. An analyst reviews. The outcome is release, permanent freeze pending law enforcement, or account closure.

The screening rests on two layers of inference, both of which are usually treated as fact. Clustering heuristics group addresses into entities using patterns such as common-input ownership and change detection; these are good but not perfect, and a wrong cluster assignment attributes someone else's history to your address. Attribution then labels the cluster, often from off-chain research whose method is proprietary. Indirect exposure propagates risk across hops using a model — proportional, poison, haircut — whose choice materially changes who gets flagged, and which the exchange typically does not choose.

Then comes the gap. Whether the deposit actually represented criminal proceeds is almost never determined. Law enforcement confirms a small number. A customer occasionally produces documentation good enough to satisfy an analyst, which is evidence about the documentation rather than about the funds. The rest — the overwhelming majority — resolve by the analyst releasing or not releasing, and that decision becomes the only record.

So the exchange has run a control for years, at real cost to customers and real cost in analyst time, without a precision estimate. Thresholds move when a loss occurs or when an examiner comments, in one direction only.

The asymmetry of who bears the error is the part that deserves stating plainly. A customer who received coins two hops from a mixer, or who used a privacy tool, or who was paid by an employer whose own exposure they cannot see, has their funds held and may have their account closed, with no meaningful appeal and no explanation of the evidence. Whether that person committed any offence is not established and is not, in the current process, establishable.

## Why It's Unsolved
Ground truth is genuinely scarce here in a way that is not merely an organisational failure. Criminality is determined by investigation and prosecution, which happens rarely and slowly and is not reported back to the exchange. This is a harder label problem than fraud, where a chargeback eventually arrives.

The inference layer is outsourced and opaque. Exchanges buy attribution rather than produce it, and the vendor's heuristics, labels and propagation model are proprietary. An exchange cannot validate a score whose derivation it cannot see, and vendors have limited incentive to publish false-positive rates.

The regulatory frame is one-sided, as it is across financial crime. There is an examination finding for missing illicit flows and none for freezing lawful customers, so the institutional gradient runs one way irrespective of the evidence.

And the counterfactual is unobservable in the usual way — a frozen deposit that would have been laundered is prevented, which is the point and also means the case never generates data. Meanwhile the cases that do resolve are the ones where a customer had the resources and persistence to contest, which is not a random sample.

## What a Solution Looks Like
Build the outcome record that does exist, however small. Law enforcement confirmations, subpoena correlations, customer documentation that was verified rather than merely accepted, subsequent account behaviour, and cases where the same customer was later confirmed in either direction. It is a small dataset and it is the only real one. Treating it as precious rather than incidental is the first change.

Measure the vendor. An exchange with even a few hundred resolved cases can estimate the precision of a vendor score at its operating threshold, compare vendors on its own population, and quantify how much of the flag volume comes from indirect exposure at three or more hops versus direct exposure. That last number alone usually reframes the internal conversation.

Choose the propagation model deliberately. Proportional, poison and haircut attribution produce very different flag populations from identical chain data. An exchange that has never chosen has chosen by default, and the choice is a policy judgement about how far taint should travel, not a technical detail.

Graduated response. Requesting documentation, limiting withdrawal to the originating address, or applying enhanced monitoring are all available and reversible; a full freeze on a customer's assets is the heaviest instrument and is currently applied to cases that do not require it because the system offers little else.

Explanation to the customer, to the extent law permits. Much of what is withheld is withheld by convention rather than by tipping-off rules, and a customer told that funds arrived two hops from a flagged service can usually explain it if they are given the chance.

## Impact If Solved
This control defines the exchange's relationship with both its regulators and its customers, and it operates without a measured error rate in either direction. Assembling the small genuine outcome set, measuring vendor precision on it, and making the propagation choice explicit converts an article of faith into a managed tradeoff — and materially reduces the number of lawful customers who lose access to their assets for reasons nobody can articulate to them.
