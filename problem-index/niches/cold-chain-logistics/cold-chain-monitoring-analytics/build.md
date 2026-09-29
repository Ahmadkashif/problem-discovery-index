# Excursion Root Cause as a Learned Model, Not a Case File

**Niche:** [[niches/cold-chain-logistics/cold-chain-monitoring-analytics/profile|Cold Chain Monitoring & Excursion Analytics]]
**Industry:** [[industries/cold-chain-logistics|Cold Chain Logistics]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every excursion gets investigated and the conclusion is written into a case file, so a company holding millions of temperature profiles has no model of what actually causes them.
**Tags:** #time-series-forecasting #change-point-detection #gradient-boosting #feature-engineering #evaluation-metrics #causal-inference #cross-validation #confidence-intervals #data-integration #revenue-impact

## The Problem
An excursion is expensive and urgent: product is on hold, a release decision is waiting, and someone has to determine what happened. An analyst reads the temperature trace, checks the shipment record, and concludes — a door left open at a transfer, a reefer set incorrectly, a delayed customs hold, packaging under-specified for the ambient conditions. That conclusion resolves the case and is filed against it. Across the customer base this happens at enormous volume, producing what would be a labelled dataset of profile shapes mapped to physical causes, and it is stored as prose in individual case records. So each investigation starts from the trace, the analyst's experience carries the diagnosis, and the company's accumulated understanding of why cold chains fail lives in the heads of its senior investigators.

## Why Nobody Has Built This
Investigations are delivered under time pressure where documentation is overhead, so causes are recorded in free text with no controlled vocabulary — the same failure appears as a dozen phrasings across the archive. Confirming a cause is also often impossible: the analyst infers from the trace and the shipment record, and physical verification rarely happens, so labels are hypotheses of varying quality rather than ground truth. And customer data is contractually siloed, which has made cross-customer analysis feel prohibited rather than merely unaddressed.

## What to Build
An engine that converts investigation output into a structured, learnable corpus. Causes are recorded against a controlled taxonomy at the point of investigation, with the analyst's confidence and the evidence relied on, at a cost of a few clicks rather than a documentation task. Historical case files are back-classified by parsing existing free text into the same taxonomy, which recovers years of accumulated diagnosis. Profiles are then characterized structurally — excursion shape, onset, duration, recovery, and its position in the shipment timeline — and modelled against cause, so a new excursion arrives with ranked candidate causes and the evidence for each, rather than with a blank investigation form. Where labels are uncertain, the model says so; the goal is to make the investigator faster and more consistent, not to replace a judgment that carries release consequences. Cross-customer learning runs on de-identified profile and cause pairs, which is where the contractual work is and where the value is, because failure modes recur across shippers who never see each other's data.

## Target Customer
VPs of analytics and heads of cold chain services at monitoring providers running 100-500 staff, and the quality and logistics leaders at pharmaceutical and food shippers who absorb investigation turnaround as time on hold.

## Impact If Built
Compresses the most time-critical service the company delivers, in a workflow where hours of investigation are hours of product on hold. More strategically, it converts the company's real asset from raw telemetry — which competitors also collect — into a model of causation that only the party performing millions of investigations can build. That model is also the basis for the prevention products the market wants and nobody sells credibly.
