# Payer Behaviour Change Detection from the Remittance Stream

**Niche:** [[niches/healthcare-practice-software/payer-rule-content-vendors/profile|Payer Rule & Claim Edit Content]]
**Industry:** [[industries/healthcare-practice-software|Healthcare Practice Software]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A clearinghouse sees every remittance for every customer in near real time and learns that a payer changed its adjudication rules the same way everyone else does — when a customer calls to complain weeks later.
**Tags:** #change-point-detection #hypothesis-testing #time-series-forecasting #confidence-intervals #evaluation-metrics #descriptive-statistics #automation #revenue-impact
**Contested on:** Every serious competitor in claim edit content is fighting to detect a payer's undocumented adjudication change from the remittance stream within days of the first affected claim — and whoever detects it fastest and most precisely takes the account.

## The Problem
On a Monday a regional plan starts requiring a modifier it never required before, or tightens a frequency limit, or begins bundling two codes that previously paid separately. No bulletin is issued, or one is issued in a format nobody monitors. Denials begin. Individually each looks like an ordinary coding error, and practices treat them as such — appeal, resubmit, absorb. Three to six weeks later, enough practices have complained that a pattern is recognised and a rule is written. In the interval, every practice in the network submits claims that will be denied, and the aggregate cost across a clearinghouse's book is enormous and entirely invisible because no one has ever computed it.

## Why Nobody Has Built This
The remittance stream is treated as a transaction log rather than as a measurement instrument. It is high-volume, messy, and partitioned into thousands of thin slices — a specific payer, plan, state, code and modifier combination may see only a handful of claims a week at any one customer, which is why individual practices genuinely cannot detect anything. Pooling across customers is what makes the signal visible, and pooling raises contractual questions that nobody has wanted to open. There is also a perverse commercial fact: denied claims generate resubmissions, appeals and support engagement, all of which are billable in parts of this market.

## What to Build
A monitor over the pooled remittance stream that runs change-point detection on denial rate per payer-plan-state-code-modifier cell, with the multiple-comparisons discipline the slicing demands — thousands of cells tested continuously will produce alarms from noise alone unless the false discovery rate is controlled deliberately. When a shift is confirmed, the system characterises it: what changed, from when, which claims are affected, and what correction resolved it in the cases already appealed successfully. Output is a rule delta proposed to the content team with the evidence and the affected volume attached, plus an immediate advisory to affected customers. The product discipline is precision over recall — a false advisory that tells thousands of practices to change their coding is far more damaging than a slow one, so the threshold should be conservative and the confidence stated.

## Target Customer
Clearinghouses and claim edit content vendors with pooled visibility, large billing companies, and the ambulatory EHR vendors that process claims at scale and currently buy content from someone doing this by newsletter.

## Impact If Built
Cutting detection latency from weeks to days removes the bulk of the denials a payer change causes, because the window is the whole cost. For a clearinghouse the capability is also the only genuinely defensible thing in an edit library, since rules can be copied and a live detection pipeline over a proprietary stream cannot. The affected-volume figure, computable retrospectively, is likely to be the number that funds the project.
