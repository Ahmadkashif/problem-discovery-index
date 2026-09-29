# Borrowing Normal From Similar Merchants

**Niche:** [[niches/payment-fraud-vendors/merchant-onboarding-cold-start/profile|Merchant Onboarding & Cold Start]]
**Industry:** [[industries/payment-fraud-vendors|Payment Fraud Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The new merchant's patterns are already learned on the network at twenty structurally similar merchants, and the model starts from nothing.
**Tags:** #transfer-learning #k-means-clustering #gradient-boosting #evaluation-metrics #confidence-intervals #k-nearest-neighbors #automation #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to know a new merchant's definition of normal before it has any history — and whoever transfers that from merchants already on the network wins the first ninety days the customer judges them on.

## The Problem
A new merchant goes live. Their customers buy in a particular range, ship to particular places, order at particular times, and have legitimate patterns that look alarming without context — a subscription box's identical repeat orders, a ticketing site's spikes, a marketplace's high-velocity buyers. The model has no history, so it applies generic priors, produces false positives, and is tuned over months. The merchant's impression of the vendor is formed entirely during this period, and the vendor already serves twenty merchants whose patterns are nearly the same.

## Why Nobody Has Built This
Models were built per merchant because each merchant's data is their own, so the tenancy boundary became a modelling boundary — and once a per-merchant model is the architecture, transfer requires rethinking the whole thing. Merchant similarity was never defined or computed. Onboarding is treated as an implementation phase rather than as a modelling problem. And nobody measures time to acceptable performance, so the cost of the cold start is invisible.

## What to Build
Define similarity and transfer. Build a merchant similarity model from transaction characteristics rather than from industry labels, which is the core — a vertical code is a poor predictor and the behavioural signature is a good one. Initialise a new merchant from a pooled model over their nearest neighbours, since that is immediately better than generic priors and costs nothing at runtime. Blend the transferred prior with own data as history accumulates, which is a standard hierarchical structure the category has not applied. Identify the legitimate anomalies of the merchant's type in advance, because the subscription repeat order and the ticket spike are known patterns that generate the worst early false positives. Ask the merchant a small number of high-information questions rather than a long configuration form, as a few answers about their business remove much of the uncertainty. Manage the early period explicitly with wider review bands and clear expectations, since a merchant who was told what to expect judges the same performance differently. Measure time to acceptable performance as the onboarding metric, which nobody tracks. Handle the merchant who is genuinely unlike anything on the network as a distinct case, because they exist and deserve a different approach. Monitor for drift as the merchant grows, since early normal is not later normal. And feed every new merchant back into the similarity model, so the transfer improves with the network.

## Target Customer
Onboarding and data leadership, new merchants judging the product on its worst period, customer success teams managing the complaints, and fraud platform vendors with per-merchant architectures.

## Impact If Built
The tenancy boundary became a modelling boundary, and once per-merchant models are the architecture transfer requires rethinking everything. Behavioural similarity to existing merchants is a far better starting point than a generic prior and is computable today.
