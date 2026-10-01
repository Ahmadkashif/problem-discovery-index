# The Request Sent to Three Networks

**Niche:** [[niches/expert-networks/custom-call-brokerage/profile|Custom Call Brokerage]]
**Industry:** [[industries/expert-networks|Expert Networks]]
**Type:** Fix (Pain Point)
**One-liner:** Clients send the same request to several networks, take the first good profiles, and two-thirds of the industry's sourcing work on that request is thrown away unbilled.
**Tags:** #gradient-boosting #logistic-regression #evaluation-metrics #descriptive-statistics #quick-win #revenue-impact
**Contested on:** This niche is not terminal — finding an expert for a fund that covers the same tickers every quarter and finding forty experts on a private target inside a two-week deal clock are different contests with different winners, and they are stated separately in the sub-niches.

## The Problem
A fund's analyst emails the same request to GLG, AlphaSights and Guidepoint at once. All three staff it. The analyst picks profiles from whichever arrives first with a credible screener answer. The losing networks' associates spent hours on outreach that produced nothing, and the winning network learned that it was fast, not that it was right.

## Why It's Still Broken
Multi-sourcing is rational for the client and invisible in each network's data as anything other than a request that "did not convert". Networks do not distinguish requests lost on speed from requests lost on profile quality, and they staff every request the same way regardless of their historical win rate with that client on that kind of question.

## What a Fix Looks Like
Predict win probability per request from client, topic, time zone and the network's historical conversion, and staff accordingly. Track time-to-first-credible-profile as an explicit metric. Record why a request was lost where the client says. Prioritise candidates already in the database with good call records, since they convert faster than cold outreach.

## Who Feels the Pain
Associates whose work disappears; networks paying for wasted sourcing; clients who receive duplicated outreach to the same experts from three firms.

## Impact If Fixed
A large share of sourcing effort produces nothing billable. Staffing to expected win probability and measuring time-to-credible-profile recovers associate capacity without a single new client.
