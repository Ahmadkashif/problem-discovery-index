# Entity Resolution Adapted to Provider and Clinic Restructuring

**Niche:** [[niches/chiropractic-practices/auto-injury-claims-data/profile|Auto Injury Claims Data & Medical Review Analytics]]
**Industry:** [[industries/chiropractic-practices|Chiropractic Practices]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Master data management resolves records that refer to the same entity; here the entity deliberately reconstitutes itself — new tax ID, new clinic name, same people, same address — specifically so that resolution fails.
**Tags:** #graph-neural-networks #graph-theory #contrastive-learning #random-forests #k-means-clustering #bert #evaluation-metrics #feature-engineering #data-integration #compliance

## The Problem
Every analysis the vendor sells depends on knowing who a provider is. In this segment that is adversarial. A clinic under scrutiny closes and reopens with a new tax identification number, a new corporate name, and a different billing agent, retaining the same practitioners, the same address, and the same referral relationships. Individual practitioners move between clinics that share ownership. Billing companies front for multiple entities. Standard identifiers are exactly the fields the restructuring changes. Analysts reconstruct the connections by hand when a case warrants it, which means the reconstruction happens only after suspicion exists rather than being the thing that generates it.

## What Already Exists
Entity resolution and network analytics are mature. Senzing, Quantexa, Palantir, and the enterprise MDM platforms all handle probabilistic matching, relationship graph construction, and investigative link analysis at scale, with strong tooling for financial crime use cases. Several are used in insurance fraud today and work well for what they do.

## The Customization Gap
These tools resolve entities from noisy observations of stable underlying facts. The pattern here is a stable underlying group deliberately generating discontinuous identifiers, which inverts the assumption — the identifiers are clean and the discontinuity is intentional. Resolution therefore cannot lean on identifier similarity; it has to lean on the things that are expensive to change: physical location and its history, practitioner licence numbers, equipment and facility registration, referral and treatment pattern signatures, and temporal continuity of activity across the transition. Those are domain-specific features no general product models. The adaptation is a provider identity graph built on persistence rather than similarity, with continuity scored explicitly — this new entity began operating at this address the week the prior one stopped, with four of six overlapping practitioners — and with confidence stated rather than merged silently, because a wrong linkage here is an accusation. It must also run continuously across the whole book rather than on demand in an investigation, which is the difference between detection and confirmation.

## Target Customer
Heads of data science and product at claims data vendors, and the special investigation units at insurer clients who currently reconstruct these networks manually and only after they already suspect something.

## Impact If Solved
Moves the vendor's most valuable analysis from case-triggered to continuous, which changes what the product detects — a network that reconstitutes to escape scrutiny is invisible to identifier-based resolution by design and obvious to a persistence-based graph. Explicit confidence also addresses the legitimate objection to this whole category, which is that silent linkage of unrelated providers is itself a harm.
