# Draft Designs From Similar Past Jobs

**Niche:** [[niches/electric-utilities/new-service-connection-design/profile|New Service Connection Design & Estimating]]
**Industry:** [[industries/electric-utilities|Electric Distribution Utilities]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A designer redraws a standard subdivision layout from scratch when the utility has built hundreds of nearly identical ones.
**Tags:** #k-nearest-neighbors #graph-neural-networks #large-language-models #feature-engineering #automation #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to turn a builder's or customer's new-service request into a designed, estimated and scheduled job in days, and whoever cuts request-to-energise time without redesigns in the field takes the account.

## The Problem
Most new-service jobs are variations on a few patterns: a single-family home off an existing transformer, a 40-lot underground subdivision, a strip-mall service, a commercial EV-charger upgrade. Designers recreate each from standards and experience. Senior designers know which layouts work on which soils, easements and feeder types. Juniors don't, so designs come back from the field with changes.

## Why Nobody Has Built This
Past designs live as GIS edits and work orders, not as reusable templates, and design tools treat each job as new. Field redesigns are recorded as change orders without being linked back.

## What to Build
Index past designs as graphs (transformers, spans, services, units) with job attributes (lot count, load, site type, feeder) and field outcomes (as-built changes, cost variance). For a new request, retrieve the closest past designs. Generate a draft layout, compatible-unit list and customer contribution from them, adapted to the site plan, and flag elements that often changed in the field.

## Target Customer
Design managers at utilities with growth-driven new-service backlogs and a retiring designer workforce.

## Impact If Built
Standard jobs designed in hours rather than the ~1–3 weeks of design time they take today, and ~25%–40% fewer field redesigns (estimate), with juniors producing senior-quality layouts.
