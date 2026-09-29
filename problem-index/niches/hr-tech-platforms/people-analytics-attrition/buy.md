# Survival Analysis and Cohort Methods Already Standard Elsewhere

**Niche:** [[niches/hr-tech-platforms/people-analytics-attrition/profile|People Analytics & Attrition]]
**Industry:** [[industries/hr-tech-platforms|HR Tech Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Survival analysis, cohort retention and competing risks are standard methods in medicine, subscription businesses and credit, and HR reports attrition as an annualised percentage of headcount.
**Tags:** #survival-analysis #probability-distributions #maximum-likelihood-estimation #confidence-intervals #evaluation-metrics #hypothesis-testing #descriptive-statistics #cross-validation
**Contested on:** Every serious competitor in people analytics is fighting to diagnose the structural conditions that produce attrition months before the resignations — and whoever names the condition rather than scoring the person takes the account.

## The Problem
An organisation reports 14% annual voluntary turnover. That single number averages across tenure — where the hazard is strongly non-constant, with a peak in the first year and another around common vesting and promotion points — across job families with completely different dynamics, and across voluntary exits, involuntary exits and internal transfers, which are competing outcomes that a headcount ratio treats as one. Every methodological problem here was solved decades ago in disciplines that took time-to-event analysis seriously, and HR reports a ratio.

## What Already Exists
Survival analysis is among the most developed areas of applied statistics, with hazard modelling, competing risks, time-varying covariates, censoring and cohort comparison all standard and implemented in free tooling. Subscription businesses apply exactly these methods to customer retention as a matter of course. Clinical research provides the methodological rigour and the literature on interpreting time-to-event data. Nothing needs inventing; it needs importing across a disciplinary boundary that HR analytics has rarely crossed.

## The Customization Gap
The adaptation is to employment's own structure. It requires: (1) competing risks modelled properly — voluntary exit, involuntary exit and internal transfer are different outcomes and treating a transfer as an exit or as a censoring event gives different and both defensible answers, so the choice must be explicit; (2) time-varying covariates as the norm rather than the exception, since pay, manager, role and span all change during tenure and a model using values at hire is describing a different person; (3) tenure clock choices stated — time in company, time in role and time since last promotion are three different clocks and the hazard looks different on each, which is exactly the insight most HR reporting misses; (4) cohort definition that reflects organisational reality, including hire cohort, level cohort and reorganisation exposure; and (5) presentation that a people leader can use, since a hazard curve is not a management artefact and the value has to be delivered as a condition with a remedy rather than as a statistical output.

## Target Customer
People analytics teams and vendors, HCM incumbents, and the workforce planning functions whose headcount models are built on a single annualised rate.

## Impact If Solved
Time-to-event methods immediately reveal structure that an annual percentage hides — the first-year hazard, the vesting cliff, the post-promotion window — each of which implies a different intervention at a different moment. The methods are free and mature; the barrier has been that HR analytics grew out of reporting rather than out of statistics.
