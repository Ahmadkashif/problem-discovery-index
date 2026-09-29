# Entity Resolution Applied to Infrastructure

**Niche:** [[niches/cloud-cost-management/cost-attribution-and-ownership/profile|Cost Attribution & Ownership]]
**Industry:** [[industries/cloud-cost-management|Cloud Cost Management]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Deciding which entity a record belongs to from partial and noisy evidence is entity resolution, mature for decades, and cloud cost allocation does it with a string match on a tag.
**Tags:** #graph-theory #k-nearest-neighbors #logistic-regression #gradient-boosting #evaluation-metrics #confidence-intervals #cross-validation #data-integration
**Contested on:** Every serious competitor in this niche is fighting to get a cost in front of the person who can change it, without depending on tags nobody maintains — and whoever does that takes the account, because the tagging approach has failed everywhere it has been tried.

## The Problem
Assigning records to entities using several weak, partial and occasionally contradictory signals is entity resolution, with decades of method, probabilistic frameworks and mature tooling. Cloud cost allocation faces exactly this — many signals about which team owns a resource, none complete — and resolves it by looking for an exact tag and giving up when it is absent.

## What Already Exists
Probabilistic record linkage and entity resolution frameworks; blocking and matching libraries; graph-based propagation for spreading labels through a connected structure; classification with calibrated probabilities; and active learning to direct human review where it is most informative. All mature, most free.

## The Customization Gap
The adaptation is to infrastructure resources with a graph structure. It requires: (1) graph propagation as a first-class method, since resources are connected — a subnet, a load balancer, a volume attached to an instance — and an untagged resource adjacent to tagged ones can inherit ownership with high confidence, which is the single most effective technique here and has no analogue in ordinary record linkage; (2) the deployment lineage as the strongest signal, because the pipeline that created a resource is recorded and is far more reliable than a tag; (3) calibrated confidence with an explicit review queue, so the uncertain minority gets human attention and the confident majority does not, which is what makes this practical at scale; (4) temporal validity, since ownership changes when teams reorganise and an allocation must be correct for the period being billed rather than for today; and (5) reconcilability, because the total must still add up to the bill exactly, which means unallocated must shrink rather than being replaced by an approximation that does not sum.

## Target Customer
Cloud cost management vendors, platform engineering teams, and the configuration management and asset inventory vendors for whom this is adjacent.

## Impact If Solved
A mature resolution discipline addresses precisely the problem the category has been solving with string matching. Graph propagation over connected resources is the technique with the largest effect and is entirely unused.
