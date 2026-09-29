# The Fraud Nobody Reports Because Everybody Competes

**Niche:** [[niches/freight-tech-platforms/carrier-identity-vetting/profile|Carrier Identity & Vetting]]
**Industry:** [[industries/freight-tech-platforms|Freight Tech Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A brokerage defrauded by a carrier keeps it to itself, so the same entity works its way through the industry one victim at a time, and the only party who could see the pattern is the one nobody tells.
**Tags:** #descriptive-statistics #graph-theory #evaluation-metrics #confidence-intervals #hypothesis-testing #compliance #workflow-orchestration #quick-win
**Contested on:** Every serious competitor in carrier vetting is fighting to establish who is actually going to haul a load before it moves — and whoever detects the fraudulent and re-brokering carriers earliest takes the account.

## The Problem
A brokerage loses a load to a double brokering scheme. It writes off the loss, updates its internal do-not-use list, and moves on. It does not tell its competitors, because they are competitors, because reporting takes time nobody has, and because publicly calling an entity fraudulent invites a lawsuit the brokerage does not want. The entity moves to the next brokerage, which has no way of knowing, and repeats. The industry collectively holds a complete picture of the fraud and individually holds a fragment, and the fragments never meet.

## Why It's Still Broken
The defamation exposure is the real obstacle and it is not imaginary: a broker that reports a carrier as fraudulent and is wrong has made a factual assertion about a business with a legal remedy. There is no safe harbour, no standard reporting format, and no neutral party with the standing to receive reports. Industry associations collect some information informally. Insurers hold claim data and treat it as proprietary. And the incentive is weak for the individual reporter, who bears the effort and the risk while the benefit accrues to competitors.

## What a Fix Looks Like
Build the reporting mechanism that makes contribution safe and cheap. Reports are factual and specific — this authority accepted this load on this date and it was delivered by a different carrier, or the remittance details changed mid-transaction — rather than characterisations, which is what removes most of the defamation exposure and also what makes the data useful. Contribution is structured, takes two minutes from the brokerage's own system, and is corroboration-weighted: a single unverified report is a signal, three independent ones describing the same pattern is evidence. The receiving party should be a neutral consortium or an insurer-backed body with the standing and the liability structure to hold it, not a single vendor whose competitors will not contribute. Publish aggregate statistics, because the industry currently does not know the size of its own problem — the loss figures in circulation are estimates built on estimates, and a real denominator would change how seriously this is funded.

## Who Feels the Pain
Brokerages absorbing losses one at a time from entities their competitors already know about; carriers whose identities are stolen and who spend months proving they did not haul a load; and shippers whose freight is gone.

## Impact If Fixed
A shared, factual, corroboration-weighted reporting mechanism is what makes the relational detection in the build note possible — the graph needs labels and the labels are in brokers' write-off files. The reporting standard and the liability structure are the hard parts, and they are institutional rather than technical, which is why this has not happened despite everyone wanting it.
