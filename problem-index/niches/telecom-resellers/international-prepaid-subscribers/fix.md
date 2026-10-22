# The International Route That Went Quiet

**Niche:** [[niches/telecom-resellers/international-prepaid-subscribers/profile|International-Calling & Cash-Paying Prepaid Subscribers]]
**Industry:** [[industries/telecom-resellers|Telecom Resellers]]
**Type:** Fix (Pain Point)
**One-liner:** When the wholesale route to a country is switched to a cheaper carrier, calls home start failing or sounding robotic, and subscribers leave the brand before anyone at head office notices.
**Tags:** #change-point-detection #time-series-forecasting #feature-engineering #revenue-impact #quick-win #automation
**Contested on:** Every serious competitor in this niche is fighting to be the brand the corner-store clerk recommends and can refill in seconds for cash, with calls to the subscriber's home country that keep working, and whoever wins the retailer's counter wins the subscriber.

## The Problem
Prepaid brands buy international termination on wholesale markets and route each destination to the cheapest acceptable carrier. A routing change can quietly degrade calls to one country: post-dial delay rises, calls fail, caller ID doesn't show, audio clips. For a subscriber whose reason for choosing the brand was calling family in that country, two bad weeks are enough to switch at the counter.

## Why It's Still Broken
Least-cost routing is managed by a wholesale team on price and aggregate answer rates per route. Quality is averaged across all customers and destinations, so a degradation concentrated in one country's mobile numbers, which happens to be the brand's core community, disappears in the average. Complaints arrive at shop counters, not at head office.

## What a Fix Looks Like
Monitor call outcomes per destination country and number type from the subscriber's side: answer rate, average call length, short-call share, post-dial delay and repeat-call attempts. Detect a change after each routing change or within days of a carrier's degradation, alert the wholesale team, and automatically roll back to the previous route for that destination while the cause is checked.

## Who Feels the Pain
Subscribers calling home; shop clerks fielding complaints; and brand managers who lose a community without knowing why.

## Impact If Fixed
Routing savings stop costing the subscribers the brand exists to serve, and degradations are caught in days instead of discovered through churn.
