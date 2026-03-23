# Analyst-Learning Alert Triage Automation

**Niche:** [[niches/cybersecurity-mssp/alert-triage-automation/profile|Alert Triage & Escalation Automation]]
**Industry:** [[industries/cybersecurity-mssp|Cybersecurity MSSP]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No product learns from SOC analyst triage decisions to automatically close alerts that match previously resolved false-positive patterns, while escalating novel or high-risk alerts with full context.
**Tags:** #gradient-boosting #binary-classification #tabular-ml #tacit-knowledge-ml #ai-agent

## The Problem
An experienced Tier-1 SOC analyst looks at an alert — "outbound connection to suspicious IP from marketing workstation" — and knows within 15 seconds it is a false positive because: the IP is a CDN range for the client's marketing platform, the connection was on port 443, and the user is the marketing manager who accesses this platform daily. A new analyst spends 10 minutes investigating the same alert. The experienced analyst's judgment is tacit knowledge — pattern recognition built from reviewing 100,000+ alerts. When that analyst leaves (and they will — 18-month average tenure), their pattern library walks out with them. The next analyst starts from scratch, making the same false-positive investigations the predecessor had learned to skip.

## Why Nobody Has Built This
The technical challenge is two-fold: (1) capturing the analyst's decision context (not just "closed as false positive" but "why — this is a known CDN IP for this client's marketing platform"), and (2) building a model that generalizes from specific decisions to alert patterns without overfitting (closing one instance of a CDN connection does not mean all outbound connections to that IP range are benign). The liability concern is significant — an automated triage system that misses a real attack would be catastrophic. MSSPs need a system that automates with high confidence and escalates with clear reasoning, not a black box that either passes or fails alerts.

## What to Build
A triage automation layer that sits between the SIEM and the analyst queue: (1) captures analyst triage decisions with structured context (why was this closed? why was this escalated?), (2) builds per-client alert pattern models from analyst decisions (this client's marketing team regularly connects to these CDN ranges), (3) auto-closes new alerts matching established false-positive patterns with confidence scores, (4) escalates alerts that are novel, high-severity, or match known attack patterns, (5) provides full reasoning for each automated decision ("auto-closed: matches pattern #47, CDN connection from marketing user, 98% confidence, similar to 342 previously closed alerts"). Includes an analyst override workflow and continuous model retraining from corrections.

## Target Customer
MSSPs with 10+ Tier-1 analysts processing 10,000+ alerts per day, where alert fatigue is causing missed detections and analyst attrition.

## Impact If Built
Automates 70-80% of Tier-1 triage, reducing analyst workload from 300 alerts/shift to 60-90. Reduces Tier-1 staffing requirements by 50-60%, saving $350K-$700K annually per 10-analyst reduction. Improves detection rate by focusing human attention on novel and high-risk alerts rather than repetitive false positives.
