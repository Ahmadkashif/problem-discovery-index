# The Users Who Never Appear in the Analytics

**Niche:** [[niches/edge-cdn-providers/constrained-network-delivery/profile|Constrained Network Delivery]]
**Industry:** [[industries/edge-cdn-providers|Edge & CDN Providers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Delivery is optimised for users who successfully load the page, and the users on constrained networks who abandon before it loads are absent from every measurement that would reveal them.
**Tags:** #descriptive-statistics #logistic-regression #survival-analysis #k-means-clustering #evaluation-metrics #confidence-intervals #automation #worker-facing
**Contested on:** Every serious competitor here is fighting to deliver acceptably to users on expensive, slow and intermittent connections — and whoever does that takes the markets where growth actually is, because the category's defaults assume conditions those users do not have.

## The Problem
A company's analytics show a median page load of two seconds and a healthy conversion rate. In one growing market, a substantial share of users on mobile connections never complete a page load: the payload is too large, the connection drops partway, and they leave before any client-side measurement fires. They are not slow users in the data; they are absent from it. The product team looks at the numbers, sees good performance, and concludes the market is simply not converting — which is true and is caused by something they have not measured.

## Why Nobody Has Built This
Client-side measurement requires the client to load and execute, which is precisely what fails for this population — a survivorship problem that is structural rather than an oversight. Server-side measurement sees the requests and not the outcome. Nobody has joined the two to identify sessions that began and never completed. The delivery network's own measurement points are in well-connected facilities. And the affected users are in markets that are frequently a growth priority in principle and a measurement afterthought in practice.

## What to Build
Measure the failures and adapt to the connection. Identify abandoned sessions from the server side — requests that began a page and never fetched the resources that follow, which is visible in the delivery logs and is the population client-side analytics structurally cannot see. Report them as a first-class metric by geography, network and device, since their absence is the reason the problem is invisible. Adapt the payload to the observed connection rather than statically: fewer and smaller resources, different image formats and dimensions, deferred non-essential content, and a usable experience at a fraction of the full payload — which is an existing capability configured as a fixed policy rather than as a response to conditions. Design for intermittency as normal rather than as failure, with resumable transfers and partial rendering, since a connection that drops for four seconds should not restart a download. Report the data cost to the user, because on a metered plan a heavy page is a cost the user bears and is a reason they do not return, and no product surfaces it. And place measurement vantage points in the networks that matter rather than in the facilities that are convenient.

## Target Customer
Companies with mobile-first and emerging-market user bases, delivery providers seeking growth in those markets, and the performance measurement vendors whose data structurally excludes this population.

## Impact If Built
The affected users are absent from the measurement rather than visible and slow, which makes the problem invisible in exactly the market where it matters most. Server-side abandonment measurement is the change that makes them appear, and connection-driven adaptation is the remedy that already exists as a static configuration.
