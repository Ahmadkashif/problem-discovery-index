# Sweep Cash Forecasting for the Agent's Own Account

**Niche:** [[niches/money-service-businesses/multi-brand-agent-location/profile|The Multi-Brand Agent Location]]
**Industry:** [[industries/money-service-businesses|Money Service Businesses]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A store selling three brands has three transmitters sweeping its bank account on different schedules, and finds out it was short when a sweep is returned and an agent contract is suspended.
**Tags:** #time-series-forecasting #exponential-smoothing #data-integration #worker-facing #automation #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to keep the agent's single bank account solvent across every brand's ACH sweep, so the store never has a returned debit, and whoever makes its sweeps most predictable for the agent takes the account.

## The Problem
Agents collect senders' cash and owe it to the transmitter, which debits the agent's bank account by ACH on its own schedule (estimate: daily to twice weekly). The store mixes this cash with its grocery takings, pays suppliers from the same account, and deposits when it can. A weekend surge before a holiday in Mexico or Guatemala, followed by a Monday supplier payment, produces a returned sweep. Transmitters treat returns as a credit and compliance event.

## Why Nobody Has Built This
Each transmitter sees only its own sweeps, and none builds tools for the agent's whole cash position. Agents are too small to buy treasury software.

## What to Build
A simple agent-side forecast combining each brand's transaction volume (from terminal reports or receipts), each sweep schedule, the store's bank balance and its regular payments, warning the owner when a deposit is needed before a sweep. A transmitter could offer it as an agent benefit, or a bank serving agents could.

## Target Customer
Heads of agent network at transmitters competing for multi-brand counters, and banks with many agent-store customers.

## Impact If Built
Fewer returned sweeps and suspensions, fewer agents lost to cash-flow mistakes, and a reason for the store to favour the brand that offers it.
