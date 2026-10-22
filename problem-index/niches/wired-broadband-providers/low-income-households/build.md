# Plan-Fit and Payment-Risk Model for Affordability Plans

**Niche:** [[niches/wired-broadband-providers/low-income-households/profile|Low-Income & Post-ACP Households]]
**Industry:** [[industries/wired-broadband-providers|Wired Broadband Providers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Operators decide plan, deposit and dunning for payment-constrained households with generic credit rules, when their own payment histories show which plans and arrangements households actually sustain.
**Tags:** #survival-analysis #gradient-boosting #causal-inference #evaluation-metrics #feature-engineering #revenue-impact
**Contested on:** Every serious competitor in this niche (billing and collections platforms, affordability-programme administrators and operators' own credit teams) is fighting to match each payment-constrained household to a plan and payment arrangement it can sustain without ending in non-pay disconnection, and whoever predicts that fit best takes the account.

## The Problem
A household moving off a subsidy is offered the standard plan or a low-income tier, then managed by the same dunning sequence as everyone else. Some would sustain a cheaper tier for years; some need a payment date aligned with benefit deposits; some need a short arrangement after a missed payment, not suspension.

## Why Nobody Has Built This
Collections systems optimise recovery on overdue balances, not long-run retention of low-margin customers, and fairness and regulatory concerns make operators wary of differentiated treatment.

## What to Build
A model of time-to-non-pay-disconnect by plan, payment date, autopay and arrangement type, learned from the operator's own history (with an experiment design to separate the effect of treatments from selection), that recommends the plan and arrangement maximising expected tenure and recovered revenue, with fairness checks across protected groups.

## Target Customer
Credit, collections and lifecycle teams at cable operators and telcos with large low-income plan bases.

## Impact If Built
Fewer non-pay disconnections and bad-debt write-offs, and households that stay connected.
