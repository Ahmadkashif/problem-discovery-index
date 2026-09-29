# Fix: The Mileage Log the Platform Has and the Courier Reconstructs

**Niche:** [[niches/gig-delivery-platforms/earnings-and-cost-accounting/profile|Earnings, Pay & Cost Accounting]]
**Industry:** [[industries/gig-delivery-platforms|Gig Delivery Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The platform dispatched every route and knows every mile, and the courier pays for a third-party app to reconstruct the same log from GPS.
**Tags:** #descriptive-statistics #evaluation-metrics #data-integration #compliance #workflow-orchestration #worker-facing #quick-win #automation
**Contested on:** Whether the platform will hand over a record it already holds and that costs it nothing to produce.

## The Problem

Mileage is the largest deductible expense a courier has and the primary determinant of their net income. The IRS standard mileage deduction is substantial and requires a contemporaneous log.

The platform dispatched every delivery, computed every route, and holds the distances. It reports none of it. So couriers install mileage tracking apps, pay subscriptions, run continuous GPS on their phones, drain their batteries, and produce a reconstruction of a record the platform already has — less accurately, since a GPS trace has to infer trip boundaries that the platform knows exactly.

The same applies to the earnings side at tax time: the 1099 reports gross, and reconstructing the deductible picture is left entirely to the individual.

## Why It's Still Broken

There is no positive reason, which is what makes it a clean fix. It is an omission that has never had an owner. Mileage is not a payment concern, not a dispatch concern and not a support concern, so it sits in the gap.

Two objections get raised and neither survives inspection. The first is that platform-computed route distance is not the courier's actual driven distance — true, and it is a floor rather than an estimate, which is exactly what a conservative deduction record should be, and it can be labelled as such. The second is the classification shadow: providing tax-supporting infrastructure is said to resemble employer behaviour. Providing a record of services rendered is ordinary commercial conduct between businesses, and every logistics contractor receives one.

## What a Fix Looks Like

Export the log.

Per delivery: date, dispatched route distance from the courier's location at acceptance through merchant to customer, engaged interval, and the amount paid. Annually and on demand, in a format tax software accepts. This is a report over the dispatch and payment tables.

Include the deadhead where it is dispatched. The leg from the courier's position to the merchant is driven at the platform's instruction and is the segment couriers most often fail to capture themselves. It is in the routing record.

State the basis clearly — dispatched route distance, a conservative floor, not inclusive of repositioning or personal driving — so the courier knows what they have and what they may need to supplement. A labelled partial record is far more useful than nothing.

Add the earnings decomposition alongside it. Gross by component, platform fees, top-ups and adjustments, per period, matching the 1099. Most couriers cannot currently reconcile their 1099 to their weekly statements, which generates support volume every January and a persistent suspicion that the numbers do not add up.

And publish an annual summary: deliveries, engaged hours, online hours, dispatched miles, gross earnings. Five numbers from five columns. That summary is what a courier needs for their taxes, what a researcher needs for a study, and what a courier deciding whether this work is viable has never seen about their own year.

## Who Feels the Pain

Couriers, who pay for tools and battery life to reconstruct a record that exists, and who under-claim deductions when the reconstruction fails. Newer couriers who do not know to track at all and lose the deduction entirely. Tax preparers working from incomplete records. And the platform, which generates January support volume over 1099 reconciliation it could prevent with a report.

## Impact If Fixed

Couriers get an accurate, free, contemporaneous mileage record instead of an expensive approximate one, which directly increases their net income through the deduction they are entitled to and often under-claim. The 1099 becomes reconcilable. And it costs the platform a report — the highest ratio of courier benefit to platform cost available anywhere in this industry.
