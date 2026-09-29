# Productivity Metrics Engineers Are Right to Resent

**Niche:** [[niches/work-collaboration-tools/engineering-work-tracking/profile|Engineering Work Tracking]]
**Industry:** [[industries/work-collaboration-tools|Work Collaboration Tools]]
**Type:** Fix (Pain Point)
**One-liner:** Developer productivity measurement repeatedly produces counts of commits, tickets and lines changed, which measure output volume rather than value, and engineers resist them correctly while organisations conclude that engineers dislike measurement.
**Tags:** #descriptive-statistics #hypothesis-testing #confidence-intervals #evaluation-metrics #causal-inference #worker-facing #compliance #quick-win
**Contested on:** Every serious competitor in engineering work tracking is fighting to make the tracker reflect what the code actually shows — and whoever connects the ticket to the commit, the review and the deployment most completely takes the engineering organisation.

## The Problem
An organisation deploys a productivity dashboard showing commits, pull requests and tickets closed per engineer. The engineer who spends a week deleting a subsystem that caused half the incidents appears unproductive. The one who reviews everyone else's work carefully appears unproductive. The one who mentored two new joiners appears unproductive. The one producing large volumes of mediocre code appears excellent. Engineers object, are told they are resistant to accountability, and the dashboard is either quietly abandoned or is used in performance conversations where it does real harm. This sequence has repeated across the industry for two decades.

## Why It's Still Broken
Output counts are the only thing that is trivially measurable per individual, and the demand for individual measurement is genuine — managers do need to understand their teams. The literature on why individual output metrics fail in software is substantial and is not read by the people buying the dashboards. And each new generation of tooling rediscovers the counts because they are what the data offers most readily, which means the mistake is structural rather than a lapse.

## What a Fix Looks Like
Measure the system rather than the individual, and give individuals their own information. Team-level delivery and stability measures — how long a change takes to reach production, how often deployments fail, how quickly failures are recovered — are well established, are about the system, and improve when the system improves rather than when individuals work harder. Report those. For individuals, provide information to them rather than about them: their own cycle time patterns, where their work waits, how much of their week goes to review and interruption, which is genuinely useful to a person and is not a ranking. Make the invisible work visible in its own terms, as this industry's invisible-contribution niche describes, rather than leaving it uncounted and therefore implicitly worthless. And state plainly in the product what the metrics are not for, because a vendor that ships per-engineer output counts without that statement is supplying the instrument for the harm and knows it.

## Who Feels the Pain
Engineers evaluated on counts that do not reflect their contribution; managers given a dashboard that does not answer their real question; and organisations that conclude measurement is impossible after doing it badly.

## Impact If Fixed
System-level delivery measures are well evidenced, widely documented and answer the question leadership is actually asking, without the harm. Giving individuals their own data rather than a ranking is the part that changes the relationship, and it costs nothing beyond deciding who the report is for.
