# Analytics That Restate Which Deals Were Easy

**Niche:** [[niches/contract-lifecycle-platforms/negotiation-benchmarking/profile|Negotiation Benchmarking]]
**Industry:** [[industries/contract-lifecycle-platforms|Contract Lifecycle Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Negotiation analytics report that contracts where the company held firm took longer and closed less often, which is presented as a finding about holding firm and is mostly a finding about which deals were hard.
**Tags:** #causal-inference #hypothesis-testing #confidence-intervals #descriptive-statistics #evaluation-metrics #logistic-regression #compliance #quick-win
**Contested on:** Every serious competitor here is fighting to tell a legal team what terms are actually achievable — with this counterparty, at this deal size, in this industry — and whoever assembles that corpus holds a position no single company can replicate.

## The Problem
The analytics dashboard shows that when the company insists on its preferred indemnity position, cycle time rises by nine days and the close rate falls. The obvious reading is that insisting is costly. The actual explanation is largely that the company insists when it has leverage and when the deal is strategically important, and concedes quickly on small routine deals — so the comparison is between two different populations of deals. A commercial leader reads the chart as evidence for conceding faster, and legal's position erodes on the basis of a confound.

## Why It's Still Broken
Analytics in this category are descriptive by design, and descriptive summaries of a selected population look like findings. Nobody involved in building them is thinking causally, because the feature was specified as reporting. The bias also runs in a commercially convenient direction — faster closing looks good — so nothing pushes back on it. And the legal team, who would notice, are not the ones reading the dashboard.

## What a Fix Looks Like
Make the comparison honest, which mostly means comparing like with like. Stratify by the characteristics that drive both the position and the outcome — deal size, counterparty type, strategic importance, competitive situation, urgency — and report within strata rather than in aggregate, which is the single change that fixes most of it. State the confound explicitly where stratification is insufficient, since an honest caveat is more useful than a clean chart that misleads. Prefer within-counterparty comparisons, which control for a great deal automatically and are available whenever a counterparty appears more than a few times. Encourage genuine variation where it is safe: for a routine, low-stakes clause, trying both positions across comparable deals produces a real answer and costs almost nothing, and is the only way to get one. Report uncertainty rather than point estimates, because most of these cells are small. And label descriptive analytics as descriptive, so nobody reads an association as a decision.

## Who Feels the Pain
Legal teams whose positions are eroded by charts that measure deal difficulty; commercial leaders making decisions on confounded evidence; and vendors whose analytics feature is quietly misleading its users.

## Impact If Fixed
Stratification and within-counterparty comparison are straightforward changes that remove most of the confounding, and explicit labelling costs nothing. The alternative is a feature that systematically argues for whichever behaviour correlates with easy deals.
