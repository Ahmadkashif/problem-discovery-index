# The Employer Payroll Report Nobody Checks Until Retirement

**Industry:** [[pension-funds|Pension Funds]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Hundreds of participating employers report every member's pay, hours and service each pay period, and errors in what counts as pensionable pay are found decades later, when the member retires and the benefit has to be cut or the employer billed.
**Tags:** #gradient-boosting #change-point-detection #feature-engineering #evaluation-metrics #compliance #data-integration #automation

## The Problem
A statewide public retirement system collects contributions and member data from hundreds to a few thousand employers: school districts, cities, counties, special districts and state agencies (estimate). Each pay period every employer submits a file listing each member's earnings, the pay codes behind them, hours or days worked, contribution amounts and membership tier. The system's employer reporting staff fix rejected records and chase late files. Whether each pay item is *pensionable* is a rules question: base pay, overtime, special assignment pay, uniform allowances, leave cash-outs, one-time bonuses. The answer depends on the statute, the member's tier and sometimes the bargaining agreement behind the pay item.

Most of it is accepted as reported. The errors surface at the final benefit calculation, at a compensation review when a member retires, or in an employer audit years later. California made the cost visible: before 2022 a CalPERS retiree whose pension included "disallowed compensation" repaid the overpayment and took a reduced allowance. Government Code 20164.5 now shifts most of that cost to the employer that reported it.

## What Already Exists
Pension administration systems from Sagitec, Vitech (Majesco), LRS and others include employer reporting portals with file-format and field validation. Employer payroll systems (Workday, Tyler Munis and the like) produce the files. Systems run employer compliance audits with their own audit staff, and generic data-quality tools catch missing fields and duplicates.

## The Customisation Gap
Format validation is not pensionability validation. What is missing is the plan's own rules: which pay codes are pensionable for which tier and bargaining unit, PEPRA-style anti-spiking caps, final-average-salary windows, and limits on overtime or leave cash-outs. That logic has to run against each employer's own pay-code vocabulary. It also needs history. A member whose pay jumps 25% in the final-average window, or an employer that adds a new pay code mid-year, is the signal, and a single file does not show it. Each system's rules are statutory and particular, which is why generic data-quality tools miss them.

## Impact If Solved
Catching a non-pensionable pay item in the pay period it is reported costs a phone call to a payroll clerk. Catching it at retirement costs a benefit recalculation, a repayment demand, sometimes an appeal, and a member who planned their retirement on the wrong number. Employer reporting staff stop spending the year fixing file formats and start reviewing the pay that matters.
