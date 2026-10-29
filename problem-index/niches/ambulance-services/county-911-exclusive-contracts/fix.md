# Response-Time Exemptions Argued From Memory Every Month

**Niche:** [[niches/ambulance-services/county-911-exclusive-contracts/profile|County 911 Contracts & Exclusive Operating Areas]]
**Industry:** [[industries/ambulance-services|Ambulance Services]]
**Type:** Fix (Pain Point)
**One-liner:** Late calls the contract would excuse, such as a freeway closure, a wrong address or a hospital diversion, are penalised anyway because nobody recorded the reason when it happened.
**Tags:** #large-language-models #bert #compliance #workflow-orchestration #quick-win
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor here is fighting to hold a county's or city's 911 ambulance contract. But the contract is won at bid, by pricing years of call volume, payer mix and collections into a subsidy or franchise fee, and kept month by month, by deploying units against the response-time standard. The two contests have different people, clocks and winners. Decomposed into contested sub-niches below.

## The Problem
Most 911 contracts allow exemption requests for late responses caused by conditions outside the operator's control. At month end the compliance analyst lists the late calls and asks dispatchers and crews what happened. She finds notes in CAD free text when she is lucky, then writes exemption requests the county reviews. Many legitimate exemptions are never claimed.

## Why It's Still Broken
The reason a call was late is known at the time, to the dispatcher and the crew, and is recorded inconsistently in CAD comments and radio logs. Nobody's job is to code it then.

## What a Fix Looks Like
At the moment a response crosses the standard, prompt the dispatcher for a reason code, with free-text CAD comments, traffic and weather feeds and the crew's ePCR delay field pre-classified into the contract's exemption categories. At month end the exemption package assembles itself with the evidence attached.

## Who Feels the Pain
Compliance analysts and dispatch supervisors at operators; county EMS agencies reviewing poorly documented requests; and crews blamed for delays they did not cause.

## Impact If Fixed
If 10% of a contract's late calls carry a valid but unclaimed exemption (an estimate), and penalties run ~$300 per call (an estimate), a contract with 200 late calls a month recovers ~$6,000 a month, ~$72,000 a year.
