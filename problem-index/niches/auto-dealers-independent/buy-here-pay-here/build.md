# Predictive Collections and Delinquency Early Warning

**Niche:** [[niches/auto-dealers-independent/buy-here-pay-here/profile|Buy Here Pay Here (BHPH) Dealers]]
**Industry:** [[industries/auto-dealers-independent|Independent Auto Dealers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool predicts which BHPH accounts will become delinquent next week and prioritizes collector outreach by recovery probability, leaving dealers to react to missed payments instead of preventing them.
**Tags:** #gradient-boosting #binary-classification #tabular-ml #revenue-impact #tacit-knowledge-ml

## The Problem
A BHPH dealer with 500 active accounts has a collections staff of 2-3 people making 50-100 outbound calls per day. They call delinquent accounts in order of days past due — but an experienced collector knows that some accounts show behavioral warning signs before they miss a payment: a customer who always pays on Friday but suddenly paid on Monday, a GPS device showing the car parked at an unfamiliar address, or a customer who stopped answering the phone mid-week. This tacit pattern recognition built from managing thousands of accounts is exactly the expertise that leaves when a collector quits.

## Why Nobody Has Built This
BHPH dealers are small (average 150-300 active accounts), so the per-dealer data volume is low. Building predictive models requires pooling data across dealers — but BHPH operators are private, competitive, and reluctant to share portfolio data. The behavioral signals that matter (payment timing patterns, GPS location anomalies, call responsiveness) live across 3-4 disconnected systems (DMS, GPS platform, phone system) with no integration layer.

## What to Build
A delinquency prediction engine that ingests payment history from the DMS (timing, amount, method), GPS telemetry (driving patterns, location changes), communication logs (call answer rates, voicemail vs. live answer), and account metadata (original deal structure, down payment percentage, income verification score). Produces a weekly risk score per account and a prioritized call list for collectors — calling high-risk accounts 3-5 days before expected delinquency, when intervention (payment plan adjustment, partial payment arrangement) is most effective.

## Target Customer
BHPH dealer principals with 200+ active accounts and 15%+ monthly delinquency rates who want to shift from reactive collections to proactive risk management.

## Impact If Built
Reducing delinquency rate from 20% to 14% on a 500-account portfolio at $250 average monthly payment recovers $9K/month in collections. Reducing repossession rate from 25% to 18% annually saves $35K-50K in repo and remarketing costs. Captures the tacit expertise of experienced collectors into a transferable system.
