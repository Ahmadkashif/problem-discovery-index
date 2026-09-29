# Data Quality Monitoring and Drift Detection

**Niche:** [[niches/web-data-extraction-firms/extraction-correctness/profile|Extraction Correctness]]
**Industry:** [[industries/web-data-extraction-firms|Web Data Extraction Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Data observability vendors built exactly the monitoring this needs — freshness, volume, distribution and schema change detection — and pointed it at warehouses rather than at collection.
**Tags:** #change-point-detection #hypothesis-testing #evaluation-metrics #descriptive-statistics #probability-distributions #confidence-intervals #automation #data-integration
**Contested on:** Every serious competitor in this niche is fighting to detect when an extraction is returning plausible wrong values rather than no values — and whoever does that takes the account, because silent corruption is the failure customers cannot defend against.

## The Problem
Detecting that a data feed has quietly changed character — volume moved, a field's distribution shifted, nulls appeared where they never were, a category vanished — is what the data observability category was built for, and it works. Those products monitor warehouse tables produced by internal pipelines. The most volatile, least controlled, most silently-breaking data source any company consumes is web extraction, and almost nobody points this machinery at it.

## What Already Exists
Data observability platforms with automated distribution, volume and freshness monitoring; anomaly detection tuned to data pipelines; schema change detection and alerting; data quality assertion frameworks with automatic expectation generation; and incident workflows with root cause hints.

## The Customization Gap
The adaptation is to a source that changes because someone else redesigned their website. It requires: (1) monitoring at the source and field granularity rather than at the table level, since a thousand sites feed one table and an aggregate distribution hides a single source going wrong — this granularity mismatch is why the existing tools miss the failure entirely; (2) the page structure itself as a monitored signal, which has no analogue in warehouse monitoring and is the earliest available warning; (3) tolerance for legitimate volatility, because web data genuinely moves — prices change, listings appear and vanish — and a monitor tuned for warehouse stability will alert constantly; (4) cross-source corroboration as a check, which is available here and unavailable in the internal-pipeline setting the tools were designed for; and (5) alert routing to the extraction engineer who can fix the selector rather than to a data team who cannot.

## Target Customer
Extraction firms, their customers, and the data observability vendors for whom web collection is an unserved and unusually well-suited source type.

## Impact If Solved
The monitoring machinery is mature and pointed at the most stable data a company has rather than the least. Source-and-field granularity plus page structure as a monitored signal are the two adaptations that make it catch what it currently misses.
