# Jurisdiction-Aware Tip Distribution Engine

**Niche:** [[niches/independent-restaurants/tip-pooling-workforce-management/profile|Tip Pooling & Workforce Scheduling Operations]]
**Industry:** [[industries/independent-restaurants|Independent Restaurants]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No product automatically applies the correct state and local tip pooling laws, tip credit calculations, and distribution rules to nightly tip pools — leaving restaurants exposed to six-figure DOL claims.
**Tags:** #automation #compliance #tabular-ml #worker-facing #data-integration

## The Problem
Tip pooling laws vary by state and have changed dramatically in recent years. California prohibits tip credits entirely. New York allows tip sharing with food runners and bussers but not kitchen staff. The 2024 DOL ruling expanded back-of-house tip pool eligibility in some contexts. A restaurant with a simple tip pool — "servers share 20% with bussers and 10% with bartenders" — may be operating illegally without knowing it, because the legality depends on whether the employer takes a tip credit, which roles are included, and whether the pool is mandatory or voluntary. Managers are distributing tips based on rules they set years ago and have never updated.

## Why Nobody Has Built This
The regulatory complexity is extreme: 50 states plus local jurisdictions, each with different rules, and the rules change frequently. Building a compliance engine requires maintaining a legal database that updates with legislation and DOL guidance — a content maintenance burden that most restaurant tech companies avoid. Additionally, the liability exposure is high: a tool that calculates tips incorrectly exposes the software company to the same complaints that hit the restaurant.

## What to Build
A tip distribution engine that takes the restaurant's jurisdiction, tip credit election, staff roles, and pooling preferences as inputs, validates the arrangement against current law, and calculates nightly distributions with full audit trail. When laws change, the system alerts the operator and reconfigures the pool rules. Integration with POS (for tip amounts) and scheduling (for who worked which shift) enables automatic calculation with no manual data entry.

## Target Customer
GMs of independent restaurants with 15+ tipped employees who currently calculate tip distributions manually and have not verified their pooling arrangement against current state law.

## Impact If Built
Preventing a single DOL complaint saves $50K-$250K in back-pay and penalties. Automating nightly tip calculation saves 15-30 minutes of manager time per night — 90-180 hours annually.
