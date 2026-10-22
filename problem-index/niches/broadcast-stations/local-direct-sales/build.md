# Airtime-to-Response Proof for the Local Advertiser

**Niche:** [[niches/broadcast-stations/local-direct-sales/profile|Local Direct Sales]]
**Industry:** [[industries/broadcast-stations|Broadcast TV & Radio Stations]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The station knows to the second when each spot aired and the advertiser knows when its phone rang, and nobody joins the two for a local business.
**Tags:** #causal-inference #time-series-forecasting #bayesian-inference #hypothesis-testing #feature-engineering #data-integration #revenue-impact
**Contested on:** Every serious competitor in this niche (broadcast CRM vendors, attribution and call-tracking services, and the groups' own sales research teams) is fighting to show a local business owner, in the owner's own terms (calls, leads, booked jobs, showroom visits), that the station's schedule produced customers before the annual renewal, and whoever proves that most convincingly takes the account.

## The Problem
A plumbing company spends ~$5,000 a month (estimate) on a station's morning news and drive time. Its owner sees call volume in a call-tracking or phone system and web visits in Google Analytics. The station sees the spot times in its affidavit. When renewal comes, the AE brings ratings and testimonials, while the digital competitor brings a dashboard. The owner keeps the channel that shows a number.

## Why Nobody Has Built This
TV attribution vendors serve national direct-to-consumer brands with large budgets and their own data teams. A local advertiser's signal is small and noisy, so it needs pooling across many similar advertisers to be readable, and only the station, or a group with hundreds of them, holds that pool. Traffic systems were built to schedule and bill, not to export airtimes against third-party data. Stations have also feared that measuring results would show some schedules do not work.

## What to Build
A results service that takes the airtime log and, with the advertiser's permission, its call-tracking, web-session and booking data, then estimates lift in short windows after each spot against matched baselines. Effects are pooled across advertisers in the same category and market with a hierarchical model, so a small advertiser gets a credible estimate with honest intervals. The output is a monthly one-page result in the owner's terms, plus guidance on which dayparts and creative worked.

## Target Customer
Group VPs of local sales and local sales managers at stations where home services, legal, auto and healthcare advertisers dominate local direct.

## Impact If Built
If evidenced results lifted renewal rates on local direct accounts by even a few points (estimate), that would protect the largest controllable revenue line a station has. It would also let AEs argue for the dayparts that actually work instead of discounting.
