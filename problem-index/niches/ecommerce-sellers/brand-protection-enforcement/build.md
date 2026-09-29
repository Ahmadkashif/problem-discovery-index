# Seller Network Persistence as the Enforcement Target

**Niche:** [[niches/ecommerce-sellers/brand-protection-enforcement/profile|Brand Protection & IP Enforcement Providers]]
**Industry:** [[industries/ecommerce-sellers|E-Commerce Sellers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Enforcement removes listings and the operator behind them opens new accounts the same week, so the industry measures takedowns while the underlying network is never targeted.
**Tags:** #graph-neural-networks #graph-theory #contrastive-learning #bert #transformers #evaluation-metrics #k-means-clustering #feature-engineering #data-integration #revenue-impact

## The Problem
Counterfeit selling is a network operation and enforcement treats it as a listing problem. A takedown removes an item; the operator relists under a new account, a new business name, and slightly altered imagery, frequently within days. Clients are reported takedown volumes, which rise steadily and describe nothing about whether the underlying activity fell. The firm holds the information that would connect accounts into operators — shared imagery and text patterns, fulfilment addresses, pricing behaviour, listing timing, and the sequencing of one account going dark as another appears — and uses it only when an analyst manually investigates a case that seems large enough to warrant it.

## Why Nobody Has Built This
Marketplace data is deliberately thin on the fields that would make linkage easy, and adversaries structure specifically to defeat identifier-based matching, so the signals that work are behavioural rather than registrational. Commercially, the metric the industry sells on is takedown volume, which is easy to compare in a procurement process and which network-level enforcement would initially reduce — fewer, better-targeted actions look worse on a scorecard designed for the old model. And the platforms themselves control the enforcement mechanism, so a network finding is only actionable to the extent a marketplace accepts it.

## What to Build
An operator graph maintained continuously rather than assembled per investigation. Accounts are linked on the features that are expensive for an adversary to change — imagery reuse detectable through perceptual hashing, text and description templating, fulfilment and return address overlap, pricing and inventory behaviour, and the temporal signature of account rotation — with confidence explicit, because a wrong linkage is an accusation against a legitimate seller. Enforcement then targets the operator rather than the listing, bundling evidence across accounts into a single submission that a marketplace can act on more decisively than a series of individual complaints. Measurement changes with it: recurrence rate and time-to-relist per operator become the reported outcome, which is what a rights holder actually cares about and what no competitor currently reports. The graph also supports prediction — a newly appeared account matching a known operator's signature can be flagged before it accumulates sales.

## Target Customer
VPs of brand protection and operations leaders at enforcement providers running 200-800 analysts, and the brand protection executives at rights holders who receive takedown counts and cannot tell whether infringement is falling.

## Impact If Built
Changes what the service sells from activity to outcome, which is a defensible price increase rather than a volume play. The operator graph is also strictly proprietary — it can only be built by a party observing enforcement across many brands and marketplaces — and it gets better with every client added, which is the compounding asset this segment currently lacks.
