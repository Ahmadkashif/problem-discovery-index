# Forty Containers and One Line on the Bill

**Niche:** [[niches/cloud-cost-management/kubernetes-shared-infrastructure/profile|Kubernetes & Shared Infrastructure]]
**Industry:** [[industries/cloud-cost-management|Cloud Cost Management]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The bill shows one instance and the cluster runs forty workloads on it belonging to nine teams, and every method of dividing that number produces a different answer that somebody disputes.
**Tags:** #graph-theory #linear-regression #optimization-fundamentals #descriptive-statistics #evaluation-metrics #confidence-intervals #data-integration #automation
**Contested on:** Every serious competitor here is fighting to say what a workload costs when it shares a machine with forty others — and whoever does that credibly takes the platform account, because resource-level billing stops working the moment the resource is shared.

## The Problem
A platform team reports cluster costs by namespace. A team sees a figure they dispute: they requested a large amount of memory because the application occasionally needs it, they use a fraction of it most of the time, and they are charged for the request. Another team under-requested, is throttled regularly, and is charged little. A third of the cluster's cost is headroom that exists so the scheduler can place pods, charged proportionally to everybody. The platform team's own monitoring and ingress components are in there too. Every number is defensible and none is agreed, and the report has therefore changed nobody's behaviour.

## Why Nobody Has Built This
Cost allocation tooling for containers was built to produce a number rather than to make a methodology legible, so it picks a basis and presents the result as fact. The definitional questions — request or usage, who pays for headroom, how to handle a node that exists for one workload's constraint — have real answers with different incentive consequences and nobody has written them down as a choice the organisation makes. And the orchestrator holds everything required: requests, limits, actual usage, scheduling decisions, node lifetimes and the reason each node exists.

## What to Build
Make the allocation a stated, adjustable and incentive-aware model rather than a number. Allocate on a basis the organisation chooses explicitly — maximum of request and usage is the defensible default, since it charges for the capacity reserved and for the capacity consumed and penalises both over-requesting and throttling-inducing under-requesting. Separate the components honestly: workload cost, headroom maintained for scheduling, system and platform overhead, and capacity idle because the cluster is sized for peak — because bundling these is what makes the total disputable. Attribute headroom to the workloads whose scheduling constraints require it rather than proportionally, since a workload demanding a large contiguous allocation or a specific node type is the reason the headroom exists. Report each team's own efficiency — requested against used — alongside their cost, which is the number they can act on and the one that makes the allocation incentive-compatible. Show the methodology and let it be configured, since an agreed imperfect basis produces behaviour change and an imposed perfect one produces argument. And measure the consolidation benefit, so the platform can show what running shared rather than dedicated actually saved, which nobody currently computes and which is the justification for the whole arrangement.

## Target Customer
Platform teams operating shared clusters, cost management vendors differentiating on container attribution, and the open source cost allocation projects.

## Impact If Built
The difficulty is definitional as much as technical, and the products have hidden the definition, which is why the numbers are disbelieved. Separating headroom and overhead from workload cost, and attributing headroom to its cause, removes most of the dispute.
