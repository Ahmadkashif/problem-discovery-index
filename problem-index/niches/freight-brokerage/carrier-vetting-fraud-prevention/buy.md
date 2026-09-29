# Identity Resolution Adapted to Deliberate Reconstitution

**Niche:** [[niches/freight-brokerage/carrier-vetting-fraud-prevention/profile|Carrier Vetting & Freight Fraud Prevention]]
**Industry:** [[industries/freight-brokerage|Freight Brokerage]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Identity verification products confirm that a business exists and is registered; a fraudulent carrier is a real registration, legitimately obtained or stolen, operated by someone else entirely.
**Tags:** #graph-neural-networks #graph-theory #contrastive-learning #bert #random-forests #evaluation-metrics #confidence-intervals #feature-engineering #compliance #automation

## The Problem
The registration is real. Fraud in this market works by taking over a dormant motor carrier's authority, cloning an active carrier's identity down to the insurance certificate, or standing up a legitimate new authority and operating it fraudulently after building a short clean history. Every one of those passes a check that verifies the entity exists, holds authority, and carries insurance. What distinguishes them is behavioural and relational — a contact method that does not match the registered one, an operating pattern inconsistent with the equipment on file, a sudden change in the phone or email associated with a long-dormant authority, and connections to entities previously implicated.

## What Already Exists
Business identity verification is a mature market. KYB providers, the credit bureaus' commercial products, and document verification services all confirm registration, ownership, and standing, and freight-specific vendors pull the federal authority and insurance data automatically. For confirming that an entity exists, everything needed is available.

## The Customization Gap
All of it verifies existence, and the adversary's whole method is to operate behind an existing entity. The adaptation is verification of control rather than existence: does the party presenting this authority appear to be the party that operates it. That is answered from signals no general KYB product has — contact detail drift against the registered record, dispatch and communication patterns, equipment and insurance consistency, and the relational graph connecting the presenting party to entities with prior confirmed incidents. Detection has to work in the minutes before a load tenders, which rules out anything requiring manual review as the primary path. And confidence must be calibrated and explainable, because blocking a legitimate carrier costs a broker capacity in a tight market and the operations team will override an unexplained refusal.

## Target Customer
Heads of data science and product at vetting providers, and the broker operations leaders who tender loads in minutes and cannot manually investigate every carrier.

## Impact If Solved
Attacks the failure mode the existing verification stack is structurally blind to, which is where essentially all the loss now occurs. Control-based verification also degrades gracefully into a risk score rather than a binary block, which is what a broker needs when capacity is scarce.
