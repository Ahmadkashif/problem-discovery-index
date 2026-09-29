# Anomaly Detection Adapted to Thin, Judgment-Based Markets

**Niche:** [[niches/catering-companies/commodity-price-reporting-agencies/profile|Food Commodity Price Reporting Agencies]]
**Industry:** [[industries/catering-companies|Catering Companies]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Market surveillance tools are built for exchanges with continuous order books; these markets have a handful of trades a day and a human deciding what they mean, and no product exists for that.
**Tags:** #change-point-detection #probability-distributions #confidence-intervals #hypothesis-testing #gaussian-mixture-models #time-series-forecasting #evaluation-metrics #automation #compliance #data-integration

## The Problem
A published assessment that is materially wrong causes immediate, quantifiable damage, because contracts settle on it. Errors arise from a stale input treated as current, a source's self-interested quote weighted too heavily, a data entry mistake, or a market that moved between the reporter's calls and publication. Detection today is the reporter's own judgment plus a supervising editor's read, both under deadline, and the most common way an error is found is a subscriber calling the next morning. Cross-checks against related markets — a protein cut whose price should track a neighbouring cut, a regional quote that should move with the national one — are done informally when someone thinks of it.

## What Already Exists
Market surveillance and data quality tooling is well developed. Nasdaq's and other vendors' surveillance suites detect manipulation and anomalous trading; the data observability platforms handle distribution shift, freshness, and volume anomalies with learned thresholds; statistical process control libraries cover the general problem thoroughly. All of it is inexpensive and proven.

## The Customization Gap
Every one of these assumes a data-rich series. Exchange surveillance needs an order book; observability tooling needs enough history per entity to learn a distribution. A thinly traded assessed market provides neither — some quotations rest on a handful of transactions, and the series is a sequence of human judgments rather than of observed transactions, so "anomalous" cannot be defined against the entity's own history. The information that would actually catch an error is structural: the assessment's relationship to substitutable and adjacent products, to the same product in other regions, to the input costs upstream, and to the seasonal and supply-driven patterns the reporter knows about and the tool does not. The adaptation is anomaly detection over a product relationship graph, where each assessment is evaluated against what its neighbours imply and the strength of that inference scales with how much support the day actually had. Alerting must be economically weighted — a small divergence on a heavily referenced benchmark matters far more than a large one on a quotation few contracts cite — and must arrive before publication, which means the whole thing runs inside a deadline measured in minutes.

## Target Customer
Editors and heads of market reporting responsible for published accuracy, and the compliance functions that need a demonstrable pre-publication control.

## Impact If Solved
Catches the errors that do the most contractual damage before they publish rather than after a subscriber calls. It also supplies the control evidence that benchmark governance frameworks expect, which agencies currently satisfy with process description rather than with a demonstrable check.
