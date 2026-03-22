# Cross-Location Provider Performance Analytics

**Niche:** [[niches/dental-practices/dental-service-organizations/profile|DSOs (Dental Service Organizations)]]
**Industry:** [[industries/dental-practices|Dental Practices]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A platform that benchmarks dentists across locations on production per hour, case acceptance, re-treatment rates, patient satisfaction, and schedule utilization — giving DSO leadership the granularity to identify coaching opportunities versus compensation adjustments across 50+ providers.
**Tags:** #gradient-boosting #random-forests #feature-engineering #evaluation-metrics #cross-validation #time-series-forecasting #data-integration #revenue-impact #tacit-knowledge-ml

## The Problem
A DSO with 50 locations and 150 providers has no standardized way to compare provider performance. Provider A at Location 12 produces $180/hour while Provider B at Location 7 produces $280/hour — but is that because Provider B is more skilled, because Location 7 has a wealthier patient base with better insurance, or because Location 7's office manager is better at treatment plan presentation? Disentangling provider skill from location context from support staff quality from patient mix is a multivariate problem that DSOs currently solve with gut feel and spreadsheets. Regional managers develop tacit intuition about which providers are underperforming versus which are in difficult markets, but this judgment is inconsistent across managers and doesn't scale. The consequence: underperformers are retained too long while strong performers in weak markets are unfairly penalized.

## Why Nobody Has Built This
The data sits in enterprise PMS systems (Denticon, CareStack) and is technically accessible, but building meaningful provider benchmarks requires normalizing for confounders: patient insurance mix (Medicaid vs. PPO vs. fee-for-service), procedure mix (a pediatric-heavy location will have lower production per hour than a restorative-heavy one), geographic cost of living, and support staff capability. A random forest or gradient-boosted model can control for these factors and produce a "risk-adjusted production" metric per provider, but building this requires deep dental domain knowledge to define the right features and validation from clinical leadership to ensure the metrics don't incentivize overtreatment. No analytics vendor has combined dental domain expertise with ML engineering capability at this level of specificity.

## What to Build
A provider analytics platform that ingests production data, scheduling data, procedure codes, insurance claims, patient satisfaction surveys, and re-treatment records from the enterprise PMS. The core model: a gradient-boosted regression that predicts expected production per provider-hour given the provider's location, patient mix, procedure mix, and support staff — then flags providers whose actual production deviates significantly from expected. Additional modules: case acceptance benchmarking (what percentage of diagnosed treatment do patients accept, normalized by procedure type and patient demographics), re-treatment rate tracking (how often does a provider's work need to be redone within 24 months — a quality signal), and schedule utilization (chair-hours filled vs. available, accounting for no-shows and cancellations). Each metric comes with peer comparison and trend lines, enabling coaching conversations grounded in data rather than opinion.

## Target Customer
DSOs with 20+ locations where provider performance variability directly impacts EBITDA — particularly PE-backed groups preparing for valuation events where demonstrating operational discipline commands a premium multiple.

## Impact If Built
Identifies the top and bottom decile of providers by risk-adjusted performance, enabling targeted coaching that lifts bottom-quartile production by 15-25%. For a 50-location DSO with $200M revenue, a 5% production lift from better provider management represents $10M in annual revenue — worth $500K-1M/year in software spend.
