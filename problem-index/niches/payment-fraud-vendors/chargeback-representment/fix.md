# The Evidence in Six Systems

**Niche:** [[niches/payment-fraud-vendors/chargeback-representment/profile|Chargeback Representment]]
**Industry:** [[industries/payment-fraud-vendors|Payment Fraud Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** Winning the dispute requires five documents from five systems and the specialist has four days to find them.
**Tags:** #data-integration #quick-win #workflow-orchestration #automation #worker-facing #evaluation-metrics #descriptive-statistics #large-language-models
**Contested on:** Every serious competitor in this niche is fighting to assemble the evidence a network's reason code demands, inside its deadline, only for the cases that can actually be won — and whoever predicts winnability stops spending effort on disputes that were lost before they started.

## The Problem
The reason code requires proof of delivery, proof of authentication, the terms the customer accepted, the communication history and the transaction detail. Delivery is in the shipping platform, authentication in the payment gateway, terms in the commerce platform, communications in the support tool, and transaction detail in the processor. The specialist logs into each, exports, assembles, formats and submits. Most of the case's elapsed time is retrieval, and cases are lost to the deadline rather than to the merits.

## Why It's Still Broken
Each system was integrated for its own purpose, so nobody assembled a dispute-shaped view across them — the evidence set spans a boundary no single integration was scoped to cross. The required items vary by reason code and are known informally. Specialists are measured on cases closed. And nobody times the retrieval step.

## What a Fix Looks Like
Assemble the packet automatically. Pull the standard evidence set for each reason code from the connected systems, which is the fix and removes the largest time cost in the process. Encode the required items per reason code, since they are published and are currently remembered rather than recorded. Start assembly when the chargeback arrives rather than when the specialist opens the case, so the packet is ready before anyone looks. Flag missing evidence immediately, as a case that cannot be won for lack of a document should be identified on day one rather than day four. Report time to assemble and cases lost to deadline, which will show how much is lost for reasons unrelated to merit. Preserve the evidence at transaction time where it is perishable, because some records are gone by the time a dispute arrives. Standardise the submission format per network, since formatting errors cause avoidable losses. Keep the packet with the case for appeals and for the model. Alert on approaching deadlines by expected value, so the valuable cases are not the ones that lapse. And track win rate by whether evidence was complete, which will quantify exactly what retrieval failure costs.

## Who Feels the Pain
Specialists logging into six systems per case; merchants losing winnable disputes to deadlines; and dispute teams whose recovery rate reflects retrieval capacity rather than case merit.

## Impact If Fixed
The evidence set spans a boundary no single integration was scoped to cross, so nobody ever assembled a dispute-shaped view. Automatic assembly on arrival removes the largest time cost and stops winnable cases lapsing.
