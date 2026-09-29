# A Fraudster or a Bad Month

**Niche:** [[niches/neobanks/ongoing-account-risk/profile|Ongoing Account Risk]]
**Industry:** [[industries/neobanks|Neobanks]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The competitive question in consumer fintech is which institution can tell the difference between a fraudster and a customer having a bad month, and the systems treat both as anomalies.
**Tags:** #change-point-detection #gradient-boosting #graph-theory #confidence-intervals #evaluation-metrics #compliance #survival-analysis #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to tell a fraudster from a customer having a bad month, using the institution's own ledger — and whoever does that stops freezing the wages of people who did nothing wrong.

## The Problem
A customer's account behaviour changes sharply. Unusual deposits, a new payee, transfers to an account they have never used, a balance moving in a way it never has. This is a fraud pattern. It is also what happens when someone starts a second job, receives an insurance settlement, helps a relative, sells a car, moves house or begins a small business. The monitoring system sees an anomaly, which is genuinely what it is, and treats anomaly as suspicion. The account is frozen. Some of those accounts are fraudulent, many are not, and the institution rarely learns which because a closed account produces no further evidence.

## Why Nobody Has Built This
Monitoring was built to detect deviation, and deviation is what it detects — the system answers the question it was designed for and the institution needs a different question answered. Money laundering obligations create an incentive to restrict first and investigate later, which is defensible individually and produces this pattern in aggregate. Freezing is cheap and reversing is expensive. And the false freeze generates a complaint that reaches support rather than risk, so the team that could fix it does not hear about it.

## What to Build
Model the life event as well as the fraud. Build models of the ordinary changes that produce anomalous patterns — new employment, a large one-off receipt, a house move, a new dependant, a small business starting — which is the core and is entirely learnable from the institution's own history of customers who did these things and were fine. Distinguish anomaly from suspicion explicitly in the system's own vocabulary, since conflating them is the design error underneath everything else here. Use the account's whole history rather than the recent window, because a customer with three years of consistent behaviour and one unusual fortnight is a different proposition from a new account behaving strangely, and the tenure is being discarded. Use the graph for genuine fraud signals — funding sources, shared devices, payee networks — which is where organised activity shows and individual anomaly does not. Grade the response rather than freezing, which is the fix note's subject and is the single largest improvement available to the customer experience. Establish outcome feedback, connecting to the measurement niche, since this is the decision type where the outcome is most observable and least recorded. Weight the cost of the error properly, because freezing a customer's wages has consequences the loss figure does not capture. Give the customer a route to resolve it quickly, since most false freezes could be cleared by the customer supplying one document and there is frequently no mechanism. Distinguish the compliance-mandated restrictions from the discretionary ones, so the discretionary ones can be improved. And measure the false freeze rate, which is the number that would change how this whole system is configured.

## Target Customer
Risk operations leadership at digital banks, sponsor banks accountable for programme outcomes, and the customers whose wages are frozen by an anomaly.

## Impact If Built
The monitoring answers the question it was designed for — deviation — and the institution needs a different one answered. Modelling the ordinary life events that produce anomalous patterns is learnable from the institution's own history and is what separates a fraudster from a bad month.
