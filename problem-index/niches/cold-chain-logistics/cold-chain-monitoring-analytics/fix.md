# Lane Risk Is Known Shipment by Shipment and Never in Aggregate

**Niche:** [[niches/cold-chain-logistics/cold-chain-monitoring-analytics/profile|Cold Chain Monitoring & Excursion Analytics]]
**Industry:** [[industries/cold-chain-logistics|Cold Chain Logistics]]
**Type:** Fix (Pain Point)
**One-liner:** The company observes millions of shipments across every major lane, carrier, and season, and reports on them one shipment at a time — so the question a shipper most wants answered, which lane is actually risky, is one it cannot answer.
**Tags:** #descriptive-statistics #gradient-boosting #time-series-forecasting #confidence-intervals #hypothesis-testing #evaluation-metrics #feature-engineering #dimensionality-reduction #data-integration #revenue-impact

## The Problem
The product is organized around the consignment because the customer's compliance obligation is. Each shipment gets a report, a release recommendation, and an investigation if it excursed. What the company also has, and does not use, is the aggregate: excursion rates by lane, carrier, transfer point, packaging configuration, season, and their interactions, across millions of shipments and every major shipper in the industry. That is the answer to the questions shippers actually pay consultants for — which lanes need better packaging, which handling points cause the losses, which carrier performs on this route in July. Instead the company delivers per-shipment compliance evidence and the shipper hires someone else to answer the strategic question, using far less data.

## Why It's Still Broken
The data is contractually partitioned by customer, and the terms usually address the customer's own shipments without contemplating aggregate analysis — so the safe reading has been that none is permitted, and nobody has done the work of mapping which agreements actually allow de-identified aggregation. The product organization is also built around the compliance workflow, which is where the revenue is and where the regulatory pressure comes from, so aggregate analytics has never had an owner. And there is a commercial hesitancy about publishing carrier and lane performance, since carriers are frequently channel partners.

## What a Fix Looks Like
An aggregate analytics layer built on a rights model that resolves each agreement into what it actually permits, so analyses run on the portion of the corpus that is entitled rather than on none of it. Lane risk is then characterized properly — excursion rate and severity by lane, carrier, transfer point, packaging, and season, with confidence reflecting how much support each cell has, which matters because the long tail of lanes is thin and the aggregate should say so. Customers see their own performance benchmarked against the population, which is the single most requested thing in this category and is currently unavailable from anyone. Carrier and handling-point performance is reported in a form the company can stand behind — de-identified where partner relationships require it, named where the evidence supports it, and always with the sample support stated. The same layer feeds prospective use: a shipper planning a route receives an expected risk profile before shipping rather than a compliance record afterward.

## Who Feels the Pain
Shippers making packaging and routing decisions on anecdote while the evidence sits with their monitoring vendor; quality teams unable to tell whether their excursion rate is good or bad because they have no comparison; the monitoring company, whose most defensible asset is used only to fill in per-shipment reports; and ultimately the product that spoils on a lane everyone could have known was risky.

## Impact If Fixed
Moves the company from compliance documentation, which is a commoditizing service competed on device price, to risk intelligence, which is bought by a different budget and cannot be replicated without the same shipment volume. Benchmarking alone changes the renewal conversation, because a customer who can see where they sit against the industry has a reason to keep the relationship that has nothing to do with logger cost.
