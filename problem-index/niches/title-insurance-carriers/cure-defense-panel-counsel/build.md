# Panel Counsel Graded by Outcome per Dollar

**Niche:** [[niches/title-insurance-carriers/cure-defense-panel-counsel/profile|Cure, Defense & Panel Counsel Management]]
**Industry:** [[industries/title-insurance-carriers|Title Insurance Carriers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Underwriters send title claims to panel firms by relationship and geography, with no measure of which firms resolve which claim types by cure, how fast and at what total cost.
**Tags:** #causal-inference #survival-analysis #gradient-boosting #evaluation-metrics #feature-engineering #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to resolve covered title claims by cure, negotiation or defence for less than the policy loss, and whoever closes the most claims by cure at the lowest legal spend per claim takes the account.

## The Problem
A quiet-title action in one county, a forged-deed defence in another and an easement dispute in a third go to the panel firms counsel know. Some firms cure quickly. Others litigate to judgement and bill accordingly. The underwriter pays both without comparing them on like-for-like claims.

## Why Nobody Has Built This
Claim volumes per firm are small, claim difficulty varies, and invoices and outcomes sit in different systems. A naive comparison punishes the firms that get the hardest cases.

## What to Build
Join matters, invoices and outcomes by claim. Model time to resolution and total cost with survival and regression models that adjust for claim type, jurisdiction, defect and exposure. Estimate each firm's effect on cure rate and cost with intervals wide enough to be honest. Use the result to route new matters and set budgets.

## Target Customer
Chief claims counsel and litigation managers at underwriters with national panels.

## Impact If Built
More claims closed by cure at lower legal spend, and routing based on evidence instead of habit.
