# Experience Studies Rebuilt by Hand Every Year

**Industry:** [[life-insurance-carriers|Life Insurance Carriers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every carrier rebuilds its mortality, lapse and annuitisation experience studies from admin extracts each year, in SAS and spreadsheets, because generic analytics tools do not know what an exposure year is.
**Tags:** #survival-analysis #bayesian-inference #feature-engineering #descriptive-statistics #confidence-intervals #data-integration #compliance #automation

## The Problem
Assumption-setting depends on experience studies. They compare actual deaths, lapses, surrenders, partial withdrawals and income-rider elections against what was expected, cut by issue age, duration, class, face band, distribution channel and underwriting path. LDTI requires cash-flow assumptions to be reviewed at least annually, PBR under VM-20 requires company experience with credibility-weighted margins, and VM-51 requires experience to be reported to the NAIC. So the studies are never one-offs. In practice an experience-study team pulls extracts from several admin systems, each with its own status codes and date conventions. It reconstructs policy histories, computes exposure by policy year and calendar year, joins deaths from claims and death-master matching, and rebuilds the same tables in SAS, Python and Excel. Then it spends weeks reconciling counts to the valuation file. The same carrier may run separate, inconsistent versions for pricing, valuation and reinsurance.

## What Already Exists
General BI and data platforms (Snowflake, Databricks, Power BI, Tableau) store and chart the data. Actuarial projection systems (Moody's AXIS, FIS Prophet) consume assumptions but do not build them. Some consultancies and vendors sell experience-study tooling, and the SOA publishes industry tables and its own study methods. Reinsurers run studies on ceded business.

## The Customisation Gap
The life-specific logic is where the work sits. Exposure calculation on policy-year and calendar-year bases with fractional exposure at entry and exit. Mapping admin status codes (lapse, surrender, reduced paid-up, extended term, conversion, death, claim pending) across systems and decades. Incurred-but-not-reported deaths and late death-match adjustments. Select-and-ultimate structure, mortality improvement and industry-table comparisons. Credibility weighting of company experience against industry tables, as VM-20 prescribes. Dynamic lapse as a function of moneyness and surrender charge. And output in the VM-51 format and the assumption-governance package auditors review. A generic tool computes a ratio. It does not know that a policy which lapsed in its grace period and then reinstated was never a lapse.

## Impact If Solved
A study cycle that takes a team two to three months (estimate) shrinks to weeks. Pricing, valuation and reinsurance work from one reconciled study, and the actuary spends the time on what the experience means rather than on rebuilding exposure. For a carrier facing annual LDTI assumption reviews and the VM-22 rollout, that is the difference between assumption changes driven by evidence and ones driven by the calendar.
