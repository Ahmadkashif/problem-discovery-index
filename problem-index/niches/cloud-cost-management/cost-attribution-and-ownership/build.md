# Tagging Discipline That Does Not Exist

**Niche:** [[niches/cloud-cost-management/cost-attribution-and-ownership/profile|Cost Attribution & Ownership]]
**Industry:** [[industries/cloud-cost-management|Cloud Cost Management]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The bill is organised by resource and the decisions are organised by team, service and feature, and bridging the two depends on tagging discipline that does not exist.
**Tags:** #graph-theory #k-nearest-neighbors #gradient-boosting #k-means-clustering #evaluation-metrics #confidence-intervals #data-integration #automation
**Contested on:** Every serious competitor in this niche is fighting to get a cost in front of the person who can change it, without depending on tags nobody maintains — and whoever does that takes the account, because the tagging approach has failed everywhere it has been tried.

## The Problem
A FinOps team has run a tagging programme for two years. Coverage is at sixty-one percent and has been for eight months. The untagged remainder includes everything created before the policy, everything created by a Terraform module that predates it, several managed services whose sub-resources cannot carry tags, and a long tail created by automation nobody can identify. The monthly report allocates what it can and puts the rest in a bucket called unallocated, which is large enough that every team disputes their number. Meanwhile the deployment system knows which team deployed almost all of it, the repository knows who owns the code, and the access logs know who uses it.

## Why Nobody Has Built This
The category adopted tagging early because it is what the providers offered, and the entire product architecture assumes an allocation key on the resource. Treating ownership as something to be inferred rather than declared is a different design, and it produces probabilistic answers, which a finance function reconciling a bill finds uncomfortable — although a confident wrong allocation is worse than a probabilistic right one. The evidence needed for inference lives outside the billing data, in deployment, repository and identity systems, which every vendor treats as integrations rather than as primary inputs.

## What to Build
Infer ownership from the evidence and use tags as one signal among several. Join the deployment record, which knows which pipeline created which resource and from which repository; the repository, which knows the owning team; the identity system, which knows who has accessed it; the naming conventions, which encode more than anyone admits; and the network relationships, which connect an untagged resource to tagged neighbours it serves. Produce an ownership assignment per resource with a confidence, and route the uncertain minority to a human rather than leaving the whole remainder unallocated. Extend beyond team to service and feature, which is the layer the business actually asks about and which nobody attempts — a resource's owning service is usually determinable from the same evidence. Detect staleness, since teams reorganise and an ownership map without a freshness mechanism will drift exactly as a tag set does. Write the inference back as tags where possible, so the rest of the ecosystem benefits and the coverage problem shrinks permanently. And report confidence alongside the allocation, because a finance function will accept a probabilistic allocation that states its uncertainty and will not accept one that hides it.

## Target Customer
FinOps and platform engineering teams with a large unallocated fraction, and the cost management vendors for whom tagging coverage has been a ceiling on their own product's usefulness.

## Impact If Built
Tagging has failed structurally rather than culturally, which means a better tagging programme will not fix it and inference will. Extending attribution to service and feature reaches the layer the business actually asks about, and writing inferences back as tags improves every other tool at once.
