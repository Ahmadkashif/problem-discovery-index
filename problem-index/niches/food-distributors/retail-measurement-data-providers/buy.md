# Item Coding Adapted to Continuous Assortment Churn

**Niche:** [[niches/food-distributors/retail-measurement-data-providers/profile|Retail Measurement Data Providers]]
**Industry:** [[industries/food-distributors|Food Distributors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Product classification tooling assumes a catalogue that mostly holds still; food assortment turns over continuously, and a misclassified new item corrupts exactly the category a client is watching.
**Tags:** #bert #transformers #contrastive-learning #cnns #random-forests #word-embeddings #evaluation-metrics #transfer-learning #automation #data-integration

## The Problem
Everything rests on placing each item in the taxonomy correctly — category, subcategory, form, flavour, claims, pack size, brand hierarchy. Food assortment churns constantly: new items, reformulations, pack changes, private label ranges, and seasonal items enter every week, and each must be coded before it can be measured. Coders work from item descriptions, images, and manufacturer data of uneven quality, at a volume that forces prioritization. A misplaced item does not merely lose a row; it moves share between competitors in the category a client is paying to watch, and it is discovered when that client disputes their number.

## What Already Exists
Product classification is a well-served commodity. The retail AI vendors, the general vision and text models, and the PIM platforms all handle attribute extraction and category assignment with good accuracy, and taxonomy management tooling is mature.

## The Customization Gap
Off-the-shelf classifiers optimize average accuracy, and the cost structure here is not average — an error in a low-volume category nobody subscribes to is nearly free, and an error in a heavily subscribed category between two competing brands is a client dispute. So the routing decision has to be economically weighted, which no general tool expresses. The adaptation is classification with calibrated confidence and consequence-weighted routing: high-confidence placements in low-stakes cells flow through, and anything uncertain in a heavily watched category goes to a coder. Brand hierarchy needs domain treatment, since the commercially decisive question is frequently which corporate parent an item rolls up to, and that changes with acquisitions rather than with the product. Every coder decision is captured with its full input context, building the labelled corpus that classification operations of this kind routinely discard. And a standing consistency check over the existing coded base surfaces where historical placements disagree with current convention, which is how accumulated drift becomes visible.

## Target Customer
Heads of data operations and taxonomy at retail measurement providers, and the client insight teams who discover coding errors by finding their share number implausible.

## Impact If Solved
Removes the largest silent error source in the flagship product and concentrates expert coding time where a mistake actually costs something. Retrospective consistency checking also addresses the quiet liability underneath every trend series the client has been buying.
