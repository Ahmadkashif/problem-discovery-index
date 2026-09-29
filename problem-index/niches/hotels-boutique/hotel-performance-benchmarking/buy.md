# Competitive Set Construction as a Modelling Problem

**Niche:** [[niches/hotels-boutique/hotel-performance-benchmarking/profile|Hotel Performance Benchmarking & Demand Data]]
**Industry:** [[industries/hotels-boutique|Boutique Hotels]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** The entire product rests on which hotels a property is compared against, and that set is chosen by the hotel's own general manager.
**Tags:** #k-means-clustering #ml-recommendation #graph-ml #evaluation-metrics #data-integration

## The Problem
Everything downstream of the competitive set inherits its errors. RevPAR index, penetration, fair share — all of it is performance relative to a group of four to eight hotels, and that group is nominated by the property, subject to eligibility rules and a manual review.

General managers are not neutral about this. A flattering set makes the index look good, which affects owner reporting, incentive compensation, and how a management contract is read. Sets also go stale: hotels renovate, reposition, change brand, or lose relevance as a market's supply shifts, and the set often does not move for years.

The reviewers know the weak sets. They cannot systematically identify them across hundreds of thousands of properties, so the review catches what it happens to see.

## What Already Exists
Peer group construction is a solved problem in adjacent domains. Financial benchmarking builds peer sets from characteristics and return correlation; retail site analytics builds trade area comparables; clustering and similarity learning are standard, well-tooled techniques.

## The Customization Gap
Hotel competition has properties that none of the standard approaches encode.

**Similarity is behavioural, not just descriptive.** Two hotels of the same class a mile apart may not compete, because one serves airport traffic and the other serves a convention centre. What identifies genuine competitors is correlated demand — occupancy that moves together on the same nights — and the panel measures exactly that. Attribute similarity is a starting point; observed co-movement is the answer, and no off-the-shelf peer tool looks at it.

**The set must remain defensible to the customer.** This is not an internal model. A hotel will contest a set it does not recognize, so the output has to be explainable in the customer's own terms — comparable class, comparable location, comparable segment — while being selected on evidence. That constraint rules out most of the obvious methods and is rarely faced by generic peer tooling.

**Disclosure rules constrain the composition.** Sets must be large enough and mixed enough that no individual contributor's performance is inferable. The optimizer is therefore constrained in ways that have nothing to do with similarity, and the constraints are part of the problem specification rather than a post-hoc filter.

**Sets have to age.** A hotel renovating, rebranding, or repositioning changes what it competes with. Detecting that from its own performance pattern and prompting a review is a change-detection problem the current process handles by waiting for someone to ask.

**Gaming needs to be measurable.** A property whose chosen set consistently underperforms comparable evidence-based sets is a pattern, and it is one the business should be able to see — not to accuse anyone, but because the integrity of the index is the whole product.

## Target Customer
Head of Data Science or VP of Product at the benchmarking business, where competitive set quality is understood internally as the soft spot in an otherwise unassailable dataset.

## Impact If Solved
The index is the number the industry runs on — owner reporting, management contracts, lender covenants, incentive compensation. Making the comparison evidence-based rather than self-nominated improves the quality of every decision made on it, and it removes the one legitimate criticism customers make of the product.
