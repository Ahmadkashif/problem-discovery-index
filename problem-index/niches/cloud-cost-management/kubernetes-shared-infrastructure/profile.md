# Kubernetes & Shared Infrastructure

**Parent Industry:** [[industries/cloud-cost-management|Cloud Cost Management]]
**Category:** Low Digitized
**Contested on:** Every serious competitor here is fighting to say what a workload costs when it shares a machine with forty others — and whoever does that credibly takes the platform account, because resource-level billing stops working the moment the resource is shared.

## Profile
**Market Size:** ~$460M US attributable to container and shared infrastructure cost allocation
**Share of Parent Industry:** ~15% of category revenue
**Digital Adoption:** Low — the allocation exists and is widely disbelieved
**Target Buyer:** Platform teams operating shared clusters
**Automation Potential:** Very High — the scheduler and the runtime know everything required

## What Makes This a Distinct Niche
Cloud billing is organised around resources, and the whole model breaks when many workloads share one. A cluster node appears on the bill as a single instance; on it run forty containers belonging to nine teams, each with a resource request that may bear little relation to what it uses, alongside system overhead, unused headroom deliberately maintained for scheduling, and capacity idle because the cluster is provisioned for peak. Deciding what each team owes requires answering questions the bill cannot: allocate by request or by usage, who pays for the headroom, who pays for the node that exists because of one workload's affinity rule. Every answer is defensible and produces different numbers, which is why container cost allocation is simultaneously widely deployed and widely disbelieved. This is a distinct contest because the difficulty is definitional as much as technical, and because the data required sits in the orchestrator rather than in the bill.

## Current Tools & Gaps
Open source container cost allocation and commercial equivalents, namespace and label-based grouping, and cluster utilisation dashboards. The gaps: allocation by request punishes conservative sizing and by usage punishes nobody for over-requesting, and most tools pick one without saying why; idle and headroom capacity is either distributed proportionally or ignored, and it is frequently a large share of the total; the cost of the platform team's own components is rarely separated; multi-tenant efficiency — whether consolidating workloads saved anything — is never measured; and the numbers are disbelieved precisely because the methodology is invisible.

## Problems
- [[niches/cloud-cost-management/kubernetes-shared-infrastructure/build|🔨 Build: Forty Containers and One Line on the Bill]]
- [[niches/cloud-cost-management/kubernetes-shared-infrastructure/buy|🛒 Buy: Cost Allocation Methods From Shared Services Accounting]]
- [[niches/cloud-cost-management/kubernetes-shared-infrastructure/fix|🔧 Fix: Who Pays for the Empty Space]]
