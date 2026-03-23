# Inventory Forecasting for Podcast Ad Sales

**Niche:** [[niches/podcasting-networks/podcast-ad-sales-houses/profile|Podcast Ad Sales Houses]]
**Industry:** [[industries/podcasting-networks|Podcasting Networks]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Salesforce forecasts sales pipeline revenue, but podcast ad sales teams need to forecast available advertising inventory — how many impressions each show will generate next quarter — to avoid overselling or underutilizing their catalog.
**Tags:** #time-series-forecasting #gradient-boosting #tabular-ml #revenue-impact #automation

## The Problem
A podcast ad sales team sells against future inventory: "We can deliver 500,000 impressions on our true crime shows in Q3." But accurately predicting future inventory requires forecasting how many downloads each show will generate per episode over the next 3 months — a function of historical download trends, seasonal patterns (podcasting dips in summer), new show launches, and show cancellations. Sales teams either oversell (committing to more impressions than shows will deliver, requiring makegoods or refunds) or undersell (leaving inventory unsold because they padded forecasts conservatively). Both cost revenue: overselling costs credibility and makegood expense; underselling leaves money on the table.

## What Already Exists
Salesforce and HubSpot forecast sales pipeline revenue (deals in progress, weighted by probability). Podcast hosting platforms show historical download data. But no tool forecasts future podcast inventory — the number of available ad impressions by show, by placement type (pre-roll, mid-roll, post-roll), by episode frequency, by date range. The sales team builds inventory projections in Excel using average downloads per episode multiplied by planned episode count, with a manual adjustment for seasonality. This is a crude estimate that doesn't account for show-level growth/decline trends, one-time spikes (viral episodes), or the impact of new show launches on the network's audience.

## The Customization Gap
Podcast inventory forecasting needs to: (1) predict downloads per episode per show for the next 1–4 quarters using time-series models trained on each show's history, (2) account for podcast-specific seasonality (summer dip, holiday spike, new year resurgence), (3) model the impact of episode frequency changes (a weekly show going biweekly), (4) incorporate new show launch projections based on comparable show performance, (5) calculate available inventory by placement type (subtracting committed/sold inventory from total forecasted), and (6) present a sales-ready inventory availability view: "We have 200,000 unsold pre-roll impressions in true crime for Q3, 150,000 in business." Integration with the CRM shows committed vs. available in real-time as deals close.

## Target Customer
Sales directors and revenue operations managers at podcast ad sales houses managing inventory across 100+ shows.

## Impact If Solved
Reduces overselling incidents from 10–15% of campaigns to under 3%, saving $50K–$200K annually in makegood costs. Increases inventory utilization from 60–70% to 80–85% by enabling sales teams to sell confidently closer to actual capacity — worth $200K–$1M in additional annual revenue for a mid-size sales house.
