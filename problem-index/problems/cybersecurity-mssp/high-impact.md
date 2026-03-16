# SOC Alert Triage & True Positive Identification

**Industry:** [[cybersecurity-mssp|Cybersecurity MSSPs]]
**Type:** High Impact
**One-liner:** SOC analysts stop drowning in 500-1,000 daily alerts and focus only on the 2-5% that represent real threats, cutting mean-time-to-detect from hours to minutes.
**Tags:** #gradient-boosting #bert #binary-classification #nlp #tabular-ml #tacit-knowledge-ml #revenue-impact

## The Problem
An MSSP's SOC receives 500-1,000+ alerts per day across its client base from SIEM rules, EDR detections, and threat intel feeds. Over 95% are false positives — benign activity that matches a signature, misconfigured rules, or known-good behavior that hasn't been whitelisted yet. L1 analysts spend 5-15 minutes per alert pulling up context: checking the source IP against reputation feeds, reviewing the user's behavioral baseline, looking at the asset's criticality tag, reading the raw log payload, and cross-referencing recent similar alerts. An experienced L1 analyst develops an intuition that lets them dismiss noise in seconds — they recognize the "shape" of a false positive from the combination of alert source, severity mapping, time-of-day, client environment, and payload snippet — but this judgment lives entirely in their head and leaves when they do.

## Why It's Unsolved
The tacit knowledge problem is severe: a senior SOC analyst's triage decision integrates 15-20 contextual signals simultaneously — alert type, MITRE ATT&CK mapping, source/destination pairing, historical false positive rate for that rule in that client's environment, time-of-day anomaly, asset role, user privilege level, and subtle payload characteristics. Capturing this decision process requires logging not just the alert metadata but the analyst's disposition reasoning at scale, which most MSSPs don't do systematically. Labeling is noisy because analysts disagree on borderline cases, and ground truth (was this actually malicious?) often takes weeks to confirm through full investigation. Deployment is hard because the model must be faster and more transparent than the analyst — a black-box score that occasionally misses a real intrusion destroys trust instantly. Each client environment has different baselines, so the model must generalize across tenants while respecting per-client context.

## What a Solution Looks Like
A model that ingests each alert's structured metadata (source, severity, rule ID, MITRE mapping, asset tags, user context) plus the unstructured log payload and alert description, and outputs a true-positive probability score with an explanation of the top contributing features. Alerts scoring below a tunable threshold are auto-closed with audit trail. Alerts above threshold are promoted to L2 with a pre-populated investigation context card showing why the model flagged it. The system continuously retrains on analyst disposition feedback, creating a flywheel where every human decision improves the next prediction.

## Impact If Solved
Reduces L1 analyst workload by 70-80%, allowing an MSSP to handle 3-4x the client base with the same headcount. Cuts mean-time-to-detect for real incidents from hours to under 10 minutes, which is the single metric that determines client retention and contract value.
