# Hedge Documentation Written at Audit Time

**Niche:** [[niches/commodity-brokers/mid-size-commercial-hedgers/profile|Mid-Size Commercial Hedgers]]
**Industry:** [[industries/commodity-brokers|Commodity Brokers]]
**Type:** Fix (Pain Point)
**One-liner:** Hedge designation memos that should exist when a hedge is placed are written months later, when the auditor asks for them.
**Tags:** #large-language-models #compliance #workflow-orchestration #quick-win #automation
**Contested on:** Every serious competitor in this niche is fighting to give a company too small for a bank's OTC desk a hedging programme (exposure measurement, futures execution and hedge-accounting documentation) that one finance person can run, and whoever gets a programme running on the least finance-staff time and through a clean audit takes the account.

## The Problem
Hedge accounting requires contemporaneous documentation of the hedged item, the instrument, the risk and how effectiveness will be assessed. Small companies place hedges by phone and document nothing until year end, when it is too late to qualify.

## Why It's Still Broken
Nobody in the placing workflow (company, broker, FCM) is responsible for the memo, and the auditor sees it only after the fact.

## What a Fix Looks Like
When an order from a designated commercial account is filled, the system drafts the designation memo from the fill, the company's exposure record and its hedge policy, and sends it to the controller to confirm the same day.

## Who Feels the Pain
Controllers, auditors, and FCM commercial brokers whose clients stop hedging after an earnings surprise.

## Impact If Fixed
More hedges qualify for hedge accounting at almost no cost, so a company's reported results reflect its economics.
