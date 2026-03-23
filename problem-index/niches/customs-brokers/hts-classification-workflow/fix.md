# Classification Inconsistency Across Analysts

**Niche:** [[niches/customs-brokers/hts-classification-workflow/profile|HTS Classification Workflow]]
**Industry:** [[industries/customs-brokers|Customs Brokers]]
**Type:** Fix (Pain Point)
**One-liner:** Different classification analysts at the same brokerage classify the same product differently — Analyst A codes a leather phone case under 4202 (articles of leather) while Analyst B codes an identical product under 4205 (other articles of leather) — creating inconsistent duty rates, CBP audit exposure, and client confusion.
**Tags:** #automation #compliance #data-integration #quick-win

## The Problem
A customs brokerage with 5 classification analysts classifies 500+ products per month. When the same product is classified by different analysts on different occasions (the same client imports the same product from different suppliers, or the product appears in a new entry months later), each analyst may reach a different HTS code. The classification depends on interpretation — "essential character," "principal use," and "component of chief value" are judgment calls where experienced analysts can reasonably disagree. A 2023 industry study found that classification consistency across analysts at the same brokerage is 82-87% — meaning 13-18% of products would receive a different code from a different analyst. Each inconsistency creates a compliance risk: if CBP finds that the same product was classified under two different codes by the same broker, it raises questions about the broker's "reasonable care" obligation.

## Why It's Still Broken
No system tracks whether a product has been previously classified and what code was assigned. When Analyst B encounters a product that Analyst A classified 3 months ago, Analyst B doesn't know about the prior classification — they classify from scratch, potentially reaching a different conclusion. The prior classification decision is buried in the entry records, not surfaced to the current analyst as a reference. There's no "classification dictionary" that stores the brokerage's classification decisions by product type.

## What a Fix Looks Like
A classification consistency system that: (1) maintains a brokerage-wide classification dictionary — a searchable database of all prior classification decisions by product description; (2) alerts the analyst when a product has been previously classified ("this product was classified as 4202.31 by Analyst A on 12/15/2025 — use the same code or document the reason for a different classification"); (3) tracks classification consistency metrics per analyst and per product category; (4) flags products where different classifications have been applied, prompting a senior analyst to establish the definitive classification.

## Who Feels the Pain
Compliance managers who discover classification inconsistencies during internal audits or when CBP flags the discrepancy. And clients who receive different duty rates for the same product across shipments and question the broker's competence.

## Impact If Fixed
Improving classification consistency from 85% to 97%+ reduces CBP audit risk and eliminates the "different analyst, different code" problem that undermines client confidence. Each inconsistency that triggers a CBP inquiry costs 4-8 hours of analyst time to research and resolve.
