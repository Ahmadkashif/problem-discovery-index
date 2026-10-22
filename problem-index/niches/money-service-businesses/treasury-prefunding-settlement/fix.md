# Agent Sweep Returns Found Two Days Late

**Niche:** [[niches/money-service-businesses/treasury-prefunding-settlement/profile|Treasury, Prefunding & Settlement Reconciliation]]
**Industry:** [[industries/money-service-businesses|Money Service Businesses]]
**Type:** Fix (Pain Point)
**One-liner:** An agent's ACH sweep bounces, the return file is matched a day or two later, and the agent keeps selling transfers on money the transmitter does not have.
**Tags:** #gradient-boosting #feature-engineering #data-integration #automation #quick-win #compliance
**Contested on:** Every serious competitor in this niche is fighting to prefund each payout partner and currency just enough each morning — no failed payouts, no cash idle abroad — and whoever forecasts payout demand by partner-day most accurately takes the account.

## The Problem
Returns arrive in bank files with codes that must be matched to the agent and the sweep. Matching is partly manual, the agent's terminal stays live until someone acts, and repeated returns are a credit loss and an agent-oversight signal.

## Why It's Still Broken
Settlement sits with treasury, agent limits with the agent network team and risk ratings with compliance; returns fall between them.

## What a Fix Looks Like
Automatic matching of returns on arrival, immediate limit reduction or terminal hold by rule, a short-horizon score of which agents are likely to return the next sweep based on volume surges and past behaviour, and every return written to the agent's risk file.

## Who Feels the Pain
Treasury staff matching files, agent managers chasing owners, and compliance teams learning late that a risky agent was also not paying.

## Impact If Fixed
Exposure to a failing agent is cut to hours, and payment behaviour joins the agent risk record where it belongs.
