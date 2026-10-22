# A Net Distribution Margin Model by Station and Contract

**Niche:** [[niches/broadcast-stations/retransmission-and-affiliation/profile|Retransmission & Network Affiliation Economics]]
**Industry:** [[industries/broadcast-stations|Broadcast TV & Radio Stations]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A group knows its gross retrans revenue and its network payments, but not what it keeps per subscriber, station by station, over the coming cycle as subscribers fall and contracts reset on different dates.
**Tags:** #monte-carlo-methods #bayesian-inference #time-series-forecasting #feature-engineering #data-integration #revenue-impact
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor in this niche (distribution advisers, contract audit firms, and contract and royalty software vendors) is fighting to raise the station's net distribution revenue per subscriber after reverse compensation, but that splits into two contests with different winners: estimating what a blackout would cost each side in negotiations with each distributor, and testing distributors' self-reported subscriber counts after the agreement is signed. Decomposed into contested sub-niches below.

## The Problem
A station group negotiates dozens of distribution agreements and four or more network affiliation agreements on staggered calendars. Each affiliation agreement sets reverse compensation that may be per subscriber, a share of retrans, or a fixed fee (estimate). The group's net position, what it keeps after the network, moves with every renewal on either side and with subscriber decline.

## Why Nobody Has Built This
The terms are confidential, held by a few executives, and modelled in spreadsheets built for each negotiation. No vendor sees enough agreements to sell a model, and industry estimates are averages that do not match any one group's contracts.

## What to Build
A model per station of gross retrans, reverse comp and net margin for each year of the coming cycle. It projects subscribers per distributor with uncertainty, applies each contract's escalators and expiry, and simulates renewal outcomes on both the distribution and network sides. It shows which renewals matter most to net margin and what a given network demand does to each station's economics.

## Target Customer
Group EVPs of distribution and CFOs of multi-station TV groups.

## Impact If Built
The group negotiates each side knowing its effect on the other, and can show lenders and boards a defensible forecast of its second-largest revenue line.
