# Parish Subsidy Impact Forecaster

**Niche:** [[niches/k12-private-schools/parish-diocesan-schools/profile|Parish & Diocesan Schools]]
**Industry:** [[industries/k12-private-schools|K-12 Private Schools]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool models how changes in parish financial health (Sunday collections, capital campaign results, pastor priorities) will impact the school subsidy and what tuition adjustments are needed to maintain viability.
**Tags:** #linear-regression #time-series-forecasting #tabular-ml #revenue-impact

## The Problem
A parish school's budget depends on a subsidy from the parish — typically $200K-$800K per year, covering 15-35% of operating costs. This subsidy is set annually by the pastor and parish finance council, and it can change with little warning when parish revenue declines (decreased Sunday collections, parishioner attrition) or parish priorities shift (new church building, pastor change). Principals learn of subsidy changes too late to adjust tuition, financial aid, or staffing, creating budget crises that result in emergency cuts.

## Why Nobody Has Built This
Parish financial data (Sunday collections, offertory trends, capital campaign performance) sits in parish accounting systems completely disconnected from school financial systems. The subsidy decision is partially financial and partially pastoral (a new pastor may view the school differently), making it resistant to pure data modeling. The market — 6,000 parish schools — is price-sensitive and accustomed to making do with Excel.

## What to Build
A financial planning tool that connects parish revenue trends (Sunday collections, major donor giving, capital campaign status) with school financial projections (enrollment, tuition, financial aid, operating costs). The tool models scenarios: "If parish subsidy drops 20%, what tuition increase or enrollment growth is needed to maintain current staffing?" It provides early warning when parish revenue trends suggest a subsidy reduction, giving the principal 6-12 months to plan instead of 60 days.

## Target Customer
Parish school principals and diocese superintendents managing financial planning across 10-50 parish schools, currently relying on annual budget conversations with limited forward visibility.

## Impact If Built
Gives principals 6-12 months of advance warning on subsidy changes versus the current 60-day notice. Prevents the 5-8% of parish school closures per decade that result from sudden financial shocks. Enables diocesan superintendents to identify financially vulnerable schools across the system and allocate stabilization funds proactively.
