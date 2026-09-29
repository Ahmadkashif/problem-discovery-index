# Spend Classification and the Supplier Master

**Industry:** [[procurement-spend-platforms|Procurement & Spend Platforms]]
**Type:** High Impact
**One-liner:** Classify at the line item rather than the supplier, and resolve the supplier master into real entities — because every negotiation, consolidation and savings claim in the category rests on two layers that are quietly wrong.
**Tags:** #bert #word-embeddings #large-language-models #dbscan #k-nearest-neighbors #gradient-boosting #feature-engineering #evaluation-metrics #data-integration

## The Problem
Spend analytics answers one question: what do we buy, from whom, and where is the leverage. Every procurement platform sells it. It rests on two foundations and both are broken.

The first is classification. Transactions are mapped to a category taxonomy — UNSPSC, or the company's own — usually by rules keyed off the supplier name. That works for a supplier who sells one thing and fails for the ones who matter. A large distributor sells office supplies, safety equipment, MRO parts and janitorial chemicals to the same company, and all of it lands in one category. So the company's "office supplies" spend includes bearings, and the category manager negotiating office supplies is working from a number that describes something else.

The second is the supplier master. The same vendor exists as eleven records: different spellings, different subsidiaries, different remit-to addresses, entries created by three ERP migrations. Total spend with that supplier is therefore unknown, which means the company negotiates from a fraction of its actual volume and does not know it.

Everything downstream inherits both errors. Consolidation opportunities are invisible because the duplicate suppliers look small. Tail spend analysis is meaningless. Savings reports are computed against baselines built on misclassified categories. Executives are shown a spend cube that is confidently wrong in ways nobody can see.

## Why It's Unsolved
Classification at supplier level is cheap and works well enough to demonstrate. Line-item classification requires reading the description on the invoice line, and invoice line descriptions are abbreviated, supplier-specific free text — the same fastener described six ways by six distributors. Doing it properly is entity resolution over a large, drifting catalogue, and no vendor has funded it because the supplier-level version passes the demonstration.

Supplier resolution has a specific failure mode that makes vendors cautious: merging two records that are genuinely different suppliers corrupts payment routing, and in a system that pays money that is a serious incident. So thresholds are set conservatively and duplicates survive.

There is also a structural incentive problem. Procurement teams are measured on reported savings, savings are computed against a baseline, and better classification frequently reveals that historical savings were overstated. Nobody in the chain is rewarded for discovering that.

And the cross-customer asset goes unused. A supplier's item catalogue and a commodity's price distribution are observable across thousands of enterprises on the same platform, which would make classification and benchmarking dramatically easier, and the vendors treat each customer's data as an island.

## What a Solution Looks Like
Line-item classification from the description, the supplier, the price and the unit — trained across the customer base, so a line seen ten thousand times elsewhere is not classified from scratch at the ten-thousand-and-first enterprise.

Supplier resolution as continuous entity resolution with the merge asymmetry explicit: high precision, full reversibility, and payment routing frozen until a merge is confirmed by a human. The corporate family structure that matters is who the company actually contracts and pays, not the legal hierarchy a data provider sells.

And the benchmark that only the platform can produce: what comparable enterprises pay for this item, from this supplier, in this region. That is the single most valuable output the category could deliver and the one none of them offers.

## Impact If Solved
Every procurement decision, negotiation and savings claim rests on the spend cube, and the spend cube is built on supplier-name rules and a duplicated master. Fixing the foundation changes what the entire category's analytics mean, and the cross-customer price benchmark is a genuinely defensible product that no single enterprise could ever build.
