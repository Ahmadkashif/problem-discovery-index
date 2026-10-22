# One Political Ledger Across Every Represented Station

**Niche:** [[niches/media-rep-firms/political-ad-sales/profile|Political Advertising Sales]]
**Industry:** [[industries/media-rep-firms|Media Representative Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A rep's political desk handles orders for hundreds of stations, each with its own traffic system and political file, and no single record shows what was ordered, quoted, cleared, preempted and disclosed across them.
**Tags:** #large-language-models #time-series-forecasting #compliance #workflow-orchestration #data-integration #revenue-impact
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every competitor is fighting to capture national political dollars for its stations in the final weeks before an election. But candidate orders are a compliance contest, won by quoting each station's lowest unit charge correctly and moving disclosure paperwork in hours. Issue and PAC orders are a pricing contest over scarce inventory, won by forecasting demand. The two have different inputs, clocks and winners. Decomposed into contested sub-niches below.

## The Problem
In October of an election year a political buyer may place, revise and cancel orders for dozens of stations a day through the rep. Each order touches a station's traffic system, the station's political file and the rep's commission ledger. Each one is either a candidate order under the lowest-unit-charge regime or an issue order at market rates. When a candidate's campaign later asks whether it got the lowest unit charge, or a station's counsel asks what the rep quoted, the answer is reconstructed from email.

## Why Nobody Has Built This
Political volume is biennial and concentrated in a few weeks, so vendors build political modules inside station traffic systems rather than across them. Rep firms work around the gap with extra temporary staff.

## What to Build
A rep-level political ledger that ingests every order, revision, quote and disclosure packet across represented stations. It tags each as candidate or non-candidate, links it to the race and window dates, and tracks clearance, preemption and political-file status per station. It feeds the two sub-niche products below: LUC quoting for candidate orders and demand-based pricing for issue orders.

## Target Customer
Heads of political sales at rep firms and station group political directors.

## Impact If Built
One record replaces the email reconstruction, makes every quote defensible, and lets the desk see the whole cycle's pacing in one place.
