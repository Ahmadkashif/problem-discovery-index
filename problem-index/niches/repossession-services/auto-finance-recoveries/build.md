# Recovery Rate Adjusted for File Difficulty

**Niche:** [[niches/repossession-services/auto-finance-recoveries/profile|Auto Finance Recoveries]]
**Industry:** [[industries/repossession-services|Repossession Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Forwarders and lenders rank agencies by raw recovery rate, which rewards the agency handed easy files and punishes the one working skips, and nobody adjusts for what each agency was given.
**Tags:** #logistic-regression #gradient-boosting #causal-inference #evaluation-metrics #data-integration #revenue-impact
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor is fighting to close more of a lender's auto assignments inside its window without a wrongful-repossession event — but a file with a good address is won at the curb on the first attempt, while a skip is won before the truck moves by finding the car, and the two contests have different inputs, pay and rivals. Decomposed into contested sub-niches below.

## The Problem
A forwarder with ~1M assignments a year spread across hundreds of agencies decides who gets the next file largely on recovery rate, time to recovery and compliance record. But files differ enormously: a three-week-delinquent sedan at a confirmed home address and a fourteen-month skip with no working address are not the same job. An agency in a dense metro with good addresses looks excellent; an agency covering a rural territory or taking a client's older files looks weak. Allocation follows the raw number, so hard territories are under-served and agencies stop accepting the files that drag their score.

## Why Nobody Has Built This
Forwarders have the cross-agency data but are paid to allocate, not to explain; agencies see only their own files and have no baseline; and difficulty adjustment requires features — address freshness, skip status, days delinquent, vehicle type — that sit in assignment records the agency cannot share freely.

## What to Build
A difficulty-adjusted recovery score: a model of each file's expected recovery probability at assignment from its features, and each agency's performance as observed minus expected, with confidence intervals that reflect small volumes. Sold to agencies as evidence in allocation and fee conversations, and to forwarders as a fairer panel score. An agency-owned version trains on members' own outcomes; a forwarder version on the panel.

## Target Customer
Owners of mid-sized and multi-state agencies negotiating allocation; vendor managers at forwarders and lenders who want to keep coverage in hard territories.

## Impact If Built
Allocation that rewards skill rather than territory keeps capable agencies working hard files, and recovery rates on the hardest decile of assignments are where lenders lose the most collateral value.
