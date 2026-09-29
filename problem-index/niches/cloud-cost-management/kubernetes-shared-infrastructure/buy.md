# Cost Allocation Methods From Shared Services Accounting

**Niche:** [[niches/cloud-cost-management/kubernetes-shared-infrastructure/profile|Kubernetes & Shared Infrastructure]]
**Industry:** [[industries/cloud-cost-management|Cloud Cost Management]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Allocating the cost of a shared resource among its users is a solved accounting problem with several established methods and a literature about their incentive properties, and container cost tools pick one silently.
**Tags:** #linear-regression #optimization-fundamentals #descriptive-statistics #hypothesis-testing #confidence-intervals #evaluation-metrics #revenue-impact #automation
**Contested on:** Every serious competitor here is fighting to say what a workload costs when it shares a machine with forty others — and whoever does that credibly takes the platform account, because resource-level billing stops working the moment the resource is shared.

## The Problem
Dividing the cost of a shared facility among its users is a problem management accounting has addressed for a century — direct, step-down and reciprocal allocation methods, activity-based costing, and a body of work on how each affects behaviour. Cooperative game theory adds allocation rules with explicit fairness properties. Container cost tooling chooses an allocation basis in code and presents the output as a measurement.

## What Already Exists
Service department cost allocation methods from management accounting; activity-based costing; cooperative game theory allocation rules with fairness axioms; peak-responsibility pricing from utilities, which addresses exactly the question of who pays for capacity maintained for peak; and the transfer pricing literature on incentive effects. All published and none of it applied here.

## The Customization Gap
The adaptation is to a scheduler-driven, rapidly changing shared resource. It requires: (1) allocation at a fine time granularity, since workloads appear and disappear in minutes and an hourly or daily allocation misrepresents both the burst workload and the steady one; (2) explicit treatment of reserved-but-unused capacity, which is the core dispute and where peak-responsibility pricing offers a directly applicable principle — the party that causes the peak pays for the capacity maintained for it; (3) incentive-compatibility as a stated design goal, because the allocation basis determines whether teams over-request or under-request and the current defaults reliably produce one or the other; (4) attribution of scheduling-driven costs, since a node that exists because one workload requires a particular instance type is not a shared cost at all and treating it as one is simply wrong; and (5) transparency of the method, since the accounting literature's clearest finding is that an allocation basis participants understand and have agreed changes behaviour and one imposed does not.

## Target Customer
Platform teams, container cost allocation projects and vendors, and the technology business management vendors for whom this is the hardest part of their allocation model.

## Impact If Solved
A century of allocation methodology with explicit incentive analysis has not reached a problem that is entirely about allocation and incentives. Peak-responsibility treatment of headroom and explicit incentive-compatibility are the two adaptations with the largest effect.
