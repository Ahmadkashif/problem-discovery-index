# Retention Priced So You Discard What You Will Need

**Niche:** [[niches/observability-vendors/security-audit-log-analytics/profile|Security & Audit Log Analytics]]
**Industry:** [[industries/observability-vendors|Observability Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Intrusions are routinely discovered months after they begin and log retention is priced so that most organisations keep ninety days, which means the investigation starts after the evidence was deleted.
**Tags:** #dimensionality-reduction #k-means-clustering #descriptive-statistics #time-series-forecasting #evaluation-metrics #confidence-intervals #compliance #revenue-impact
**Contested on:** Every serious competitor here is fighting to make years of security-relevant logs affordable to keep and fast to investigate — and whoever does that takes the security operations account, because retention is mandated and the cost of it is the reason teams keep changing vendors.

## The Problem
An organisation discovers evidence of an intrusion that appears to have begun eight months earlier. The investigation needs authentication logs, network flows and endpoint telemetry from that period. Ninety days are available at full fidelity; six months at reduced fidelity with several sources dropped; nothing before that. The scope of the compromise cannot be established, which means the disclosure cannot be accurate, the remediation cannot be targeted, and the regulator's question about what was accessed has no answer. The retention decision that caused this was made in a budget conversation about gigabytes.

## Why Nobody Has Built This
Security log volume is enormous and priced per gigabyte ingested, which makes multi-year retention of everything unaffordable for most organisations — so they choose, badly, because nothing tells them which sources matter for which investigation types. Tiering exists and is coarse: hot or cold, with cold frequently meaning unqueryable without a restoration process measured in hours. And the vendors' revenue is proportional to what is kept hot, which is the same commercial conflict the engineering half of the category has and is equally unaddressed.

## What to Build
Retention driven by investigative value rather than by age. Classify every log source by what it supports: which detection rules depend on it, which investigation types have historically required it, whether it establishes identity, access, movement or exfiltration — which produces a value ranking that is completely absent today and is the basis for every subsequent decision. Reduce rather than delete: aggressive structural reduction of the high-volume low-entropy sources, keeping the fields investigations actually use and discarding the rest, which typically preserves investigative value at a fraction of the volume. Tier by access pattern with genuinely queryable cold storage, since a cold tier that requires a restoration project is not retention in any operational sense. Model the retention decision explicitly against the discovery-time distribution — if intrusions are commonly found after six months, ninety days of retention is a decision to be unable to investigate, and stating it that way changes the budget conversation. Track investigative regret, recording when an investigation needed data that had been deleted, which is the measurement that makes the whole case. And report coverage against the detection content, so an organisation can see which rules are unsupported by retained data.

## Target Customer
Security operations and compliance functions, security log analytics vendors, and the data platform vendors positioning security lakes as the cheaper alternative.

## Impact If Built
Retention economics determine what can be investigated, and the choices are currently made in units of gigabytes rather than of investigative value. Structural reduction and genuinely queryable cold storage change the affordable horizon substantially, and regret tracking is the evidence that makes the case.
