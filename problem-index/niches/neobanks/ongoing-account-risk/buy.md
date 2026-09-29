# Anomaly Detection Practice

**Niche:** [[niches/neobanks/ongoing-account-risk/profile|Ongoing Account Risk]]
**Industry:** [[industries/neobanks|Neobanks]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Anomaly detection is a developed field that has long distinguished novelty from malice, and transaction monitoring treats every deviation as a threat.
**Tags:** #change-point-detection #gaussian-mixture-models #dbscan #confidence-intervals #evaluation-metrics #hypothesis-testing #gradient-boosting #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to tell a fraudster from a customer having a bad month, using the institution's own ledger — and whoever does that stops freezing the wages of people who did nothing wrong.

## The Problem
Anomaly detection is a mature area with a substantial literature, and one of its oldest lessons is that an anomaly is not necessarily a problem — novelty detection, concept drift and contextual anomaly are established distinctions, and practitioners in fraud, security and industrial monitoring all learned that alerting on every deviation produces an unusable system. The techniques for contextualising an anomaly, modelling per-entity normality and distinguishing benign change from malicious change are documented. Transaction monitoring at these institutions largely alerts on deviation.

## What Already Exists
Contextual and collective anomaly frameworks; per-entity normality modelling; novelty versus outlier distinction; concept drift detection; and alert triage with severity grading.

## The Customization Gap
The adaptation is to a domain where the benign anomalies are life events and the response is confiscatory. It requires: (1) a taxonomy of benign causes, since the institution can enumerate the ordinary reasons a customer's behaviour changes and use them as competing explanations — this positive modelling of benign change is what generic anomaly detection lacks and is the substantive addition; (2) a graded response, because the standard practice raises an alert and here the system takes an action against the customer immediately; (3) regulatory obligations that constrain what may be ignored, which no industrial monitoring context has; (4) an adversary who studies the thresholds, so the normality model must be robust to deliberate conditioning; and (5) customer tenure and history as a strong prior, which per-entity modelling supports well and which current implementations underuse.

## Target Customer
Risk operations and compliance teams at digital banks, transaction monitoring vendors, and anomaly detection practitioners for whom benign-cause modelling is an unserved requirement.

## Impact If Solved
The field learned long ago that alerting on every deviation produces an unusable system, and transaction monitoring does exactly that. Enumerating benign causes as competing explanations is the addition generic anomaly detection lacks and the institution's own history supplies.
