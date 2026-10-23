# One Ledger for Cash and Uptime per Machine

**Niche:** [[niches/armored-car-services/atm-managed-services/profile|ATM Managed Services]]
**Industry:** [[industries/armored-car-services|Armored Car Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An ATM owner gets a cash report from one system and an uptime report from another, and cannot see that half its cash-outs were really faults and half its faults followed bad loads.
**Tags:** #time-series-forecasting #gradient-boosting #causal-inference #data-integration #workflow-orchestration #revenue-impact
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor is fighting to keep each ATM in a bank's or deployer's fleet available to withdraw from, but writing it produces two contests with different winners: holding the least cash in machines at the contracted cash-out rate, which forecasting vendors, carriers' forecasting desks and banks' cash teams compete on; and restoring faulted machines fastest without sending technicians into staged jams, which carriers' service arms, ATM makers' service businesses and independent service organisations compete on. Decomposed into contested sub-niches below.

## The Problem
A machine that is "down" may be empty, jammed, offline or vandalised. Managed-service contracts measure availability and cash-out rates separately, and different teams own them. Disputes about service credits turn on which cause applied.

## Why Nobody Has Built This
Forecasting and field service grew up as separate products and separate departments. ATM owners buy pieces from different vendors. The data to join them — device journals, cassette counts, visit records, forecasts — sits in at least three systems.

## What to Build
A per-machine ledger joining every hour of every ATM's state: cash by cassette, forecast versus actual, faults and their codes, visits by type and outcome. Downtime is attributed to cause (cash-out, device fault, communication, vandalism, host-site closure) and to the decision that could have prevented it (load size, visit timing, parts, remote reset). Owners see true availability and its drivers; carriers see which decisions to change.

## Target Customer
Heads of self-service channels at banks and of operations at independent deployers; AMS product leaders at carriers.

## Impact If Built
Separating cash causes from technical causes ends the service-credit arguments and shows owners where an extra point of availability is cheapest to buy.
