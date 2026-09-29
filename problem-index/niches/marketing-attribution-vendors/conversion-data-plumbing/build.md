# Rebuilt From Scratch at Every Client

**Niche:** [[niches/marketing-attribution-vendors/conversion-data-plumbing/profile|Conversion Data Plumbing]]
**Industry:** [[industries/marketing-attribution-vendors|Marketing Attribution Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every measurement model depends on a conversion record that is now partial, consent-dependent and silently modelled by each platform in its own favour, and the plumbing to fix it is rebuilt from scratch at every client.
**Tags:** #data-integration #workflow-orchestration #compliance #automation #evaluation-metrics #descriptive-statistics #confidence-intervals #quick-win
**Contested on:** Every serious competitor in this niche is fighting to build the conversion record once instead of rebuilding it at every client — and whoever does that owns the input every model in the category depends on.

## The Problem
An engagement starts. Before any modelling happens, someone must establish what a conversion is for this business, find where those events live, work out which are client-side and which server-side, handle the consent regime, deduplicate across sources, reconcile against finance, and decide what to do about the platform-reported conversions that may or may not be observations. This takes weeks, is done by a data engineer who will leave, is documented in a shared document nobody updates, and is redone entirely at the next client — even though the same twenty problems appear every time.

## Why Nobody Has Built This
Integration is treated as bespoke because each client's stack is different, which is true of the details and false of the structure — the same twenty problems recur and the conflation of a custom stack with a custom problem is why nothing is reused. The work is unglamorous and the category's identity is statistical. It is billed as services, so efficiency reduces revenue. And nobody owns the conversion record as a product.

## What to Build
Build the conversion record as a product. Define a standard conversion schema with the fields every model needs — event, value, timestamp, identity, source, consent state, observed-or-modelled — which is the foundation and is the thing no client has and every model needs. Build reusable connectors for the common stacks, since the long tail of bespoke work hides a short head of very common configurations. Handle consent as a first-class field rather than as a filter applied somewhere, because consent state determines what may be used for what and is currently lost in the pipeline. Separate observed from modelled conversions at ingestion, connecting to the path attribution work, which is a small field change with large consequences downstream. Deduplicate across sources with a stated method, since the same order arriving from three systems is the most common defect and is usually resolved by someone's judgement. Reconcile against the client's financial record as a standing check, which bounds every downstream number and is rarely automated. Monitor the pipeline for silent failure, which is the fix note's subject. Document by generating from configuration, so the record survives the engineer. Make it portable, so a client changing measurement vendors keeps their conversion record — which is good for the client and is exactly why incumbent vendors have not built it. And report conversion record completeness, because a model fitted to a record with known gaps should say so.

## Target Customer
Measurement vendors, client data and analytics teams, and the data platform vendors for whom the conversion record is an unclaimed standard.

## Impact If Built
A custom stack was conflated with a custom problem, so the same twenty issues are re-solved at every client. A standard conversion schema with consent state and an observed-or-modelled flag is what every model in the category needs and no client has.
