# Which Voices Move Which Offices

**Niche:** [[niches/public-relations-agencies/public-affairs-advocacy/profile|Public Affairs & Issue Advocacy]]
**Industry:** [[industries/public-relations-agencies|Public Relations Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Public affairs firms recruit validators and constituents for every campaign and never record which of them changed a legislator's position, so each campaign rebuilds the same guesswork.
**Tags:** #tacit-knowledge-ml #gradient-boosting #causal-inference #graph-theory #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to show legislators and agencies verifiable support from real constituents and credible third parties before a vote or comment deadline, and whoever produces support that survives scrutiny for astroturfing takes the account.

## The Problem
A senior public affairs consultant knows that one committee chair listens to rural hospital administrators, another to a particular union local, and a third only to donors and local press. That knowledge decides whom the firm recruits and where it spends a client's budget. Juniors and new clients get a generic plan: letters from everyone, op-eds anywhere.

## Why Nobody Has Built This
Outcomes are public (votes, co-sponsorships, rule changes) but the inputs (meetings, calls, validator contacts, local press placed) are scattered across consultants' notes, and attributing a vote to any one input is hard. Firms also treat their relationship maps as proprietary.

## What to Build
A campaign ledger recording every touch per legislative office (validator, constituent type, meeting, local coverage, timing) joined to each office's subsequent actions, plus a relationship graph of offices, validators and interest groups. Models estimate which touch types precede position changes for which kinds of office, controlling for party, district and prior position, and surface the senior consultant's past choices as evidence for the next plan.

## Target Customer
Public affairs practice leads at PR firms and specialist advocacy firms; corporate heads of government affairs who fund multiple campaigns.

## Impact If Built
Budgets aimed at the voices that move specific offices, and a firm memory that survives consultant turnover between sessions.
