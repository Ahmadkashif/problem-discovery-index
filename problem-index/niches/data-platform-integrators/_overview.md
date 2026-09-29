# Niche Analysis — Data Platform Integrators

**Parent Industry:** [[industries/data-platform-integrators|Data Platform Integrators]]

## Niche Selection

These firms build the systems other functions use to measure things and do not measure their own output. Query logs record every access, lineage records every dependency, and cost attribution records what each model costs to run — and no integrator joins the three. The eight niches below follow that: what of the estate earns its keep, what a migration should actually carry, what breaks in ways the monitoring cannot see, what it costs to run, and who absorbs the accumulation.

| # | Niche | Category | Est. Market Size | Digital Adoption | Target Buyer |
|---|---|---|---|---|---|
| 1 | Estate Utilisation | 🔵 High Market Share | ~$4.5B | Very low — never measured | Data leadership |
| 2 | Migration Scoping | 🔵 High Market Share | ~$3.6B | Low — translate everything | Programme leadership |
| 3 | Semantic Data Quality | 🟠 Low Digitized | ~$2.7B | Medium, wrong target | Data engineering leadership |
| 4 | Consumption Cost Engineering | 🟠 Low Digitized | ~$2.2B | Low — found on the bill | Platform and finance leadership |
| 5 | The Analytics Engineer | 🟣 Underserved Audience | ~$1.8B | Low — tracing by hand | Engineering leads |
| 6 | The On-Call Pipeline Engineer | 🟣 Underserved Audience | ~$1.4B | Low — rerun and backfill | Platform operations |
| 7 | Model Layer Discovery | ⚡ Highly Automatable | ~$1.1B | Low — naming conventions | Analytics engineering |
| 8 | Environment & Deployment Automation | ⚡ Highly Automatable | ~$0.7B | Medium — partial | Platform engineering |

## Why These Niches

Estate utilisation and migration scoping carry the money and the same unanswered question: which of what has been built is used, and therefore what should be carried forward. Semantic data quality and consumption cost are the two places where the tooling watches the wrong thing — freshness thresholds that miss a meaning change, and a transformation layer whose cost appears on a bill rather than in a review. The two underserved audiences are the engineer tracing four similarly-named models to add a column, and the one who reruns and backfills before the morning reports. The last two are mechanical: finding what exists, and shipping changes to it.

## Niches

- [[niches/data-platform-integrators/estate-utilisation/profile|🔵 Estate Utilisation]]
  - [[niches/data-platform-integrators/usage-instrumentation/profile|🎯 Usage Instrumentation]]
  - [[niches/data-platform-integrators/retirement-and-rationalisation/profile|🎯 Retirement & Rationalisation]]
- [[niches/data-platform-integrators/migration-scoping/profile|🔵 Migration Scoping]]
- [[niches/data-platform-integrators/semantic-data-quality/profile|🟠 Semantic Data Quality]]
- [[niches/data-platform-integrators/consumption-cost/profile|🟠 Consumption Cost Engineering]]
- [[niches/data-platform-integrators/the-analytics-engineer/profile|🟣 The Analytics Engineer]]
- [[niches/data-platform-integrators/the-oncall-pipeline-engineer/profile|🟣 The On-Call Pipeline Engineer]]
- [[niches/data-platform-integrators/model-discovery/profile|⚡ Model Layer Discovery]]
- [[niches/data-platform-integrators/deployment-automation/profile|⚡ Environment & Deployment Automation]]

## Filter Notes

Seven of the eight are terminal — each names one contest that every serious competitor is fighting over, and decomposing further would produce features rather than markets.

**Estate utilisation** is not. It names a property, and obtaining the benefit requires two things that fail for entirely different reasons. Usage instrumentation asks which assets are actually queried and by whom — a measurement problem over query logs, lineage and cost data that the platform already produces, deliverable as a report, and immediately valuable because no data platform owner can currently prove which part of their estate is inventory. Retirement and rationalisation asks how to act on that report — establishing that nothing depends on an asset, getting an owner to agree it can go, and deleting it without breaking something downstream — which is a risk, lineage and accountability problem rather than an analytical one, and is where every rationalisation effort actually stalls. Firms that have produced the usage report have watched nothing get deleted, because knowing an asset is unused is a long way from being willing to remove it. The two are separately bought and separately hard.

Two adjacent candidates were rejected as belonging elsewhere: **configuring the business applications that feed the platform** belongs to [[industries/saas-implementation-partners|SaaS Implementation Partners]], and **the warehouse product itself** sits with [[industries/database-platform-vendors|Database Platform Vendors]].
