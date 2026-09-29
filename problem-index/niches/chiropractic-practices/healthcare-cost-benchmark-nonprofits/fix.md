# Thin Geographies Get the Same Confidence as Dense Ones

**Niche:** [[niches/chiropractic-practices/healthcare-cost-benchmark-nonprofits/profile|Healthcare Cost Benchmark Data Organizations]]
**Industry:** [[industries/chiropractic-practices|Chiropractic Practices]]
**Type:** Fix (Pain Point)
**One-liner:** A percentile for a common procedure in a dense metro rests on hundreds of thousands of claims and a percentile for an uncommon one in a rural county rests on a handful, and both are published as a number with no distinction.
**Tags:** #confidence-intervals #bayesian-inference #probability-distributions #hypothesis-testing #evaluation-metrics #descriptive-statistics #gaussian-mixture-models #compliance #data-integration #feature-engineering

## The Problem
The benchmark is published as a value across an enormous grid of procedure by geography by percentile, and the density of that grid varies by orders of magnitude. Where support is thick the figure is precise. Where it is thin the same figure carries error large enough to change the outcome of a payment dispute, and nothing in the product distinguishes the two. The users least able to detect the problem are the ones most affected: an arbitrator settling an out-of-network dispute over an uncommon service in a small market receives a number formatted exactly like every other number. Internally the sparsity is understood and handled with minimum-cell suppression rules, which is a blunt instrument — it removes the thinnest cells entirely and leaves everything above the threshold looking equally solid.

## Why It's Still Broken
The product's authority derives partly from its apparent definitiveness, and there is a longstanding, understandable worry that publishing uncertainty invites parties to argue about the number rather than accept it. Suppression thresholds were the compromise, and they have the virtue of being simple to explain and defend. Doing better requires estimating uncertainty properly across a very large and heterogeneous grid, which is real statistical work with no obvious owner in an organization structured around production. And no user has demanded it, because users do not know the variation exists.

## What a Fix Looks Like
Uncertainty published alongside every figure, and estimated properly rather than approximated. Sample support and an interval attach to each cell, with the interval derived in a way that handles the actual distributional shape of charge data rather than assuming normality, which it plainly is not. Where a cell is thin, partial pooling toward related geographies and clinically similar procedures produces a better estimate than either the raw thin figure or suppression — with the degree of pooling stated, so the user knows what they are looking at. The presentation matters as much as the statistics: an arbitrator needs to see immediately whether this figure is solid or indicative, which is a design problem as much as a methodological one. And suppression rules become a floor for privacy rather than the organization's only answer to sparsity.

## Who Feels the Pain
Arbitrators and courts settling disputes on figures whose precision they cannot assess; providers and patients in rural and low-density markets, where the figures are weakest and the stakes are identical; the organization's methodologists, who know the variation exists and have no way to express it; and the organization's standing, which suffers most if a thin-cell figure is publicly shown to have been unreliable.

## Impact If Fixed
Improves the estimates in exactly the cells where they are currently worst, and does it while making the product more honest rather than less authoritative — an organization that publishes its uncertainty is demonstrating rigour, not conceding weakness. Given that these benchmarks are increasingly named in federal and state dispute resolution processes, being able to state the precision of any cited figure is close to a prerequisite for keeping that role.
