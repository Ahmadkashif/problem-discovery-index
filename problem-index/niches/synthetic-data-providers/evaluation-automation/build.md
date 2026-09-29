# Every Metric Exists and No Two Runs Are Comparable

**Niche:** [[niches/synthetic-data-providers/evaluation-automation/profile|Evaluation Automation]]
**Industry:** [[industries/synthetic-data-providers|Synthetic Data Providers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The metrics the category needs are all published and implemented somewhere, and there is no standard harness that runs them identically, so no two vendors' results can be compared.
**Tags:** #evaluation-metrics #hypothesis-testing #cross-validation #confidence-intervals #monte-carlo-methods #automation #workflow-orchestration #probability-distributions
**Contested on:** Every serious competitor in this niche is fighting to make evaluation a standard, reproducible run that a customer can execute themselves — and whoever does that takes the category's credibility, because a claim the buyer cannot reproduce is a claim they have to take on faith.

## The Problem
A buyer evaluating three vendors receives three reports. One reports a discriminator-based fidelity score, one reports marginal and pairwise distances, one reports downstream accuracy on a task of their choosing. All three report a privacy parameter computed under different accounting assumptions. One ran a membership inference attack, with a method and strength they do not specify. The buyer cannot rank them, cannot reproduce any of it, and ends up choosing on the demo and the reference call — which is how a technical category ends up sold on impressions.

## Why Nobody Has Built This
A standard harness is a public good and nobody's revenue. Vendors benefit from incomparability, which is not a conspiracy but a stable equilibrium nobody has an incentive to leave first. The metrics come from separate communities — modelling, statistics, privacy — with no shared maintainer. Downstream task evaluation resists standardisation because it needs a task. And the party best placed to build it, an independent body, does not exist in this category yet.

## What to Build
Build the harness and make it the default. Implement the full metric set in one place with pinned configurations, so a number means the same thing wherever it appears — which is the whole product and the reason the incumbents have not built it. Run it as a pipeline stage on every generation run rather than on demand, so results are versioned alongside the model and a regression is caught by the vendor rather than by the customer. Report a fixed core set every time, since selective reporting is the mechanism by which the current situation persists and a mandatory core removes the choice. Make attack strength a specified protocol rather than a parameter, which the fix note develops. Support a customer-supplied downstream task as a first-class input, because that is the measure that matters and the standard argument against standardising it is really an argument for making the task an input rather than a constant. Produce a signed, reproducible result artefact that a third party can re-run and verify, which is what makes the claim checkable. Track results across generator versions so drift and regression are visible over time, which nobody does. And release it openly, since a proprietary standard is not a standard and adoption is the only thing that gives it value.

## Target Customer
Buyers evaluating vendors, vendors who would benefit from a credible comparison, assurance firms, and the research community that produced the metrics.

## Impact If Built
Incomparability is the category's stable equilibrium and a standard harness is the only thing that breaks it. A mandatory core metric set removes selective reporting, and a signed reproducible artefact makes a vendor's claim something a buyer can check rather than accept.
