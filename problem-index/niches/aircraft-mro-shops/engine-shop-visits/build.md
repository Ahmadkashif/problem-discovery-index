# An Induction Pack That Reads the Engine Before Teardown

**Niche:** [[niches/aircraft-mro-shops/engine-shop-visits/profile|Engine Shop Visits & Overhaul]]
**Industry:** [[industries/aircraft-mro-shops|Aircraft MRO & FBO Shops]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An engine arrives at the shop with its borescope history, trend data and records in three different places, and the shop learns what is wrong with it only after teardown.
**Tags:** #cnns #gradient-boosting #feature-engineering #large-language-models #data-integration #workflow-orchestration #revenue-impact
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every engine shop is fighting to release a serviceable engine at the lowest cost per flight hour inside the date it quoted. Cost and date are won by different capabilities, though: the workscope and life-limited-part decisions are won on records and engineering prediction, while the date is won on slot capacity and control of parts and repair vendors. Decomposed into contested sub-niches below.

## The Problem
When an engine is removed, the operator or lessor sends it to a shop with a removal reason and a records package. The shop's engineers build an initial workscope from the removal reason, the engine's hours and cycles, LLP status and the customer's maintenance policy. The on-wing evidence that would sharpen it often arrives late or not at all: the last borescope videos and findings from the line station, the exhaust-gas-temperature margin and vibration trends from the trend-monitoring service, previous shop visit reports from a different MRO. The real condition becomes clear only at teardown, days into the visit, and the workscope, parts order and quote then change.

## Why Nobody Has Built This
Each input belongs to a different party and system: borescope media sits with the line station or the operator's engineering department, trend data with the OEM or a monitoring service, records with the owner. OEM networks see more of it for engines under their own service agreements and keep it inside those programmes. Independent shops have treated induction as an engineering judgement rather than a data product.

## What to Build
An induction pack assembled automatically when a removal is scheduled. It requests and ingests the last on-wing borescope inspections and findings, the trend history and prior shop visit reports. It reads records for LLP status and open ADs, and produces a pre-teardown condition estimate by module (fan, compressor, combustor, turbines) with the evidence for each. A gradient-boosting model trained on the shop's own history predicts likely module findings and the probability that the workscope will grow. Engineers start the visit with a ranked list of what to look at first and which long-lead parts to reserve.

## Target Customer
Engineering managers at independent engine shops and airline engine shops working on CFM56, LEAP, V2500, GTF and business-aviation turbofans.

## Impact If Built
Moving workscope growth discovery from teardown to induction could take ~5–10 days off a ~60–120 day shop visit (estimate) by ordering long-lead parts earlier. At ~$100,000–$200,000 a month in spare-engine lease cost, that is worth ~$15,000–$65,000 per visit to the owner.
