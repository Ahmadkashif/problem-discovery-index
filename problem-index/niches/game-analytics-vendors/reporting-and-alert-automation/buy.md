# Alerting Discipline From Site Reliability

**Niche:** [[niches/game-analytics-vendors/reporting-and-alert-automation/profile|Reporting & Alert Automation]]
**Industry:** [[industries/game-analytics-vendors|Game Analytics Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Site reliability learned that unmaintained alerts get muted and built the discipline to fix it, and analytics alerting is where monitoring was a decade ago.
**Tags:** #automation #change-point-detection #evaluation-metrics #confidence-intervals #workflow-orchestration #descriptive-statistics #hypothesis-testing #data-integration
**Contested on:** Every serious competitor in this niche is fighting to get the right number to the right person at the right moment without an analyst assembling it, and whoever automates that takes the account.

## The Problem
Site reliability engineering learned the hard way that alerts set by hand and never revisited produce fatigue and get ignored, and built a discipline in response: alert on symptoms rather than causes, derive thresholds from measured behaviour, require every alert to be actionable, audit which alerts have ever led to action, and retire the ones that have not. Analytics alerting sits where monitoring sat before any of that.

## What Already Exists
Symptom-based alerting principles; thresholds derived from historical behaviour; actionability requirements per alert; alert quality auditing; and routing and escalation policies.

## The Customization Gap
The adaptation is to metrics that move for legitimate reasons constantly. It requires: (1) business metrics with strong seasonality, campaign effects and genuine variance, where a departure from normal is frequently correct and uninteresting — this is the substantive difference and makes the actionability bar much harder to define; (2) response times of days rather than minutes, so paging is the wrong model entirely; (3) recipients who are product managers rather than on-call engineers; (4) movements whose significance depends on context an alert cannot see; and (5) no incident concept, so the alert must carry its own explanation to be useful.

## Target Customer
Studio analytics teams, game analytics vendors, publishers, and monitoring and alerting vendors.

## Impact If Solved
Reliability engineering learned that unmaintained alerts get muted and built the discipline in response. Business metrics that move constantly for legitimate reasons make the actionability bar far harder to define, which is the work.
