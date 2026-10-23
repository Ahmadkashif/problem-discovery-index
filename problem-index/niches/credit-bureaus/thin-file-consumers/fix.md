# Rent Reported Only When It Helps

**Niche:** [[niches/credit-bureaus/thin-file-consumers/profile|Thin-File & Credit-Invisible Consumers]]
**Industry:** [[industries/credit-bureaus|Credit Bureaus]]
**Type:** Fix (Pain Point)
**One-liner:** Rent is reported for tenants who opt in and properties that subscribe, often positive-only, so lenders cannot tell what a rent tradeline is worth.
**Tags:** #causal-inference #logistic-regression #evaluation-metrics #feature-engineering #data-integration
**Contested on:** Every serious competitor in this niche is fighting to get rent, utility, telecom or cash-flow data into the lender's production underwriting model rather than a side score, and whoever clears the lender's model validation and fair-lending review first takes the account.

## The Problem
A rent tradeline on one consumer's file may mean a property manager reports every tenant, positive and negative; on another, that the tenant paid a service to report their on-time payments only. Scoring models and lenders see a tradeline either way, and discount all rent data because some of it is selected.

## Why It's Still Broken
Rent reporting grew through opt-in consumer products and landlord marketing programmes, each with its own policy, and the Metro 2 record does not say which policy produced it.

## What a Fix Looks Like
Carry the reporting policy with every rent tradeline (full-file or opt-in, positive-only or full history), measure the selection effect on outcomes by policy, and let scoring and lenders weight each accordingly.

## Who Feels the Pain
Renters whose real payment history counts for little; lenders who cannot use it; furnishers whose full-file reporting is discounted with the rest.

## Impact If Fixed
Rent data that carries its own credibility, which is the condition for using it inside a model.
