# A Policy Engine That Learns From Exceptions

**Niche:** [[niches/travel-agencies/corporate-travel-management/profile|Corporate Travel Management]]
**Industry:** [[industries/travel-agencies|Travel Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Corporate travel policy is a set of static caps and rules, and the thousands of exceptions approved every month — the real policy — are never analysed.
**Tags:** #gradient-boosting #logistic-regression #causal-inference #evaluation-metrics #large-language-models #compliance #revenue-impact
**Contested on:** *Not terminal as stated.* The honest partial sentence is "every serious competitor in this niche is fighting to keep a company's travel inside its managed programme", but that splits into two contests with different winners: getting a growing company's employees to book in the tool without calling an agent, and accounting for every traveller within minutes of an incident. Decomposed into contested sub-niches below.

## The Problem
A travel policy says economy under six hours, a hotel cap per city, book 14 days ahead. The booking tool flags violations and routes them to a manager, who approves most of them with a reason code. Over a year a mid-size programme generates thousands of these approvals. Nobody looks at them together: which caps are routinely broken because they are wrong for the city, which reasons predict a trip that turned out to be necessary, which approvals simply mean the manager clicked yes.

## Why Nobody Has Built This
Booking tools are built to enforce rules at the moment of booking; reporting tools summarise spend after the fact. Neither treats the exception decision as data. Travel managers update policy annually from benchmarks and anecdotes, and TMCs earn their fees on transactions, not on better rules.

## What to Build
A policy analytics layer that ingests every booking, flag, approval and reason code, joins them to fares and hotel rates available at the time and to what the trip cost in the end, and estimates which rules save money and which only generate friction. It proposes city-level hotel caps from actual market rates, predicts which exceptions a manager will approve so routine ones can be pre-cleared, and simulates the cost of a policy change before it is made.

## Target Customer
Travel managers and procurement directors at companies spending ~$10-200M a year on travel (estimate), and TMCs that want an advisory product beyond transaction fees.

## Impact If Built
Fewer meaningless approvals for managers, faster booking for travellers, and a policy grounded in evidence; for a programme of ~$50M (estimate), correcting a handful of unrealistic caps and pre-clearing routine exceptions is worth several percent of hotel spend in avoided out-of-programme bookings.
