# Per-Block Economics on a Thirty-Year Asset

**Niche:** [[niches/agtech-platforms/specialty-permanent-crops/profile|Specialty & Permanent Crops]]
**Industry:** [[industries/agtech-platforms|Agtech Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A replant decision commits a block for thirty years and several thousand dollars an acre, and it is made from a manager's sense of which blocks are tired rather than from any per-block record of what each one has returned.
**Tags:** #survival-analysis #time-series-forecasting #gradient-boosting #confidence-intervals #evaluation-metrics #descriptive-statistics #revenue-impact #optimization-fundamentals
**Contested on:** Every serious competitor in specialty crop software is fighting to manage a permanent planting at the block and the tree rather than at the field — and whoever makes per-block economics and harvest labour legible takes the operation.

## The Problem
An orchard has forty blocks planted between 1998 and 2021, across eight varieties on several rootstocks. Which blocks are earning their keep, which are declining, and which should be replanted next — and to what — is the operation's most consequential recurring decision. It is made from yield recollection, a sense of which blocks are hard to harvest, and the varieties the marketer says are wanted. The per-block record that would answer it — yield, quality grade-out, labour hours, input cost, and revenue by year over the block's life — exists in fragments across a spreadsheet, a packing house statement and a labour record, and has never been assembled.

## Why Nobody Has Built This
Block-level accounting requires attributing labour and input costs to blocks, which means capturing where crews worked and what was applied where — a field data capture problem in an operation with a large seasonal workforce and limited administrative staff. Revenue attribution is harder still, because fruit is frequently pooled at the packing house and returns come back as a settlement covering a lot rather than a block. Both are solvable and neither has been solved, so the industry's longest-horizon decision is made on the shortest-horizon evidence.

## What to Build
A block as a financial and agronomic entity with a life history. Costs attributed at capture: crews record the block they worked, applications record the block treated, which requires the field capture to be trivially easy and is the main implementation effort. Revenue attributed through the packing house settlement where lot identity is preserved, and estimated with stated assumptions where it is not — being explicit about the estimation is better than the current silence. From that, per-block return per acre by year, over the planting's life, with the cost of harvest separated out because harvestability differs enormously between blocks and drives more of the economics than yield does. Replant analysis follows: the return on replacing this block with that variety, given establishment cost, the years to production, and the performance of comparable blocks. Variety and rootstock performance accumulates across the operation and, across a platform, across the region — which is information no individual operation can produce and every one of them wants.

## Target Customer
Orchard and vineyard operations of any scale, the specialist platform vendors serving them, and the nurseries and marketers whose variety recommendations currently rest on thin evidence.

## Impact If Built
The replant decision allocates capital for thirty years and is made on impression. Per-block economics converts it into an analysis, and the harvest cost separation in particular routinely changes the ranking — blocks with good yield and poor harvestability are frequently worse than they appear. The accumulated variety performance record is the long-run asset and is the kind of knowledge that currently retires with a manager.
