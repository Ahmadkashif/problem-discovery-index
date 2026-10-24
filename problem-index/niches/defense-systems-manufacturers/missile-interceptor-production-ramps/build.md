# A Rate Model for Every Missile Line

**Niche:** [[niches/defense-systems-manufacturers/missile-interceptor-production-ramps/profile|Missile & Interceptor Production Ramps]]
**Industry:** [[industries/defense-systems-manufacturers|Defense Systems Manufacturers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No missile programme has one model that says how many rounds it can deliver each month and which part, process or test stand will stop it.
**Tags:** #graph-neural-networks #survival-analysis #monte-carlo-methods #gradient-boosting #data-integration #revenue-impact
**Contested on:** *Not terminal as stated.* The honest partial sentence is: every serious competitor in this niche is fighting to raise delivered rounds per month on a qualified missile line, but the shortage that caps the rate sits in two places with different winners — sub-tier motors and their energetic ingredients, where whoever delivers qualified motors at rate wins, and the prime's own final assembly and acceptance test, where whoever raises first-pass yield wins. Decomposed into contested sub-niches below.

## The Problem
A missile programme's delivery rate is the minimum of many rates: motor deliveries, seeker and guidance electronics, warhead and fuze, airframe sections, final assembly labour, test station hours and first-pass acceptance yield. Each is tracked by a different team in a different tool. When a customer asks whether the line can go from 550 to 2,000 interceptors a year (the PAC-3 MSE question CNAS raises), the answer is assembled by hand in slide decks, and the binding constraint is often discovered when it binds.

## Why Nobody Has Built This
The data are split across ERP, MES, supplier portals and test databases, all CUI or classified, so cloud planning vendors can't see them. Supply planning suites model materials but not acceptance-test yield or requalification lead times, and primes have treated rate planning as an internal engineering exercise rather than a software purchase.

## What to Build
An on-premises rate model per line: a graph of every part, process step and test with its demonstrated rate, lead time, yield and qualification status, fed from the order book, MES and test data. Monte Carlo simulation produces a deliverable-rounds forecast with its distribution, and a learned shortage model flags which nodes will bind in the next one to three quarters, ranked by rounds lost. Scenario views show what a second motor source or an extra test station buys.

## Target Customer
Programme directors and production VPs on multi-year missile and interceptor programmes at the primes, and the government programme offices that fund capacity.

## Impact If Built
A programme that sees its binding constraint a quarter earlier can fund the fix in time. On a line delivering hundreds of rounds a year at a million dollars or more each (estimate), recovering a month of rate is worth tens of millions of dollars in revenue pulled forward.
