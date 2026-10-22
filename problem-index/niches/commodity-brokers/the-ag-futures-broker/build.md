# A Morning Book for the Broker, Not the FCM

**Niche:** [[niches/commodity-brokers/the-ag-futures-broker/profile|The Ag Futures Broker]]
**Industry:** [[industries/commodity-brokers|Commodity Brokers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An ag broker spends the first two hours of every day reassembling clients' positions that no system holds in one place.
**Tags:** #large-language-models #transformers #time-series-forecasting #feature-engineering #worker-facing #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to let one registered broker serve a few hundred farm accounts (positions, cash sales, insurance, margin) with a morning view and a compliant record of every recommendation, and whoever lets one broker serve the most farms without a missed call or an undocumented recommendation takes the account.

## The Problem
Before the open the broker needs to know which clients are in margin, which options expire, which hedges need rolling, which farms are over-hedged against what they planted, and what to tell everyone about the overnight move. The answers sit in the FCM portal, elevator contract confirmations, insurance summaries and the broker's notebook.

## Why Nobody Has Built This
Vendors sell to FCMs (back office) or to traders (front ends). Brokers are individually small buyers, and the data they need from elevators and insurance agents isn't the FCM's to share.

## What to Build
A broker workstation that pulls positions from the FCM. It reads client-forwarded elevator confirmations and insurance documents, ranks the day's calls with reasons, drafts the morning comment from the overnight move in the broker's own style, and after each recorded call drafts a recommendation note for the broker to confirm.

## Target Customer
Agricultural associated persons at introducing brokers and FCM farm desks, bought by IB principals or ag desk heads for their teams.

## Impact If Built
An hour or two a day returned to each broker (estimate), more farms served well per broker, and fewer missed calls in volatile weeks.
