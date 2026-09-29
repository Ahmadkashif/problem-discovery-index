# Build: Detection Before the Label

**Niche:** Novel Harm Response
**Industry:** [[industries/trust-safety-tooling-vendors|Trust & Safety Tooling Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Watch for the signals that precede a label — clustering, coordination, uncategorisable escalations, report free text — so a novel pattern is detected in days rather than after a retraining cycle.
**Tags:** #change-point-detection #contrastive-learning #k-means-clustering #graph-neural-networks #bert #evaluation-metrics #confidence-intervals #automation
**Contested on:** Whether a new abuse pattern can be detected in the weeks when it does most of its damage.

## The Problem

The response to a novel harm is sequential and slow. Somebody notices. It is escalated to policy. A definition is written. Labelled examples are produced. A model is retrained. The update is deployed. Weeks, sometimes longer.

During that interval the classifier is blind to it, and the interval is exactly when the harm does most of its damage. A coordinated campaign is designed to run quickly. A novel scam format works until it is known. An emergent harassment pattern establishes itself in the period before anything responds.

Meanwhile the signals were present from early on. Content that clusters tightly in embedding space without matching an existing category. Accounts behaving in coordination — creation timing, posting patterns, mutual amplification. Reviewers escalating items as uncategorisable at a rising rate. User reports whose free text describes something the report categories do not cover. And the same pattern appearing on other platforms, frequently earlier.

None of it is monitored. The detection system watches for known categories, and a novel harm is by construction not one.

## Why Nobody Has Built This

**Products are built around categories.** A classifier detects defined harms. A system detecting that something undefined is happening is a different product and does not fit the category-based architecture.

**Anomaly detection produces false alarms.** Content clusters for many innocent reasons — a news event, a meme, a product launch — so a clustering signal without context generates noise.

**The escalation path ends at policy.** Reviewers escalating uncategorisable items feed a policy queue rather than a detection system, so the signal is consumed as a case rather than as data.

**Report free text is discarded.** Report categories are structured and the free text explaining why someone reported something is frequently not analysed at all.

**Cross-platform signals require cooperation.** A pattern visible on several platforms is the strongest early signal and no mechanism exists for sharing it in most categories.

**Nobody measures the interval.** How long between a novel harm appearing and the classifier detecting it is not tracked anywhere, so the cost of the gap has no number.

## What to Build

**Monitor for emergent clusters.** Content clustering tightly in representation space that matches no existing category, with a rising volume. This is unsupervised detection and it is the earliest available signal.

**Watch coordination signals.** Account creation timing, posting synchrony, mutual amplification and shared infrastructure. Coordinated campaigns are detectable as coordination before their content is classifiable.

**Turn reviewer escalations into a detection signal.** A rising rate of items escalated as not matching any category is a direct human signal that something new is happening, and it currently reaches a policy queue rather than a monitor.

**Read the report free text.** Users describing why they reported something frequently name a novel harm before the taxonomy does. This is unstructured text that is collected and not analysed.

**Enable rapid deployment without retraining.** Few-shot classification, embedding-based similarity to a handful of confirmed examples, or a lightweight rule — something deployable in hours from a small number of labelled items rather than in weeks from a retraining cycle.

**Measure the detection interval.** From first appearance to detection to deployed response, per incident. This is the metric that would make the gap visible and it is not tracked anywhere.

**Share cross-platform signals where possible.** Novel patterns appear on several platforms and existing sharing mechanisms cover only the most severe categories. Extending them is a governance problem with a large payoff.

## Target Customer

Platform trust and safety operations, for whom the interval between a novel harm appearing and responding to it is the failure mode they experience most acutely and measure least.

Vendors, for whom novel harm detection is a genuinely differentiated capability that does not depend on unverifiable accuracy claims about known categories.

Platforms with large user bases in fast-moving contexts, where novel patterns emerge most frequently and the damage during the interval is greatest.

## Impact If Built

The gap between a novel harm appearing and a system responding to it is where most of the damage happens, and it is currently determined by a retraining cycle.

Turning reviewer escalations and report free text into detection signals uses information the platform already collects from humans who noticed something first, and routes it to a system rather than to a queue.

And few-shot deployment from a handful of confirmed examples would compress the response from weeks to hours, which is the difference between catching a campaign during its run and describing it afterwards.
