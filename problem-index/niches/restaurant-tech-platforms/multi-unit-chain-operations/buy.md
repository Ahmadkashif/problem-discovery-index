# Data Quality Tooling Applied to Above-Store Reporting

**Niche:** [[niches/restaurant-tech-platforms/multi-unit-chain-operations/profile|Multi-Unit Chains — Making Units Comparable]]
**Industry:** [[industries/restaurant-tech-platforms|Restaurant Tech Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Data observability and quality tooling is a mature, largely open-source category built for exactly this problem — many sources, drifting semantics, silent breakage — and restaurant above-store reporting has adopted none of it.
**Tags:** #descriptive-statistics #hypothesis-testing #change-point-detection #evaluation-metrics #confidence-intervals #data-integration #automation #compliance
**Contested on:** Every serious competitor selling to multi-unit restaurant operators is fighting to make forty locations' numbers mean the same thing, so that an underperforming unit can be identified rather than argued about — and whoever makes units genuinely comparable takes the account.

## The Problem
A unit's inventory counts stop arriving because a manager left and nobody was trained on the Monday count. The above-store report continues to produce numbers for that unit, carried forward from the last count, and looks entirely normal for six weeks. Nobody notices until a period close produces an absurd variance. Every failure mode in this niche has this shape — silent, gradual, and invisible in a report designed to display numbers rather than to notice their absence.

## What Already Exists
Great Expectations, Soda, dbt tests, Monte Carlo and the broader data observability category provide freshness monitoring, volume and distribution checks, schema drift detection and anomaly alerting, most of it open source and all of it mature. These are precisely the controls this problem needs, developed for analytics pipelines that look structurally identical to a forty-unit reporting stack.

## The Customization Gap
The adaptation is defining what a check means in restaurant terms and routing it to someone who can act. It requires: (1) freshness and completeness expectations per unit per feed — counts, invoices, waste logs, schedules — with thresholds that reflect the unit's own pattern rather than a global rule, since a unit that counts weekly and one that counts daily are both fine; (2) distributional checks framed operationally, so the alert says "unit 23 has reported no waste for eleven days, which it has never done before" rather than reporting a statistical anomaly; (3) item catalogue drift detection against the group canonical, which is the single most common and most damaging failure and is trivially detectable; (4) routing to the district manager rather than to a data team, because there is no data team and the fix is a conversation with a general manager; and (5) expressing the consequence, so the alert explains which reports are currently unreliable for that unit, which is what makes it get acted on.

## Target Customer
Multi-unit operators and franchise systems, and the above-store vendors who could add a quality layer far more cheaply than they could add another report.

## Impact If Solved
Silent data failures are the largest source of wasted above-store effort and the reason variance meetings are inconclusive, and detecting them is a solved problem in a neighbouring discipline. The tooling is mostly free; the work is in the restaurant-specific expectations and in routing alerts to people who do not think of themselves as data users.
