# Component Identification From Tags and Photos

**Niche:** [[niches/auto-parts-distributors/heavy-duty-parts-counters/profile|Heavy-Duty Truck & Trailer Parts Counters]]
**Industry:** [[industries/auto-parts-distributors|Auto Parts Distributors & Stores]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A fleet mechanic texts a photo of a corroded air valve with half a tag; the counter needs the current part and its interchanges in under a minute, and only one person on shift can do it.
**Tags:** #tacit-knowledge-ml #cnns #transfer-learning #contrastive-learning #k-nearest-neighbors #evaluation-metrics #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to get a down truck or trailer the right part from an OE number, a component tag or a photo, and whoever fills the largest share of fleet breakdown orders with the correct part on the first call takes the account.

## The Problem
Heavy-duty requests often arrive without a vehicle to decode: a photo of a brake chamber, a slack adjuster's worn stamping, a fleet's internal part number, an OE number superseded twice. The veteran recognises the component and its family by sight and knows which aftermarket brands interchange; newer staff call the supplier's tech line while the truck waits.

## Why Nobody Has Built This
There is no heavy-duty equivalent of a VIN-to-part catalog for many components, photos taken in a dark shop are poor, and resolutions are not logged, so there is no labelled set to learn from.

## What to Build
A counter tool that takes a photo, partial tag text or a number, reads markings with OCR, matches the image against a library of component photos with contrastive embeddings, resolves the result through interchange and supersession tables, and returns a ranked shortlist with stock. Every confirmation is logged with its photo, building the labelled library the trade lacks.

## Target Customer
Heavy-duty distributors and programme groups; component makers who want their parts identified correctly.

## Impact If Built
If identification on photo and tag requests fell from ~10–20 minutes to ~2 (estimate), a branch handling ~30 such requests a day would recover ~5 hours of senior counter time daily.
