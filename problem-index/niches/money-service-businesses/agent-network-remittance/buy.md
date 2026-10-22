# Merchant Risk Monitoring Pointed at Agent Counters

**Niche:** [[niches/money-service-businesses/agent-network-remittance/profile|Agent-Network Retail Remittance]]
**Industry:** [[industries/money-service-businesses|Money Service Businesses]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Card acquirers already monitor millions of merchants for laundering and fraud; an agent counter is a merchant that moves cash across borders, and the acquirer models do not know that.
**Tags:** #gradient-boosting #feature-engineering #evaluation-metrics #compliance #data-integration #automation
**Contested on:** Every serious competitor in this niche is fighting to tell a complicit or careless agent from a merely busy one before a regulator, prosecutor or sponsor bank does, and whoever tells them apart earliest takes the account.

## The Problem
Agent oversight teams build their own agent risk ratings in spreadsheets from volume and alert counts. These ratings drive visit schedules and enhanced-due-diligence reviews, and they reward quiet agents whether or not quiet means clean.

## What Already Exists
Payment processors and acquirers run merchant monitoring: transaction-laundering detection, web content checks, chargeback and fraud ratios, and ownership screening, sold by specialist vendors and built in-house (see [[industries/payment-processors|Payment Processors]]).

## The Customization Gap
The adaptation needs agent-specific signals: corridor mix against the store's neighbourhood and clientele; threshold-adjacent amounts and splits across a sender's visits; one receiver collecting from many senders at one store; refund and cancellation patterns; consumer-fraud reports per thousand sends; returned ACH sweeps; clerk turnover and training completion; and the agent's other brands where known. It also needs BSA vocabulary — outputs framed as enhanced due diligence, suspension and SAR referral, not chargeback thresholds.

## Target Customer
Agent oversight leads at mid-sized transmitters who cannot fund an in-house data science team.

## Impact If Solved
A defensible, data-driven agent risk rating replaces a spreadsheet heuristic, sending field auditors to the stores most likely to be in trouble rather than the ones with the most alerts.
