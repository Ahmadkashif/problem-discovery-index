# An Agent Risk File That Learns From Investigators

**Niche:** [[niches/money-service-businesses/agent-network-remittance/profile|Agent-Network Retail Remittance]]
**Industry:** [[industries/money-service-businesses|Money Service Businesses]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Senior investigators know which agent patterns mean trouble, and no system records their reasoning or grades it against what later happened to the agent.
**Tags:** #tacit-knowledge-ml #gradient-boosting #survival-analysis #graph-neural-networks #large-language-models #evaluation-metrics #compliance
**Contested on:** Every serious competitor in this niche is fighting to tell a complicit or careless agent from a merely busy one before a regulator, prosecutor or sponsor bank does, and whoever tells them apart earliest takes the account.

## The Problem
An agent's risk is spread across five systems: monitoring alerts, a case tool, field-visit forms, complaint logs and treasury's record of returned sweeps. A senior investigator pulls them together for the few agents that reach the top of a queue and reaches a judgement — corridor mix wrong for the neighbourhood, round-amount runs to one city, an owner too curious about thresholds. That judgement is written, if at all, as a closing memo. When the agent is convicted or terminated years later, nobody links the outcome back to the signals that were visible at the time.

## Why Nobody Has Built This
Monitoring vendors sell alert engines tuned to transactions, not to agents. Confirmed outcomes are rare, late and confidential under the BSA, so no vendor can pool them across transmitters. And agent networks are owned by sales teams who resist scores that flag high-volume locations.

## What to Build
A longitudinal agent file joining transaction features, visit findings, complaints, sweep returns, ownership changes and every investigator action, with closing reasons drafted from the case record and confirmed in one click. On top, a time-to-adverse-outcome model trained on investigator escalations (early label) and confirmed outcomes (late label), graph features over shared senders and receivers across stores, and every flag explained by the features and comparable past cases behind it.

## Target Customer
Chief compliance officers and heads of agent oversight at transmitters with more than a few thousand agents.

## Impact If Built
Field visits and investigator hours go where risk is, captured agents are caught months rather than years earlier, and every suspension rests on a documented, consistent basis an examiner or monitor can follow.
