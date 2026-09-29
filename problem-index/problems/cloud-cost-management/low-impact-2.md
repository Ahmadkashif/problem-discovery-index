# Recommendation Credibility

**Industry:** [[cloud-cost-management|Cloud Cost Management]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every platform generates rightsizing recommendations and engineers ignore them, because the second time a tool suggests downsizing a standby that exists precisely to be idle, the feature is dead.
**Tags:** #gradient-boosting #time-series-forecasting #confidence-intervals #hypothesis-testing #k-means-clustering #evaluation-metrics #automation

## The Problem
Cost platforms produce recommendations: downsize this instance, delete this unattached volume, remove this idle load balancer, schedule this environment to shut down overnight.

The recommendations are frequently correct and are almost universally ignored. The reason is that a subset are confidently wrong in a way that reveals the tool does not understand what it is looking at. The instance running at four per cent utilisation is a standby that takes over during a failover. The idle load balancer is in a disaster recovery region. The over-provisioned cluster is sized for a quarterly batch job. The oversized database has headroom for a launch next month.

An engineer who acts on a wrong recommendation and causes an incident will not act on another. Two bad recommendations are sufficient to make an entire feature dead, and every platform generates them because they are computed from utilisation alone.

So the recommendations accumulate as an unread backlog with an aggregate saving figure that finance quotes and nobody realises.

## What Already Exists
Rightsizing recommendations are standard in the hyperscalers' native tooling and in every third-party product. Idle and unattached resource detection is universal. Scheduling automation for non-production environments is widely available. Anomaly detection on spend exists in most tools. Some products offer automated remediation with approval workflows.

## The Customisation Gap
Purpose is the missing dimension. A resource's role — production, standby, disaster recovery, batch, development, canary — determines whether low utilisation is waste or design, and it is inferable from naming, tags, network position, traffic patterns, deployment configuration and the behaviour of its peers. No recommendation engine attempts it, which is why they are wrong in exactly the cases that destroy credibility.

Risk should be stated alongside saving. A recommendation carrying an assessment of what could go wrong, and a confidence that this resource is what the tool thinks it is, would let an engineer triage rather than dismiss.

Acceptance history is the feedback loop nobody closes. Which recommendations were accepted, rejected, or accepted and reverted is directly observable and is the strongest available signal for improving future ones — and no platform learns from it.

Cross-organisational context is the vendor's unique asset: what utilisation is normal for this workload shape across thousands of organisations tells you whether this instance is genuinely oversized or typical for its role.

## Impact If Solved
Recommendation engines in this category generate large notional savings and realise few of them, because credibility was destroyed by a minority of confidently wrong suggestions. Inferring resource purpose and stating risk is what makes the output triageable, and acceptance history is a free feedback loop that nobody has connected.
