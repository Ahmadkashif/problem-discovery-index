# Retailer-Level Retention Scoring

**Niche:** [[niches/telecom-resellers/international-prepaid-subscribers/profile|International-Calling & Cash-Paying Prepaid Subscribers]]
**Industry:** [[industries/telecom-resellers|Telecom Resellers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A prepaid brand pays retailers for activations and refills without knowing which shops' customers stay for a year and which churn after the first month.
**Tags:** #survival-analysis #gradient-boosting #k-means-clustering #feature-engineering #revenue-impact #data-integration
**Contested on:** Every serious competitor in this niche is fighting to be the brand the corner-store clerk recommends and can refill in seconds for cash, with calls to the subscriber's home country that keep working, and whoever wins the retailer's counter wins the subscriber.

## The Problem
Thousands of independent shops activate and refill a prepaid brand's SIMs. Commission plans pay per activation and a share of refills. Some shops' customers refill every month for years. Others activate lines that never refill, sometimes because the clerk pushed a promotion, sometimes because the activation was fake. The brand sees totals per distributor, not retention per shop, so its field reps and commission money go to the busiest counters rather than the best ones.

## Why Nobody Has Built This
Activation, refill and usage data sit in different systems: the BSS, the refill distributor's network and the commission platform. The retailer identifier often doesn't survive the hop. Prepaid brands are lean, and analytics teams are rare.

## What to Build
Join activations, refills and usage back to the activating and refilling retailer. Model each shop's subscriber survival curve and refill value, adjusted for its neighbourhood and the countries its customers call, and flag shops whose activations look fabricated (no usage, identical patterns). Feed the result into commission tiers, field-rep visit plans and point-of-sale material in the languages each shop's customers speak.

## Target Customer
Heads of prepaid distribution and retail channel at prepaid MVNOs and international-calling brands.

## Impact If Built
Commission money and rep time move to the counters that build lasting subscribers, and paying for activations that never refill largely stops.
