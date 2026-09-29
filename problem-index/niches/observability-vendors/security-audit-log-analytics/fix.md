# The Log Source That Stopped Forwarding

**Niche:** [[niches/observability-vendors/security-audit-log-analytics/profile|Security & Audit Log Analytics]]
**Industry:** [[industries/observability-vendors|Observability Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** A firewall stops forwarding logs after a configuration change and nobody notices for five months, because a source that sends nothing looks exactly like a source with nothing to report.
**Tags:** #change-point-detection #time-series-forecasting #descriptive-statistics #hypothesis-testing #confidence-intervals #compliance #quick-win #automation
**Contested on:** Every serious competitor here is fighting to make years of security-relevant logs affordable to keep and fast to investigate — and whoever does that takes the security operations account, because retention is mandated and the cost of it is the reason teams keep changing vendors.

## The Problem
During an investigation an analyst notices that a particular device's logs stop in March. A firmware update changed the syslog configuration and the forwarding was not restored. Five months of network events from a perimeter device do not exist, in an environment where their existence is a compliance requirement and their absence is a gap in every investigation covering that period. Nothing alerted, because the platform monitors what arrives and has no expectation of what should.

## Why It's Still Broken
Ingestion monitoring is volume-based and aggregate, so one source among hundreds going silent is lost in the total. There is frequently no authoritative inventory of which sources are expected to forward, which means the platform cannot know something is missing — the same inventory problem the shadow endpoint niche describes. Source onboarding is a project and source health is nobody's continuing responsibility. And the failure is silent by construction: an absent log generates no event.

## What a Fix Looks Like
Monitor expectation rather than arrival. Maintain an inventory of expected sources with their owners, derived from the asset inventory rather than from a spreadsheet, which is the prerequisite and is usually the missing piece. Baseline each source's normal volume and periodicity — including the ones that are legitimately quiet overnight or at weekends — and alert on silence relative to that baseline, which catches the March firewall in hours rather than months. Validate format as well as arrival, since a source that changed its log format is still forwarding and is no longer parsing, which is an equally silent failure and is frequently worse because the volume looks correct. Check field-level completeness, because a source that stopped populating the user field is intact by every volume measure and useless for investigation. Report coverage against the detection rules that depend on each source, so the security consequence of a gap is stated rather than implied. And treat source health as a compliance control with an owner and a report, since in most regulated environments that is exactly what it is.

## Who Feels the Pain
Analysts discovering gaps mid-investigation; compliance functions attesting to logging they cannot verify; and organisations whose incident scope cannot be established because a device stopped talking.

## Impact If Fixed
Volume baselining per source with silence alerting is elementary and catches the commonest failure within hours instead of months. Format and field-completeness validation catches the subtler variants, and coverage-against-detections states the consequence in terms a security leader can act on.
