# A Rate Adequacy Monitor for Every State and Line

**Niche:** [[niches/property-casualty-insurers/personal-lines-pricing/profile|Personal Lines Pricing & Rate Filings]]
**Industry:** [[industries/property-casualty-insurers|Property & Casualty Insurers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A national personal-lines writer files rates in fifty-plus jurisdictions on different calendars, and nobody sees in one place where the approved rate has fallen behind loss trend.
**Tags:** #time-series-forecasting #bayesian-inference #confidence-intervals #feature-engineering #evaluation-metrics #revenue-impact
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor is fighting to keep filed personal-lines rates ahead of loss trend, but writing it produces two contests with different winners: in auto, ranking drivers more finely than the carrier quoting next to them and getting that segmentation through rate review; in homeowners, getting a modelled catastrophe load and the cost of reinsurance accepted in high-hazard states without being forced to shrink. Decomposed into contested sub-niches below.

## The Problem
Rate adequacy is computed state by state, line by line, at the moment someone prepares a filing. Between filings, loss trend moves: repair costs, medical severity, litigation in a given venue, catastrophe exposure. The indicated rate drifts away from the approved one. A state whose filing was disapproved or cut runs inadequate for a year or more before anyone re-runs the numbers, and by then the carrier is often non-renewing or restricting new business.

## Why Nobody Has Built This
Indications live in actuarial spreadsheets owned by individual state actuaries. Approval outcomes live in the filing team's tracker, and emerging losses in the reserving data. Rating engine vendors sell rate deployment, not monitoring. Each team sees one piece.

## What to Build
A continuously updated indication for every state, line and major coverage. It blends emerging losses with credibility weighting toward the countrywide trend, carries uncertainty bands, and records what was filed, what the regulator approved, when it took effect and what each filing said would happen. It flags states where the approved rate trails the indication beyond tolerance, and estimates the premium lost per month of delay.

## Target Customer
Chief pricing actuaries and personal-lines product heads at national and super-regional carriers.

## Impact If Built
Filing priorities follow measured inadequacy instead of the calendar, and executives see the cost of a disapproved filing before it turns into a market withdrawal.
