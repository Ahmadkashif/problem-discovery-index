# Compression Against New Hires Nobody Monitors

**Niche:** [[niches/hr-tech-platforms/compensation-and-pay-equity/profile|Compensation & Pay Equity]]
**Industry:** [[industries/hr-tech-platforms|HR Tech Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** New hires are paid at current market and existing employees receive a merit increase, so the gap between them widens every year, and the single most computable driver of both attrition and pay inequity is monitored almost nowhere.
**Tags:** #descriptive-statistics #evaluation-metrics #hypothesis-testing #confidence-intervals #survival-analysis #revenue-impact #quick-win #automation
**Contested on:** Every serious competitor in compensation software is fighting to check a pay decision for equity and market position before it is made rather than after — and whoever moves the check to the point of decision takes the account.

## The Problem
A team's four-year veterans were hired when the market rate for their role was one number and have received three percent increases since. The two people hired last quarter were paid the current market rate, which is meaningfully higher. Everyone eventually finds out, because salary information circulates and because pay transparency rules increasingly post the range. The veterans are simultaneously the most productive, the most expensive to replace, and the most underpaid relative to the market they can access. They leave, and are replaced at the new market rate, which is the most expensive possible resolution. The comparison that would have revealed it — what this organisation is currently paying to hire into this role, against what it pays the incumbents — is a query against its own offer data.

## Why It's Still Broken
Merit increase budgets and external hiring budgets are set by different processes with different constraints, and nothing reconciles them: the merit budget is a percentage of payroll set by finance, and the offer is set by what the market demands. The comparison falls between total rewards and talent acquisition. And the correction is expensive — adjusting a whole cohort of incumbents costs real money in-year — so an organisation that computes the number acquires an obligation, which is a reliable reason for the number not to be computed.

## What a Fix Looks Like
Compute compression continuously and report it by role and by team. For every role where the organisation has hired externally in the past year, compare the offers made to the pay of incumbents at the same level, controlling for the factors that legitimately differ. Report the gap with the affected population and the cost to close it, which is the number a total rewards leader needs to make the argument to finance and currently has to assemble by hand. Add the attrition link, which is what turns it from a fairness finding into a business case: compression is measurably associated with departure in most organisations' own data, and the cost of the departures is comparable to or larger than the cost of the correction. Flag compression at the point of offer, as the build note describes, so the problem stops being created. And be honest in the reporting about which incumbents are affected, because the remedy is a specific list of people and an aggregate gap invites an aggregate response that reaches nobody.

## Who Feels the Pain
Long-tenured employees paid below people they are training; managers who lose them and cannot explain why; and the organisation, which pays market rate for the replacement anyway and loses the institutional knowledge as well.

## Impact If Fixed
Compression is computable from the organisation's own offer and payroll data, is one of the strongest known attrition drivers, and is monitored by almost nobody. Pairing the gap with the attrition cost is what makes the correction fundable, and the point-of-offer flag is what stops the gap being recreated the following quarter.
