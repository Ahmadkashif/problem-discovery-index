# Indices Weighted by Committee When the Economics Are Measurable

**Niche:** [[niches/livestock-operations/livestock-genetic-evaluation/profile|Livestock Genetic Evaluation Programmes]]
**Industry:** [[industries/livestock-operations|Livestock Operations]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Selection indices tell producers which animals to breed by combining a dozen traits with weights set by committee judgment.
**Tags:** #tabular-ml #causal-inference #gradient-boosting #evaluation-metrics #revenue-impact

## The Problem
A genetic evaluation produces dozens of trait predictions — growth, carcass, maternal, fertility, docility, feed intake — and no producer can select on all of them. So the associations publish selection indices: single numbers combining traits with economic weights, meant to represent profitability under a defined production and marketing scenario.

The indices are the most consequential product. Producers select bulls on them, and those decisions compound through the national herd for decades.

The economic weights are derived from bioeconomic models built on assumed prices, assumed cost structures, and assumed marketing endpoints, reviewed periodically by committees. They are thoughtful and they are assumptions. Whether the index actually ranks animals by realized profitability for the producers using it has not been measured, because the outcome data — what the progeny of a given sire actually earned at the packer, at a given feed cost — sits with feeders and packers rather than with the association.

## Why Nobody Has Built This
Quantitative genetics has an authoritative internal answer. Evaluation accuracy is measured rigorously — prediction error variance, reliability, and validation against later progeny performance on the traits themselves — and the profession's standards are about the genetic prediction rather than about the economics layered on top.

The economic layer arrived later and was built by a different discipline. Bioeconomic modelling is agricultural economics, it is peer-reviewed, and it is separated from the data operation by both organizational structure and academic convention.

And the outcome data is genuinely elsewhere. Carcass results belong to packers, feeding performance to feedlots, and neither has any obligation to share. That has been treated as a wall rather than as a partnership problem.

## What to Build
Fit the economic weights to realized outcomes instead of assuming them.

**Assemble sire-linked outcome data.** Carcass grading and yield results are captured on every animal that goes through a plant, and feeding performance is captured by feedlots. Where source herds are identified — increasingly common under verified and grid marketing programmes — the link back to genetics exists. Building that data partnership is the foundational work.

**Estimate realized trait economics.** What a unit of a given trait was actually worth, under real prices and real cost structures, rather than under a modelled scenario. Prices move enormously and the weights are revised on a multi-year cycle.

**Publish scenario-specific indices with uncertainty.** A cow-calf operator retaining ownership through the feedlot and one selling weaned calves face different economics, and the index that serves both serves neither well. Fitted weights make segmentation honest rather than arbitrary.

**Validate the index directly.** Rank sires by index, observe realized progeny profitability, and report how well the ranking held. Nobody in this industry has ever published that, and it is the single number that would justify the whole apparatus.

## Target Customer
Director of Genetic Evaluation or Chief Science Officer at a breed association or dairy evaluation body. The competitive context is that the large genetics companies increasingly run proprietary indices on their own nucleus data, and the associations' authority rests on being the neutral, evidenced standard.

## Impact If Built
Selection decisions made on these indices shape the national herd for generations, and the economic weights driving them are assumptions nobody has tested. Fitting them to realized outcomes would change which animals get bred across a $100 billion industry — and the data required exists, split across three parties who have never been asked to join it.
