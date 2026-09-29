# A Ticket Is Free Text Describing a Hole Somebody Wants to Dig

**Niche:** [[niches/utility-contractors/underground-locating-damage-prevention/profile|Underground Utility Locating & Damage Prevention]]
**Industry:** [[industries/utility-contractors|Utility Contractors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** The dig site is described in a sentence typed by a caller, and screening it against buried facilities is a geographic judgment made from prose.
**Tags:** #transformers #large-language-models #transfer-learning #graph-neural-networks #data-integration

## The Problem
The first analytical step in the whole system is screening: given a ticket, which facility operators have something buried inside the dig area and must be notified. Notify too few and a line goes unmarked. Notify too many and every operator's locators are dispatched to sites where they have no facilities, which is where a large share of the industry's wasted field hours go.

The difficulty is the input. A ticket describes the work location in free text — a street address, a cross-street, a distance and direction from a landmark, sometimes a hand-drawn polygon, often an approximation typed by a caller in a hurry. The extent of the dig is described in words. Screening compares that description to facility geometries whose own positional accuracy varies from surveyed to approximate to decorative.

So the screen is a geometric comparison between an imprecisely described area and an imprecisely mapped network, done with buffers tuned by hand — generous enough to be safe, which guarantees over-notification.

Every jurisdiction and every one-call centre has its own conventions, its own ticket format, and its own rules about how the dig area may be described.

## What Already Exists
Geocoding and geospatial libraries are mature. Language models handle short location descriptions well. One-call centres already run automated screening with polygon buffers, and mapping platforms handle facility geometry competently.

What is missing is the treatment of uncertainty. Existing screening resolves a description to an area and compares it deterministically. The real quantities — how precisely the caller described the site, and how accurately the facility is mapped — are both uncertain, and the decision that matters is a probability that a facility lies inside the actual dig.

## The Customization Gap
**Location description is a genre.** "Fifty feet north of the intersection, east side, from the pole to the driveway" is not an address, and parsing it requires models adapted to how excavators actually describe sites, per region.

**Both geometries carry uncertainty and it must be modelled.** The dig area has positional uncertainty from the description; the facility has positional uncertainty from its records vintage and survey method. The screen should compute an overlap probability, not a boolean.

**Records accuracy is estimable and is not estimated.** Historical mislocates and unmarked-facility damages reveal where maps are wrong. Feeding that back as a per-area accuracy prior is the single largest available improvement and requires no new data collection.

**The asymmetry is extreme and must be explicit.** A missed notification can kill someone; an unnecessary one wastes a truck roll. The threshold is a stated policy, and it should be visible and tunable rather than buried in a buffer distance.

**Every screen must be reproducible.** Screening decisions are examined after incidents. What was screened, against which map version, under which rule, has to be reconstructible.

**Facility networks are graphs.** Services branch from mains; a main's presence implies services to adjacent structures that may not be mapped at all. Reasoning over network topology catches facilities that geometry alone misses.

## Target Customer
Chief Technology Officer at a one-call centre, or VP of Data at a facility operator running its own screening.

## Impact If Solved
Over-notification wastes an enormous share of the industry's finite locator capacity, and under-notification is the mechanism behind unmarked-facility damages. Probabilistic screening with modelled records uncertainty improves both sides of that trade simultaneously — and produces, as a by-product, the map-accuracy estimates the whole system currently lacks.
