# Retail Media Networks

## Profile
**Category:** Adtech & Martech
**Market Size:** ~$60B US retail media spend and growing faster than any other advertising channel; margins of 70-90% make it the profit engine of several large retailers
**Tech Maturity:** High and unevenly distributed. Amazon Ads operates at a level nobody else approaches; Walmart Connect, Roundel, Kroger Precision Marketing, Instacart Ads and CVS Media Exchange are serious businesses; below the top tier most networks run on a licensed platform from Criteo, Epsilon's CitrusAd, Topsort or Moloco and differentiate on data they have not yet learned to use.
**Workforce:** Ad platform and auction engineers, campaign and account managers, measurement and insights analysts, category merchants and buyers, retail media sales teams, data and clean room engineers

## Key Pain Themes
Retail media has the one thing the rest of advertising has spent twenty years failing to build: a genuinely closed loop. The same company shows the ad, owns the shelf, takes the order and records the purchase, in one system, under one identity. And the industry has pointed that instrument almost entirely at last-click attributed ROAS — counting sales to shoppers who searched a brand by name and would have bought it anyway, and rarely subtracting the organic sale the sponsored placement displaced.

Nobody involved is unaware. Brands increasingly demand incrementality; the trade press has run the cannibalisation argument for years; the retailers themselves can run the experiment on any given Tuesday. The reason it persists is that the reported number funds a profit pool that has become load-bearing for the retailer's earnings, and the honest number is smaller.

Underneath that sits a quieter tension. Every sponsored placement costs something in shopper experience — a slot that would have shown a better-matched or better-margin product, a search results page that is now a quarter advertising. That cost lands in basket size and return visits, over months, at a horizon no campaign report covers, while the revenue lands this week. The people holding the other side of that trade are category merchants, whose shelf has been sold out from under them without a number attached.

## Current Tech Landscape
Amazon's advertising business is the reference implementation and the competitive pressure that created the category. Walmart Connect's Vizio acquisition and Kroger's partnership strategy show the offsite and CTV extension. Criteo, CitrusAd, Topsort, Moloco and Pentaleap supply the auction and serving layer to everyone else, which means most networks share the same ranking technology and differentiate only on data. Clean rooms — Amazon Marketing Cloud, LiveRamp, Habu, Snowflake — carry offsite measurement. The IAB and MRC retail media standards arrived late and are only partially adopted, so cross-network comparison is still not possible.

## Problems
- [[problems/retail-media-networks/high-impact|🔴 High Impact: The Only Closed Loop in Advertising, Spent Counting Sales That Were Already Happening]]
- [[problems/retail-media-networks/low-impact-1|🟡 Low Impact: Ranking Under Competing Objectives]]
- [[problems/retail-media-networks/low-impact-2|🟡 Low Impact: Offsite Audience Activation and Clean Room Measurement]]
- [[problems/retail-media-networks/worker-life-1|🟢 Worker Life: The Account Manager Running Four Hundred Campaigns by Hand]]
- [[problems/retail-media-networks/worker-life-2|🟢 Worker Life: The Merchant Whose Shelf Was Sold]]
- [[problems/retail-media-networks/ml-opportunity|🧠 ML Opportunities]]
- [[problems/retail-media-networks/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
This is the inverse of the programmatic problem and it is more interesting for it. Everywhere else in advertising the outcome is unobservable and the industry substitutes a proxy; here the outcome is perfectly observable, sitting in the same database as the impression, and the industry substitutes a proxy anyway — because measuring properly would reduce a reported number that a public company's margin story depends on. The retailer is the only party that can run the experiment, has no external barrier to running it, and has a direct financial reason not to. That makes the honest measurement layer a genuine product opportunity rather than a technical one, and it makes the second-order question — what ad load costs in basket and loyalty over a year — the thing nobody in the category can currently answer about their own business.
