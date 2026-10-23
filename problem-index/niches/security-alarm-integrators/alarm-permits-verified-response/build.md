# A Dispatch-Eligibility Ledger for Every Account

**Niche:** [[niches/security-alarm-integrators/alarm-permits-verified-response/profile|Alarm Permits, False-Alarm Fines & Verified-Response Compliance]]
**Industry:** [[industries/security-alarm-integrators|Security Alarm Integrators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Nobody can tell a dealer which of its accounts police will still answer, because the rules live in thousands of ordinances and the counts live with the cities.
**Tags:** #large-language-models #transformers #feature-engineering #logistic-regression #compliance #revenue-impact #data-integration
**Contested on:** Every serious competitor in this niche is fighting to keep each customer's alarm eligible for police response under its own city's ordinance (permitted, under the false-alarm limit and verified to the local standard), and whoever keeps the most accounts dispatchable with the fewest fines takes the account.

## The Problem
Each account sits in a jurisdiction with its own permit requirement, false-alarm allowance, fine schedule, suspension threshold and verification rule. The station knows how many dispatches it requested. The city or its billing vendor knows how many it counted as false and what it billed. The dealer knows neither until a customer calls angry about a fine or a burglary goes unanswered.

## Why Nobody Has Built This
Ordinances are local legal text in inconsistent formats, they change, and they are enforced by different vendors with different portals. Dealers individually cover too few cities to justify a registry, and stations treat the rules as account notes.

## What to Build
An ordinance registry, with LLM extraction of rules from municipal codes and a human review queue, joined to each account's address and dispatch history. It computes each account's eligibility state: permitted, allowance remaining, next fine, suspension risk and the verification needed. A predictive layer flags accounts likely to cross a threshold from their recent alarm pattern, which triggers service before the fine rather than after.

## Target Customer
Compliance and monitoring-operations leaders at dealers and stations with accounts across hundreds of jurisdictions.

## Impact If Built
Accounts stay dispatchable, avoidable fines become service visits, and one of the main triggers of cancellation is handled before the customer knows about it.
