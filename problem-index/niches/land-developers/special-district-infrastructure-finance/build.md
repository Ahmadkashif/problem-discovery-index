# Eligible-Cost Ledger Built as Costs Are Paid

**Niche:** [[niches/land-developers/special-district-infrastructure-finance/profile|Special-District Infrastructure Finance]]
**Industry:** [[industries/land-developers|Land Developers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Developers reconstruct which infrastructure costs a district can reimburse years after paying them, when the classification could be made the day each invoice is approved.
**Tags:** #large-language-models #bert #feature-engineering #evaluation-metrics #compliance #data-integration #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to turn a developer's infrastructure spend into district bond reimbursement, and whoever recovers the largest share of eligible cost in each bond series takes the account.

## The Problem
Before each bond series, the developer's accountant and the district engineer go back through years of pay applications, invoices, change orders and waivers to build the reimbursement exhibit. Lines that mix eligible and ineligible scope have to be split, costs allocated between districts and phases, and missing support chased from subcontractors who may have moved on.

## Why Nobody Has Built This
District finance is a state-specific niche (mainly Texas and Florida, plus a few others), the rules vary by district creation documents, and the people doing the work are small engineering and accounting firms billing hourly. Accounting vendors serve the general case.

## What to Build
A ledger that reads every approved invoice and pay-application line, classifies it against the district's eligible facility categories with a confidence, splits mixed lines, checks for the waiver and proof of payment, and keeps a running exhibit by district, phase and series. It forecasts what the next series can carry given assessed value and debt limits, so the developer prioritises the costs that will be reimbursed soonest.

## Target Customer
CFOs of developers active in MUDs and CDDs, and the district engineers and accountants who prepare reimbursements.

## Impact If Built
Every eligible dollar documented at payment is reimbursable in the first series that can carry it. On ~$30M of eligible infrastructure, moving 10% into the first series ~2 years earlier is worth ~$0.6M at ~10% a year, and it cuts ~2–4 weeks of preparation per bond application (all estimates).
