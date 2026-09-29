# Catalogue and Stock Synchronisation

**Industry:** [[dropshipping-suppliers|Dropshipping Suppliers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Catalogue import and stock sync are the baseline feature of every platform in the category, and merchants still oversell items their supplier stopped carrying weeks ago.
**Tags:** #change-point-detection #time-series-forecasting #gradient-boosting #confidence-intervals #hypothesis-testing #evaluation-metrics #data-integration

## The Problem
A merchant imports a supplier's catalogue into their storefront. Prices, images, descriptions and stock levels flow through on a schedule.

The synchronisation is only as good as what the supplier publishes and how often it is polled. Suppliers vary enormously: some provide a real-time feed, some a daily file, some a spreadsheet by email, some nothing beyond a website. Stock levels are frequently approximate even when supplied. Products are discontinued without notice and simply stop appearing. Prices change and a merchant discovers it when their margin is gone.

The failure the merchant experiences is overselling — taking an order for something the supplier cannot ship. On a marketplace this carries a metric penalty and can suspend an account, which is a far larger consequence than the single order.

Merchants defend by carrying buffers, delisting anything volatile and manually checking their best sellers, which is exactly the manual work the platform was supposed to remove.

## What Already Exists
Catalogue import and mapping tooling is standard across the category. Scheduled polling and webhook-based sync are both supported. Price and stock rules with markup and rounding are configurable. Product variant mapping is handled. Some platforms offer stock buffers and automatic delisting on stock-out. Marketplace listing integration handles the downstream publishing.

## The Customisation Gap
Sync frequency is uniform when the risk is not. A slow-moving item polled hourly is over-served and a volatile best-seller polled hourly is under-served. Prioritising sync frequency by predicted volatility and by the merchant's actual exposure is straightforward and is not done.

Stock reliability per supplier is unmeasured. Some suppliers' published levels are accurate and some are decorative, and the platform can measure this directly by comparing published stock against subsequent fulfilment failures — which turns a buffer chosen by guesswork into one sized by evidence.

Discontinuation detection is reactive. A product disappearing from a feed, or ceasing to be fulfilled, is detectable immediately and is usually noticed when an order fails.

Price change monitoring with margin impact is the fourth gap. A supplier price increase silently erodes a merchant's margin, and alerting on it with the resulting margin computed is trivial and largely absent.

## Impact If Solved
Overselling costs marketplace standing rather than merely an order, and merchants defend against it with manual checking that negates the automation. Risk-weighted sync frequency and evidence-based stock buffers address the actual failure, using performance data the platform already generates on every order.
