# The Claim With Evidence Behind It

**Niche:** [[niches/procurement-spend-platforms/supplier-diversity-verification/profile|Supplier Diversity Verification]]
**Industry:** [[industries/procurement-spend-platforms|Procurement & Spend Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A company publishes a diverse spend figure built on certification documents it has not rechecked and tier-two numbers its suppliers assert, and the figure influences contract awards and public reporting.
**Tags:** #data-integration #descriptive-statistics #evaluation-metrics #confidence-intervals #hypothesis-testing #compliance #graph-theory #automation
**Contested on:** Every serious competitor in supplier diversity software is fighting to make a diverse spend claim verifiable rather than self-reported — and whoever can evidence what actually reached diverse suppliers takes the programme.

## The Problem
A company reports diverse supplier spend of a stated percentage. Within it: several suppliers whose certification lapsed two years ago and were never rechecked; one that was acquired by a large group and no longer qualifies; a substantial tier-two component reported by three large suppliers on a methodology none of them has documented; and an attribution built on a supplier master that counts one diverse supplier as three records and another's subsidiary as a separate business. The number is reported externally, is used by customers in their own supplier decisions, and nobody involved could reconstruct it.

## Why Nobody Has Built This
Verification would lower reported numbers, which is a bad outcome for everyone who reports them and for the vendors who supply the reporting tools. Certification registries are maintained separately by many organisations with varying technical capability, so live checking requires integrations nobody has built. Tier-two has no methodology standard, which means each company constructs one and comparison is meaningless — and standardising it would expose the variation. And the constituency with the strongest interest in accuracy, diverse suppliers themselves, has no role in the measurement at all.

## What to Build
Verification at every link. Certification status checked live against the issuing registry rather than captured as a document, with expiry and revocation surfaced automatically — which requires registry integration and is the foundational fix. Spend attributed through the resolved supplier graph rather than through raw supplier records, so subsidiaries, duplicates and acquired entities are handled correctly in both directions. Tier-two reported against a stated methodology with the basis disclosed — what was included, how it was allocated, whether it was audited — so that a number is comparable or is honestly labelled as not. Change of ownership monitored, since acquisition is the most common reason a supplier ceases to qualify and is currently detected by chance. And the reported figure carries its own provenance: this proportion verified against a live registry, this proportion self-asserted, this proportion tier-two under this methodology — which is a more honest artefact and is what would let a customer relying on the number know what they are relying on.

## Target Customer
Supplier diversity management vendors, large organisations reporting diverse spend externally, the certifying organisations whose registries are the authoritative source, and the diverse suppliers whose participation is the subject.

## Impact If Built
A verified number will be lower than an asserted one and will mean something, which matters because these figures influence contract awards and public commitments. The certification currency check is the immediate fix and prevents the most common error, and the provenance disclosure is what would let the whole reporting practice be taken seriously rather than treated as a claim.
