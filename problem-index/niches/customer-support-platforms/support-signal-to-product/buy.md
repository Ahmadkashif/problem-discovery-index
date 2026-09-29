# Topic Modelling and Emerging Issue Detection

**Niche:** [[niches/customer-support-platforms/support-signal-to-product/profile|Support Signal to Product]]
**Industry:** [[industries/customer-support-platforms|Customer Support Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Clustering text into topics and detecting when a new one emerges is a mature commodity used in social listening and operational monitoring, and support ticket analysis is a pivot table over routing categories.
**Tags:** #bert #k-means-clustering #change-point-detection #contrastive-learning #evaluation-metrics #confidence-intervals #time-series-forecasting #automation
**Contested on:** Every serious competitor with a support corpus is fighting to turn it into a product defect and friction signal the product organisation actually acts on — and whoever closes that loop takes a use of the data nobody currently serves.

## The Problem
A release goes out on Tuesday. By Thursday a specific interaction is generating contacts at eleven times its normal rate, described by customers in a dozen different ways none of which matches an existing category. The routing categories show a slight increase in a broad bucket. Nobody notices until the following week, when an agent mentions it. Detecting a new cluster emerging in a text stream is exactly what topic modelling and novelty detection are for, and both have been commodity for years.

## What Already Exists
Text clustering with modern embeddings, topic modelling, and novelty and change-point detection over streams are all mature with free implementations. Social listening platforms do precisely this over public text at scale. Anomaly detection on categorical and volume time series is standard. Alerting infrastructure is commodity. Every component is available and the corpus is cleaner and better structured than the social media text these methods were refined on.

## The Customization Gap
The adaptation is to a support corpus and to a product audience. It requires: (1) clustering on the failure rather than on the customer's language, which means incorporating the resolution, the product area and any error identifiers alongside the ticket text — since customers describe the same failure in many ways and the resolution is the consistent signal; (2) baseline modelling that accounts for seasonality, volume growth and release cadence, so an alert means something rather than firing on every Monday; (3) release correlation, joining detected changes to the deployments that preceded them, which is what makes an alert immediately actionable and which requires a connection to the product's own release stream; (4) severity estimation from the cost model rather than volume alone, since a small cluster with high refund and churn association matters more than a large cluster of people asking where a button moved; and (5) delivery into the product team's own tools with enough context to act — the cluster, its trend, its cost, example tickets and the suspected release — since a product engineer will not open a support dashboard.

## Target Customer
Product and engineering organisations, support platform vendors, and the observability vendors for whom customer-reported failures are an adjacent signal to the telemetry they already handle.

## Impact If Solved
Emerging issue detection over the support stream gives an organisation a customer-reported early warning that complements its telemetry, catching the failures that do not throw errors — confusion, broken expectations, silent data problems — which are invisible to monitoring and obvious to customers. Release correlation is the adaptation that makes it actionable within hours rather than interesting within weeks.
