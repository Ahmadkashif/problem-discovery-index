# Pipeline Reliability and Data Quality Monitoring

**Industry:** [[data-platform-integrators|Data Platform Integrators]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Observability tooling alerts on freshness and volume against thresholds somebody set at deployment, and the failures that actually matter are semantic changes the thresholds do not see.
**Tags:** #change-point-detection #time-series-forecasting #gradient-boosting #hypothesis-testing #dbscan #confidence-intervals #evaluation-metrics #data-integration

## The Problem
Data platforms fail continuously and mostly quietly. A source system changes a field's meaning without changing its type. A currency column starts arriving in a different denomination. An upstream team deprecates a status value and introduces two new ones. A join that was one-to-one becomes one-to-many after a business process change, silently duplicating rows.

None of that trips a freshness or row-count check. The pipeline runs, the tests pass, and the numbers are wrong. Discovery happens when someone downstream notices a figure that does not match their expectation, usually weeks later, and then the team works backwards through the lineage to find where it started — and has to decide how much reporting was affected in the interim.

The tests that exist are the ones somebody wrote at build time: not null, unique, accepted values, referential integrity. They are valuable and they encode the assumptions the builder happened to think of, which is a subset of the assumptions the models actually rely on.

## What Already Exists
Monte Carlo, Bigeye, Metaplane, Elementary and Soda all provide data observability with automated anomaly detection on freshness, volume and schema, and they are genuinely useful. dbt tests are ubiquitous and cheap to write. Great Expectations provides a rich assertion framework. Contracts and schema enforcement have improved in dbt and in streaming platforms. Lineage from catalogues supports impact analysis once a problem is identified.

## The Customisation Gap
The generic monitors watch structural properties — did the data arrive, is there the usual amount of it, did the schema change — and the expensive failures are semantic. The distribution of a categorical column shifting, a numeric column's scale changing, the cardinality of a join relationship changing, a value that always appeared now missing for one segment: each of these is detectable as a distributional change against a learned baseline, and each requires knowing what normal looks like for this specific table rather than applying a general rule.

The second gap is the propagation. When a semantic change is detected, the question is which downstream numbers were affected and which reports were consumed in the interim — which is answerable by combining lineage with query history and is not offered by any observability product. It is also the question that determines whether anyone has to be told.

The third is that alert volume determines whether monitoring works at all. A system that fires on every distributional wobble gets muted within a fortnight, after which it is worse than nothing. Prioritising alerts by the downstream consumption of the affected asset — a change in a table feeding the board report matters differently from one in a staging model nobody queries — is the obvious fix and requires exactly the usage data nobody joins.

## Impact If Solved
Silent semantic failures are the most expensive class of data problem because they corrupt decisions rather than stopping pipelines, and the current monitoring layer is structurally unable to see them. Distributional baselines catch them; lineage-plus-query propagation tells an organisation exactly what was affected and who consumed it; and consumption-weighted prioritisation is what keeps the alerts being read.
