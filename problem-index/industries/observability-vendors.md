# Observability Vendors

## Profile
**Category:** Developer Tools & Infrastructure
**Market Size:** ~$12B US observability, monitoring and logging
**Tech Maturity:** Very high and painfully expensive — Datadog, Splunk, New Relic, Dynatrace, Grafana and Elastic collect and query telemetry at extraordinary scale. The category's defining complaint is that the bill grows faster than the value, and its defining failure is that during an incident the tooling shows everything and answers nothing.
**Workforce:** Solutions architects, support engineers, instrumentation and integration engineers, pricing and packaging analysts, site reliability advocates

## Key Pain Themes
Observability spend has become a board-level line item at many engineering organisations, frequently rivalling the infrastructure being observed, and customers cannot tell which telemetry is earning its cost. Volume-based pricing rewards collection while nobody measures which signals ever get queried, so teams pay to store data that has never been read and cut the wrong things when the bill forces a decision. The second failure is diagnostic: during an incident an engineer has dashboards, traces and logs and must construct the causal story themselves, under time pressure, at whatever hour it is. Alerting sits between the two — thresholds set by hand on services whose normal behaviour nobody characterised, producing a stream that gets muted. Support engineers spend their days on cardinality explosions and instrumentation gaps, and the on-call engineer is the person the whole category was built to help and mostly does not.

## Current Tech Landscape
Datadog leads the integrated market and is the reference point for the pricing complaint; Splunk dominates security-adjacent logging; Grafana and its open-source stack have grown as the cost-conscious alternative; Elastic serves search-shaped workloads. OpenTelemetry has genuinely succeeded as an instrumentation standard and is decoupling collection from vendors, which is reshaping competitive dynamics. Managed Prometheus and columnar log stores have shifted cost structures. Incident response tooling is adjacent and increasingly overlapping. Automated root cause analysis is claimed widely and trusted narrowly.

## Problems
- [[problems/observability-vendors/high-impact|🔴 High Impact: Causal Diagnosis During an Incident]]
- [[problems/observability-vendors/low-impact-1|🟡 Low Impact: Telemetry Cost Attribution and Retention]]
- [[problems/observability-vendors/low-impact-2|🟡 Low Impact: Alert Threshold Configuration]]
- [[problems/observability-vendors/worker-life-1|🟢 Worker Life: The On-Call Engineer at Three in the Morning]]
- [[problems/observability-vendors/worker-life-2|🟢 Worker Life: Support Engineer on Cardinality and Instrumentation]]
- [[problems/observability-vendors/ml-opportunity|🧠 ML Opportunities]]
- [[problems/observability-vendors/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
These vendors hold the most detailed record of how production software actually fails that exists anywhere: telemetry from millions of services across thousands of organisations, with incidents, their propagation and their resolutions attached. Failure modes repeat across companies far more than any individual engineer can see, since each one experiences only their own outages. The category sells storage and query over that corpus and has never used it to say what an incident probably is — which is the only thing the person paging at three in the morning actually wants.
