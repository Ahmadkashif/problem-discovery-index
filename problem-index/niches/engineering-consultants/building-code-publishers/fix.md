# Product Evaluation Reports Are Written Once and Never Revisited

**Niche:** [[niches/engineering-consultants/building-code-publishers/profile|Building Code Publishers]]
**Industry:** [[industries/engineering-consultants|Engineering Consultants]]
**Type:** Fix (Pain Point)
**One-liner:** An evaluation report certifies that a product complies with specific code provisions, the code changes every three years, and nobody systematically re-derives which reports the new edition invalidated.
**Tags:** #graph-neural-networks #bert #transformers #word-embeddings #change-point-detection #evaluation-metrics #compliance #data-integration #workflow-orchestration #confidence-intervals

## The Problem
Evaluation reports are how a manufacturer proves to a building official that a product satisfies the code, and they are written against a specific edition and specific provisions. When the code cycle changes those provisions, some reports remain valid, some need revision, and some no longer support the conclusion they state. Determining which is which requires knowing, per report, the provisions its conclusion actually rests on — which is stated in the report as prose and not held as structured dependency. So the reconciliation happens partially, driven by manufacturer renewal cycles rather than by code change, and building officials in the field rely on reports whose current validity nobody has systematically confirmed.

## Why It's Still Broken
Reports are produced as documents for a manufacturer client and archived that way; the dependency on specific code provisions lives in the reasoning rather than in a field. The evaluation service is also organized around issuing and renewing reports on manufacturer-driven schedules, which is a commercial cadence rather than a technical one. And the volume across a large report library makes a manual sweep after each code cycle impractical, which has meant it does not happen rather than that it happens differently.

## What a Fix Looks Like
Reports linked at provision level to the code they were evaluated against, captured at issuance rather than reconstructed later — which is cheap at the point of writing and expensive afterward. Historic reports back-linked by mining the existing library against the code text. A code cycle change then resolves automatically to the affected reports, classified by whether the change is immaterial, requires revision, or invalidates the conclusion. That converts a triennial impossibility into a scoped queue, prioritized by how widely a report is relied on. Building officials and manufacturers gain the thing neither currently has — a statement of whether a given report is still good under the edition in force in their jurisdiction, which requires the adoption and amendment layers and is the point at which the three pieces compose into one product.

## Who Feels the Pain
Building officials accepting reports whose validity under their adopted edition is unverified; manufacturers discovering at renewal that a report needed revising two cycles ago; the evaluation service, whose credibility rests on reports being current; and engineers specifying products on the strength of a certification nobody has re-checked.

## Impact If Fixed
Protects the integrity of a certification system that building officials rely on, and turns the code cycle from a disruption into a routine reconciliation. Combined with adoption and amendment tracking, it produces a single answerable question — is this product acceptable here, today — which no one in the industry can currently answer.
