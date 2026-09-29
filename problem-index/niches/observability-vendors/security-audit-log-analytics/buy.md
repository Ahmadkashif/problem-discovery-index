# Detection Engineering as a Measured Discipline

**Niche:** [[niches/observability-vendors/security-audit-log-analytics/profile|Security & Audit Log Analytics]]
**Industry:** [[industries/observability-vendors|Observability Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Detection rules are written, deployed and never evaluated, which is exactly the alerting problem the engineering half of this category has, with the added property that nobody knows what the rules failed to catch.
**Tags:** #hypothesis-testing #confidence-intervals #evaluation-metrics #logistic-regression #cross-validation #descriptive-statistics #compliance #automation
**Contested on:** Every serious competitor here is fighting to make years of security-relevant logs affordable to keep and fast to investigate — and whoever does that takes the security operations account, because retention is mandated and the cost of it is the reason teams keep changing vendors.

## The Problem
A security operations centre runs several hundred detection rules. Some fire constantly and are tuned down or ignored. Some have never fired. Nobody can say which rules have ever led to a confirmed incident, which are silently broken because their log source changed format, or what proportion of actual intrusion techniques the rule set covers. The discipline of evaluating detections exists in the practitioner community and the tooling to support it mostly does not.

## What Already Exists
Detection engineering practice with published frameworks and a threat technique taxonomy that provides a coverage vocabulary; adversary emulation and breach simulation tooling that generates known-malicious activity to test against; detection-as-code practices with version control and testing; and the entire precision-recall apparatus from machine learning evaluation. Purple team exercises as the manual version of the same idea.

## The Customization Gap
The adaptation is to rare events with no ground truth. It requires: (1) coverage measured against a technique taxonomy rather than by rule count, since three hundred rules concentrated on two techniques is worse than eighty spread across thirty, and rule count is the number currently reported; (2) synthetic positives from emulation tooling to establish recall, because real positives are far too rare to measure against and emulation is the only practical source of known-true events; (3) rule health monitoring separate from rule firing, since a rule that stopped matching because its log source changed format looks identical to a rule with nothing to detect — and this silent failure is the commonest and least noticed; (4) an honest alert quality inventory in the four classes the engineering alerting niche describes — fired and actioned, fired and ignored, never fired, missed the incident — which needs no modelling and is the fastest available improvement; and (5) analyst outcome capture, since whether an alert led anywhere is known to the analyst and recorded nowhere in a form that can be aggregated.

## Target Customer
Security operations functions, security analytics vendors, detection content providers, and the breach and attack simulation vendors whose output is the missing evaluation input.

## Impact If Solved
Detection rule sets are unevaluated in exactly the way engineering alert sets are, with the additional problem that the misses are invisible. Technique coverage and emulation-based recall are the two adaptations, and rule health monitoring catches the silent failures that currently go unnoticed for months.
