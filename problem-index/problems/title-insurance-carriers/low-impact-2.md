# Statistical Plans and Rate Proceedings

**Industry:** [[title-insurance-carriers|Title Insurance Carriers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Statistical reporting and rate-filing tools are standard in property and casualty insurance, but title rates in Texas and the bureau states rest on agent-level premium, expense and loss data that the generic tools were never built to collect, reconcile or defend at a contested hearing.
**Tags:** #descriptive-statistics #linear-regression #confidence-intervals #hypothesis-testing #feature-engineering #compliance #data-integration #automation

## The Problem
In most states a title underwriter files its own rate manual. In Texas the commissioner sets the rates. TDI publishes a rate report from statistical data the underwriters and agents submit, and holds a hearing where the Texas Land Title Association, the Office of Public Insurance Counsel and TDI staff each present their own actuarial calculations. In February 2025 the commissioner ordered a 10% cut on a reported 26.6% industry profit ratio; TLTA, which had recommended no change, appealed on the ground that the data ran only through 2022. In December 2025 Order 2025-9697 cut basic premium rates by 6.2% from 1 March 2026, after TDI's September report gave indications of −6.2% to −14.9% on experience through 2024. Texas was the largest title state in 2025 at $2.7B of premium (ALTA). In New York and Pennsylvania, licensed rating bureaus (TIRSA and TIRBOP) file manuals that bind their members.

The underwriter's actuarial and statistical staff assemble the numbers from thousands of agents' production systems. Each system codes premium splits, reissue credits, simultaneous-issue discounts, endorsement charges and escrow fees differently. They reconcile the result to statutory annual statements, then defend it under cross-examination. Agent expense data matters here because agents keep most of the premium, which is not true of P&C statistical plans.

## What Already Exists
Property and casualty carriers report to statistical agents through mature pipelines and edit packages, described in [[niches/property-casualty-insurers/statistical-reporting-data-calls/profile|⚡ Statistical Reporting & Regulatory Data Calls]]. Rate filing consultancies prepare exhibits (see [[niches/property-casualty-insurers/rate-form-filing-consultancies/profile|🔍 Rate, Rule & Form Filing Consultancies]]), and BI and actuarial reserving tools handle the triangles.

## The Customisation Gap
Title needs its own logic layered on top. Transactions must be counted by rate bracket and policy type, with simultaneous-issue and reissue rules applied per state manual. Agent-level income and expense data has to be collected and audited, since agent retention is part of the rate base in Texas. Losses must be developed by policy year over a tail where 65–75% of claim amounts are known by year six (First American). Escrow fees have to be separated from premium. And each figure must trace from the hearing exhibit back to the agent's record, because opposing actuaries will challenge any number that cannot be traced. The generic tools assume a carrier that holds its own policy and claim data. A title underwriter holds the claims, but most of the premium detail sits with its agents.

## Impact If Solved
A traceable statistical pipeline turns each rate cycle from a scramble to rebuild agent data into a refresh. It also gives the underwriter and its association a defensible record at a hearing where a few points of indicated rate change are worth tens of millions of dollars a year in Texas alone (estimate).
