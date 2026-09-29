# Who Pays for the Empty Space

**Niche:** [[niches/cloud-cost-management/kubernetes-shared-infrastructure/profile|Kubernetes & Shared Infrastructure]]
**Industry:** [[industries/cloud-cost-management|Cloud Cost Management]]
**Type:** Fix (Pain Point)
**One-liner:** A large share of every cluster is capacity nobody is using, and it is either split proportionally across teams or quietly omitted, and in both cases nobody is accountable for reducing it.
**Tags:** #descriptive-statistics #time-series-forecasting #optimization-fundamentals #hypothesis-testing #confidence-intervals #quick-win #revenue-impact #automation
**Contested on:** Every serious competitor here is fighting to say what a workload costs when it shares a machine with forty others — and whoever does that credibly takes the platform account, because resource-level billing stops working the moment the resource is shared.

## The Problem
A cluster runs at a modest average utilisation. The rest is headroom for scheduling, capacity provisioned for a peak that occurs twice a week, nodes that cannot be drained because of a workload's placement constraints, and over-requested memory that no workload will ever use. Collectively this is a substantial share of the bill. In the cost report it is either divided proportionally across teams, where it is nobody's responsibility, or excluded entirely, where it is invisible. Either way no individual or team is accountable for it, and it does not shrink.

## Why It's Still Broken
Idle capacity has no natural owner: the platform team provisioned it, the workload teams caused it by their requests and constraints, and the scheduler placed it. Proportional allocation makes it everyone's and therefore no one's, which is the classic outcome. Nobody separates the components — headroom, peak provisioning, constraint-driven waste, over-request — although they have different causes and different remedies. And the platform team, who could reduce it, is measured on cluster availability rather than on efficiency, so the incentive is to over-provision.

## What a Fix Looks Like
Decompose the empty space and give each part an owner. Separate the categories explicitly: scheduling headroom, peak provisioning, constraint-driven fragmentation, over-requested-and-unused, and genuinely idle nodes — each of which has a different cause and a different fix, and lumping them together is why nothing happens. Attribute over-request directly to the workload that caused it, since that is not shared waste at all and is frequently the largest single component. Attribute fragmentation to the workloads whose placement constraints cause it, which is computable from the scheduler's own decisions. Assign the remaining genuine headroom and peak capacity to the platform team as an owned efficiency metric, with a target, since somebody must be accountable and they are the only party who can act. Report the cluster's efficiency trend alongside its availability, so the platform team is held to both rather than to one. And quantify the trade-off honestly, because some headroom is necessary and the useful conversation is about how much rather than about whether.

## Who Feels the Pain
Teams charged for waste they did not cause; platform teams incentivised to over-provision because only availability is measured; and organisations paying substantially for capacity nobody has been asked to reduce.

## Impact If Fixed
Decomposing the idle capacity into its causes is computable from scheduler data and turns an unowned total into several owned components. Attributing over-request to its workload is the largest single reallocation and is not shared waste at all.
