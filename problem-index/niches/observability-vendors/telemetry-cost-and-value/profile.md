# Telemetry Cost & Value

**Parent Industry:** [[industries/observability-vendors|Observability Vendors]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor here is fighting to tell an engineering organisation which telemetry is worth its cost — and whoever does that takes the budget conversation, because customers are currently cutting by volume, which is the only attribute they can see.

## Profile
**Market Size:** ~$1.6B US attributable to observability cost management and telemetry optimisation
**Share of Parent Industry:** ~13% of category revenue
**Digital Adoption:** None — value is unmeasured everywhere
**Target Buyer:** Engineering and platform leadership, and the finance function asking about the bill
**Automation Potential:** Very High — query, alert and ingestion data are all complete inside the platform

## What Makes This a Distinct Niche
Observability cost has become a board-level line item at many engineering organisations, frequently rivalling the infrastructure being observed, and the customers cannot tell which telemetry is earning its cost. Volume-based pricing rewards collection while nobody measures which signals ever get queried, so teams pay to store data that has never been read and then cut the wrong things when the bill forces a decision. What makes this a distinct and unusually clean contest is that the value signal is complete and sitting inside the platform: query logs record what was touched and by whom, alert definitions record what underpins a rule, incident investigations record what an engineer actually looked at, and ingestion records the cost. Joining those four produces a value-per-dollar ranking, and the reason it does not exist is commercial rather than technical — which is also why the natural home for it is a collector layer or a third party rather than an incumbent.

## Current Tools & Gaps
Usage and billing dashboards, per-index cost breakdowns, retention settings, and a small number of cost management vendors. The gaps: cost is reported and value is not, so every decision is made on one side of a ratio; retention and sampling are global policies where the right answer is per stream; the regret of a cut — whether the dropped data was subsequently needed — is never measured, which is the only test a customer will believe; cost anomalies are reported at the account level rather than attributed to the service, metric and label that caused them; and the incumbents' incentives run against all of it.

## Problems
- [[niches/observability-vendors/telemetry-cost-and-value/build|🔨 Build: Cutting by Volume Because Volume Is All You Can See]]
- [[niches/observability-vendors/telemetry-cost-and-value/buy|🛒 Buy: Cache and Retention Policy Is a Solved Optimisation]]
- [[niches/observability-vendors/telemetry-cost-and-value/fix|🔧 Fix: The Cost Anomaly Attributed to a Team]]
