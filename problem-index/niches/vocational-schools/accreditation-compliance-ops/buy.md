# Continuous Compliance Monitoring Dashboard

**Niche:** [[niches/vocational-schools/accreditation-compliance-ops/profile|Accreditation & Compliance Operations]]
**Industry:** [[industries/vocational-schools|Vocational Schools]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Higher education compliance dashboards exist but don't track the specific metrics vocational accreditors (ACCSC, COE) require — completion rate by program, placement rate by cohort, licensure pass rates — leaving schools blind to compliance risk until the accreditation cycle approaches.
**Tags:** #time-series-forecasting #gradient-boosting #tabular-ml #compliance #quick-win

## The Problem
Vocational schools learn they have a compliance problem when they start preparing their self-study — by then, the problem has been compounding for 2-3 years. ACCSC requires minimum 70% completion and placement rates by program; a school discovering it has fallen to 65% with 6 months until site visit has no time to correct course. Continuous monitoring of accreditation metrics would surface declining trends years before they become compliance failures, but no tool computes these metrics in real time from existing school data.

## What Already Exists
Higher education analytics platforms (Civitas, Watermark Student Success & Engagement) provide dashboards for academic institutions tracking retention and graduation rates for regional accreditation. BI tools (Tableau, Power BI) can visualize any data given proper configuration. Accreditation management platforms (Watermark/EAC) track standard compliance documentation status but don't compute performance metrics.

## The Customization Gap
ACCSC and COE metric definitions are specific and non-obvious: placement rate denominators exclude students unavailable for employment (disability, incarceration, military service, continued education) with specific documentation requirements for each exclusion. Completion rate calculations differ by program length and start date cohort definition. These metric-specific computations must be built as pre-configured calculations, not custom Tableau dashboards that each school must build from scratch. The tool needs to pull data from whichever SIS the school uses, compute metrics using the correct accreditor-specific formulas, and display trend lines with threshold alerts.

## Target Customer
School directors and compliance officers at accredited vocational schools who want year-round visibility into their accreditation performance metrics instead of discovering problems during self-study preparation.

## Impact If Solved
Provides 2-3 years of lead time to address declining performance metrics before accreditation cycle. Eliminates the manual metric computation process that consumes weeks of staff time during reporting periods. Prevents surprise accreditation findings that can result in probation (threatening Title IV eligibility and enrollment) — an existential risk worth $500K-$5M in annual tuition revenue.
