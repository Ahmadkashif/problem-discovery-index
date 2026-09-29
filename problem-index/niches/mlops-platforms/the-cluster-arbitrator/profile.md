# The Cluster Arbitrator

**Parent Industry:** [[industries/mlops-platforms|MLOps Platforms]]
**Category:** Underserved Audience
**Contested on:** Every serious competitor in this niche is fighting to schedule accelerators on what a job will actually need and be worth rather than on what its author requested — and whoever does that takes the account, because the cluster is the largest line in the budget and it is allocated by negotiation.

## Profile
**Market Size:** ~$210M US in scheduling tooling and recovered capacity
**Share of Parent Industry:** ~7% of category revenue
**Digital Adoption:** None — allocation is a conversation
**Target Buyer:** Platform and ML infrastructure teams, with finance as the sponsor
**Automation Potential:** Very High — duration and outcome are both predictable from history

## What Makes This a Distinct Niche
Someone has to decide which researcher gets the accelerators. The scheduler knows how many each job requested and nothing about how long it will run, whether it will finish, whether it will use what it reserved, or what it is worth. So the platform engineer arbitrates: in a channel, by seniority, by who asked most recently, by who complained loudest. They are the most senior generalist on the team spending their week on a queueing problem, the cluster runs at a utilisation nobody publishes, and the accumulated history that would make every one of these decisions mechanical sits unused in the tracking platform.

## Current Tools & Gaps
Cluster schedulers with queues, quotas and priorities; reservation systems; utilisation dashboards; and chargeback reporting. The gaps: no duration prediction, so the queue cannot be ordered sensibly; no detection of jobs that reserved far more than they use, which is the largest single source of waste; no early termination of runs that are clearly going nowhere; no notion of a job's value, so priority is a political input; and no visibility for the researcher into when their job will actually start.

## Problems
- [[niches/mlops-platforms/the-cluster-arbitrator/build|🔨 Build: A Scheduler That Knows Nothing About the Work]]
- [[niches/mlops-platforms/the-cluster-arbitrator/buy|🛒 Buy: Cluster Scheduling and Capacity Planning]]
- [[niches/mlops-platforms/the-cluster-arbitrator/fix|🔧 Fix: Reserved Eight, Using Two]]
