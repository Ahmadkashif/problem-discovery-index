# Cycle Counting Targeted by Expected Error

**Niche:** [[niches/retail-pos-platforms/store-associate-tools/profile|Store Associate Tools]]
**Industry:** [[industries/retail-pos-platforms|Retail POS Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Statistical cycle counting — counting the items most likely to be wrong rather than everything in rotation — is settled inventory practice in warehousing and enterprise retail, and independent stores count a fixed section every week.
**Tags:** #descriptive-statistics #hypothesis-testing #gradient-boosting #confidence-intervals #evaluation-metrics #optimization-fundamentals #automation #worker-facing
**Contested on:** Every serious competitor building for store staff is fighting to let an associate answer a customer's question from the sales floor without walking to the back — and whoever the associates actually use takes the store.

## The Problem
The store counts a section a week on a rotation, so every item is counted with the same frequency regardless of how likely it is to be wrong. Items with high theft exposure, high unit velocity, recent receiving errors or frequent returns drift out of accuracy within days; slow-moving items stay accurate for a year. The rotation spends the same effort on both. Associates spend evenings counting things that were right, and the items that matter are wrong again before their turn comes round.

## What Already Exists
ABC and statistical cycle counting are standard inventory management practice with decades of literature and implementation in warehouse management and enterprise retail systems. Count sampling methodology, accuracy measurement and variance-driven recount logic are all established. Mobile counting with barcode scanning is commodity. Nothing in the approach is new; it has simply never been packaged for a store without an inventory manager.

## The Customization Gap
The adaptation is to predict error at item level in a small store. It requires: (1) an error-likelihood model per item built from the store's own count history plus cross-store patterns — velocity, price point, category theft exposure, return rate, recent receiving activity, and time since last count — which is where the platform's multi-merchant data does the work a single store cannot; (2) count assignments sized to the available minutes rather than to a section, since the real constraint is that an associate has twenty minutes before close; (3) discrepancy triage that distinguishes a probable data error from probable shrink, because the two need different responses and lumping them produces the dead-end investigations described elsewhere in this niche; (4) recount logic that verifies a surprising result before it is posted, since an erroneous count corrupts the very accuracy the exercise is for; and (5) accuracy reported as a store-level metric over time, which almost no independent tracks and which is the only way to know whether counting is working.

## Target Customer
Independent retailers and small chains with meaningful SKU counts, and the POS vendors whose counting features are section rotations.

## Impact If Solved
Targeted counting raises inventory accuracy substantially for the same or less counting labour, which is the trade every store would take. Accuracy is also the precondition for the floor tool, the multichannel sync and the merchandising work elsewhere in this industry — it is the foundation that several other capabilities are silently blocked on.
