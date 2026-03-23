# Alert Triage & Escalation Automation

**Parent Industry:** [[industries/cybersecurity-mssp|Cybersecurity MSSP]]
**Category:** Highly Automatable

## Profile
**Market Size:** $2B (internal spend)
**Share of Parent Industry:** N/A (operational cost, not revenue)
**Digital Adoption:** Medium — MSSPs use SIEM and SOAR platforms, but Tier-1 alert triage remains 80% manual: analysts review each alert, check context, make a decision, and document the outcome.
**Target Buyer:** SOC managers and Tier-1 analyst team leads at MSSPs spending 60-70% of analyst time on alert triage.
**Automation Potential:** Very High — 85-90% of SIEM alerts are false positives following recognizable patterns that could be auto-closed with appropriate confidence scoring.

## What Makes This a Distinct Niche
Alert triage is the single largest labor cost in MSSP operations. A mid-size MSSP processing 50,000 alerts per day across 100 clients employs 15-20 Tier-1 analysts to review, categorize, and either close or escalate each alert. Each analyst handles 200-400 alerts per shift, spending an average of 5-10 minutes per alert. Of these, 85-90% are false positives or benign true positives (known behavior, maintenance activity, legitimate scans). The analyst's job is to find the 10-15% that require investigation — a needle-in-haystack problem that causes alert fatigue, analyst burnout (average Tier-1 analyst tenure is 18 months), and missed detections when real threats are buried in noise.

## Current Tools & Gaps
SOAR platforms (Cortex XSOAR, Swimlane, Tines) automate response actions (block IP, disable account) but do not automate the triage decision itself — the analyst still decides whether the alert is real. SIEM platforms (Splunk, Sentinel) provide risk scoring and correlation, but their scores are based on rule-defined logic, not learned patterns from analyst decisions. No platform learns from analyst triage outcomes (which alerts were closed as false positives, which were escalated) to improve triage automation over time.

## Problems
- [[niches/cybersecurity-mssp/alert-triage-automation/build|🔨 Build: Analyst-Learning Alert Triage Automation]]
- [[niches/cybersecurity-mssp/alert-triage-automation/buy|🛒 Buy: Context-Enriched Alert Deduplication]]
- [[niches/cybersecurity-mssp/alert-triage-automation/fix|🔧 Fix: Alert Documentation Consistency Gap]]
