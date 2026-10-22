# Reliability-Ranked Assignment

**Niche:** [[niches/notary-signing-services/signing-order-dispatch/profile|Signing Order Dispatch]]
**Industry:** [[industries/notary-signing-services|Notary & Signing Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Coordinators assign the first agent who answers, when their own history could say which agent is least likely to no-show or cause a redraw on this order.
**Tags:** #gradient-boosting #survival-analysis #logistic-regression #evaluation-metrics #workflow-orchestration #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to fill each signing order, within minutes of receipt, with the agent most likely to arrive on time and finish clean, and whoever predicts agent reliability best takes the title company's overflow orders.

## The Problem
A no-show or a redraw costs the service its title client's trust. Reliability varies by agent and by situation: some agents are excellent on weekday refinances and poor on late-evening purchases with three signers; some accept everything and cancel the night before.

## Why Nobody Has Built This
Services are small, their history is spread across tools, and outcomes are logged as notes rather than coded fields. Marketplaces rank agents across all clients, not on a service's own outcomes.

## What to Build
Per agent-order predictions of clean completion, on-time arrival and cancellation from coded history (loan type, signer count, appointment time, distance, document arrival, past outcomes), plus a time-to-acceptance model for fee offers. The assignment step balances reliability, fee and giving new agents enough orders to build history, and explains each recommendation to the coordinator.

## Target Customer
Signing-service owners with a few thousand orders a month or more; title companies with in-house panels.

## Impact If Built
Fewer no-shows and redraws per hundred orders, and coordinators freed from guesswork at peak volume.
