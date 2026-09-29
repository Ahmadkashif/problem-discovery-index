# The Rejected Recommendation That Returns

**Niche:** [[niches/cloud-cost-management/engineering-facing-optimisation/profile|Engineering-Facing Optimisation]]
**Industry:** [[industries/cloud-cost-management|Cloud Cost Management]]
**Type:** Fix (Pain Point)
**One-liner:** An engineer dismisses a wrong recommendation with an explanation, and it reappears the following month unchanged, which is how a tool teaches people to stop reading it.
**Tags:** #descriptive-statistics #k-means-clustering #logistic-regression #evaluation-metrics #confidence-intervals #worker-facing #quick-win #automation
**Contested on:** Every serious competitor here is fighting to produce a recommendation an engineer will actually act on — specific, safe and verifiably right — and whoever does that takes engineering, because after two bad suggestions the feature is dead permanently.

## The Problem
An engineer opens the cost tool, sees a recommendation to downsize a standby, and dismisses it. Next month it is back. They dismiss it again, this time writing a note explaining what the resource is. The month after, it is back. The tool has now demonstrated that engaging with it is pointless, which is a stronger lesson than any individual wrong recommendation, and the engineer stops opening it. The information they supplied — that this resource is a standby — was exactly what the tool needed and was discarded.

## Why It's Still Broken
Recommendations are recomputed from current metrics each cycle and are stateless, so a dismissal is an interface action rather than a piece of knowledge. Capturing a reason requires a taxonomy and somewhere to put it, which nobody built. And the vendor's metric is recommendations generated and potential savings identified, both of which are maximised by regenerating everything, so the incentive runs directly against remembering.

## What a Fix Looks Like
Treat every dismissal as information about the resource. Capture a reason from a short structured list — standby, peak-sized, cache, compliance retention, bottlenecked elsewhere, planned change — which is quick for the engineer and immediately reusable. Suppress the recommendation permanently unless the underlying evidence changes materially, and say so, since the engineer needs to know their input was accepted. Propagate the knowledge: if this resource is a standby, its counterparts probably are too, and similar resources across the estate can be excluded by the same reasoning — which turns one dismissal into many correct suppressions. Report dismissal reasons in aggregate, since they are a precise specification of the context the recommendation engine lacks and the top two or three usually account for most of the errors. Re-examine suppressed recommendations only when the resource's behaviour genuinely changes, with the change stated. And measure acted-on rate rather than potential savings identified, because the latter is maximised by exactly the behaviour that destroys the former.

## Who Feels the Pain
Engineers who explained something once and were ignored; platform teams whose cost tool has no audience; and organisations paying for a recommendation engine whose output nobody reads.

## Impact If Fixed
Capturing and honouring a dismissal is a small piece of state that prevents the specific behaviour that destroys trust. The aggregated dismissal reasons are a free specification of the missing context, and propagating to similar resources multiplies each correction.
