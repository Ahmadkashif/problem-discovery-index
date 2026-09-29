# Semantic Data Quality

**Parent Industry:** [[industries/data-platform-integrators|Data Platform Integrators]]
**Category:** 🟠 Low Digitized
**Contested on:** Every serious competitor in this niche is fighting to catch the data failures that matter — a field whose meaning changed — when the monitoring watches freshness and volume against thresholds somebody set at deployment.

## Profile
**Market Size:** ~$2.7B US
**Share of Parent Industry:** ~15% of category revenue
**Digital Adoption:** Medium, wrong target
**Target Buyer:** Data engineering leadership
**Automation Potential:** High — distribution and semantic drift detection

## What Makes This a Distinct Niche
Observability tooling alerts on freshness and volume against thresholds somebody set at deployment, and the failures that actually matter are semantic changes the thresholds do not see. A source system starts populating a field differently, a category is renamed upstream, a currency changes, a status code is reused. Every row arrives on time, the volume is normal, the pipeline reports success, and every number downstream is quietly wrong for weeks.

## Current Tools & Gaps
Freshness and volume monitors, a null check, and thresholds set once. The gaps: no distribution monitoring; no detection of category or code changes; no semantic contract with source systems; no downstream impact assessment; and no alerting on changes that pass every technical check.

## Problems
- [[niches/data-platform-integrators/semantic-data-quality/build|🔨 Build: Catching the Change That Passes Every Check]]
- [[niches/data-platform-integrators/semantic-data-quality/buy|🛒 Buy: Drift Detection From Machine Learning Operations]]
- [[niches/data-platform-integrators/semantic-data-quality/fix|🔧 Fix: The Status Code That Started Meaning Something Else]]
