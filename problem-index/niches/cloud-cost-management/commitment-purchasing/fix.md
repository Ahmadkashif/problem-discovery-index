# Coverage Reported as a Single Percentage

**Niche:** [[niches/cloud-cost-management/commitment-purchasing/profile|Commitment Purchasing]]
**Industry:** [[industries/cloud-cost-management|Cloud Cost Management]]
**Type:** Fix (Pain Point)
**One-liner:** Commitment coverage is reported as one number for the whole estate, which conceals that some workloads are over-committed and stranded while others pay list rates.
**Tags:** #descriptive-statistics #hypothesis-testing #confidence-intervals #evaluation-metrics #time-series-forecasting #quick-win #revenue-impact #automation
**Contested on:** Every serious competitor here is fighting to turn a multi-year capacity commitment into a decision made under stated uncertainty rather than an extrapolation of last quarter — and whoever does that takes the largest single controllable lever in the category.

## The Problem
The dashboard reports commitment coverage at seventy-four percent, which looks healthy and is the number reviewed monthly. Underneath it, one instance family is over-committed and the excess is being wasted every hour; another has grown substantially and is running entirely at list rates; a third region has no commitments at all because nobody noticed it existed. The aggregate conceals all three, because over-commitment in one place and under-commitment in another average into a comfortable figure, and the organisation is simultaneously wasting money and paying too much.

## Why It's Still Broken
Coverage was defined as a headline metric for executive reporting, where a single number is what is wanted, and it has become the operational metric by default. Decomposing it requires attributing commitments to the usage they actually cover, which is complicated by the flexible instruments that float across families and regions, so most tools report the aggregate and stop. And the two errors offset each other in the aggregate, which is precisely why the aggregate is the wrong metric.

## What a Fix Looks Like
Report coverage by the dimensions along which commitments are actually made. Coverage per instance family, per region and per term, with under- and over-commitment shown separately rather than netted, which immediately reveals the offsetting errors the aggregate hides. Waste explicitly: commitment purchased and not used, per hour, in money, which is a number nobody reports and is usually uncomfortable. Uncovered spend at list rates, ranked by size, which is the opportunity list. Expiry schedule with the concentration visible, since a large share of commitment expiring in one month is a renewal decision under time pressure and is avoidable by laddering. Utilisation trend per commitment, so a commitment drifting toward waste is visible before it expires rather than after. And the effective rate achieved against the list rate, which is the outcome measure the whole activity exists to produce and is more meaningful than coverage in any form.

## Who Feels the Pain
Cloud economics teams reporting a healthy number over an unhealthy position; finance functions paying for unused commitment and list rates simultaneously; and organisations whose largest cost lever is managed by an averaged metric.

## Impact If Fixed
Decomposing coverage by family, region and term is a grouping of data every tool already holds, and it reveals the offsetting errors the aggregate is designed to hide. Reporting waste and uncovered spend separately gives two actionable lists where there was one comfortable percentage.
