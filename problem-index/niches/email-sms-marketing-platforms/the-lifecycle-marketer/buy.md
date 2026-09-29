# Production Operations Practice

**Niche:** [[niches/email-sms-marketing-platforms/the-lifecycle-marketer/profile|The Lifecycle Marketer]]
**Industry:** [[industries/email-sms-marketing-platforms|Email & SMS Marketing Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Software engineering built monitoring, alerting, change control and runbooks for systems that must keep working, and marketing automation has a diagram.
**Tags:** #workflow-orchestration #change-point-detection #automation #evaluation-metrics #compliance #descriptive-statistics #worker-facing #data-integration
**Contested on:** Every serious competitor in this niche is fighting to make fifty automated journeys comprehensible and monitored by one person — and whoever does that changes how much of a brand's lifecycle programme actually runs.

## The Problem
Running automated systems reliably is a mature engineering discipline: monitoring and alerting on the behaviour that matters, change control with review and rollback, documentation generated from configuration, dependency mapping, incident response and postmortems. Any team running production software does all of this as standard. Marketing automation is production software — it runs continuously, touches customers, and fails silently — and is operated with none of it by people who were never offered it.

## What Already Exists
Metric monitoring with anomaly alerting; change management with review, staging and rollback; configuration-as-documentation; dependency and service mapping; and incident response with postmortem practice.

## The Customization Gap
The adaptation is to an operator who is a marketer and a system whose failures are silent. It requires: (1) alerting on absence rather than on errors, since a flow that stops firing produces nothing and every monitoring default is built around error signals — this inversion is the central adaptation; (2) alert definitions a non-engineer can set and understand, since the operator will not write a query language; (3) change control that does not slow a marketer whose job includes changing things weekly, which is a genuine tension and where heavy process would simply be bypassed; (4) the blast radius being customer trust rather than system availability, which changes what warrants an alert — four messages in a day is an incident that no infrastructure model would flag; and (5) cross-flow interaction as a first-class concern, since the flows are independent by construction and the customer experiences their sum.

## Target Customer
Lifecycle marketers and marketing operations, messaging platform vendors, and observability vendors for whom marketing automation is an unserved production system.

## Impact If Solved
Marketing automation is production software operated with none of the practice, by people never offered it. Alerting on absence rather than errors is the inversion that matters, and the blast radius is customer trust rather than availability.
